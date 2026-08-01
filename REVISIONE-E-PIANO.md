# Revisione del progetto e piano di lavoro

Revisione completa (tecnica, visiva, logica, didattica) di Matematica-0.
Ogni intervento è numerato, con file, punto esatto e criterio di accettazione,
pensato per essere eseguito da modelli economici (Haiku/Sonnet) un task alla volta.

**VINCOLO NON NEGOZIABILE:** le 59 schede in `schede/` rispecchiano una a una le 59
unità didattiche del programma universitario reale di Analisi Matematica 1, generate
dalle dispense ufficiali del corso. Nessuna scheda va aggiunta, rimossa, fusa o
rinominata. Si può intervenire solo su: l'ORDINE in `schede/index.json`, la correzione
di errori puntuali di merito (Fase 3.1), e la normalizzazione del campo `gruppo:` nel
front matter. Qualunque task che sembri richiedere altro sui contenuti delle schede va
fermato e riportato all'utente.

Giudizio d'insieme: il progetto è solido e ben pensato. L'idea "un solo file, nessun
backend, contenuto separato dal codice" è giusta ed è rispettata con coerenza. Il sistema
visivo "quaderno a quadretti" è bello e va conservato: gli interventi visivi proposti lo
raffinano, non lo sostituiscono. La struttura delle schede in sei sezioni (Prerequisiti /
Definizioni / Risultati / Metodi / Errori tipici / Tipologie di esercizio) è esattamente
ciò che serve a un tutor AI: da docente, è la parte migliore del progetto.

I problemi veri sono pochi e concentrati: due bug logici nelle statistiche, la correzione
non ancorata a soluzioni di riferimento, e l'ordinamento dell'indice che produce una
sequenza didattica sbagliata (Taylor prima della definizione di derivata, l'Hôpital
prima delle derivate).

---

## FASE 0 — Correzioni banali (modello: Haiku)

### 0.1 Percorso sbagliato nel README
`riordina_indice.py` sta nella radice del repo, ma il README (righe 54-55) dice
`python3 tools/riordina_indice.py`. Spostare il file in `tools/` (coerente con
`genera_schede.py`) e verificare che il README ora corrisponda.
**Accettazione:** `python3 tools/riordina_indice.py --prova` funziona dalla radice.

### 0.2 Codice morto
In `index.html`: `updateKeyStatus(hasKey)` ignora il parametro e chiama solo
`aggiornaConfigUI()` — eliminare la funzione e sostituire le chiamate.
**Accettazione:** nessun riferimento residuo, app invariata.

### 0.3 Favicon e meta
Manca favicon e `<meta name="description">`. Aggiungere favicon inline
(SVG data-URI con il glifo ∫, coerente col benvenuto) e una descrizione breve.
**Accettazione:** niente 404 su favicon, tab con icona.

### 0.4 Toast sovrapposti
`showToast` appende ogni toast come elemento `position:fixed` nello stesso punto:
due toast ravvicinati si sovrappongono. Creare un contenitore fisso che li impila.
**Accettazione:** due toast consecutivi visibili uno sopra l'altro.

### 0.5 Formule larghe su mobile
Le formule display di MathJax sfondano il pannello sugli schermi stretti.
Aggiungere `mjx-container[display="true"]{overflow-x:auto;overflow-y:hidden;max-width:100%}`.
**Accettazione:** una formula lunga scorre nel suo riquadro, la pagina non scrolla in orizzontale.

---

## FASE 1 — Bug logici e affidabilità del tutor (modello: Sonnet) — LA PIÙ IMPORTANTE

### 1.1 KPI "Precisione" rotto due volte
In `updateKPIs` (index.html, ~riga 1902):
1. `updateKPIs('generate')` incrementa `stats.totalSubmissions`: generare esercizi
   conta come una consegna e sgonfia la precisione.
2. In `checkAnswers` la correttezza è dedotta con
   `response.includes("esatto")` — che matcha anche "inesatto" e "non esatto",
   e comunque valuta l'intera consegna (10 esercizi) come un unico giusto/sbagliato.

**Soluzione (unica, per entrambi):** chiedere al modello di chiudere la correzione con un
blocco strutturato, con lo stesso meccanismo già usato per i grafici:

```
```esiti
[{"n":1,"esito":"giusto"},{"n":2,"esito":"sbagliato"},{"n":3,"esito":"non_svolto"}]
```
```

Estrarlo con una `estraiEsiti` gemella di `estraiGrafici`, toglierlo dal testo mostrato,
e contare i giusti/sbagliati per esercizio. `totalSubmissions` diventa "esercizi valutati".
Etichetta del KPI: "Precisione" → chiaro perché ora è (giusti / valutati).
**Accettazione:** generare esercizi non tocca la precisione; una correzione con 6 giusti
su 8 svolti mostra 75%; "la risposta è inesatta" non conta come giusto.

### 1.2 Correzione non ancorata: il tutor corregge alla cieca
Oggi il modello genera esercizi senza soluzioni, e alla correzione deve rifare i conti
da zero: è il punto in cui un modello economico sbaglia più spesso, e mina la fiducia
nello strumento. **Soluzione:** in `generateExercises` chiedere anche un blocco

```
```soluzioni
[{"n":1,"risultato":"x=5","passaggi_chiave":"raccogliere n^2 ..."}]
```
```

Estrarlo, NON mostrarlo mai, salvarlo in una variabile (`currentSolutions`) e passarlo
al prompt di correzione e alla guida passo-passo come `<SoluzioniRiservate>` con
l'istruzione esplicita di non rivelarle mai, usarle solo per giudicare.
**Accettazione:** il blocco non compare mai a schermo; il prompt di `checkAnswers` e
`startGuidedSession`/`sendGuidedStep` lo contiene; la correzione cita risultati coerenti.

### 1.3 marked corrompe il LaTeX
`marked.parse` gira PRIMA di MathJax: dentro `$...$` gli underscore e gli asterischi
vengono interpretati come corsivo/grassetto (es. `$a_n + b_n$ ... $c_n$` su una riga
produce `<em>`). Soluzione standard: prima di `marked.parse`, mascherare i segmenti
`$$...$$`, `$...$`, `\(...\)`, `\[...\]` con placeholder, poi ripristinarli dopo il parse.
Applicarla in un'unica funzione `renderMarkdownConMatematica(testo)` usata da tutti i
punti che oggi chiamano `marked.parse` (teoria, esercizi, feedback, chat, guida, schede).
**Accettazione:** una risposta con `$a_n$ e $b_n$ e $x^{*}$` nella stessa riga si
visualizza correttamente.

### 1.4 Risposte troncate senza accorgersene
`callAnthropic` usa `max_tokens: 4000`: 10 esercizi + LaTeX + blocco grafici + soluzioni
possono superarli, e il troncamento mangia proprio i blocchi in coda. Portare a 8000,
leggere `stop_reason` (Anthropic) e `finishReason` (Gemini) e, se troncato, avvisare con
un toast ("Risposta troncata: rigenera o scegli un modello più capiente").
**Accettazione:** stop_reason ≠ "end_turn" produce l'avviso.

### 1.5 Errori API con alert()
`callAI` usa `alert(...)`: bloccante e fuori stile. Sostituire con un pannello di errore
inline nel foglio (stesso stile `.esito-ko`), con il dettaglio e i suggerimenti attuali
(404 modello dismesso, 401/403 chiave, 429 quota).
**Accettazione:** nessun `alert` residuo per gli errori API.

### 1.6 Richieste non annullabili
Il velo di attesa copre tutto e non si può interrompere una chiamata partita per sbaglio.
Usare `AbortController` in `callGemini`/`callAnthropic` e aggiungere un bottone
"Annulla" nel velo di attesa.
**Accettazione:** cliccando Annulla il velo sparisce e la fetch viene abortita.

### 1.7 Sanitizzazione dell'HTML generato
Tutto l'output del modello finisce in `innerHTML` via marked, senza sanitizer. Il rischio
è basso (chiave e contenuti propri) ma la difesa costa poco: aggiungere DOMPurify da CDN
e passarci l'output di marked nella funzione unica del punto 1.3.
**Accettazione:** `<img onerror=...>` in una risposta non esegue nulla.

### 1.8 Statistiche volatili
`stats` si azzera a ogni reload mentre i moduli completati sopravvivono: incoerente.
Persistere `stats` in localStorage accanto a `tutor_moduli_completati`.
**Accettazione:** dopo un reload i contatori restano.

---

## FASE 2 — Indice e ordinamento didattico (modello: Sonnet, revisione finale umana)

### 2.1 Il problema
`riordina_indice.py` ordina gli argomenti ALFABETICAMENTE dentro ogni area
(riga 156: `sorted(..., key=lambda v: v["titolo"].lower())`), e `genera_schede.py`
fa lo stesso. Risultato attuale in `schede/index.json`:
- "Calcolo dei limiti mediante de l'Hôpital" è il n. 5, PRIMA che esista la derivata
  (l'Hôpital è al posto sbagliato anche di area: sta in "Successioni e limiti" perché
  `senza_accenti` non converte la "ô" e la keyword "hopital" non matcha "hôpital";
  il suo front matter dice correttamente "Calcolo differenziale");
- "Formula di Taylor" è il n. 27, la "Definizione di derivata" il n. 29;
- "Uniforme continuità e Teorema Fondamentale del Calcolo" (front matter: Calcolo
  integrale) è finita in "Funzioni e continuità" al n. 26, prima di derivate e integrali.

### 2.2 La soluzione di fondo
`schede/index.json` diventa curato a mano e fonte di verità. Gli script servono solo
al bootstrap: `genera_schede.py` NON deve riscrivere `index.json` se il file esiste già
(aggiunga solo le voci nuove in coda a "Da ordinare"), e `riordina_indice.py` va
documentato come strumento una-tantum.
**Accettazione:** rigenerare una scheda non tocca l'ordine dell'indice.

### 2.3 Fix minori negli script
- `senza_accenti` (riordina_indice.py riga 89): usare `unicodedata.normalize('NFD')`
  + rimozione dei combining, come già fa `normalizza()` in index.html, così "hôpital",
  "î", "ü" ecc. sono coperti.
- Eliminare la logica di indicizzazione duplicata: `scrivi_indice` in genera_schede.py
  e il main di riordina_indice.py fanno lo stesso lavoro con regole diverse.

### 2.4 Sequenza proposta per index.json (da validare sul programma reale del corso)
Numerazione progressiva, ordine dentro i gruppi:

1. **Preliminari:** NozioniPreli → MassMinimoMe → 55Mercatorum → combinepdfMe
   (nota: 55Mercatorum e combinepdfMe si sovrappongono su estremi/induzione — vedi 3.2)
2. **Successioni e limiti:** LimitiMercat → EseLimSucMer → StampaMercat →
   NeperoMercat → DefinizioneM (teorema ponte) → NotevoliMerc → PotenzeMerca
3. **Serie numeriche:** IntroMercato → SerieMercato → TerminiMerca → EseSerNumMer
4. **Funzioni e continuità:** FunzRealiMer → Esponenziali → Trigonometri →
   GraficoMerca → FunzioniMerc → TeoremaMerca → WeierstrassM → ContinuitaMe
5. **Calcolo differenziale:** DerivataMerc → FunzElMercat → DerivFunz3Me →
   TeoremiMerca → CalcoloMerca (l'Hôpital) → FormulaMerca → AppForMercat
6. **Studio di funzione:** Criteri2Merc → StuGraFunMer
7. **Calcolo integrale:** IntRieMercat → ProIntMercat → DeriMercator (TFC) →
   IntIndMercat → IntParMercat → SosSpeMercat → FunRazMercat → IntImMercato →
   EseIntImpMer
8. **Spazi vettoriali:** VetGeo2Merca → NozSpaVetMer → SotSpaVeMerc → EseSpaVetMer →
   DipLinVet3Me → DipIndLinSis → DimBasSpaVet
9. **Matrici, applicazioni lineari e sistemi:** MatAppMercat → AppLin2Merca →
   EseAppLinMer → CalDetMercat → ProDetMercat → AlgGauMercat → RisSis2Merca →
   CalRanMercat → RanMat2Merca → SisLinEquMer → SisLinIntMer

**Accettazione:** l'indice nell'app mostra questa sequenza; nessun argomento usa
strumenti introdotti dopo di lui.

### 2.5 "Analisi 1" contiene metà algebra lineare
16 schede hanno gruppo "Algebra Lineare": metterle sotto la sezione "Analisi 1" è
fuorviante. Nella barra laterale usare tre sezioni: "Basi · Matematica 0",
"Analisi 1", "Algebra lineare" (basta un campo `sezione` nei gruppi di index.json e
una piccola modifica a `loadSyllabus`).
**Accettazione:** tre sezioni richiudibili, conteggi separati.

---

## FASE 3 — Contenuti delle schede (modello: Sonnet con revisione, o Opus)

La qualità matematica campionata è buona: definizioni di limite, criterio di Cauchy,
somme di Riemann, criteri per le serie, tabella delle derivate e valori di arctan nelle
schede di sopravvivenza sono tutti corretti. Interventi puntuali:

### 3.1 Correzioni di merito
- **NeperoMercat.md, "Errori tipici" n. 3:** la frase è contorta e si contraddice
  ("può essere di Cauchy solo se... ma se non converge non può essere di Cauchy").
  Riscrivere: "In ℝ una successione limitata ma non convergente non è mai di Cauchy:
  Cauchy ⟺ convergente. La limitatezza garantisce solo sottosuccessioni convergenti."
- **LimitiMercat.md, definizione di successione:** "$a_n: \mathbb{N} \to \mathbb{R}$"
  confonde la funzione ($a$) col suo valore ($a_n$). Scrivere
  "$a: \mathbb{N} \to \mathbb{R}$, $n \mapsto a_n$".
- **DerivataMerc.md, Risultati n. 3:** riporta solo $\frac{d}{dx}x^2 = 2x$; aggiungere
  la regola generale $\frac{d}{dx}x^n = nx^{n-1}$ (verificare prima che la dispensa la
  introduca a questo punto del corso).
- **Front matter incoerenti:** i `gruppo:` delle schede usano nomi liberi
  ("Algebra Lineare", "Calcolo Integrale", "Analisi Matematica 1 - Calcolo dei limiti"...).
  Normalizzarli ai 9 nomi della sequenza 2.4, così ogni strumento futuro li legge uguali.

### 3.2 Schede su argomenti affini — NESSUNA AZIONE
Alcune unità didattiche coprono lo stesso argomento da angolazioni diverse (es.
IntImMercato/EseIntImpMer sugli impropri; le cinque UD su rango e sistemi): rispecchiano
dispense distinte del corso reale, quindi restano tutte, così come sono, con i loro
titoli. L'unico strumento per orientare lo studente è l'ordine dell'indice (Fase 2.4),
che mette la scheda di teoria prima di quella di esercitazione.

### 3.3 Perimetro del programma — NESSUNA AZIONE
Il programma è definito dalle 59 UD caricate: è completo per definizione. Non vanno
generate schede per argomenti "mancanti" (numeri complessi, equazioni differenziali,
ecc.): se non hanno una dispensa, non sono nel corso.

### 3.4 Nuove schede di sopravvivenza (riferimenti/)
Le due esistenti (limiti, derivate) sono ben fatte. Aggiungere con lo stesso stile:
- "Serie: quale criterio uso?" (albero di decisione: condizione necessaria → confronto
  asintotico → rapporto/radice → Leibniz);
- "Primitive immediate" (tabella speculare a quella delle derivate);
- "Studio di funzione: la checklist" (dominio → simmetrie → segno → limiti/asintoti →
  f' → f'' → grafico).
Registrarle in `riferimenti/index.json`.

---

## FASE 4 — Rifiniture visive (modello: Sonnet)
Il sistema "quaderno" resta: questi interventi lo rafforzano.

### 4.1 Il margine rosso del quaderno
Sul `.foglio`, aggiungere la riga verticale del margine (come nei quaderni veri):
un `background` aggiuntivo `linear-gradient` verticale color `--rossa` al 10% di opacità,
posizionato a ~64px da sinistra, sotto i quadretti. Solo desktop (nasconderla <820px).
**Accettazione:** riga sottile visibile ma discreta, non interferisce col contenuto.

### 4.2 Esercizi leggibili, non un muro di testo
Oggi i 10 esercizi sono un flusso markdown. Chiedere al modello di separarli con `---`
e, via CSS/JS, renderizzare ogni esercizio in un blocco con: numero grande in stile
`.voce-num`, spazio bianco sotto ("spazio per i conti"), e bordo tratteggiato tra
esercizi. Nessuna nuova dipendenza: solo split sul separatore e wrapping in div.
**Accettazione:** dieci blocchi distinti, numerati, ariosi.

### 4.3 Attesa non bloccante
Sostituire il velo a schermo intero con uno stato di caricamento DENTRO il pannello
interessato (skeleton con i tre puntini esistenti): mentre si genera si può ancora
leggere la teoria o consultare il prontuario. Il bottone Annulla di 1.6 vive lì.
**Accettazione:** durante una generazione il resto dell'app resta usabile.

### 4.4 Progresso per sezione
"Moduli superati 0/86" mescola basi e corso. Mostrare il conteggio per sezione
(es. "Basi 12/27 · Analisi 5/43 · Algebra 0/16") sotto la barra, che resta globale.
**Accettazione:** i tre conteggi si aggiornano al toggle di un modulo.

### 4.5 Quaderno di sera (dark mode)
Variante `prefers-color-scheme: dark` + toggle manuale: carta `#1E2126`, quadretti
`#2A2F35`, inchiostro che passa a un indaco chiaro `#8F8AE0`, grafite invertita.
I canvas dei grafici leggono i colori da variabili CSS invece che da costanti.
**Accettazione:** contrasto AA su testo normale in entrambi i temi.

### 4.6 Micro-dettagli
- `.velo` (prontuario/config): chiudere anche cliccando sullo sfondo, non solo con ✕/Esc.
- Focus trap nei modali (tab resta dentro finché aperti).
- Pinch-zoom sui canvas dei grafici (due pointer → scala), oggi c'è solo la rotella.

---

## FASE 5 — Didattica avanzata (opzionale, modello: Opus o Sonnet ben guidato)

### 5.1 La valvola di sfogo sulla filosofia "mai dare il risultato"
La scelta di non rivelare i risultati è pedagogicamente difendibile (sforzo produttivo),
ma senza uscita di sicurezza produce frustrazione e abbandono sull'esercizio sbagliato
tre volte. Proposta: dopo 2 tentativi falliti sullo stesso esercizio (tracciabili ora
che esiste il blocco `esiti` di 1.1), compare "Mostrami la soluzione completa" che fa
generare lo svolgimento commentato passo-passo, e l'esercizio si conta come "visto,
non superato". Il divieto resta il default: cade solo su richiesta esplicita e solo
dopo tentativi reali.

### 5.2 Dosaggio degli esercizi
"Sempre esattamente 10" è rigido: aggiungere una scelta 5/10 ("ripasso veloce" /
"allenamento completo"). La difficoltà crescente resta.

### 5.3 Mini-schede per Matematica 0
Le basi generano esercizi dal solo titolo: la notazione può divergere da quella del
corso. Generare una volta sola 27 mini-schede (anche 10 righe l'una: notazione, 3 errori
tipici, 3 tipologie d'esercizio) con `genera_schede.py` o a mano, così anche le basi
hanno la loro `<SchedaDelCorso>`.

### 5.4 Vocabolario nel contesto
Quando si genera teoria per un argomento, passare al modello le 5-10 voci del
vocabolario pertinenti (match sul titolo), così il lessico resta identico a quello del
prontuario che lo studente consulta.

---

## Ordine di esecuzione consigliato

| Priorità | Fase | Perché |
|---|---|---|
| 1 | Fase 1 (1.1, 1.2, 1.3) | Sono i bug che toccano la fiducia nel tutor: statistiche false, correzioni non ancorate, formule rotte |
| 2 | Fase 2 | L'ordine del programma è la spina dorsale didattica |
| 3 | Fase 0 + resto Fase 1 | Pulizia veloce |
| 4 | Fase 3 | Contenuti: pochi fix mirati, poi le schede nuove |
| 5 | Fase 4 | Estetica |
| 6 | Fase 5 | Evoluzioni |

Regola pratica per contenere i costi: un task per sessione, Haiku per la Fase 0,
Sonnet per tutto il resto, Opus solo per 2.4 (validazione della sequenza) e per la
Fase 5. Ogni task ha già il suo criterio di accettazione: verificarlo prima di passare
al successivo.
