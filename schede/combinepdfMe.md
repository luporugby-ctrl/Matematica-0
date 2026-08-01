---
titolo: Topologia della retta e principio di induzione
gruppo: Preliminari
---
# Topologia della retta reale e induzione

## Prerequisiti
Nozioni basilari di algebra, conoscenza delle proprietà delle disuguaglianze e dimestichezza con la notazione di sommatoria.

## Definizioni e notazione del corso
- **Valore assoluto:** $|a| = \max\{a, -a\}$.
- **Distanza:** $d(x,y) = |x-y|$.
- **Intorno sferico:** $B_r(x_0) = \{x \in \mathbb{R} : |x - x_0| < r\}$.
- **Insieme aperto:** $A \subseteq \mathbb{R}$ è aperto se $\forall x \in A, \exists r > 0$ tale che $B_r(x) \subseteq A$.
- **Insieme chiuso:** $D \subseteq \mathbb{R}$ è chiuso se il suo complementare $D^c$ è aperto.
- **Punto di accumulazione:** $x \in \mathbb{R}$ è di accumulazione per $A$ se ogni intorno di $x$ contiene almeno un punto di $A$ distinto da $x$.
- **Notazione:** Si usano i simboli $\bigcup$ e $\bigcap$ per unioni e intersezioni, anche su famiglie numerabili.

## Risultati fondamentali
1. **Disuguaglianza triangolare:** $d(x,y) \le d(x,z) + d(z,y)$.
2. **Proprietà topologiche:** L'unione (anche infinita numerabile) di aperti è aperta; l'intersezione di un numero finito di aperti è aperta.
3. **Chiusi e accumulazione:** Un insieme è chiuso se e solo se contiene tutti i suoi punti di accumulazione.
4. **Principio di induzione:** Se una proprietà $P(n)$ è vera per $n=1$ (base) e $P(n) \implies P(n+1)$ (passo induttivo), allora è vera per ogni $n \in \mathbb{N}$.
5. **Disuguaglianza di Bernoulli:** $(1+x)^n \ge 1+nx$ per ogni $x \ge -1$ e $n \in \mathbb{N}$.

## Metodi risolutivi usati nel corso
- **Verifica di aperti/chiusi:** Per testare se un insieme è aperto, occorre mostrare che per ogni suo punto esiste un raggio $r$ sufficientemente piccolo da mantenere l'intorno all'interno dell'insieme.
- **Dimostrazione per induzione:** 
  1. Verificare la base ($n=1$ o $n=n_0$).
  2. Supporre la tesi vera per $n$ (ipotesi induttiva).
  3. Utilizzare l'ipotesi per dimostrare la validità per $n+1$, manipolando algebricamente l'espressione (es. sommatorie).
- **Dimostrazione per assurdo:** Usata frequentemente per negare l'appartenenza a $\mathbb{Q}$ o per provare la chiusura di un insieme.

## Errori tipici da segnalare allo studente
1. Confondere un intorno di un punto con un insieme aperto in generale.
2. Dimenticare di verificare il "passo base" nella dimostrazione per induzione.
3. Sbagliare la manipolazione algebrica nel passaggio da $n$ a $n+1$ nelle somme, specialmente nel gestire l'ultimo termine aggiunto.
4. Pensare che l'intersezione di infiniti aperti sia sempre aperta (non è garantito).

## Tipologie di esercizio da generare
- Determinazione delle proprietà topologiche (aperto/chiuso) di un insieme dato come intersezione o unione di intervalli.
- Identificazione dei punti di accumulazione per insiemi definiti come unioni numerabili.
- Dimostrazione di uguaglianze riguardanti sommatorie mediante il principio di induzione.
- Dimostrazione di divisibilità di espressioni polinomiali usando il principio di induzione.
- Applicazione del principio di induzione per provare disuguaglianze.
