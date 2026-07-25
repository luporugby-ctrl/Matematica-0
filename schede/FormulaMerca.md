---
titolo: Approssimazione polinomiale e Formula di Taylor
gruppo: Calcolo differenziale
---
# Approssimazione di funzioni tramite polinomi

## Prerequisiti
Conoscenza di base del calcolo dei limiti, del concetto di derivata e del significato geometrico della retta tangente al grafico di una funzione. Capacità di calcolare derivate successive di funzioni elementari.

## Definizioni e notazione del corso
- **Approssimazione lineare**: $f(x) \approx f(x_0) + f'(x_0)(x - x_0)$ per $x$ vicino a $x_0$.
- **O-piccolo ($o$):** La notazione $f(x) = o(g(x))$ per $x \to x_0$ indica che $\lim_{x \to x_0} \frac{f(x)}{g(x)} = 0$.
- **Polinomio di Taylor di grado $n$**: $p_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k$.
- **Formula di Maclaurin**: È il caso particolare della formula di Taylor centrato in $x_0 = 0$.
- **Convenzione**: Si pone $0! = 1$ e $f^{(0)}(x) = f(x)$.

## Risultati fondamentali
1. **Formula di Taylor**: Data $f(x)$ derivabile $n$ volte in $x_0$:
   $f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k + R_n(x)$
   con resto $R_n(x)$ tale che $\lim_{x \to x_0} \frac{R_n(x)}{(x - x_0)^n} = 0$.
2. **Relazione con l'o-piccolo**: Il resto si scrive come $R_n(x) = o((x - x_0)^n)$.
3. **Applicazione al calcolo dei limiti**: $\lim_{x \to x_0} \frac{f(x)}{g(x)} = \lim_{x \to x_0} \frac{p_n(f)(x) + o((x-x_0)^n)}{p_m(g)(x) + o((x-x_0)^m)}$, permettendo la semplificazione tramite polinomi.

## Metodi risolutivi usati nel corso
- **Linearizzazione**: Uso della retta tangente per stime numeriche veloci (es. radici quadrate).
- **Costruzione del polinomio**: Si calcolano le derivate di ordine $0, 1, \dots, n$ in $x_0$, si dividono per $k!$ e si moltiplicano per le potenze $(x-x_0)^k$.
- **Sviluppo di funzioni composte**: Si applica la formula di Taylor calcolando le derivate successive della funzione composta.

## Errori tipici da segnalare allo studente
1. Dimenticare di dividere i coefficienti per il fattoriale $k!$ della derivata.
2. Errata centratura del polinomio: sviluppare attorno a $x_0=0$ (Maclaurin) quando il problema richiede lo sviluppo attorno a un $x_0 \neq 0$.
3. Confusione tra il valore della funzione e il valore della derivata nel punto $x_0$.
4. Errore nell'applicazione della catena per derivate successive in funzioni composte.

## Tipologie di esercizio da generare
1. **Stima numerica**: Approssimare il valore di una funzione (es. radice, logaritmo) usando la retta tangente (grado 1).
2. **Calcolo polinomiale**: Determinare il polinomio di Taylor di grado $n$ (tipicamente $n=2$ o $3$) di una funzione assegnata in un punto $x_0$ specifico.
3. **Scelta multipla**: Identificare il corretto sviluppo polinomiale tra diverse opzioni fornite.
