---
titolo: Calcolo del rango e sistemi lineari
gruppo: Algebra Lineare
---
# Calcolo del rango e sistemi lineari

## Prerequisiti
Conoscenza di base del calcolo matriciale, definizione di determinante, proprietà fondamentali delle matrici, concetto di dipendenza/indipendenza lineare di vettori e righe/colonne di una matrice.

## Definizioni e notazione del corso
- Sia $A$ una matrice $(m, n)$. $A(i_1, \dots, i_h; j_1, \dots, j_h)$ indica la sottomatrice quadrata ottenuta selezionando le righe e colonne specificate.
- Un minore $A(i_1, \dots, i_h; j_1, \dots, j_h)$ è detto *minore fondamentale* se è non nullo e $h$ è il massimo ordine possibile, ovvero se ogni suo orlato (ottenuto aggiungendo una riga e una colonna) ha determinante nullo.
- Il rango $rk(A)$ è l'ordine del massimo minore non nullo.

## Risultati fondamentali
1. **Teorema degli orlati**: Se $A$ contiene un minore $M$ di ordine $h$ non nullo, e tutti i suoi orlati di ordine $h+1$ sono nulli, allora $rk(A) = h$.
2. **Corollario 1**: Il rango di $A$ è pari all'ordine del suo massimo minore fondamentale.
3. **Teorema di Cramer**: In un sistema $A \mathbf{x} = \mathbf{c}$ di $n$ equazioni in $n$ incognite, se $\det(A) \neq 0$, la soluzione unica è $\xi_i = \frac{\det(A^i)}{\det(A)}$, dove $A^i$ è la matrice con la colonna $i$-esima sostituita dal vettore dei termini noti.

## Metodi risolutivi usati nel corso
- **Algoritmo degli orlati**: Si parte da un elemento non nullo (minore di ordine 1). Si procede "orlando" tale minore (aggiungendo una riga e una colonna) e calcolando i determinanti degli orlati. Se tutti gli orlati di ordine $k+1$ sono nulli, il rango è $k$.
- **Risoluzione sistemi lineari**:
    1. Si calcola $rk(A)$ e $rk(B)$ (matrice completa). Il sistema è compatibile se $rk(A) = rk(B) = r$.
    2. Si individuano le $r$ equazioni (righe) e le $r$ incognite (colonne) che formano il minore non nullo.
    3. Si portano le restanti $n-r$ variabili a secondo membro come parametri.
    4. Si risolve il sistema di ordine $r$ risultante tramite la regola di Cramer.

## Errori tipici da segnalare allo studente
1. Dimenticare di verificare la condizione $rk(A) = rk(B)$ prima di procedere con la risoluzione (cercando la soluzione per sistemi incompatibili).
2. Errata identificazione delle colonne/righe da eliminare durante la riduzione del sistema a forma normale (non selezionare quelle del minore fondamentale).
3. Confondere il rango della matrice incompleta con quello della completa.
4. Applicare Cramer a sistemi non quadrati o con determinante nullo.

## Tipologie di esercizio da generare
- Determinazione del rango di una matrice $A \in M(m, n, \mathbb{R})$ tramite l'algoritmo degli orlati.
- Verifica della compatibilità di un sistema lineare $A\mathbf{x} = \mathbf{c}$ confrontando il rango della matrice incompleta e completa.
- Risoluzione completa di un sistema lineare (compatibile) con espressione delle soluzioni in forma parametrica.
- Esercizi teorici sul riconoscimento di minori fondamentali o sull'applicazione del Teorema degli orlati su matrici specifiche.
