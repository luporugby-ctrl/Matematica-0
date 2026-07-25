---
titolo: Introduzione ai vettori geometrici
gruppo: Geometria vettoriale
---
# Introduzione ai vettori geometrici

## Prerequisiti
Conoscenza basilare della geometria euclidea (concetti di punto, retta, segmento, parallelismo e congruenza).

## Definizioni e notazione del corso
- **Vettore applicato:** Data una coppia ordinata di punti $(P, Q)$, il segmento orientato da $P$ a $Q$ è indicato con $\vec{PQ}$ (o $Q-P$). $P$ è l'origine, $Q$ la fine.
- **Equipollenza ($\sim$):** Relazione tra vettori applicati. Due vettori sono equipollenti se hanno stessa direzione, stessa lunghezza e stesso verso.
- **Vettore libero ($\mathbf{v}$):** Classe di equivalenza di vettori applicati rispetto alla relazione di equipollenza. Lo spazio dei vettori liberi è indicato con $\mathcal{V}$.
- **Notazione:** Si usano lettere minuscole in grassetto ($\mathbf{v}, \mathbf{w}$) per i vettori liberi. Il vettore nullo è indicato con $\mathbf{0}$.

## Risultati fondamentali
1. **Esistenza di un rappresentante:** Per ogni vettore $\mathbf{v} \in \mathcal{V}$ e ogni punto $P \in E$, esiste un unico punto $Q$ tale che $\mathbf{v} = \vec{PQ}$.
2. **Proprietà della somma ($\mathbf{v} + \mathbf{w}$):** Operazione associativa, commutativa, con elemento neutro $\mathbf{0}$ ed elemento opposto $-\mathbf{v}$ (dove $-\vec{PQ} = \vec{QP}$).
3. **Prodotto per uno scalare ($a\mathbf{v}$):** Rispetta le proprietà di distributività rispetto alla somma di scalari $(a+b)\mathbf{v} = a\mathbf{v} + b\mathbf{v}$ e di vettori $a(\mathbf{v} + \mathbf{w}) = a\mathbf{v} + a\mathbf{w}$, oltre all'associatività $(ab)\mathbf{v} = a(b\mathbf{v})$.

## Metodi risolutivi usati nel corso
- **Metodo punta-coda:** Per sommare $\mathbf{v}$ e $\mathbf{w}$, si applica il rappresentante di $\mathbf{w}$ a partire dall'estremo finale del rappresentante di $\mathbf{v}$.
- **Metodo del parallelogramma:** Per sommare vettori con la stessa origine, si costruisce il parallelogramma di cui i due vettori sono lati adiacenti; la somma è la diagonale uscente dall'origine comune.
- **Interpretazione geometrica del prodotto per scalare:** Moltiplicare $\mathbf{v}$ per $a$ significa dilatare/contrarre la lunghezza del vettore di un fattore $|a|$ e invertirne il verso se $a < 0$.

## Errori tipici da segnalare allo studente
1. Confondere un vettore applicato (che ha un punto di origine fisso) con un vettore libero (che è una classe di equipollenza).
2. Non considerare l'inversione del verso nel calcolo della differenza tra vettori ($\mathbf{v} - \mathbf{w} = \mathbf{v} + (-\mathbf{w})$).
3. Dimenticare che il prodotto per uno scalare negativo inverte il verso del vettore originale.
4. Errata interpretazione grafica della somma: tracciare il vettore risultante con l'orientamento sbagliato rispetto ai componenti.

## Tipologie di esercizio da generare
- Identificazione della relazione di equipollenza tra vettori applicati graficamente.
- Determinazione della combinazione lineare di vettori data una configurazione geometrica (es. trovare $\mathbf{a}$ in funzione di $\mathbf{v}$ e $\mathbf{w}$ tramite osservazione di parallelogrammi o triangoli).
- Esercizi di "lettura" grafica: dati dei vettori in un piano, identificare quale operazione vettoriale (somma, differenza o prodotto per scalare) descrive il vettore risultante.
