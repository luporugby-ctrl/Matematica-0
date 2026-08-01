---
titolo: Insiemi, estremi e principio di induzione
gruppo: Preliminari
---
# Insiemi, estremi e principio di induzione

## Prerequisiti
Conoscenza della logica di base, delle proprietà fondamentali dei numeri reali, delle operazioni aritmetiche e della notazione insiemistica elementare.

## Definizioni e notazione del corso
* **Insiemi:** Operazioni di unione $A \cup B = \{x : x \in A \lor x \in B\}$, intersezione $A \cap B = \{x : x \in A \land x \in C\}$, differenza $A \setminus B = \{x \in A : x \notin B\}$.
* **Sottoinsiemi:** $A$ è sottoinsieme di $B$ se ogni elemento di $A$ appartiene a $B$.
* **Insieme delle parti:** $\mathcal{P}(A)$ indica l'insieme di tutti i sottoinsiemi di $A$, incluso l'insieme vuoto $\emptyset$.
* **Estremi:** Sia $E \subseteq \mathbb{R}$. $m$ è un minorante se $m \leq x$ per ogni $x \in E$. L'estremo inferiore $\inf E$ è il massimo dei minoranti. Il minimo $\min E$ esiste se $\inf E \in E$. Analogamente per maggioranti, estremo superiore $\sup E$ e massimo $\max E$.

## Risultati fondamentali
1. **Principio di induzione:** Data una proprietà $P(n)$ definita per $n \in \mathbb{N}$, se $P(1)$ è vera e $P(n) \implies P(n+1)$, allora $P(n)$ è vera per ogni $n \in \mathbb{N}$.
2. **Induzione forte:** Si assume che $P(k)$ sia vera per ogni $k \leq n$ per dimostrare $P(n+1)$.
3. **Caratterizzazione del minimo/massimo:** Se $\inf E \in E$ allora $\inf E = \min E$. Se $\sup E \in E$ allora $\sup E = \max E$.

## Metodi risolutivi usati nel corso
* **Analisi di insiemi:** Per verificare se un insieme è limitato o ammette estremi, si riscrive l'insieme (es. esplicitando le condizioni su $x \in \mathbb{R}$) e si analizza il comportamento della funzione o della successione che lo definisce.
* **Dimostrazioni induttive:**
    1. Base: Verificare la validità per $n=1$.
    2. Ipotesi induttiva: Assumere vera la tesi per $n$.
    3. Passo induttivo: Manipolare algebricamente l'espressione per $n+1$ in modo da far comparire quella per $n$, permettendo l'applicazione dell'ipotesi. Per le divisibilità, si cerca di scomporre il termine $n+1$ isolando multipli del divisore.

## Errori tipici da segnalare allo studente
1. **Confusione tra estremo e minimo/massimo:** Assumere che un insieme ammetta sempre massimo o minimo solo perché possiede estremo superiore o inferiore (dimenticando che devono appartenere all'insieme).
2. **Incompleta definizione di $\mathcal{P}(A)$:** Dimenticare l'insieme vuoto $\emptyset$ o l'insieme stesso $A$ come sottoinsiemi.
3. **Errori nel passo induttivo:** Non manipolare correttamente l'espressione di $\alpha(n+1)$ per isolare $\alpha(n)$, rendendo impossibile sfruttare l'ipotesi induttiva.
4. **Verifica dei minoranti:** Confondere il "minore o uguale a ogni elemento" con l'appartenenza all'insieme stesso.

## Tipologie di esercizio da generare
* Determinazione di unione, intersezione e differenza tra insiemi finiti di oggetti o numeri.
* Verifica della relazione di sottoinsieme tra insiemi dati o definizioni di $\mathcal{P}(A)$.
* Analisi di insiemi di numeri reali: individuazione di $\inf, \sup, \min, \max$ e verifica se l'insieme è limitato superiormente/inferiormente.
* Dimostrazioni di divisibilità di espressioni polinomiali o esponenziali tramite il principio di induzione.
* Dimostrazioni di disuguaglianze tra espressioni numeriche (es. factorials, potenze) usando l'induzione.
