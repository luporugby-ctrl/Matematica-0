---
titolo: Teoremi di Fermat, Rolle e Lagrange
gruppo: Calcolo differenziale
---
# Teoremi di Fermat, Rolle e Lagrange

## Prerequisiti
Conoscenza del calcolo dei limiti, della definizione di derivata e del concetto di funzione continua e derivabile in un intervallo.

## Definizioni e notazione del corso
- Intorno sferico: $B_{\delta}(x_0) = \{x \in [a, b] : |x - x_0| < \delta\}$.
- Punto di massimo relativo: $x_0$ tale che $f(x_0) \geq f(x)$ per ogni $x \in B_{\delta}(x_0)$.
- Punto di minimo relativo: $x_0$ tale che $f(x_0) \leq f(x)$ per ogni $x \in B_{\delta}(x_0)$.
- Punto stazionario: punto interno in cui $f'(x_0) = 0$.

## Risultati fondamentali
1. **Teorema di Fermat**: Se $f$ è definita in $[a, b]$, $x_0 \in (a, b)$ è un estremo relativo e $f$ è derivabile in $x_0$, allora $f'(x_0) = 0$.
2. **Proposizione sui punti di frontiera**: Se $x_0 = a$ è massimo, $f'(a) \leq 0$. Se $x_0 = b$ è massimo, $f'(b) \geq 0$.
3. **Teorema di Rolle**: Se $f$ è continua in $[a, b]$, derivabile in $(a, b)$ e $f(a) = f(b)$, allora esiste almeno un $x_0 \in (a, b)$ tale che $f'(x_0) = 0$.
4. **Teorema di Lagrange**: Se $f$ è continua in $[a, b]$ e derivabile in $(a, b)$, allora esiste $x_0 \in (a, b)$ tale che $f'(x_0) = \frac{f(b) - f(a)}{b - a}$.

## Metodi risolutivi usati nel corso
- Per verificare i teoremi, accertarsi preventivamente della continuità nell'intervallo chiuso e della derivabilità in quello aperto.
- Per il Teorema di Lagrange, calcolare il coefficiente angolare della secante $\frac{f(b) - f(a)}{b - a}$ ed eguagliarlo alla derivata prima $f'(x)$.
- Per funzioni definite a tratti, verificare la continuità e derivabilità nei punti di giunzione prima di applicare i teoremi.

## Errori tipici da segnalare allo studente
- Pensare che $f'(x_0) = 0$ sia una condizione sufficiente per l'esistenza di un massimo o minimo (es. $f(x) = x^3$ in $x=0$).
- Dimenticare di verificare le ipotesi di continuità su tutto l'intervallo $[a, b]$ prima di applicare Rolle o Lagrange.
- Confondere gli estremi relativi con gli estremi assoluti.
- Applicare i teoremi in punti di non derivabilità della funzione.

## Tipologie di esercizio da generare
- Esercizi di verifica dell'applicabilità dei teoremi (Rolle/Lagrange) su funzioni date.
- Ricerca del punto $x_0$ la cui esistenza è garantita dal Teorema di Lagrange o di Rolle per funzioni assegnate.
- Quesiti di teoria sui controesempi (es. funzione derivabile con derivata nulla in un punto che non è massimo né minimo).
- Analisi di funzioni a tratti per verificare se soddisfano le ipotesi dei teoremi negli intervalli dati.
