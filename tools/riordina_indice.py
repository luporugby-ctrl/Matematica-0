#!/usr/bin/env python3
"""
Riordina schede/index.json raggruppando gli argomenti in macro-aree coerenti.

Uso:
    python3 tools/riordina_indice.py            # riscrive schede/index.json
    python3 tools/riordina_indice.py --prova    # mostra solo cosa farebbe

Il problema che risolve: le schede sono state generate una dispensa alla volta, quindi
ogni scheda si e scelta il proprio nome di gruppo. Il risultato sono decine di gruppi
da uno o due argomenti. Qui ogni scheda viene ricondotta a una macro-area del programma,
guardando titolo, gruppo dichiarato e nome del file.

Le schede non vengono modificate: cambia solo l'indice.
"""

import argparse
import json
import os
import re
import sys

CARTELLA = "schede"

# L'ordine di questa lista e l'ordine in cui compaiono le sezioni nell'app.
# Il primo gruppo che trova una parola chiave si prende l'argomento, quindi le aree
# piu specifiche vanno prima di quelle generiche.
AREE = [
    # L'ordine di questa lista e l'ordine delle aree nella barra laterale: segue il programma.
    # L'assegnazione invece non dipende dall'ordine, ma da dove compare la parola chiave nel titolo.
    ("Preliminari", [
        "insieme", "insiemi", "numeri reali", "numeri naturali", "valore assoluto",
        "potenza", "potenze", "esponenziale", "logaritmo", "logaritmi",
        "trigonometria", "goniometri", "piano cartesiano", "preliminari",
        "introduzione al corso", "richiami", "calcolo combinatorio",
        "nozionipreli", "potenze", "esponenziali", "trigonometri",
    ]),
    ("Successioni e limiti", [
        "successione", "successioni", "limite", "limiti", "notevole", "notevoli",
        "nepero", "forma indeterminata", "forme indeterminate", "infinitesim",
        "confronto", "carabinieri", "teorema ponte",
        "eselimsuc", "limiti", "notevoli", "nepero", "definizione",
    ]),
    ("Serie numeriche", [
        "serie", "somma parziale", "somme parziali", "criterio", "criteri",
        "convergenza assoluta", "leibniz", "armonica", "geometrica",
        "eseser", "criteri", "termini",
    ]),
    ("Funzioni, continuita e limiti di funzione", [
        "continuita", "continua", "discontinuita", "weierstrass", "zeri",
        "funzione reale", "funzioni reali", "funzione elementare", "funzioni elementari",
        "funzione razionale", "funzioni razionali", "dominio", "funzione composta",
        "funzione inversa", "limite di funzione", "limiti di funzione",
        "continuita", "funzreali", "funzel", "funraz", "funzioni",
    ]),
    ("Calcolo differenziale", [
        "derivata", "derivate", "derivabil", "rapporto incrementale",
        "rolle", "lagrange", "cauchy", "hopital", "taylor", "maclaurin",
        "differenziale", "retta tangente",
        "deri", "derivfunz", "appfor", "formula",
    ]),
    ("Studio di funzione", [
        "studio di funzione", "studio del grafico", "grafico di una funzione",
        "massimo", "minimo", "massimi", "minimi", "concavita", "flesso", "flessi",
        "asintoto", "asintoti", "stugrafun", "massminimo", "grafico",
    ]),
    ("Calcolo integrale", [
        "integrale", "integrali", "primitiva", "primitive", "integrazione",
        "riemann", "per parti", "sostituzione", "improprio", "impropri",
        "intind", "intrie", "intpar", "intim", "eseintimp", "proint",
    ]),
    ("Matrici, determinanti e sistemi lineari", [
        "matrice", "matrici", "determinante", "rango", "gauss", "cramer",
        "sistema lineare", "sistemi lineari", "riduzione a scala", "minore",
        "alggau", "caldet", "prodet", "calran", "ranmat", "sislin", "rissis", "matapp",
    ]),
    ("Spazi vettoriali e applicazioni lineari", [
        "spazio vettoriale", "spazi vettoriali", "sottospazio", "sottospazi",
        "base", "basi", "dimensione", "dipendenza lineare", "indipendenza lineare",
        "combinazione lineare", "applicazione lineare", "applicazioni lineari",
        "nucleo", "immagine di un'applicazione", "vettori", "vettore geometrico",
        "spavet", "sotspave", "dimbas", "diplin", "dipind", "applin", "vetgeo", "nozspavet",
    ]),
]

RESIDUO = "Da ordinare"


def senza_accenti(t):
    tab = str.maketrans("àèéìòùÀÈÉÌÒÙ", "aeeiouAEEIOU")
    return t.translate(tab)


def leggi_front_matter(percorso):
    testo = open(percorso, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---", testo, re.S)
    meta = {}
    if m:
        for riga in m.group(1).splitlines():
            if ":" in riga:
                k, v = riga.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
    if not meta.get("titolo"):
        t = re.search(r"^#\s+(.+)$", testo, re.M)
        meta["titolo"] = t.group(1).strip() if t else os.path.basename(percorso)[:-3]
    return meta


def assegna_area(ident, meta):
    """Vince la parola chiave che compare prima nel titolo, a parita di posizione la piu
    lunga. Il titolo apre la stringa, quindi conta piu del gruppo dichiarato e del nome file:
    'Derivate delle funzioni elementari' va nel calcolo differenziale, non tra le funzioni."""
    spia = senza_accenti(" ".join([
        meta.get("titolo", ""), meta.get("gruppo", ""), ident
    ]).lower())
    migliore, posizione, lunghezza = RESIDUO, 10 ** 6, 0
    for area, parole in AREE:
        for parola in parole:
            p = senza_accenti(parola)
            dove = spia.find(p)
            if dove == -1:
                continue
            if dove < posizione or (dove == posizione and len(p) > lunghezza):
                migliore, posizione, lunghezza = area, dove, len(p)
    return migliore


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prova", action="store_true", help="mostra il risultato senza scrivere")
    ap.add_argument("--cartella", default=CARTELLA)
    args = ap.parse_args()

    if not os.path.isdir(args.cartella):
        sys.exit("Cartella non trovata: " + args.cartella +
                 "\nLancia il comando dalla cartella del progetto.")

    file_md = sorted(f for f in os.listdir(args.cartella) if f.endswith(".md"))
    if not file_md:
        sys.exit("Nessuna scheda in " + args.cartella)

    per_area = {}
    for nome in file_md:
        ident = nome[:-3]
        meta = leggi_front_matter(os.path.join(args.cartella, nome))
        area = assegna_area(ident, meta)
        per_area.setdefault(area, []).append({"id": ident, "titolo": meta["titolo"]})

    ordine = [a for a, _ in AREE if a in per_area]
    if RESIDUO in per_area:
        ordine.append(RESIDUO)

    indice = {"titolo": "Analisi 1 (L-9)", "gruppi": []}
    n = 1
    for area in ordine:
        voci = sorted(per_area[area], key=lambda v: v["titolo"].lower())
        argomenti = []
        for v in voci:
            argomenti.append({"id": v["id"], "num": str(n), "titolo": v["titolo"]})
            n += 1
        indice["gruppi"].append({"gruppo": area, "argomenti": argomenti})

    for g in indice["gruppi"]:
        print(f"\n## {g['gruppo']}  ({len(g['argomenti'])})")
        for a in g["argomenti"]:
            print(f"     {a['num']:>3}  {a['titolo']}")

    print(f"\n{len(file_md)} schede in {len(indice['gruppi'])} aree.")
    if RESIDUO in per_area:
        print(f"Attenzione: {len(per_area[RESIDUO])} schede non riconosciute, "
              f"finite in \"{RESIDUO}\". Puoi spostarle a mano in schede/index.json.")

    if args.prova:
        print("\n(prova: nessun file scritto)")
        return

    percorso = os.path.join(args.cartella, "index.json")
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(indice, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("\nScritto", percorso)


if __name__ == "__main__":
    main()
