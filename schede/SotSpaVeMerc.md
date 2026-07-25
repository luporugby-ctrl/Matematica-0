---
titolo: Sottospazi di uno spazio vettoriale
gruppo: Algebra Lineare
---
# Sottospazi di uno spazio vettoriale

## Prerequisiti
Conoscenza della definizione di $K$-spazio vettoriale, delle proprietà delle operazioni di somma tra vettori e prodotto per uno scalare, e della struttura di campo $K$.

## Definizioni e notazione del corso
- Un sottoinsieme $V' \subseteq V$ è detto **stabile** per somma e prodotto se $\forall u, v \in V' \implies u+v \in V'$ e $\forall u \in V', k \in K \implies k \cdot u \in V'$.
- Un sottoinsieme stabile e non vuoto $V'$ si dice **$K$-sottospazio vettoriale** (o sottospazio).
- **Sottospazi banali**: Lo spazio $V$ stesso e il sottospazio nullo $\{0\}$, denotato anche con $(0)$.
- **Matrici**: Denotate con $M(n, m, K)$, ovvero tabelle a doppia entrata di tipo $(n, m)$. $A^T$ indica la trasposta.
- **Notazione**: $K^n$ per vettori numerici; $M(n, m, K)$ per matrici; $M(I, K)$ per applicazioni da $I$ in $K$.

## Risultati fondamentali
1. Ogni sottospazio $V'$ di un $K$-spazio vettoriale $V$ è esso stesso uno spazio vettoriale rispetto alle operazioni indotte.
2. Un sottospazio $V'$ deve necessariamente contenere il vettore nullo $\mathbf{0}$ e, per ogni $v \in V'$, il suo opposto $-v \in V'$.
3. L'intersezione di una famiglia di sottospazi $\{V_i\}_{i \in I}$ è un sottospazio di $V$.
4. **Proprietà di combinazione lineare**: Un sottoinsieme non vuoto $V' \subseteq V$ è un sottospazio se e solo se contiene ogni combinazione lineare del tipo $\sum_{i=1}^n k_i v_i$ con $v_i \in V'$ e $k_i \in K$.

## Metodi risolutivi usati nel corso
- Per verificare se un sottoinsieme $S$ è un sottospazio, si controllano i due assiomi di chiusura:
    1. Verifica se $\mathbf{0} \in S$.
    2. Verifica se $\forall u, v \in S \implies u+v \in S$.
    3. Verifica se $\forall u \in S, k \in K \implies k \cdot u \in S$.
- Spesso è sufficiente mostrare che $S$ è chiuso rispetto alla combinazione lineare (punto 4 dei risultati).
- Per le matrici, verificare le definizioni specifiche (es. simmetria $A=A^T$, diagonalità $a_{ij}=0$ per $i \neq j$, ecc.) in relazione alla stabilità per somma e prodotto scalare.

## Errori tipici da segnalare allo studente
1. Dimenticare di verificare se il vettore nullo appartiene all'insieme $S$.
2. Confondere l'unione di sottospazi con la loro somma: l'unione di due sottospazi, in generale, non è un sottospazio.
3. Considerare come sottospazio insiemi definiti da condizioni non omogenee (es. $x+y=1$), che non contengono l'origine.
4. Applicare le operazioni di somma tra matrici o vettori di dimensioni incompatibili.

## Tipologie di esercizio da generare
- Verifica di sottospazio: dato un sottoinsieme $S \subset K^n$ definito da equazioni (es. $x-3y=0$, $x+y=c$), determinare se è un sottospazio.
- Analisi di insiemi definiti da condizioni non lineari o non omogenee (es. $x \neq y$, $y=3$, $v_1 \cdot v_2 \cdot v_3 = 1$) per dimostrare che non sono sottospazi.
- Verifica della struttura di sottospazio in insiemi di matrici: matrici simmetriche, diagonali, o con vincoli lineari sulle entrate (es. $a+c=b+d$).
- Esercizi teorici brevi: dimostrare che l'unione di due sottospazi non è un sottospazio (es. $V(d) \cup V(d')$).
