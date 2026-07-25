---
titolo: Formula di Taylor e applicazioni allo studio locale
gruppo: Calcolo differenziale
---
# Formula di Taylor e applicazioni allo studio locale

## Prerequisiti
Conoscenza di limiti, derivate di funzioni elementari, studio di funzioni, definizione di intorni e continuità.

## Definizioni e notazione del corso
- La notazione di Landau $o(x^n)$ è usata per indicare infinitesimi di ordine superiore.
- Una funzione è di classe $C^k(A)$ se ammette derivate continue fino all'ordine $k$ nell'insieme $A$.
- Sviluppo di Maclaurin: polinomio di Taylor centrato in $x_0 = 0$.
- Intorno sferico: $B_{\delta}(x_0) = (x_0 - \delta, x_0 + \delta)$.

## Risultati fondamentali
1. **Primo criterio (derivate seconde):** Se $f'(x_0) = 0$ e $f''(x_0) > 0$ ($<0$), allora $x_0$ è punto di minimo (massimo) relativo.
2. **Secondo criterio (ordine superiore):** Sia $f$ di classe $C^n$ con $f'(x_0) = \dots = f^{(n-1)}(x_0) = 0$ e $f^{(n)}(x_0) \neq 0$:
   - Se $n$ è pari e $f^{(n)}(x_0) > 0$ ($<0$), allora $x_0$ è minimo (massimo) relativo.
   - Se $n$ è dispari, $x_0$ non è né massimo né minimo.
3. **Sviluppo di Maclaurin generale:** $f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(0)}{k!} x^k + o(x^n)$.
4. **Algebra degli o-piccoli:** Regole formali per gestire il resto di Peano durante operazioni di somma, prodotto, composizione e potenze di infinitesimi (es. $o(x^\alpha) \cdot o(x^\beta) = o(x^{\alpha+\beta})$).

## Metodi risolutivi usati nel corso
- **Calcolo di limiti:** Sostituzione delle funzioni presenti nel limite con il relativo polinomio di Maclaurin troncato all'ordine necessario per eliminare la forma indeterminata.
- **Algebra degli o-piccoli:** Semplificazione rigorosa dei termini trascurabili in espressioni complesse.
- **Studio di punti critici:** Utilizzo delle derivate successive per determinare la natura dei punti in cui la derivata prima si annulla.
- **Sostituzione:** Uso di cambi di variabile (es. $y = -x^2$) negli sviluppi noti per ottenere sviluppi di funzioni composte.

## Errori tipici da segnalare allo studente
1. **Troncamento errato:** Fermarsi a un ordine troppo basso del polinomio di Maclaurin, che non permette di "liberarsi" dell'infinitesimo al denominatore.
2. **Uso improprio dell'algebra degli o-piccoli:** Trattare gli o-piccoli come quantità algebriche generiche (es. sommare o-piccoli senza considerare il grado minimo).
3. **Scambio di parità:** Confondere la condizione per $n$ pari e dispari nel secondo criterio per i massimi e minimi.
4. **Argomenti errati:** Applicare lo sviluppo di Maclaurin in $x=0$ a funzioni i cui argomenti non tendono a 0.

## Tipologie di esercizio da generare
- Determinazione della natura di un punto critico (massimo o minimo) tramite derivazione di ordine superiore.
- Calcolo di limiti di forme indeterminate del tipo $0/0$ tramite approssimazione polinomiale.
- Determinazione dello sviluppo di Maclaurin per funzioni composte o prodotto di funzioni elementari.
- Identificazione corretta del polinomio di Maclaurin troncato all'ordine $n$ per una data funzione.
