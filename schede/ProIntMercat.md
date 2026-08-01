---
titolo: Proprietà dell'integrale di Riemann
gruppo: Calcolo integrale
---
# Proprietà dell'integrale di Riemann

## Prerequisiti
Conoscenza della definizione di integrale di Riemann tramite somme superiori $S(P)$ e inferiori $s(P)$, concetto di partizione di un intervallo, nozioni base su estremi superiore e inferiore di una funzione, continuità di una funzione in un intervallo chiuso e limitato.

## Definizioni e notazione del corso
- Partizione $P$ di un intervallo $[a, b]$: insieme finito di punti $a = x_0 < x_1 < \dots < x_n = b$.
- Somme integrali: $S(P)$ somma superiore, $s(P)$ somma inferiore.
- Integrale di Riemann: la funzione $f$ è integrabile se l'elemento separatore tra le somme superiori e inferiori è unico.
- Convenzione sugli estremi: l'integrale è definito anche come $\int_{\beta}^{\alpha} f(x)dx = -\int_{\alpha}^{\beta} f(x)dx$ e $\int_{\alpha}^{\alpha} f(x)dx = 0$.

## Risultati fondamentali
1. Additività rispetto all'intervallo: dato $c \in [a, b]$, $\int_a^b f(x)dx = \int_a^c f(x)dx + \int_c^b f(x)dx$.
2. Linearità: se $f, g$ sono integrabili e $\alpha \in \mathbb{R}$, allora $\int_a^b [f(x) + g(x)]dx = \int_a^b f(x)dx + \int_a^b g(x)dx$ e $\int_a^b \alpha f(x)dx = \alpha \int_a^b f(x)dx$.
3. Monotonia: se $f(x) \leq g(x)$ per ogni $x \in [a, b]$, allora $\int_a^b f(x)dx \leq \int_a^b g(x)dx$.
4. Disuguaglianza del valore assoluto: $\left| \int_a^b f(x)dx \right| \leq \int_a^b |f(x)|dx$.
5. Teorema della media: se $f$ è continua in $[a, b]$, esiste $x_0 \in [a, b]$ tale che $\int_a^b f(x)dx = f(x_0)(b-a)$.

## Metodi risolutivi usati nel corso
- Scomposizione di integrali in somme o differenze sfruttando l'additività.
- Manipolazione delle costanti moltiplicative fuori dal segno di integrale tramite linearità.
- Confronto tra aree sottese ai grafici di due funzioni per stabilire disuguaglianze integrali senza calcolare esplicitamente la primitiva.
- Stima del valore di un integrale usando i valori di massimo e minimo della funzione (applicazione del Teorema della media).

## Errori tipici da segnalare allo studente
1. Confusione nel cambio di segno quando si invertono gli estremi di integrazione.
2. Applicazione errata della linearità su prodotti o quozienti di funzioni (es. pensare che l'integrale del prodotto sia il prodotto degli integrali).
3. Errata gestione dei valori assoluti all'interno dell'integrale, ignorando che la disuguaglianza $\left| \int f \right| \leq \int |f|$ non è un'uguaglianza.
4. Ignorare il segno della funzione: applicare le proprietà di monotonia senza verificare che la funzione mantenga un segno costante o che l'ordine delle funzioni sia rispettato su tutto l'intervallo.

## Tipologie di esercizio da generare
- Esercizi a scelta multipla che richiedono di identificare l'equivalenza di un'espressione integrale manipolata (uso di additività e linearità).
- Esercizi di confronto tra integrali definiti (dire quale integrale è maggiore o minore) basati sullo studio del grafico o della funzione.
- Esercizi di stima che richiedono di trovare un limite superiore e inferiore per $\int_a^b f(x)dx$ conoscendo i valori di estremo.
- Esercizi di verifica della disuguaglianza triangolare integrale (modulo di integrale vs integrale del modulo).
