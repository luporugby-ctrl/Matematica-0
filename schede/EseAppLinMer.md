---
titolo: Applicazioni Lineari, Nucleo e Immagine
gruppo: Algebra Lineare
---
# Applicazioni Lineari

## Prerequisiti
Conoscenza di base degli spazi vettoriali, basi canoniche, calcolo matriciale e risoluzione di sistemi di equazioni lineari.

## Definizioni e notazione del corso
- Un'applicazione $f: U \to V$ tra $K$-spazi vettoriali è lineare se soddisfa la linearità rispetto alla somma $f(x + y) = f(x) + f(y)$ e allo scalare $f(\lambda x) = \lambda f(x)$.
- $Ker(L) = \{v \in \mathbb{R}^n : L(v) = 0\}$ (Nucleo).
- $Im(L) = \{w \in \mathbb{R}^m : \exists v \in \mathbb{R}^n, L(v) = w\}$ (Immagine).
- Matrice $M$: matrice che rappresenta $L$ rispetto alla base canonica, le cui colonne sono le immagini dei vettori della base canonica.
- Convenzione: I vettori sono rappresentati come colonne (vettori colonna).

## Risultati fondamentali
1. Teorema nullità-rango: $\dim(\mathbb{R}^n) = \dim(Ker L) + \dim(Im L)$.
2. Dimensione immagine: $\dim(Im L) = rk(M)$.
3. Condizione di linearità: l'applicazione deve trasformare lo zero in zero (le costanti additive non nulle non sono ammesse).

## Metodi risolutivi usati nel corso
- Verifica linearità: Applicare direttamente la definizione testando la somma di vettori e la moltiplicazione per uno scalare.
- Calcolo matrice associata: Calcolare $L(e_i)$ per ogni vettore della base canonica e disporre i risultati come colonne della matrice $M$.
- Calcolo base di Im $L$: Estrarre le colonne linearmente indipendenti di $M$ (o usare il rango).
- Calcolo base di Ker $L$: Risolvere il sistema omogeneo $Mv = 0$ usando la riduzione o eliminazione di parametri.
- Passaggio tra rappresentazioni: Convertire equazioni parametriche in cartesiane eliminando i parametri, o viceversa.

## Errori tipici da segnalare allo studente
- Confondere un'applicazione affine con una lineare (es. presenza di termine noto $b \neq 0$).
- Dimenticare che le colonne della matrice associata sono le immagini dei vettori della base canonica.
- Sbagliare il calcolo del rango della matrice, portando a dimensioni errate per Ker o Im.
- Confondere la variabile libera del sistema (parametro $\lambda$) con lo scalare dell'applicazione lineare.

## Tipologie di esercizio da generare
- Verifica della linearità di una funzione data (polinomiale, matriciale, su basi canoniche).
- Determinazione della matrice associata $M$ rispetto alle basi canoniche date.
- Calcolo di basi e dimensioni di $Ker(L)$ e $Im(L)$.
- Riscrittura di sottospazi (Ker e Im) in forma parametrica e cartesiana.
- Composizione di applicazioni lineari (calcolo di $L^2$).
