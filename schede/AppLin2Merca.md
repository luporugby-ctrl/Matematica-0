---
titolo: Applicazioni Lineari e Prodotto tra Matrici
gruppo: Algebra Lineare
---
# Applicazioni Lineari e Prodotto tra Matrici

## Prerequisiti
Conoscenza degli spazi vettoriali, basi, dimensione, sistemi di generatori e indipendenza lineare. Concetti base di calcolo matriciale.

## Definizioni e notazione del corso
- Un'applicazione $f: V \to W$ è lineare (o omomorfismo) se $f(v + w) = f(v) + f(w)$ e $f(kv) = kf(v)$.
- Epimorfismo (suriettiva), monomorfismo (iniettiva), isomorfismo (biettiva), endomorfismo ($V=W$), automorfismo (endomorfismo biettivo).
- Spazio delle matrici di tipo $(m, n)$ su $K$ indicato come $M(m, n; K)$.
- La scrittura $D(k_1, \dots, k_n)$ indica una matrice diagonale.
- Convenzione: si opera con vettori riga e colonna; il prodotto righe per colonne è definito come $a \cdot b = \sum_{h=1}^n a_h b_h$.

## Risultati fondamentali
1. Linearità e zero: $f(\mathbf{0}) = \mathbf{0}$ e $f(-\mathbf{v}) = -f(\mathbf{v})$.
2. Proprietà dell'immagine: se $V'$ è sottospazio di $V$, $f(V')$ è sottospazio di $W$. Se $V'$ è finito, $\dim f(V') \le \dim V'$.
3. Conservazione dell'indipendenza: se $f$ è iniettiva e $S$ è linearmente indipendente, allora $f(S)$ è linearmente indipendente.
4. Isomorfismo canonico: ogni spazio vettoriale di dimensione $n$ su $K$ è isomorfo a $M(n, 1; K)$ tramite la scelta di un riferimento $R$.
5. Determinazione univoca: un'applicazione lineare $F: V \to W$ è definita univocamente dai valori che assume sugli elementi di una base $H$ di $V$.

## Metodi risolutivi usati nel corso
- Per verificare la linearità: testare le due condizioni fondamentali (additività e omogeneità).
- Per il prodotto tra matrici: il prodotto $A \cdot B$ è definito solo se il numero di colonne di $A$ coincide con il numero di righe di $B$.
- Per il prodotto con matrici diagonali: moltiplicare a destra per $D(k_i)$ scala le colonne; moltiplicare a sinistra scala le righe.

## Errori tipici da segnalare allo studente
- Confondere un'applicazione lineare con una funzione affine (es. aggiungere una costante $f(x) = ax + b$ non è lineare).
- Tentare di eseguire prodotti tra matrici con dimensioni incompatibili.
- Credere che il prodotto tra matrici sia commutativo ($A \cdot B \neq B \cdot A$ in generale).
- Dimenticare che $f(\mathbf{0})$ deve necessariamente essere il vettore nullo per ogni applicazione lineare.

## Tipologie di esercizio da generare
- Esercizi di classificazione: data $f: \mathbb{R}^n \to \mathbb{R}^m$, determinare se è omomorfismo, endomorfismo, iniettiva, suriettiva o isomorfismo.
- Calcolo di prodotti tra matrici di diverse dimensioni $(m,n) \times (n,p)$.
- Calcolo del prodotto tra una matrice generica e una matrice diagonale.
- Verifica della linearità di espressioni polinomiali in $x, y, z$.
