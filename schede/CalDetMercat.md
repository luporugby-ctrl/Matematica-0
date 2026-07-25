---
titolo: Teoria delle permutazioni e calcolo del determinante
gruppo: Algebra Lineare
---
# Teoria delle permutazioni e calcolo del determinante

## Prerequisiti
Nozioni di base di insiemistica, applicazione tra insiemi (battività), operazioni aritmetiche fondamentali e rudimenti di algebra delle matrici.

## Definizioni e notazione del corso
- $I_n = \{1, \dots, n\}$: insieme dei primi $n$ naturali.
- $S_n$: insieme delle permutazioni di $n$ elementi.
- $\sigma \in S_n$: una permutazione è una funzione biettiva $\sigma: I_n \to I_n$.
- $\text{sign}(\sigma)$: segno della permutazione (1 se pari, -1 se dispari).
- $\det A$: determinante della matrice $A \in M_n(K)$.
- $\bar{A}_{ij}$: minore complementare di $a_{ij}$ (determinante della matrice ottenuta cancellando riga $i$ e colonna $j$).
- $A_{ij} = (-1)^{i+j} \bar{A}_{ij}$: complemento algebrico dell'elemento $a_{ij}$.

## Risultati fondamentali
1. Numero di permutazioni di $n$ elementi: $N = n!$.
2. Definizione di determinante: $\det A = \sum_{\sigma \in S_n} \text{sign}(\sigma) a_{1\sigma(1)} a_{2\sigma(2)} \dots a_{n\sigma(n)}$.
3. Teorema di Laplace (sviluppo per riga/colonna):
   $\det A = \sum_{j=1}^n a_{ij} A_{ij}$ (sviluppo lungo la riga $i$)
   $\det A = \sum_{i=1}^n a_{ij} A_{ij}$ (sviluppo lungo la colonna $j$)

## Metodi risolutivi usati nel corso
- **Regola di Sarrus**: Applicabile solo a matrici $3 \times 3$, sommando i prodotti delle diagonali e sottraendo quelli delle antidiagonali.
- **Sviluppo di Laplace**: Metodo ricorsivo per ridurre l'ordine del determinante. Si sceglie preferibilmente la riga o colonna con il maggior numero di zeri per semplificare i calcoli.
- **Identificazione di parità**: Per determinare il segno di una permutazione, si conta il numero di scambi necessari per tornare alla configurazione identica.

## Errori tipici da segnalare allo studente
1. Errata applicazione della Regola di Sarrus su matrici di ordine superiore a 3.
2. Dimenticanza del segno $(-1)^{i+j}$ nel calcolo del complemento algebrico.
3. Errata individuazione della matrice complementare (cancellazione della riga e colonna errate).
4. Confusione tra permutazioni pari e dispari nel calcolo manuale del segno.

## Tipologie di esercizio da generare
- Esercizi teorici sulla natura di una data applicazione (verificare se è una permutazione, determinarne il segno).
- Calcolo esplicito del determinante per matrici $2 \times 2$ e $3 \times 3$ (usando Sarrus o definizione).
- Calcolo del determinante per matrici $4 \times 4$ o superiori tramite lo sviluppo di Laplace (sfruttando righe/colonne con zeri).
- Esercizi di selezione multipla dove viene richiesto di calcolare il determinante di matrici con entrate numeriche o frazionarie.
