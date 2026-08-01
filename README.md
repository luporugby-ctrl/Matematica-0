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

Ogni scheda e' un file Markdown con questa struttura:

- Prerequisiti
- Definizioni e notazione del corso
- Risultati fondamentali
- Metodi risolutivi usati nel corso
- Errori tipici da segnalare allo studente
- Tipologie di esercizio da generare

Le schede sono riassunti sintetici (1-2k token), non trascrizioni delle dispense: servono a
dare al modello la notazione e i metodi del corso senza saturare il contesto a ogni chiamata.

## Riordinare l'indice

Le schede vengono generate una dispensa alla volta, quindi ognuna si sceglie il proprio nome di
gruppo e l'indice esce frammentato. Per ricondurre tutto a poche macro-aree del programma:

```bash
python3 tools/riordina_indice.py --prova   # mostra il risultato senza scrivere
python3 tools/riordina_indice.py           # riscrive schede/index.json
```

Lo script legge titolo e gruppo dal front matter di ogni scheda e assegna l'area guardando quale
parola chiave compare per prima nel titolo. Le schede non vengono toccate: cambia solo l'indice.
Quello che non riconosce finisce nel gruppo "Da ordinare", cosi si vede subito e si sposta a mano.
Le aree e le loro parole chiave sono in cima al file, nella lista `AREE`.

## Le due sezioni

La barra laterale mostra sempre due sezioni:

- **Basi - Matematica 0**: i 27 argomenti di ripasso (frazioni, potenze, radicali, polinomi,
  equazioni, disequazioni, logaritmi, goniometria). Sono integrati nel codice e non hanno
  scheda: l'AI genera esercizi dal titolo dell'argomento, come nella prima versione dell'app.
  Limiti e limiti notevoli non stanno qui ma in Analisi 1, dove hanno la loro scheda.
- **Analisi 1**: gli argomenti caricati da `schede/index.json`, ciascuno con la sua scheda.

Le basi restano disponibili anche se `schede/index.json` manca o non carica.

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

## Teoria e domande di chiarimento

Sotto la spiegazione della teoria c'e un campo per chiedere chiarimenti su quella spiegazione.
Lo scambio resta in memoria finche non si cambia argomento, cosi le domande successive
tengono conto delle precedenti. La spiegazione stessa viene passata al modello come contesto,
quindi le risposte restano ancorate a quello che si sta leggendo invece di ripartire da zero.

## Grafici

Quando genera esercizi o teoria, il modello aggiunge un blocco `grafici` in coda alla risposta:

```
[{"n":1,"titolo":"parabola","f":["x**2-4"],"x":[-5,5]}]
```

L'app lo estrae, lo toglie dal testo e disegna un piano cartesiano per ciascuna voce, su canvas.
Si puo trascinare per spostarsi, usare la rotella per ingrandire e fare doppio clic per rimettere
a posto la vista.

Le espressioni in `f` sono in sintassi JavaScript (`*` per moltiplicare, `**` per le potenze).
Prima di essere valutate passano da `compilaEspressione`, che accetta soltanto numeri, la variabile
`x`, gli operatori e una lista chiusa di funzioni (`sin`, `cos`, `tan`, `arctan`, `exp`, `log`,
`sqrt`, `abs` e poche altre). Qualsiasi altro identificatore fa fallire la compilazione, quindi una
risposta malformata produce al massimo un grafico in meno, mai codice eseguito.

Ci sono tre forme:

- **funzione**: `{"f":["x**2-4"],"x":[-5,5]}`
- **definita a tratti**, per continuita e discontinuita:
  `{"tratti":[{"e":"x+1","a":1},{"e":"x**2","da":1}],"buchi":[[1,2,"vuoto"],[1,1,"pieno"]]}`
  I pallini vuoti e pieni mostrano quale valore la funzione assume davvero nel punto critico.
- **successione o serie**: `{"tipo":"successione","a":"1/n**2","nmax":40,"somme":true,"limite":1.6449}`
  Con `somme` il grafico disegna le somme parziali, cioe la convergenza vista a occhio.

Non tutto e rappresentabile: matrici, sistemi lineari, rango e dimostrazioni astratte non
producono grafici, ed e il modello stesso a ometterli.

## Prontuario e vocabolario

Il pulsante **Prontuario e vocabolario** in alto apre un pannello di consultazione, sempre
raggiungibile qualunque argomento sia selezionato. Contiene due schede:

- **Vocabolario**: i termini e i simboli del corso, con la ricerca. Il contenuto sta in
  `riferimenti/vocabolario.json`. Per aggiungere una voce basta una riga:
  `{ "termine": "...", "simbolo": "...", "significato": "...", "esempio": "..." }`
  (`simbolo` ed `esempio` sono facoltativi). La ricerca guarda anche dentro i significati.
- **Schede di sopravvivenza**: i formulari veloci, in Markdown con LaTeX. Per aggiungerne una,
  crea il file in `riferimenti/` e registralo in `riferimenti/index.json`.

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
