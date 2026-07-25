---
titolo: Proprietà del determinante e applicazioni
gruppo: Algebra Lineare
---
# Proprietà del determinante e applicazioni

## Prerequisiti
Conoscenza della teoria degli spazi vettoriali, del concetto di campo, della definizione di matrice, delle operazioni tra matrici e della definizione operativa di determinante (sviluppo di Laplace).

## Definizioni e notazione del corso
- Un'applicazione $\phi: V_1 \times \dots \times V_n \to V$ è *multilineare* se è lineare in ogni variabile, fissate le altre.
- Un'applicazione multilineare $\phi$ su $W$ (dove $W$ è uno spazio vettoriale) è *alternante* se $\phi(v_1, \dots, v_n) = 0$ ogni volta che due vettori tra i $v_i$ sono uguali.
- Il determinante è visto come l'unica applicazione multilineare alternante sulle righe di una matrice che vale $1$ sulla matrice identità $I_n$.
- $A_{ij}$ indica il complemento algebrico dell'elemento di posto $(i, j)$ della matrice $A$.

## Risultati fondamentali
1. **Antisimmetria**: Se $\phi$ è alternante, allora lo scambio di due vettori cambia il segno dell'applicazione: $\phi(\dots, v_i, \dots, v_j, \dots) = -\phi(\dots, v_j, \dots, v_i, \dots)$.
2. **Proprietà di invarianza**: Il determinante non cambia se a una riga (o colonna) si somma una combinazione lineare delle altre.
3. **Dipendenza lineare**: $\det(A) = 0$ se e solo se le righe (o colonne) sono linearmente dipendenti (rango $< n$).
4. **Formula inversa**: Se $\det(A) \neq 0$, allora $A^{-1} = \frac{1}{\det A} (\text{adj} A)$, dove $(\text{adj} A)_{ij} = A_{ji}$ (trasposta della matrice dei complementi algebrici).
5. **Teorema di annullamento**: $\sum_{j=1}^n a_{ij} A_{kj} = 0$ per $i \neq k$ (somma dei prodotti degli elementi di una riga per i complementi di un'altra riga).

## Metodi risolutivi usati nel corso
- Per verificare se una funzione è multilineare: testare la linearità (somma e prodotto per scalare) separatamente per ogni argomento.
- Per il calcolo di $\det(A)$: usare le trasformazioni elementari (primo tipo) per semplificare la matrice (es. creare zeri) senza alterare il valore, o sviluppare secondo Laplace.
- Per il calcolo di $A^{-1}$: 
  1. Calcolare $\det(A)$.
  2. Calcolare la matrice dei complementi algebrici $C = (A_{ij})$.
  3. Costruire $A^{-1} = \frac{1}{\det A} C^T$.

## Errori tipici da segnalare allo studente
1. Confondere la linearità globale con la multilinearità (pensare che la funzione sia lineare nell'intero prodotto cartesiano).
2. Dimenticare il segno $(-1)^{i+j}$ nel calcolo del complemento algebrico $A_{ij}$.
3. Non trasporre la matrice dei complementi algebrici quando si calcola l'inversa (usare $C$ anziché $C^T$).
4. Applicare proprietà del determinante che valgono solo per matrici quadrate a matrici rettangolari.

## Tipologie di esercizio da generare
- Esercizi teorici di classificazione: data un'applicazione $\phi(v_1, v_2)$, determinare se è multilineare, simmetrica o alternante.
- Calcolo del determinante: esercizi su matrici $3 \times 3$ o $4 \times 4$ mediante trasformazioni elementari o Laplace.
- Calcolo della matrice inversa: determinazione di $A^{-1}$ tramite la formula dei complementi algebrici.
- Esercizi di verifica: testare se una matrice data è singolare o invertibile in base al valore del determinante.
