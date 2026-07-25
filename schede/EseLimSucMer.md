---
titolo: Calcolo di limiti di successioni numeriche
gruppo: Successioni e limiti
---
# Calcolo di limiti di successioni numeriche

## Prerequisiti
Conoscenza delle proprietà fondamentali di potenze, logaritmi ed esponenziali, dei principali limiti notevoli, delle proprietà del fattoriale e delle gerarchie degli infiniti. Capacità di maneggiare disequazioni per l'applicazione del teorema dei carabinieri.

## Definizioni e notazione del corso
- La successione è indicata come $a_n$.
- Si opera per $n \to +\infty$.
- Uso sistematico del confronto di ordini di infinito e dell'algebra dei limiti.
- Utilizzo della forma esponenziale $a^b = e^{b \log a}$ per gestire forme indeterminate del tipo $1^\infty$ o $\infty^0$.

## Risultati fondamentali
1. Limite di successione geometrica: $\lim_{n \to +\infty} a^n = 0$ per $-1 < a < 1$.
2. Gerarchia degli infiniti: $\lim_{n \to +\infty} \frac{n^b}{a^n} = 0$ per $b > 0, a > 1$ e $\lim_{n \to +\infty} \frac{\log n}{n^b} = 0$ per $b > 0$.
3. Limite della radice $n$-esima: $\lim_{n \to +\infty} \sqrt[n]{n^b} = 1$ per ogni $b \in \mathbb{R}$.
4. Limite notevole del numero di Nepero: $\lim_{n \to +\infty} (1 + \frac{1}{n})^n = e$.
5. Teorema del confronto (carabinieri): se $a_n \le c_n \le b_n$ e $\lim a_n = \lim b_n = L$, allora $\lim c_n = L$.
6. Criterio del rapporto: se $\lim_{n \to +\infty} \frac{a_{n+1}}{a_n} = L$, allora la successione tende a $0$ se $L < 1$ e a $+\infty$ se $L > 1$.

## Metodi risolutivi usati nel corso
- Messa in evidenza: si isola il termine di grado massimo (o di ordine superiore nella gerarchia) sia al numeratore che al denominatore per semplificare la frazione.
- Scomposizione in sottosuccessioni: si analizzano separatamente i termini di posto pari e dispari per verificare l'esistenza del limite (es. in presenza di $(-1)^n$).
- Algebra dei limiti e forme indeterminate: trasformazione tramite logaritmi ed esponenziali per ricondursi a limiti notevoli o confronti asintotici.
- Maggiorazione/Minorazione: uso di disuguaglianze per applicare il teorema dei carabinieri (specialmente con termini limitati come $\sin n$ o $\cos n$).

## Errori tipici da segnalare allo studente
- Trascurare il valore assoluto quando si estrae il termine di grado massimo, portando a errori di segno nei limiti.
- Dimenticare che per $(-1)^n$ il limite non esiste se le sottosuccessioni pari e dispari convergono a valori diversi.
- Applicare erroneamente le proprietà dei logaritmi o degli esponenziali in forme indeterminate (es. non convertire correttamente $f(n)^{g(n)}$ in $e^{g(n) \log f(n)}$).
- Sbagliare la gerarchia degli infiniti, confondendo l'ordine di crescita tra fattoriale, esponenziale, potenza e logaritmo.

## Tipologie di esercizio da generare
- Calcolo di limiti di rapporti tra polinomi, radici o combinazioni di funzioni elementari.
- Limiti contenenti potenze con base o esponente dipendenti da $n$.
- Limiti che richiedono il criterio del rapporto (es. successioni con fattoriali).
- Limiti con parametri (es. $\alpha \in \mathbb{R}$) che richiedono la discussione del risultato.
- Limiti di espressioni contenenti termini oscillanti (seno, coseno, $(-1)^n$) gestiti tramite il teorema dei carabinieri o il prodotto di una successione limitata per una infinitesima.
