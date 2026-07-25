# Matematica 0 e Analisi 1

Generatore di esercizi con tutor AI, basato sulle dispense del corso.

L'app e' un unico file `index.html`: nessun build, nessun backend. Si apre da GitHub Pages
o da qualsiasi server statico locale.

## Come funziona

1. Scegli il motore AI (Gemini o Claude) e incolla la tua chiave. Resta nel browser, in `localStorage`.
2. Scegli un argomento dalla barra laterale.
3. L'app carica la **scheda** di quell'argomento e la passa al modello insieme alla richiesta.
4. Puoi chiedere la teoria, generare 10 esercizi, farti correggere, o farti guidare passo-passo.

## Le schede

Il contenuto e' separato dal codice. L'app legge `schede/index.json` all'avvio e, quando
selezioni un argomento, carica `schede/<id>.md`.

`schede/index.json`:

```json
{
  "titolo": "Analisi 1 (L-9)",
  "gruppi": [
    {
      "gruppo": "1. Successioni e limiti",
      "argomenti": [
        { "id": "A01", "num": "1", "titolo": "Limiti notevoli di funzioni trigonometriche" }
      ]
    }
  ]
}
```

Ogni scheda e' un file Markdown con questa struttura (vedi `schede/A01.md`):

- Prerequisiti
- Definizioni e notazione del corso
- Risultati fondamentali
- Metodi risolutivi usati nel corso
- Errori tipici da segnalare allo studente
- Tipologie di esercizio da generare

Le schede sono riassunti sintetici (1-2k token), non trascrizioni delle dispense: servono a
dare al modello la notazione e i metodi del corso senza saturare il contesto a ogni chiamata.

Se `schede/index.json` non e' raggiungibile, l'app ricade sul programma di Matematica 0
integrato nel codice, cosi' resta comunque utilizzabile.

## Generare le schede dalle dispense

Le schede si producono una volta sola, con uno script che gira sul tuo computer.
Le dispense non entrano mai nel repository: lo script le legge da una cartella locale
(che puo' essere anche una cartella sincronizzata da Google Drive) e scrive solo i `.md`.

```bash
pip install pillow pypdfium2
export AI_API_KEY="la-tua-chiave"

python3 tools/genera_schede.py ~/dispense --provider gemini --dry-run   # controlla cosa legge
python3 tools/genera_schede.py ~/dispense --provider gemini             # genera davvero
```

Lo script riconosce i PDF con testo, i PDF scansionati e gli archivi ZIP di immagini.
Si puo' interrompere in qualsiasi momento: al rilancio salta le schede gia' scritte.
Alla fine `schede/index.json` viene ricostruito raggruppando gli argomenti per macro-area.

Rileggi le schede prima di commettere: il modello puo' sbagliare un titolo o mettere un
argomento nel gruppo sbagliato, e correggere un file di 2 KB costa dieci secondi.

Poi basta:

```bash
git add schede/ && git commit -m "schede Analisi 1" && git push
```

## Aprire l'app in locale

`fetch` non funziona su `file://`, serve un server:

```bash
python3 -m http.server 8000
# poi apri http://localhost:8000
```

## Motori AI supportati

| Provider | Chiave | Note |
|---|---|---|
| Google Gemini | https://aistudio.google.com/apikey | ha un piano gratuito |
| Anthropic Claude | https://console.anthropic.com/settings/keys | a consumo |

I modelli si aggiornano nell'oggetto `PROVIDERS` in cima allo script. Se un modello viene
dismesso l'API risponde 404: basta selezionarne un altro dal menu.
