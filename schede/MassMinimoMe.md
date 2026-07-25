---
titolo: Proprietà degli insiemi di numeri reali
gruppo: Numeri reali, estremi e proprietà topologiche elementari
---
# Proprietà degli insiemi di numeri reali

## Prerequisiti
Conoscenza di base degli insiemi numerici ($\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$) e delle operazioni algebriche fondamentali. Comprensione della notazione insiemistica e degli intervalli.

## Definizioni e notazione del corso
- $L$ è maggiorante di $A$ se $\forall a \in A$ si ha $a \le L$.
- $l$ è minorante di $A$ se $\forall a \in A$ si ha $a \ge l$.
- $M \in A$ è massimo di $A$ se è un maggiorante appartenente ad $A$.
- $m \in A$ è minimo di $A$ se è un minorante appartenente ad $A$.
- $\sup A$ (estremo superiore): è il minimo dell'insieme dei maggioranti di $A$.
- $\inf A$ (estremo inferiore): è il massimo dell'insieme dei minoranti di $A$.
- Si conviene $\sup A = +\infty$ se $A$ non è limitato superiormente, e $\inf A = -\infty$ se non è limitato inferiormente.

## Risultati fondamentali
1. Assioma di completezza: ogni insieme di numeri reali limitato superiormente ammette estremo superiore in $\mathbb{R}$.
2. Caratterizzazione dell'estremo superiore: $L = \sup A \iff$ ($1. \forall a \in A, a \le L$) e ($2. \forall b < L, \exists a \in A : a > b$).
3. Proprietà di Archimede: $\forall x \in \mathbb{R}, \exists n \in \mathbb{N} : n > x$.
4. Densità di $\mathbb{Q}$ in $\mathbb{R}$: $\forall a, b \in \mathbb{R}$ con $a < b$, esiste $q \in \mathbb{Q}$ tale che $a < q < b$.

## Metodi risolutivi usati nel corso
- Per determinare sup/inf di un insieme definito da una successione, si analizza il comportamento della funzione o della sequenza al variare di $n$.
- Per insiemi unione di intervalli o punti, si confrontano gli estremi dei singoli blocchi per identificare il massimo/minimo globale e gli estremi.
- Si utilizzano le proprietà algebriche (es. disuguaglianze) per dimostrare che un valore è un maggiorante e che è il più piccolo tra essi.
- Per provare che un valore non è il sup, si mostra che esiste un elemento dell'insieme che lo supera (o si usa la definizione negativa).

## Errori tipici da segnalare allo studente
1. Confondere l'estremo superiore (che può non appartenere all'insieme) con il massimo (che deve appartenere all'insieme).
2. Credere che ogni insieme limitato ammetta sempre sia massimo che minimo.
3. Non considerare correttamente i punti isolati o i singoli punti in unione ad intervalli durante la ricerca di sup e inf.
4. Dimenticare di verificare la seconda condizione di caratterizzazione dell'estremo superiore nei casi limite.

## Tipologie di esercizio da generare
- Determinazione di sup, inf, massimo e minimo di insiemi definiti tramite espressioni dipendenti da $n \in \mathbb{N}$ (es. $A = \{1 - \frac{1}{n^2}\}$).
- Analisi di insiemi definiti come unione di intervalli e punti singoli per identificarne i limiti.
- Problemi su insiemi definiti tramite proprietà algebriche (es. $A = \{x \in \mathbb{Q} : x^2 \le 2\}$).
- Quesiti concettuali sull'estensione dell'estremo superiore nel caso di unione di più insiemi.
