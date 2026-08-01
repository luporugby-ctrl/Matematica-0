---
titolo: Introduzione alle serie numeriche
gruppo: Serie numeriche
---
# Serie numeriche: definizioni, convergenza e proprietà

## Prerequisiti
Conoscenza del concetto di successione di numeri reali, calcolo dei limiti di successioni, principio di induzione, algebra dei limiti.

## Definizioni e notazione del corso
- Somme parziali: $s_n := \sum_{k=1}^{n} a_k$.
- Serie numerica: $\sum_{k=1}^{\infty} a_k$ è definita come il limite delle somme parziali $\lim_{n \to +\infty} s_n$.
- Convergenza: la serie converge a $s \in \mathbb{R}$ se il limite è finito.
- Divergenza: la serie diverge a $+\infty$ o $-\infty$ se il limite è infinito.
- Indeterminatezza: la serie è indeterminata se il limite non esiste.
- Resto $n$-esimo (coda): $R_n = \sum_{k=n+1}^{\infty} a_k$.

## Risultati fondamentali
1. Serie geometrica: $\sum_{k=0}^{\infty} a^k$ converge a $\frac{1}{1-a}$ per $|a| < 1$; diverge per $a \ge 1$; è indeterminata per $a \le -1$.
2. Serie di Mengoli: $\sum_{k=1}^{\infty} \frac{1}{k(k+1)} = 1$.
3. Criterio di Cauchy per serie: la serie converge se e solo se $\forall \varepsilon > 0, \exists n_0 \in \mathbb{N} : \left| \sum_{k=n+1}^{n+p} a_k \right| < \varepsilon, \forall n > n_0, \forall p \in \mathbb{N}$.
4. Condizione necessaria: se $\sum_{k=1}^{\infty} a_k$ converge, allora $\lim_{k \to +\infty} a_k = 0$.
5. Linearità: se le serie sono regolari, $\sum (a_k + b_k) = \sum a_k + \sum b_k$ e $\sum c \cdot a_k = c \sum a_k$.
6. Teorema del resto: se una serie converge, allora il suo resto $R_n$ è infinitesimo, ovvero $\lim_{n \to +\infty} R_n = 0$.

## Metodi risolutivi usati nel corso
- Studio del limite delle somme parziali $s_n$ tramite semplificazioni algebriche o telescopiche (es. serie di Mengoli).
- Verifica della condizione necessaria per la convergenza: se il termine generale non tende a zero, la serie non può convergere.
- Utilizzo della serie geometrica come riferimento per calcoli di somme di serie.
- Applicazione delle proprietà di linearità per calcolare la somma di serie combinate o serie a termini noti.

## Errori tipici da segnalare allo studente
1. Confondere la condizione necessaria (limite del termine generale uguale a 0) con una condizione sufficiente. La serie armonica $\sum \frac{1}{k}$ ne è il controesempio classico.
2. Applicare le proprietà di linearità (somma di serie) in presenza di forme indeterminate (es. $\infty - \infty$).
3. Non prestare attenzione all'indice di partenza (es. $k=0$ vs $k=1$) nel calcolo della somma della serie geometrica, che altera il valore del limite delle somme parziali.
4. Errata manipolazione dei resti o troncamento prematuro della serie senza verificare la convergenza della serie originale.

## Tipologie di esercizio da generare
- Verifica del carattere di serie date (convergenza, divergenza, indeterminatezza) basata su definizioni.
- Calcolo della somma di serie combinando termini di serie note (geometriche o di Mengoli) mediante linearità.
- Domande teoriche sul comportamento dei resti o sulla condizione necessaria di Cauchy.
- Esercizi che richiedono il calcolo esplicito del limite delle somme parziali per testare la comprensione del processo di convergenza.
