---
titolo: Dimensione, basi e sistemi di vettori
gruppo: Spazi vettoriali
---
# Dimensione e basi di spazi vettoriali

## Prerequisiti
Conoscenza della definizione di spazio vettoriale, sottospazio, combinazione lineare, dipendenza/indipendenza lineare e concetto di insieme di generatori.

## Definizioni e notazione del corso
- Spazio vettoriale $V$ sul campo $K$.
- $\langle S \rangle$ indica il sottospazio generato dal sistema di vettori $S$.
- Un sistema di vettori $T$ si dice **massimale** in $S$ se $T \subseteq S$, $T$ è linearmente indipendente e $\langle T \rangle = \langle S \rangle$.
- **Base**: un insieme di vettori $S$ che sia linearmente indipendente e tale che $\langle S \rangle = V$.
- **Dimensione**: indicata come $\dim_K V$ o $\dim V$, rappresenta l'ordine di una base di $V$.
- **Riferimento**: una $n$-upla ordinata $(v_1, \dots, v_n)$ che costituisce una base.
- **Componenti**: dati un riferimento $R = (v_1, \dots, v_n)$, ogni $v \in V$ si scrive come $v = \sum k_i v_i$. Il vettore $(k_1, \dots, k_n)$ è il vettore delle componenti di $v$ in $R$.

## Risultati fondamentali
1. Ogni sistema $S$ di vettori ammette un sistema massimale di vettori linearmente indipendenti.
2. Un sistema $S$ è linearmente indipendente se e solo se coincide con il suo unico sistema massimale.
3. Proprietà di invarianza: tutti i sistemi massimali di uno stesso sistema $S$ hanno lo stesso numero di elementi (ordine).
4. Esistenza della base: uno spazio $V$ ammette basi finite se e solo se è finitamente generato.
5. In ogni spazio di dimensione $n$, ogni sistema linearmente indipendente di $m$ vettori può essere completato a base con altri $n-m$ vettori.
6. Applicazione coordinata: l'applicazione $\phi_R: K^n \to V$ che associa al vettore delle componenti $(k_1, \dots, k_n)$ il vettore $v = \sum k_i v_i$ è una biiezione.

## Metodi risolutivi usati nel corso
- **Estrazione di base**: per trovare una base da un sistema di generatori $S$, si analizzano i vettori scartando quelli linearmente dipendenti dai precedenti.
- **Verifica di base**: si controlla se l'insieme è linearmente indipendente e se il numero di vettori corrisponde alla dimensione nota dello spazio.
- **Calcolo della dimensione**: si determina tramite il rango della matrice formata dai vettori (scritti per riga o colonna).
- **Coordinate**: si risolve il sistema lineare associato all'equazione vettoriale $v = \sum k_i v_i$ per trovare le componenti di un vettore rispetto a una base assegnata.

## Errori tipici da segnalare allo studente
1. Confondere un sistema di generatori con una base (dimenticando di verificare l'indipendenza lineare).
2. Credere che un insieme di vettori sia base solo perché il numero di vettori è uguale alla dimensione dello spazio (manca la verifica del determinante o dell'indipendenza).
3. Errata assunzione che qualsiasi sottoinsieme di generatori sia una base.
4. Non gestire correttamente il passaggio tra coordinate in una base e coordinate in un'altra.

## Tipologie di esercizio da generare
- Determinare la dimensione di un sottospazio $W \subseteq K^n$ dato da un insieme di generatori.
- Verificare se un sottoinsieme di vettori costituisce una base di uno spazio o sottospazio.
- Completamento a base: dato un insieme di vettori indipendenti, aggiungere vettori canonici per formare una base di $K^n$.
- Calcolo della dimensione di sottospazi definiti da equazioni (es. $H = \{(a, 0, b, c) : a, b, c \in \mathbb{R}\}$).
- Calcolo delle componenti di un vettore rispetto a una base assegnata (non canonica).
