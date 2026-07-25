---
titolo: Definizioni e proprietà fondamentali degli spazi vettoriali
gruppo: Algebra Lineare
---
# Definizioni e proprietà fondamentali degli spazi vettoriali

## Prerequisiti
Conoscenza delle strutture algebriche elementari (insieme, operazioni interne) e familiarità con il concetto di campo (numeri reali $\mathbb{R}$, razionali $\mathbb{Q}$).

## Definizioni e notazione del corso
- **Campo $K$**: Insieme dotato di due operazioni interne ($+$, $\cdot$) che soddisfano assiomi di gruppo abeliano per la somma, gruppo abeliano per gli elementi non nulli nel prodotto, e proprietà distributiva.
- **Spazio vettoriale**: Struttura $(V, +, \cdot)$ su un campo $K$, dove $V$ è l'insieme dei vettori (denotati in grassetto, es: $\mathbf{v}$), $+$ è un'operazione interna a $V$ e $\cdot$ è un prodotto esterno tra scalari di $K$ e vettori di $V$.
- **Combinazione lineare**: Dato un insieme di vettori $(\mathbf{v}_1, \dots, \mathbf{v}_n)$ e scalari $(k_1, \dots, k_n)$, è il vettore $\sum_{i=1}^{n} k_i \mathbf{v}_i$.

## Risultati fondamentali
1. **Unicità**: In ogni campo e spazio vettoriale, l'elemento neutro (zero) e l'elemento inverso (opposto) sono unici.
2. **Leggi di annullamento**: Il prodotto di uno scalare per un vettore è $\mathbf{0}$ se e solo se lo scalare è $0$ o il vettore è $\mathbf{0}$.
3. **Regola dei segni**: $k(-\mathbf{v}) = (-k)\mathbf{v} = -(k\mathbf{v})$ e $(-k)(-\mathbf{v}) = k\mathbf{v}$.
4. **Proprietà della somma**: La somma di una $n$-upla di vettori è indipendente dall'ordine (commutatività) e dal modo in cui si associano gli addendi (associatività).

## Metodi risolutivi usati nel corso
- **Verifica assiomatica**: Per determinare se una struttura è uno spazio vettoriale, occorre testare sistematicamente tutti gli assiomi (associatività, commutatività, esistenza dello zero, esistenza dell'inverso, distributività rispetto alla somma di vettori e di scalari, compatibilità del prodotto).
- **Controesempi**: Per dimostrare che una struttura non è uno spazio vettoriale, è sufficiente mostrare il fallimento di un singolo assioma.
- **Induzione**: Tecnica usata per dimostrare le proprietà delle combinazioni lineari e della somma di $n$ vettori al variare di $n$.

## Errori tipici da segnalare allo studente
- Confondere le operazioni definite nel problema (che possono essere non standard) con le operazioni classiche di $\mathbb{R}^n$.
- Non verificare correttamente l'esistenza dell'elemento neutro o dell'inverso per le operazioni "strane" (es. operazioni che non includono lo zero standard).
- Sbagliare la verifica della proprietà distributiva quando le operazioni di somma/prodotto sono ridefinite.
- Dimenticare che il prodotto scalare-vettore deve essere chiuso in $V$.

## Tipologie di esercizio da generare
- Verifica se un dato insieme, dotato di operazioni specifiche non standard, costituisce un campo.
- Verifica se una struttura $(V, +, \cdot)$ definita su un insieme $V$ con operazioni personalizzate sia uno spazio vettoriale su un campo $K$.
- Identificazione di quale assioma (tra quelli di spazio vettoriale) fallisce in una struttura proposta.
- Riconoscimento di una corretta combinazione lineare all'interno di uno spazio vettoriale dato.
