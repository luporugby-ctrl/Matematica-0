#!/usr/bin/env python3
"""
Genera le schede degli argomenti a partire dalle dispense.

Uso:
    export AI_API_KEY="..."
    python3 tools/genera_schede.py ~/dispense --provider gemini

Legge ogni dispensa dalla cartella indicata, manda le pagine al modello e scrive
schede/<id>.md. Aggiorna schede/index.json. Si puo' interrompere e riprendere:
le schede gia' esistenti vengono saltate.

Formati riconosciuti:
  - PDF con testo         -> estrae il testo (economico)
  - PDF scansionati       -> rasterizza le pagine e le manda come immagini
  - archivi ZIP di JPEG   -> manda le immagini (formato delle dispense Mercatorum)

Dipendenze opzionali:
    pip install pillow pypdfium2
Senza pillow le immagini non vengono ridimensionate (costa di piu').
Senza pypdfium2 i PDF veri non possono essere rasterizzati.
"""

import argparse
import base64
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
import zipfile

# ----------------------------------------------------------------- costanti

MAX_LATO = 1024          # ridimensiona le pagine: sotto questa soglia si legge ancora bene
MAX_PAGINE = 60          # limite di sicurezza per dispensa
PAUSA = 2.0              # secondi tra una dispensa e l'altra, per non sbattere sui rate limit

MODELLI = {
    "gemini": "gemini-3.1-flash-lite",
    "anthropic": "claude-haiku-4-5-20251001",
}

RESIDUO = "Da ordinare"

PROMPT = """Ricevi le pagine di una dispensa universitaria di Analisi Matematica 1.

Scrivi una SCHEDA di studio sintetica che servira' a un tutor AI per generare
esercizi coerenti con questo corso. La scheda deve stare sotto le 700 parole.

Regole:
- Scrivi con parole tue. Non trascrivere il testo della dispensa.
- Riporta le formule in LaTeX, usando la stessa notazione della dispensa.
- Se la dispensa usa una convenzione particolare, segnalala esplicitamente.

Rispondi ESATTAMENTE in questo formato, senza premesse e senza blocchi di codice:

---
titolo: <titolo breve dell'argomento, max 8 parole>
gruppo: <macro-area del programma, es. "Successioni e limiti", "Calcolo differenziale">
---
# <titolo>

## Prerequisiti
<cosa bisogna gia' sapere>

## Definizioni e notazione del corso
<definizioni chiave e simboli usati>

## Risultati fondamentali
<teoremi e formule, elenco numerato>

## Metodi risolutivi usati nel corso
<le tecniche concrete, come si applicano>

## Errori tipici da segnalare allo studente
<3-5 errori>

## Tipologie di esercizio da generare
<i tipi di esercizio che compaiono nella dispensa o all'esame>
"""


# ----------------------------------------------------------------- lettura dispense

def ridimensiona(dati_jpeg):
    try:
        from PIL import Image
    except ImportError:
        return dati_jpeg
    im = Image.open(io.BytesIO(dati_jpeg))
    if max(im.size) <= MAX_LATO:
        return dati_jpeg
    im.thumbnail((MAX_LATO, MAX_LATO))
    buf = io.BytesIO()
    im.convert("RGB").save(buf, format="JPEG", quality=80)
    return buf.getvalue()


def leggi_zip_di_immagini(percorso):
    """Formato Mercatorum: zip con 1.jpeg, 2.jpeg, ... e manifest.json."""
    immagini = []
    with zipfile.ZipFile(percorso) as z:
        nomi = z.namelist()
        if "manifest.json" in nomi:
            manifest = json.loads(z.read("manifest.json"))
            ordine = [p["image"]["path"] for p in manifest["pages"]]
        else:
            jpg = [n for n in nomi if n.lower().endswith((".jpg", ".jpeg", ".png"))]
            ordine = sorted(jpg, key=lambda n: int(re.sub(r"\D", "", n) or 0))
        for nome in ordine[:MAX_PAGINE]:
            immagini.append(ridimensiona(z.read(nome)))
    return "immagini", immagini


def leggi_pdf(percorso):
    """Prova il testo; se la resa e' povera, rasterizza."""
    testo = ""
    try:
        import subprocess
        out = subprocess.run(["pdftotext", percorso, "-"],
                             capture_output=True, timeout=120)
        testo = out.stdout.decode("utf-8", "ignore").strip()
    except Exception:
        pass

    if len(testo) > 800:
        return "testo", testo

    try:
        import pypdfium2 as pdfium
    except ImportError:
        raise RuntimeError(
            "PDF senza testo e pypdfium2 non installato. Esegui: pip install pypdfium2 pillow")

    doc = pdfium.PdfDocument(percorso)
    immagini = []
    for i in range(min(len(doc), MAX_PAGINE)):
        pil = doc[i].render(scale=1.6).to_pil()
        pil.thumbnail((MAX_LATO, MAX_LATO))
        buf = io.BytesIO()
        pil.convert("RGB").save(buf, format="JPEG", quality=80)
        immagini.append(buf.getvalue())
    return "immagini", immagini


def leggi_dispensa(percorso):
    with open(percorso, "rb") as f:
        firma = f.read(4)
    if firma[:2] == b"PK":
        return leggi_zip_di_immagini(percorso)
    if firma[:4] == b"%PDF":
        return leggi_pdf(percorso)
    raise RuntimeError("formato non riconosciuto")


# ----------------------------------------------------------------- chiamate API

def chiama_gemini(chiave, modello, tipo, contenuto):
    parti = [{"text": PROMPT}]
    if tipo == "testo":
        parti.append({"text": "\n\n--- DISPENSA ---\n" + contenuto[:180000]})
    else:
        for img in contenuto:
            parti.append({"inline_data": {"mime_type": "image/jpeg",
                                          "data": base64.b64encode(img).decode()}})

    corpo = json.dumps({"contents": [{"role": "user", "parts": parti}]}).encode()
    url = ("https://generativelanguage.googleapis.com/v1beta/models/"
           + modello + ":generateContent")
    req = urllib.request.Request(url, data=corpo, headers={
        "Content-Type": "application/json", "x-goog-api-key": chiave})
    with urllib.request.urlopen(req, timeout=600) as r:
        dati = json.loads(r.read())
    parti = dati["candidates"][0]["content"]["parts"]
    return "\n".join(p["text"] for p in parti if "text" in p).strip()


def chiama_anthropic(chiave, modello, tipo, contenuto):
    blocchi = []
    if tipo == "testo":
        blocchi.append({"type": "text", "text": contenuto[:180000]})
    else:
        for img in contenuto:
            blocchi.append({"type": "image", "source": {
                "type": "base64", "media_type": "image/jpeg",
                "data": base64.b64encode(img).decode()}})
    blocchi.append({"type": "text", "text": PROMPT})

    corpo = json.dumps({"model": modello, "max_tokens": 3000,
                        "messages": [{"role": "user", "content": blocchi}]}).encode()
    req = urllib.request.Request("https://api.anthropic.com/v1/messages",
                                 data=corpo, headers={
                                     "content-type": "application/json",
                                     "x-api-key": chiave,
                                     "anthropic-version": "2023-06-01"})
    with urllib.request.urlopen(req, timeout=600) as r:
        dati = json.loads(r.read())
    return "\n".join(b["text"] for b in dati["content"]
                     if b["type"] == "text").strip()


# ----------------------------------------------------------------- utilita'

def separa_front_matter(testo):
    testo = re.sub(r"^```(?:markdown)?\s*|\s*```$", "", testo.strip())
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", testo, re.S)
    if not m:
        return {}, testo
    meta = {}
    for riga in m.group(1).splitlines():
        if ":" in riga:
            k, v = riga.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, m.group(2).strip()


def id_da_nome(nome, usati):
    base = re.sub(r"[^A-Za-z0-9]+", "", os.path.splitext(nome)[0])[:12] or "DISP"
    ident, n = base, 2
    while ident in usati:
        ident, n = base + str(n), n + 1
    return ident


def costruisci_indice_da_zero(cartella):
    """Nessun index.json esistente: raggruppa TUTTE le schede della cartella per il loro
    gruppo dichiarato nel front matter, ordine alfabetico. E' solo un punto di partenza:
    l'ordine didattico va sistemato a mano in seguito (vedi tools/riordina_indice.py e la
    nota su schede/index.json come fonte di verita curata a mano)."""
    file_md = sorted(f for f in os.listdir(cartella) if f.endswith(".md"))
    gruppi = {}
    for nome in file_md:
        ident = nome[:-3]
        testo = open(os.path.join(cartella, nome), encoding="utf-8").read()
        meta, _ = separa_front_matter(testo)
        gruppo = meta.get("gruppo") or RESIDUO
        gruppi.setdefault(gruppo, []).append({"id": ident, "titolo": meta.get("titolo", ident)})

    indice = {"titolo": "Analisi 1 (L-9)", "gruppi": []}
    n = 1
    for nome_gruppo in sorted(gruppi):
        argomenti = []
        for v in sorted(gruppi[nome_gruppo], key=lambda x: x["titolo"]):
            argomenti.append({"id": v["id"], "num": str(n), "titolo": v["titolo"]})
            n += 1
        indice["gruppi"].append({"gruppo": nome_gruppo, "argomenti": argomenti})
    return indice


def id_gia_indicizzati(indice):
    presenti = set()
    for g in indice.get("gruppi", []):
        for a in g.get("argomenti", []):
            presenti.add(a["id"])
    return presenti


def prossimo_numero(indice):
    n = 0
    for g in indice.get("gruppi", []):
        for a in g.get("argomenti", []):
            try:
                n = max(n, int(a.get("num", 0)))
            except ValueError:
                pass
    return n + 1


def aggiungi_voci_nuove(indice, voci_nuove):
    """schede/index.json e curato a mano: non lo si ricostruisce mai da capo. Le schede
    davvero nuove (non ancora presenti in nessun gruppo) finiscono in coda al gruppo
    'Da ordinare', senza toccare l'ordine di quelle gia' sistemate."""
    presenti = id_gia_indicizzati(indice)
    da_aggiungere = [v for v in voci_nuove if v["id"] not in presenti]
    if not da_aggiungere:
        return indice, 0

    n = prossimo_numero(indice)
    gruppo_residuo = next((g for g in indice["gruppi"] if g["gruppo"] == RESIDUO), None)
    if gruppo_residuo is None:
        gruppo_residuo = {"gruppo": RESIDUO, "argomenti": []}
        indice["gruppi"].append(gruppo_residuo)

    for v in sorted(da_aggiungere, key=lambda x: x["titolo"]):
        gruppo_residuo["argomenti"].append({"id": v["id"], "num": str(n), "titolo": v["titolo"]})
        n += 1

    return indice, len(da_aggiungere)


# ----------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cartella_dispense")
    ap.add_argument("--provider", choices=["gemini", "anthropic"], default="gemini")
    ap.add_argument("--modello")
    ap.add_argument("--out", default="schede")
    ap.add_argument("--dry-run", action="store_true",
                    help="analizza le dispense senza chiamare l'API")
    args = ap.parse_args()

    chiave = os.environ.get("AI_API_KEY", "")
    if not chiave and not args.dry_run:
        sys.exit("Manca AI_API_KEY. Esegui: export AI_API_KEY=\"...\"")

    modello = args.modello or MODELLI[args.provider]
    os.makedirs(args.out, exist_ok=True)

    file_dispense = sorted(
        f for f in os.listdir(args.cartella_dispense)
        if f.lower().endswith((".pdf", ".zip"))
    )
    if not file_dispense:
        sys.exit("Nessuna dispensa trovata in " + args.cartella_dispense)

    print(f"{len(file_dispense)} dispense, provider {args.provider}, modello {modello}\n")

    voci_nuove, usati, falliti = [], set(), []

    for i, nome in enumerate(file_dispense, 1):
        percorso = os.path.join(args.cartella_dispense, nome)
        ident = id_da_nome(nome, usati)
        usati.add(ident)
        destinazione = os.path.join(args.out, ident + ".md")

        print(f"[{i}/{len(file_dispense)}] {nome}", end=" ... ", flush=True)

        if os.path.exists(destinazione):
            # Scheda gia' scritta in un run precedente: non tocca l'indice, che e'
            # curato a mano (vedi aggiungi_voci_nuove piu sotto).
            print("gia' fatta, salto")
            continue

        try:
            tipo, contenuto = leggi_dispensa(percorso)
        except Exception as e:
            print("ERRORE lettura:", e)
            falliti.append((nome, str(e)))
            continue

        quante = len(contenuto) if tipo == "immagini" else len(contenuto)
        unita = "pagine" if tipo == "immagini" else "caratteri"
        print(f"{quante} {unita}", end=" ... ", flush=True)

        if args.dry_run:
            print("dry-run")
            continue

        try:
            if args.provider == "anthropic":
                risposta = chiama_anthropic(chiave, modello, tipo, contenuto)
            else:
                risposta = chiama_gemini(chiave, modello, tipo, contenuto)
        except urllib.error.HTTPError as e:
            dettaglio = e.read().decode("utf-8", "ignore")[:300]
            print(f"ERRORE HTTP {e.code}: {dettaglio}")
            falliti.append((nome, f"HTTP {e.code}"))
            continue
        except Exception as e:
            print("ERRORE:", e)
            falliti.append((nome, str(e)))
            continue

        meta, corpo = separa_front_matter(risposta)
        with open(destinazione, "w", encoding="utf-8") as f:
            f.write(f"---\ntitolo: {meta.get('titolo', ident)}\n"
                    f"gruppo: {meta.get('gruppo', RESIDUO)}\n---\n{corpo}\n")

        voci_nuove.append({"id": ident, "titolo": meta.get("titolo", ident)})
        print("scheda scritta")
        time.sleep(PAUSA)

    percorso_indice = os.path.join(args.out, "index.json")
    if os.path.exists(percorso_indice):
        # L'indice esiste gia' ed e' curato a mano: si tocca solo per aggiungere le
        # schede davvero nuove, mai per riordinare quelle gia' sistemate.
        with open(percorso_indice, encoding="utf-8") as f:
            indice = json.load(f)
        indice, quante_nuove = aggiungi_voci_nuove(indice, voci_nuove)
        if quante_nuove:
            with open(percorso_indice, "w", encoding="utf-8") as f:
                json.dump(indice, f, ensure_ascii=False, indent=2)
                f.write("\n")
            print(f"\n{quante_nuove} schede nuove aggiunte in coda a \"{RESIDUO}\" in {percorso_indice}.")
            print("L'ordine delle schede gia' presenti non e stato toccato: spostale a mano.")
        else:
            print(f"\nNessuna scheda nuova: {percorso_indice} lasciato invariato.")
    elif voci_nuove:
        indice = costruisci_indice_da_zero(args.out)
        with open(percorso_indice, "w", encoding="utf-8") as f:
            json.dump(indice, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"\n{percorso_indice} creato da zero (nessuno esisteva prima).")

    if falliti:
        print("\nNon riuscite:")
        for nome, motivo in falliti:
            print(" -", nome, "->", motivo)
        print("Rilancia lo stesso comando: le schede gia' fatte vengono saltate.")


if __name__ == "__main__":
    main()
