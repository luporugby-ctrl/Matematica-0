---
titolo: Algoritmo di Gauss e rango di matrici
gruppo: Algebra Lineare
---
# Algoritmo di Gauss e rango di matrici

## Prerequisiti
Conoscenza della definizione di spazio vettoriale, sottospazio, sistema di generatori, indipendenza lineare, base e dimensione. Nozioni di base sulle matrici (righe, colonne, tipo $(m, n)$).

## Definizioni e notazione del corso
- $V$ è un $K$-spazio vettoriale; $\Sigma = (\mathbf{v}_1, \dots, \mathbf{v}_m)$ è una $m$-upla ordinata di vettori.
- Trasformazione elementare di prima specie $(i, j; k)$: sostituisce $\mathbf{v}_i$ con $\mathbf{v}_i + k\mathbf{v}_j$.
- Trasformazione elementare di seconda specie $(i, j)$: scambio dei vettori di posto $i$ e $j$.
- Notazione per le matrici: una matrice $A$ è ridotta $(i_1, \dots, i_r; j_1, \dots, j_r)$ se nella colonna $j_h$ l'unica componente non nulla è quella di posto $i_h$. Se anche le altre righe sono nulle, la matrice è "completamente ridotta".

## Risultati fondamentali
1. Le trasformazioni elementari preservano lo spazio generato dai vettori.
2. Esistenza dell'algoritmo: per ogni matrice non nulla esiste una sequenza finita di trasformazioni elementari di riga che la trasforma in una forma ridotta.
3. Il rango di una matrice (dimensione del sottospazio generato dalle righe/colonne) è uguale al numero di righe (o colonne) linearmente indipendenti trovate tramite l'algoritmo.
4. Se una matrice è completamente ridotta, le righe di posto $i_1, \dots, i_r$ formano un sistema massimo di righe linearmente indipendenti.

## Metodi risolutivi usati nel corso
- Applicazione sistematica delle operazioni elementari di riga per annullare gli elementi sotto (e sopra) i pivot.
- Identificazione del "primo indice di colonna" non nullo per ogni riga, procedendo in modo iterativo per ridurre la matrice.
- Sostituzione di righe: $R_i \leftarrow R_i + k R_j$.
- Scambio di righe per facilitare il calcolo (es. portare una riga con valore $1$ in posizione di pivot).

## Errori tipici da segnalare allo studente
1. Errore di calcolo nei coefficienti scalari $k$ durante la riduzione (molto comuni nelle frazioni).
2. Confusione tra l'operazione di somma algebrica tra righe e la moltiplicazione per uno scalare.
3. Non riuscire a distinguere tra una matrice "ridotta" e una "completamente ridotta".
4. Sbagliare l'ordine degli indici o dimenticare di aggiornare correttamente tutte le componenti della riga durante il passo $(i, j; k)$.

## Tipologie di esercizio da generare
- Esercizi di identificazione: "Data la matrice $A_1$ e $A_2$, quale trasformazione elementare trasforma $A_1$ in $A_2$?".
- Esercizi di classificazione: "Data una matrice, determinare se è ridotta o completamente ridotta rispetto a determinati indici".
- Esercizi di calcolo del rango: "Applicare l'algoritmo di Gauss per portare una matrice in forma ridotta e calcolarne il rango".
- Esercizi di verifica: "Applicare l'algoritmo di Gauss per determinare una matrice risultante" (scelta multipla tra opzioni date).
