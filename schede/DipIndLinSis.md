---
titolo: Indipendenza lineare e teoremi fondamentali dei vettori
gruppo: Spazi vettoriali
---
# Indipendenza Lineare di Sistemi di Vettori

## Prerequisiti
Conoscenza della definizione di $K$-spazio vettoriale, operazioni di somma tra vettori e prodotto per uno scalare, concetto di combinazione lineare e di sottospazio generato.

## Definizioni e notazione del corso
- Un sistema di vettori è indicato come $S = [\mathbf{v}_1, \dots, \mathbf{v}_n]$.
- Il sottospazio generato dal sistema $S$ è indicato con la notazione $\langle S \rangle$.
- $S$ è linearmente indipendente se l'unica soluzione dell'equazione $k_1\mathbf{v}_1 + \dots + k_n\mathbf{v}_n = 0$ è la soluzione banale $k_1 = \dots = k_n = 0$.
- $S$ è linearmente dipendente se esistono scalari $k_i$, non tutti nulli, tali che $k_1\mathbf{v}_1 + \dots + k_n\mathbf{v}_n = 0$.
- Convenzione: il sistema vuoto è considerato linearmente indipendente.

## Risultati fondamentali
1. Un sistema $S$ è dipendente se e solo se esiste almeno un vettore $\mathbf{v} \in S$ che dipende linearmente dai rimanenti vettori, cioè $\langle S \rangle = \langle S - \{\mathbf{v}\} \rangle$.
2. Se un sistema $T$ è linearmente dipendente, ogni sovrainsieme $S$ ($T \subseteq S$) è linearmente dipendente.
3. Teorema di Steinitz: Dati due sistemi $S$ (ordine $n$) e $T$ (ordine $m$), se $T$ è linearmente indipendente e $T \subseteq \langle S \rangle$, allora $m \le n$.
4. Un sistema è indipendente se e solo se ogni suo sottosistema è indipendente.
5. In un sistema indipendente, ogni vettore del sottospazio generato si esprime in modo unico come combinazione lineare dei vettori del sistema.

## Metodi risolutivi usati nel corso
- Verifica dell'indipendenza: impostare l'equazione $k_1\mathbf{v}_1 + \dots + k_n\mathbf{v}_n = 0$ e risolvere il sistema lineare omogeneo associato per i coefficienti $k_i$.
- Riduzione di un sistema: identificare vettori linearmente dipendenti (multipli di altri o combinazioni lineari) per rimuoverli dal sistema senza modificare $\langle S \rangle$.
- Applicazione del Teorema di Steinitz: utilizzare la cardinalità dei sistemi per dedurre l'indipendenza o la dipendenza in contesti dove il calcolo diretto risulti oneroso.

## Errori tipici da segnalare allo studente
- Confondere la dipendenza lineare con la semplice proporzionalità tra soli due vettori (la proporzionalità vale solo per sistemi di ordine 2).
- Dimenticare che la dipendenza di un sistema non implica che *ogni* vettore sia multiplo degli altri, ma che *almeno uno* possa essere espresso come combinazione degli altri.
- Errata interpretazione del Teorema di Steinitz: invertire le ipotesi di indipendenza tra i due sistemi messi a confronto.
- Trattare il sistema dei vettori come un insieme, ignorando che la dipendenza lineare dipende dalla specifica lista di vettori (inclusa l'eventuale presenza di vettori nulli).

## Tipologie di esercizio da generare
- Dati $n$ vettori in $\mathbb{R}^m$ o $M(n, m)$, determinare se il sistema è linearmente indipendente.
- Data una lista di vettori, identificare quale vettore può essere rimosso affinché il nuovo sistema generi lo stesso sottospazio del sistema originale.
- Verificare la validità di identità del tipo $\langle S \rangle = \langle S - \{\mathbf{v}\} \rangle$.
- Trovare combinazioni lineari non banali che producono il vettore nullo per sistemi linearmente dipendenti dati.
