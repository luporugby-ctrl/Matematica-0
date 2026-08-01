---
titolo: Limiti di successioni, Numero di Nepero e Cauchy
gruppo: Successioni e limiti
---
# Limiti di successioni, Numero di Nepero e Cauchy

## Prerequisiti
Conoscenza della definizione di limite di una successione, teorema dei carabinieri, permanenza del segno, definizione di successione monotona e limitata. Familiarità con la disuguaglianza di Bernoulli $(1+x)^n \geq 1 + nx$.

## Definizioni e notazione del corso
- Numero di Nepero: $e = \lim_{n \to +\infty} \left(1 + \frac{1}{n}\right)^n$.
- Successione estratta: data $a_n$, la successione $a_{n_k}$ dove $n_k$ è una sottosuccessione strettamente crescente di indici.
- Successione di Cauchy: $\forall \epsilon > 0, \exists n_0 \in \mathbb{N} : |a_j - a_k| < \epsilon, \forall j, k > n_0$.

## Risultati fondamentali
1. La successione $a_n = (1 + 1/n)^n$ è strettamente crescente e limitata, dunque convergente a $e$.
2. Generalizzazioni del limite fondamentale: se $x_n \to \pm \infty$, allora $(1 + 1/x_n)^{x_n} \to e$.
3. Teorema di Bolzano-Weierstrass: ogni successione limitata ammette almeno una sottosuccessione convergente.
4. Ogni successione convergente è di Cauchy.
5. Ogni successione di Cauchy è limitata.
6. Criterio di convergenza di Cauchy: una successione in $\mathbb{R}$ è convergente se e solo se è di Cauchy.

## Metodi risolutivi usati nel corso
- Per dimostrare la convergenza al numero di Nepero, si riconduce la successione alla forma $(1 + 1/x_n)^{x_n}$ manipolando algebricamente l'espressione.
- Per dimostrare che una successione è limitata (Bolzano-Weierstrass), si utilizza il metodo di bisezione su intervalli che contengono infiniti termini della successione.
- Per verificare la proprietà di Cauchy, si sfrutta l'equivalenza con la convergenza: se la successione converge, è di Cauchy; se è di Cauchy, ammette una sottosuccessione convergente e, per le proprietà dei lemmi di Cauchy, converge l'intera successione.

## Errori tipici da segnalare allo studente
- Confondere una successione limitata (che ammette sottosuccessioni convergenti) con una successione convergente (che ammette limite unico).
- Errata applicazione del limite notevole quando $x_n \to 0$ anziché $x_n \to \infty$.
- Pensare che una successione limitata ma non convergente possa comunque essere di Cauchy: in $\mathbb{R}$ vale l'equivalenza Cauchy $\Leftrightarrow$ convergente, quindi se non converge non è di Cauchy. La sola limitatezza garantisce solo l'esistenza di una sottosuccessione convergente (Bolzano-Weierstrass), non la convergenza dell'intera successione.
- Dimenticare che la proprietà di Cauchy è una condizione *necessaria e sufficiente* per la convergenza in $\mathbb{R}$.

## Tipologie di esercizio da generare
- Calcolo del limite di successioni esponenziali del tipo $(1 + \alpha/n)^{\beta n}$ riconducibili al numero di Nepero.
- Analisi del comportamento di successioni contenenti logaritmi, potenze e termini esponenziali (gerarchia degli infiniti).
- Domande teoriche o esercizi di verifica sulla natura di Cauchy di una successione data.
- Esercizi basati sulla limitatezza e l'estrazione di sottosuccessioni convergenti da successioni non convergenti.
