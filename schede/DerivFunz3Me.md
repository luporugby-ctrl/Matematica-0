---
titolo: Continuità, derivate di funzioni composte e inverse
gruppo: Calcolo differenziale
---
# Continuità, derivate di funzioni composte e inverse

## Prerequisiti
Concetti base di funzione, limite, calcolo di derivate elementari, definizione di continuità in un punto e conoscenza del significato grafico di derivabilità.

## Definizioni e notazione del corso
- La derivata di una funzione $f$ in $x_0$ è definita tramite il limite del rapporto incrementale: $f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$.
- La notazione $\frac{d}{dx}$ è usata per indicare l'operatore di derivazione.
- Per le funzioni inverse, il corso usa la notazione $D f^{-1}(y) = \frac{1}{f'(x)}$ dove $y = f(x)$.

## Risultati fondamentali
1. **Teorema di continuità:** Ogni funzione derivabile in un punto $x_0$ è anche continua in $x_0$. Viceversa non è sempre vero (es. $f(x) = |x|$ in $x_0=0$ è continua ma non derivabile).
2. **Derivata di funzione composta:** Date $g$ derivabile in $x$ e $f$ derivabile in $g(x)$, la composta $f \circ g$ è derivabile e vale: $\frac{d}{dx}(f \circ g)(x) = \frac{d}{dg(x)}f(g(x)) \cdot \frac{d}{dx}g(x)$.
3. **Derivata di funzione inversa:** Data $f$ continua e strettamente monotona in $[a, b]$, derivabile in $x \in (a, b)$ con $f'(x) \neq 0$, la funzione inversa $f^{-1}$ è derivabile in $y = f(x)$ con: $D f^{-1}(y) = \frac{1}{f'(x)} = \frac{1}{f'(f^{-1}(y))}$.

## Metodi risolutivi usati nel corso
- **Studio della continuità/derivabilità di funzioni definite a tratti:** Imporre la continuità (uguaglianza dei limiti destro e sinistro) e poi la derivabilità (uguaglianza dei limiti destri e sinistri dei rapporti incrementali o delle derivate) nel punto di giunzione.
- **Applicazione della regola della catena:** Identificare correttamente la funzione "esterna" e quella "interna" per applicare il teorema di derivazione composta.
- **Calcolo derivata inversa:** Calcolare la derivata della funzione originale, invertirla ed esprimerla in funzione di $y$, oppure utilizzare la formula diretta basata su $f^{-1}(y)$.

## Errori tipici da segnalare allo studente
1. Confondere la continuità con la derivabilità: assumere che, se una funzione è continua in un punto, sia automaticamente derivabile.
2. Applicazione errata della regola della catena: dimenticare di moltiplicare per la derivata della funzione interna.
3. Errore nel calcolo del rapporto incrementale per funzioni definite a tratti: calcolare solo il limite della funzione e non quello della derivata nel punto di giunzione.
4. Dimenticare la condizione $f'(x) \neq 0$ per l'esistenza della derivata della funzione inversa.

## Tipologie di esercizio da generare
1. Determinazione di parametri in funzioni definite a tratti affinché la funzione risulti continua e/o derivabile in un punto critico.
2. Calcolo della derivata prima di funzioni composte mediante la regola della catena.
3. Calcolo della derivata della funzione inversa in un punto assegnato utilizzando il teorema di derivazione della funzione inversa.
