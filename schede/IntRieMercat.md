---
titolo: Introduzione all'Integrale di Riemann
gruppo: Calcolo integrale
---
# Introduzione all'Integrale di Riemann

## Prerequisiti
Conoscenza delle funzioni elementari, proprietà dei supremi e degli infimi, nozioni base di sommatorie e calcolo dei limiti.

## Definizioni e notazione del corso
- Partizione $P$ di $[a, b]$: insieme di punti $a = x_0 < x_1 < \dots < x_n = b$.
- Somme inferiori: $s(P) = \sum_{k=1}^n m_k(x_k - x_{k-1})$ dove $m_k = \inf \{f(x) : x \in [x_{k-1}, x_k]\}$.
- Somme superiori: $S(P) = \sum_{k=1}^n M_k(x_k - x_{k-1})$ dove $M_k = \sup \{f(x) : x \in [x_{k-1}, x_k]\}$.
- Integrale definito: denotato con $\int_a^b f(x) dx$, esiste se il valore di separazione tra le somme inferiori e superiori è unico.

## Risultati fondamentali
1. Per ogni partizione $P$, vale sempre $s(P) \leq S(P)$.
2. Se $R = P \cup Q$ è un raffinamento, allora $s(P) \leq s(R) \leq S(R) \leq S(Q)$.
3. Una funzione $f$ limitata è integrabile secondo Riemann in $[a, b]$ se e solo se per ogni $\epsilon > 0$ esiste una partizione $P$ tale che $S(P) - s(P) < \epsilon$.
4. Per una funzione costante $f(x) = c$, l'integrale è $\int_a^b c \, dx = c(b-a)$.
5. Proprietà degli estremi: $\int_a^b f(x) dx = -\int_b^a f(x) dx$ e $\int_a^a f(x) dx = 0$.

## Metodi risolutivi usati nel corso
- Metodo di esaustione: approssimazione dell'area tramite rettangoli inscritti e circoscritti, calcolando il limite per $n \to +\infty$ delle somme.
- Calcolo esplicito di somme inferiori e superiori: per funzioni semplici, identificare $m_k$ e $M_k$ su ogni sotto-intervallo e sommare le aree.
- Caratterizzazione tramite epsilon: verificare l'integrabilità controllando se la differenza tra somma superiore e inferiore tende a zero.

## Errori tipici da segnalare allo studente
1. Confondere $m_k$ e $M_k$: scambiare inf e sup porta a calcolare somme errate.
2. Sbagliare gli estremi di integrazione: dimenticare il cambio di segno se gli estremi sono invertiti ($a > b$).
3. Non considerare la partizione completa: calcolare le somme parziali senza verificare che l'intervallo $[a, b]$ sia interamente coperto.
4. Interpretazione geometrica errata: pensare che l'integrale sia sempre un'area positiva senza considerare il segno della funzione.

## Tipologie di esercizio da generare
- Calcolo manuale di somme inferiori $s(P)$ e superiori $S(P)$ data una funzione $f(x)$ e una partizione specifica $P$.
- Verifica della integrabilità di funzioni a tratti.
- Calcolo di integrali definiti mediante le proprietà di additività dell'intervallo.
- Domande teoriche sul significato di partizione e raffinamento (lemma del confronto).
