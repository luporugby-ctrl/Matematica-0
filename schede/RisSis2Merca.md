---
titolo: Riduzione a scala e sistemi lineari
gruppo: Algebra lineare
---
# Riduzione a scala e sistemi lineari

## Prerequisiti
Conoscenza di base del calcolo algebrico, dei campi numerici e del concetto di matrice.

## Definizioni e notazione del corso
- **Matrice a scalini**: Una matrice $A$ di tipo $(m, n)$ su un campo $K$ è a scalini se, escludendo le righe nulle (che si trovano in fondo), ogni riga ha un primo elemento non nullo (pivot) a destra del pivot della riga precedente.
- **Colonne caratteristiche**: Sono le colonne che contengono i pivot.
- **Pivot**: Gli elementi non nulli $a_{i,j_i}$ che caratterizzano la forma a scalini.
- **Rango**: Identificato dal numero di righe non nulle (numero di pivot) dopo aver ridotto la matrice.
- **Matrice $D_\sigma(k_1, \dots, k_n)$**: Matrice quadrata associata a una permutazione $\sigma$, dove l'elemento di posto $(i, \sigma(i))$ è uguale a $k_i$.
- **Notazione**: Si usano trasformazioni di prima specie (scambio di righe) e di seconda specie (somma di una riga con un multiplo di un'altra) per ridurre le matrici.

## Risultati fondamentali
1. Ogni matrice $A$ può essere ridotta a forma a scalini tramite un numero finito di trasformazioni elementari sulle righe.
2. Il rango di una matrice è invariante rispetto alle trasformazioni elementari.
3. Un sistema lineare è compatibile se il rango della matrice completa è uguale al rango della matrice incompleta.
4. Se il sistema è compatibile e il numero di equazioni è minore del numero di incognite, il sistema ammette infinite soluzioni espresse in forma parametrica.
5. Se il rango della matrice completa è superiore al rango della matrice incompleta, il sistema non ammette soluzioni (è incompatibile).

## Metodi risolutivi usati nel corso
- **Algoritmo di Gauss**: Si applicano trasformazioni di prima e seconda specie per azzerare gli elementi sotto i pivot, trasformando la matrice in forma a scalini.
- **Risoluzione di sistemi**: Una volta ottenuta la matrice completa a scalini, si riscrive il sistema equivalente. Se il sistema è compatibile, si procede tramite sostituzioni all'indietro (o parametrizzazione delle variabili libere) per trovare l'insieme delle soluzioni.
- **Scrittura a blocchi**: Tecnica usata per semplificare la rappresentazione di matrici ridotte.

## Errori tipici da segnalare allo studente
1. Confondere l'ordine delle colonne caratteristiche, dimenticando che i pivot devono trovarsi in colonne progressivamente crescenti.
2. Sbagliare i calcoli nelle trasformazioni di seconda specie (es. sommare righe senza moltiplicare correttamente i coefficienti per annullare il termine desiderato).
3. Non verificare la compatibilità del sistema (confronto tra rango della matrice completa e incompleta) prima di cercare le soluzioni, portando a soluzioni errate in sistemi incompatibili.

## Tipologie di esercizio da generare
- Esercizi di classificazione: Data una matrice, stabilire se è a scalini o in una specifica forma ridotta.
- Esercizi di identificazione: Individuazione dei pivot e del rango di una matrice data.
- Esercizi di costruzione: Costruire la matrice $D_\sigma$ data una permutazione e una n-upla di scalari.
- Esercizi di risoluzione: Risoluzione completa di sistemi lineari tramite il metodo di eliminazione di Gauss, includendo la discussione della compatibilità e la scrittura delle soluzioni (particolari o parametriche).
