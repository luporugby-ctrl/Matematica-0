---
titolo: Integrali Impropri: Definizione e Convergenza
gruppo: Calcolo integrale
---
# Integrali Impropri

## Prerequisiti
Conoscenza del calcolo integrale (integrale di Riemann), tecniche di integrazione immediata, per sostituzione e per parti. Padronanza dei limiti e del comportamento asintotico delle funzioni.

## Definizioni e notazione del corso
L'integrale improprio è definito come il limite di un integrale definito su un intervallo che viene progressivamente esteso verso un punto di singolarità (funzione non limitata) o verso l'infinito.
- Se $f(x)$ non è limitata vicino a $a^+$, allora: $\int_{a}^{b} f(x) dx = \lim_{c \to a^+} \int_{c}^{b} f(x) dx$.
- Se l'intervallo è $[a, +\infty)$, allora: $\int_{a}^{+\infty} f(x) dx = \lim_{c \to +\infty} \int_{a}^{c} f(x) dx$.

## Risultati fondamentali
1. Integrale della funzione potenza $x^{-\alpha}$ su $(0, 1]$: converge se $\alpha < 1$, diverge se $\alpha \ge 1$.
2. Integrale della funzione potenza $x^{-\alpha}$ su $[1, +\infty)$: converge se $\alpha > 1$, diverge se $\alpha \le 1$.
3. Criterio del confronto: dati $0 \le f(x) \le g(x)$, se $\int g$ converge, allora converge anche $\int f$.
4. Corollario del confronto asintotico: se $f$ è non negativa e $\lim_{x \to \infty} x^\alpha f(x) = 0$ con $\alpha > 1$, allora l'integrale su $[a, +\infty)$ converge.
5. Criterio della convergenza assoluta: se $\int |f(x)| dx$ converge, allora converge anche $\int f(x) dx$.

## Metodi risolutivi usati nel corso
- Scomposizione dell'intervallo: se una funzione presenta punti di singolarità interni all'intervallo $(a, b)$, l'integrale va spezzato in somma di integrali su sotto-intervalli.
- Calcolo esplicito: si calcola la primitiva, si valuta l'integrale definito nell'intervallo $[a, c]$ e si calcola il limite per $c$ che tende alla singolarità o a infinito.
- Analisi asintotica: si confronta la funzione integranda con una funzione campione ($x^{-\alpha}$) per stabilire la convergenza senza calcolare la primitiva.

## Errori tipici da segnalare allo studente
1. Considerare convergente un integrale improprio solo perché il limite della funzione integranda è zero (non è una condizione sufficiente).
2. Dimenticare di spezzare l'integrale quando la funzione presenta una singolarità in un punto interno all'intervallo di integrazione.
3. Confondere le condizioni di convergenza per $\alpha$ tra l'intervallo limitato con singolarità in zero e l'intervallo illimitato.
4. Applicare i criteri di confronto su funzioni che cambiano segno senza verificarne la convergenza assoluta.

## Tipologie di esercizio da generare
- Esercizi di calcolo diretto: calcolare il valore esatto di integrali impropri su intervalli illimitati o con singolarità.
- Esercizi di test a scelta multipla: verificare se un dato integrale converge o diverge, o indovinarne il valore.
- Esercizi teorico-pratici: utilizzare il criterio del confronto o il confronto asintotico per determinare la convergenza di funzioni complesse (es. frazioni razionali, prodotti con logaritmi).
