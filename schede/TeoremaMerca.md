---
titolo: Funzioni continue, Teorema Zeri e Bisezione
gruppo: Funzioni, continuita e limiti di funzione
---
# Funzioni continue: Teorema degli Zeri e Bisezione

## Prerequisiti
Conoscenza della definizione di continuità di una funzione, concetto di intorno di un punto, nozioni base su successioni monotone e limitate, e proprietà fondamentali dei numeri reali (assioma di completezza).

## Definizioni e notazione del corso
- **Intorno sferico:** $B_\delta(x_0)$ indica l'intorno di $x_0$ di raggio $\delta$.
- **Teorema della permanenza del segno:** Se $f$ è continua in $x_0$ e $f(x_0) > 0$, esiste un intorno $B_\delta(x_0)$ in cui $f(x) > 0$.
- **Teorema dell'esistenza degli zeri:** Sia $f:[a,b] \to \mathbb{R}$ continua. Se $f(a) \cdot f(b) < 0$, allora $\exists x_0 \in (a,b)$ tale che $f(x_0) = 0$.
- **Metodo di bisezione:** Algoritmo iterativo per l'approssimazione numerica di $x_0$ dimezzando progressivamente l'ampiezza dell'intervallo $[a,b]$.

## Risultati fondamentali
1. **Permanenza del segno:** Una funzione continua che assume valore positivo in un punto mantiene tale segno in un opportuno intorno del punto.
2. **Esistenza degli zeri:** Condizione sufficiente per l'esistenza di almeno una radice è il cambio di segno agli estremi di un intervallo chiuso e limitato.
3. **Convergenza del metodo:** Le successioni dei punti medi $c_n$ e degli estremi $a_n, b_n$ convergono alla soluzione $x_0$.
4. **Stima dell'errore:** Dopo $n$ iterazioni, l'errore commesso approssimando la soluzione con gli estremi è inferiore a $\frac{b-a}{2^n}$, mentre con il punto medio è inferiore a $\frac{b-a}{2^{n+1}}$.

## Metodi risolutivi usati nel corso
- **Verifica esistenza zeri:** Valutazione del segno della funzione agli estremi di un intervallo. Se $f(a) \cdot f(b) < 0$, l'esistenza è garantita.
- **Applicazione bisezione:**
  1. Calcolare il punto medio $c = \frac{a+b}{2}$.
  2. Valutare $f(c)$.
  3. Se $f(c) = 0$ la soluzione è trovata; altrimenti, sostituire $a$ o $b$ con $c$ a seconda del segno, restringendo l'intervallo a quello in cui la funzione cambia segno.
  4. Iterare il processo fino alla precisione desiderata.

## Errori tipici da segnalare allo studente
1. **Confusione sulle ipotesi:** Applicare il teorema degli zeri dimenticando che la continuità in tutto l'intervallo $[a,b]$ è un requisito necessario.
2. **Interpretazione del segno:** Errato calcolo del punto medio o errata scelta dell'intervallo parziale nelle iterazioni (scambiare il segno di $f(c)$ con la posizione dell'intervallo).
3. **Assunzione di unicità:** Credere che il teorema garantisca un unico zero (ne garantisce almeno uno; l'unicità richiede solitamente la stretta monotonia).
4. **Trasferibilità:** Dimenticare che il teorema fallisce in domini non completi (es. insiemi di numeri razionali $\mathbb{Q}$).

## Tipologie di esercizio da generare
- **Verifica esistenza:** Identificazione dell'intervallo corretto tra le opzioni fornite, dati i segni della funzione agli estremi.
- **Calcolo iterativo:** Applicazione di $n$ passi del metodo di bisezione per una funzione assegnata (es. $f(x) = e^{2x} + 3x$ o $f(x) = \log x + x$) e individuazione dell'intervallo o dell'approssimazione risultante.
- **Stima approssimativa:** Calcolo del valore approssimato di una radice dopo un numero prefissato di iterazioni o valutazione dell'errore massimo teorico.
