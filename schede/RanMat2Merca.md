---
titolo: Rango di matrici e sistemi lineari
gruppo: Algebra Lineare
---
# Rango di matrici e sistemi lineari

## Prerequisiti
Concetti di base di algebra lineare: vettori, combinazioni lineari, dipendenza/indipendenza lineare, nozione di sottospazio vettoriale, basi e dimensione di uno spazio vettoriale.

## Definizioni e notazione del corso
- $A = (a_{ij})$: matrice $m \times n$ su campo $K$.
- $Rig(A)$ e $Col(A)$: sottospazi generati rispettivamente dalle righe e dalle colonne di $A$.
- $rk(A)$: rango della matrice $A$.
- $A(i_1, \dots, i_h; j_1, \dots, j_k)$: matrice subordinata (sottomatrice) ottenuta selezionando le righe e colonne indicate.
- Sistema lineare: forma compatta $A\mathbf{x} = \mathbf{c}$, dove $A$ è la matrice incompleta e $B = (A | \mathbf{c})$ è la matrice completa.

## Risultati fondamentali
1. **Teorema di invarianza del rango:** $\dim Rig(A) = \dim Col(A) = rk(A)$.
2. **Proprietà di trasposizione:** $rk(A) = rk(A^T)$.
3. **Monotonia del rango:** Se $A'$ è una matrice subordinata di $A$, allora $rk(A') \leq rk(A)$.
4. **Teorema di Rouché-Capelli:** Un sistema $A\mathbf{x} = \mathbf{c}$ è compatibile se e solo se $rk(A) = rk(B)$.
5. **Teorema di unicità (1):** Il sistema ammette un'unica soluzione se e solo se $rk(A) = rk(B) = n$ (dove $n$ è il numero delle incognite).
6. **Teorema di unicità (2):** Per i sistemi compatibili con $rk(A) = p < n$, esistono $\infty^{n-p}$ soluzioni dipendenti da $n-p$ parametri liberi.
7. **Sistemi omogenei:** Lo spazio delle soluzioni $M(A)$ è un sottospazio di $M(n, K)$ di dimensione $n - rk(A)$.

## Metodi risolutivi usati nel corso
- **Calcolo del rango:** Identificazione del sistema massimo di colonne o righe linearmente indipendenti.
- **Analisi di compatibilità:** Confronto tra $rk(A)$ e $rk(B)$ per determinare l'esistenza di soluzioni.
- **Risoluzione parametrica:** Identificazione delle variabili libere corrispondenti alle colonne non appartenenti al sistema massimo $S$, assegnazione di parametri arbitrari e risoluzione del sistema ridotto.
- **Sistemi omogenei:** Calcolo della dimensione del nucleo e determinazione di una base per lo spazio delle soluzioni.

## Errori tipici da segnalare allo studente
1. Confondere $rk(A)$ con il numero totale di righe o colonne (dimensione della matrice).
2. Dimenticare di includere la colonna dei termini noti quando si calcola il rango della matrice completa $B$.
3. Non verificare la compatibilità tramite Rouché-Capelli prima di cercare le soluzioni, portando a calcoli inutili su sistemi impossibili.
4. Sbagliare la scelta delle variabili libere: non considerare che solo le colonne del sistema massimo di indipendenza definiscono le variabili "pivot".

## Tipologie di esercizio da generare
- Determinazione del rango di una matrice data.
- Calcolo del rango di sottomatrici (subordinate) di una matrice assegnata.
- Verifica della compatibilità di un sistema lineare (dato in forma matriciale o di equazioni).
- Studio di un sistema lineare: determinare se esistono soluzioni, se sono uniche o infinite, e fornire la forma parametrica della soluzione generale.
- Esercizi su sistemi omogenei: calcolo della dimensione dello spazio delle soluzioni e determinazione di una base.
