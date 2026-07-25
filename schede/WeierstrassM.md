---
titolo: Funzioni continue: teoremi di esistenza e Weierstrass
gruppo: Analisi delle funzioni di una variabile reale
---
# Funzioni continue: Teoremi di esistenza e Weierstrass

## Prerequisiti
- Nozioni base di topologia della retta reale (intervalli chiusi e limitati, insiemi compatti).
- Definizione di continuità di una funzione in un punto e in un intervallo.
- Proprietà fondamentali delle successioni reali (convergenza, sottosuccessioni, teorema di Bolzano-Weierstrass).
- Concetto di estremo superiore ed estremo inferiore di un insieme.

## Definizioni e notazione del corso
- $f: [a, b] \to \mathbb{R}$ indica una funzione definita su un intervallo chiuso e limitato.
- $x_m, x_M \in [a, b]$ denotano rispettivamente i punti di minimo e massimo di $f$.
- I valori $f(x_m) = m$ e $f(x_M) = M$ sono il minimo e il massimo (assoluti) di $f$ su $[a, b]$.
- Convenzione: si utilizza il Teorema di Bolzano-Weierstrass per dimostrare l'esistenza di massimi e minimi.

## Risultati fondamentali
1. **Primo Teorema dei valori intermedi**: Se $f$ è continua in $[a, b]$, allora $f$ assume tutti i valori compresi tra $f(a)$ e $f(b)$.
2. **Teorema di Weierstrass**: Se $f$ è continua in un intervallo chiuso e limitato $[a, b]$, allora $f$ ammette massimo e minimo assoluti in $[a, b]$. Cioè: $\exists x_m, x_M \in [a, b]$ tali che $f(x_m) \leq f(x) \leq f(x_M)$ per ogni $x \in [a, b]$.
3. **Secondo Teorema dei valori intermedi**: Se $f$ è continua in $[a, b]$, allora l'immagine dell'intervallo è l'intervallo $[m, M]$, dove $m$ e $M$ sono il minimo e il massimo assoluti.

## Metodi risolutivi usati nel corso
- Per verificare l'appartenenza di un valore all'immagine, si calcolano i valori agli estremi dell'intervallo e si applica il primo teorema dei valori intermedi.
- Per dimostrare che una funzione non ammette massimo o minimo, si verifica la mancanza di continuità o la natura non chiusa/non limitata dell'intervallo di definizione (es. $f(x) = 1/x$ su $(0, 1]$).
- Per lo studio di funzioni definite a tratti, si controlla la continuità nei punti di raccordo prima di applicare i teoremi di esistenza.

## Errori tipici da segnalare allo studente
1. Dimenticare che il Teorema di Weierstrass richiede tassativamente un intervallo *chiuso e limitato*.
2. Applicare i teoremi di esistenza a funzioni che presentano discontinuità all'interno dell'intervallo considerato.
3. Confondere l'estremo superiore (o inferiore) con il massimo (o minimo): un valore può essere l'estremo di una funzione ma non essere assunto (non appartenere all'immagine).

## Tipologie di esercizio da generare
- Esercizi di verifica dell'appartenenza di un valore $y_0$ all'immagine di una funzione continua in $[a, b]$ tramite il teorema dei valori intermedi.
- Esercizi di analisi di funzioni definite a tratti per determinare la presenza di massimi/minimi, richiedendo di verificare preliminarmente la continuità in ogni punto.
- Quesiti a risposta multipla su funzioni non limitate o con discontinuità per testare la comprensione del ruolo delle ipotesi nei teoremi di esistenza.
