---
titolo: Sistemi lineari e Formula di Grassmann
gruppo: Matrici, determinanti, sistemi lineari e applicazioni lineari
---
# Sistemi lineari e Formula di Grassmann

## Prerequisiti
Conoscenza di base degli spazi vettoriali, del concetto di base e dimensione, e delle proprietà fondamentali delle matrici (rango). Familiarità con il Teorema di Rouché-Capelli.

## Definizioni e notazione del corso
- Campo base: $K$.
- Sistemi equivalenti: $A \iff A'$ se hanno lo stesso insieme di soluzioni, indicato con $M(A) = M(A')$.
- Sistema ridotto: un sistema le cui equazioni sono linearmente indipendenti.
- Spazio somma: $V_1 + V_2$ è il sottospazio generato dall'unione di due sottospazi $V_1$ e $V_2$.
- Somma diretta: $V_1 \oplus V_2$ se $V_1 \cap V_2 = (0)$.

## Risultati fondamentali
1. Proposizione 1: Un'equazione $\alpha$ dipende linearmente da un sistema $A$ se e solo se ogni soluzione di $A$ è soluzione di $\alpha$.
2. Formula di Grassmann: Per due sottospazi $V_1, V_2$ finitamente generati:
   $\dim V_1 + \dim V_2 = \dim(V_1 + V_2) + \dim(V_1 \cap V_2)$.
3. Corollario 2b: Ogni sistema di $n$ incognite è equivalente a un sistema di al massimo $n+1$ equazioni.
4. Proposizione 2: $V_1 + V_2$ è somma diretta se e solo se ogni vettore del sommo si scrive in modo unico come somma di un vettore di $V_1$ e uno di $V_2$.

## Metodi risolutivi usati nel corso
- Per determinare l'equivalenza: Verificare se i sistemi hanno lo stesso rango (spazio delle soluzioni).
- Per verificare la dipendenza lineare: Si analizza se l'aggiunta di una nuova equazione al sistema originale modifica il rango della matrice completa (se il rango non aumenta, l'equazione dipende linearmente dalle precedenti).
- Per calcolare l'intersezione di sottospazi: Si pongono a sistema le equazioni cartesiane definenti i due sottospazi o si uguagliano le combinazioni lineari dei generatori.
- Per verificare la somma diretta: Si controlla se $\dim(V_1 \cap V_2) = 0$.

## Errori tipici da segnalare allo studente
1. Confondere l'equivalenza di sistemi con l'uguaglianza tra le singole equazioni.
2. Dimenticare di verificare la compatibilità del sistema prima di applicare il Teorema di Rouché-Capelli.
3. Sbagliare il calcolo della dimensione della somma di sottospazi non sommando correttamente le dimensioni o ignorando il termine di intersezione nella formula di Grassmann.

## Tipologie di esercizio da generare
- Esercizi di confronto: Dati due sistemi, determinarne l'equivalenza o la compatibilità.
- Esercizi di dipendenza lineare: Data una serie di equazioni, verificare se un'equazione $\alpha$ è conseguenza lineare del sistema.
- Esercizi sulla dimensione: Calcolare $\dim(V \cap W)$ e $\dim(V + W)$ dati i generatori o le equazioni cartesiane di $V$ e $W$.
- Esercizi teorici: Verificare se una somma di sottospazi è diretta in base alla dimensione dell'intersezione o all'unicità della scomposizione dei vettori.
