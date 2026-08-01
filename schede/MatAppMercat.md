---
titolo: Matrici, Applicazioni Lineari e Matrice Inversa
gruppo: Matrici, determinanti, sistemi lineari e applicazioni lineari
---
# Matrici, Applicazioni Lineari e Matrice Inversa

## Prerequisiti
Concetti di base di spazi vettoriali, basi, dimensione, combinazione lineare e operazioni elementari tra matrici.

## Definizioni e notazione del corso
- Si denota con $M(m, n, K)$ l'insieme delle matrici con $m$ righe e $n$ colonne a coefficienti nel campo $K$.
- I vettori sono trattati come vettori colonna, identificando $M(n, 1, K)$ con lo spazio dei vettori.
- $f_A$ indica l'applicazione lineare associata alla matrice $A$, definita come $f_A(\mathbf{x}) = A \cdot \mathbf{x}$.
- $Gl(n, K)$ è l'insieme delle matrici non singolari (invertibili) di ordine $n$.
- $rk f$ indica il rango di un'applicazione (dimensione dell'immagine).
- $Ker f$ indica il nucleo di un'applicazione lineare.

## Risultati fondamentali
1. **Rappresentazione:** Data un'applicazione lineare $f: M(n, 1, K) \to M(m, 1, K)$, esiste un'unica matrice $A$ tale che $f = f_A$. Le colonne di $A$ sono le immagini dei vettori della base canonica: $\mathbf{a}^i = f(\mathbf{e}^i)$.
2. **Composizione:** Per due applicazioni lineari $f$ e $g$, vale $M(g \circ f) = M(g) \cdot M(f)$.
3. **Teorema del Rango:** Per un'applicazione $f: V \to W$ con $V$ finitamente generato: $rk f = \dim V - \dim Ker f$.
4. **Invertibilità:** $A \in Gl(n, K)$ se e solo se $rk A = n$. Esiste un'unica matrice $A^{-1}$ tale che $A \cdot A^{-1} = A^{-1} \cdot A = I_n$.

## Metodi risolutivi usati nel corso
- **Costruzione della matrice associata:** Per trovare $A$ rispetto alla base canonica, si calcolano le immagini dei vettori della base canonica e li si inserisce come colonne in $A$. Se la base di partenza non è quella canonica, si esprime l'immagine dei vettori della base data come combinazione lineare dei vettori della base del codominio.
- **Calcolo del Nucleo:** Si risolve il sistema omogeneo $A \cdot \mathbf{x} = \mathbf{0}$ applicando il metodo di eliminazione di Gauss per ridurre la matrice a scala.
- **Calcolo dell'inversa:** Si affianca alla matrice $A$ la matrice identità $I_n$, ottenendo la matrice aumentata $B = (A | I_n)$. Si applicano trasformazioni elementari sulle righe (Gauss-Jordan) per trasformare $A$ in $I_n$; la matrice che appare a destra sarà $A^{-1}$.

## Errori tipici da segnalare allo studente
1. Confusione tra righe e colonne nella costruzione della matrice associata.
2. Dimenticare che il rango dell'applicazione coincide con il rango della matrice associata solo dopo aver fissato una base.
3. Errata applicazione delle trasformazioni di Gauss-Jordan durante il calcolo dell'inversa.
4. Applicare il Teorema del Rango senza verificare che lo spazio sia finitamente generato.

## Tipologie di esercizio da generare
- Data un'applicazione $f$ definita sui vettori di una base, determinare la matrice associata $A$ rispetto a basi assegnate (o basi canoniche).
- Calcolare il nucleo ($Ker f$) e il rango ($rk f$) di una data applicazione lineare, determinandone la dimensione.
- Calcolare l'inversa di una matrice quadrata $M$ tramite l'algoritmo di Gauss-Jordan.
- Esercizi a risposta multipla su proprietà di invertibilità e dimensioni di nucleo/immagine.
