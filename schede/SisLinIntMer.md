---
titolo: Sistemi lineari e sottospazi vettoriali
gruppo: Algebra Lineare
---
# Sistemi Lineari e Sottospazi

## Prerequisiti
Concetti di base di algebra lineare: vettori colonna, operazioni tra matrici, combinazione lineare, concetto di campo $K$, definizione di spazio vettoriale e sottospazio vettoriale.

## Definizioni e notazione del corso
- Sistema lineare $\mathcal{A}$: insieme di $m$ equazioni in $n$ incognite.
- Matrice completa $B \in M(m, n+1, K)$ e matrice incompleta $A \in M(m, n, K)$.
- Vettore colonna dei termini noti $c \in M(m, 1, K)$.
- $M(\mathcal{A})$: insieme delle soluzioni del sistema $\mathcal{A}$.
- $Col(A)$: sottospazio generato dalle colonne di $A$.
- $Rig(A)$: sottospazio generato dalle righe di $A$.
- Sistema omogeneo $\mathcal{A}^{om}$: sistema con $c = 0$, dove il vettore nullo è sempre soluzione (soluzione banale).

## Risultati fondamentali
1. **Struttura delle soluzioni**: $M(\mathcal{A})$ è un $K$-sottospazio vettoriale di $M(n, K)$ se e solo se $\mathcal{A}$ è omogeneo.
2. **Teorema di compatibilità (Rouché-Capelli)**: Un sistema $\mathcal{A}$ è compatibile se e solo se il vettore dei termini noti $c$ appartiene allo spazio generato dalle colonne di $A$.
3. **Corollario**: Il sistema $\mathcal{A}$ è compatibile se e solo se $Col(A) = Col(B)$, dove $B = [A|c]$.
4. **Relazione tra soluzioni**: Se $\xi$ è una soluzione particolare di $\mathcal{A}$, ogni altra soluzione $\eta$ si scrive come $\eta = a + \xi$, dove $a \in M(\mathcal{A}^{om})$.

## Metodi risolutivi usati nel corso
- Identificazione della matrice completa $B$ e della incompleta $A$ a partire dal sistema.
- Verifica della compatibilità tramite il confronto tra lo spazio generato dalle colonne di $A$ e quello di $B$.
- Analisi della dipendenza lineare delle colonne per determinare la dimensione di $Col(A)$.
- Utilizzo della forma vettoriale $a^1 \xi_1 + \dots + a^n \xi_n = c$ per verificare l'appartenenza di $c$ al sottospazio.

## Errori tipici da segnalare allo studente
1. Confondere la matrice incompleta $A$ con la completa $B$ durante il calcolo della dimensione dei sottospazi generati.
2. Pensare erroneamente che ogni sistema ammetta sempre il vettore nullo come soluzione (vero solo per i sistemi omogenei).
3. Dimenticare che il criterio di compatibilità dipende dall'uguaglianza tra $Col(A)$ e $Col(B)$, non semplicemente dal numero di equazioni o incognite.
4. Errata deduzione della compatibilità basata su una lettura superficiale del rango, senza verificare esplicitamente la dipendenza del termine noto.

## Tipologie di esercizio da generare
- Data una matrice (completa o incompleta), determinare la dimensione del sottospazio delle colonne $dim(Col(A))$ o righe.
- Stabilire se un sistema è compatibile, confrontando gli spazi colonna delle matrici $A$ e $B$.
- Determinare se un vettore $c$ appartiene allo spazio generato dalle colonne di una matrice data.
- Identificare le proprietà dello spazio delle soluzioni (es. se è un sottospazio o se il sistema ammette soluzione nulla).
