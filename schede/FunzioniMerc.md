---
titolo: Classificazione dei punti di discontinuità
gruppo: Funzioni, continuita e limiti di funzione
---
# Classificazione dei punti di discontinuità

## Prerequisiti
Conoscenza della definizione di limite di una funzione in un punto, algebra dei limiti, proprietà delle funzioni elementari ($x^n, \log_a x, \sin x, \cos x$, ecc.) e concetto di funzione monotona.

## Definizioni e notazione del corso
- **Continuità**: $f$ è continua in $x_0 \in A$ se $\forall \varepsilon > 0, \exists \delta > 0$ tale che $\forall x \in A, |x-x_0| < \delta \implies |f(x) - f(x_0)| < \varepsilon$. Equivalentemente: $\lim_{x \to x_0} f(x) = f(x_0)$.
- **Discontinuità eliminabile**: $\exists \lim_{x \to x_0} f(x) = \ell$, ma $\ell \neq f(x_0)$ (oppure $x_0$ non è nel dominio).
- **Discontinuità di prima specie**: Esistono finiti i limiti destro e sinistro, ma sono diversi: $\lim_{x \to x_0^-} f(x) \neq \lim_{x \to x_0^+} f(x)$.
- **Discontinuità di seconda specie**: Almeno uno dei due limiti destro o sinistro non esiste o è infinito.
- **Salto**: $s(x_0) = \lim_{x \to x_0^+} f(x) - \lim_{x \to x_0^-} f(x)$.

## Risultati fondamentali
1. Le funzioni monotone ammettono sempre limite destro e sinistro in ogni punto interno al loro dominio.
2. Una funzione monotona non può avere discontinuità di seconda specie né eliminabili (ammette solo discontinuità di prima specie).
3. Una funzione monotona su $[a, b]$ ha al massimo un insieme numerabile di punti di discontinuità.
4. Ogni funzione $f$ definita in $A \setminus \{x_0\}$ che ammette limite $\ell$ in $x_0$ può essere resa continua tramite il prolungamento $\bar{f}(x) = f(x)$ per $x \neq x_0$ e $\bar{f}(x_0) = \ell$.

## Metodi risolutivi usati nel corso
- Per classificare un punto $x_0$: calcolare separatamente $\lim_{x \to x_0^-} f(x)$ e $\lim_{x \to x_0^+} f(x)$.
- Confrontare i limiti trovati con $f(x_0)$ per distinguere tra continuità, eliminabilità o salti.
- Per le funzioni definite a tratti, verificare la continuità nei punti di giunzione analizzando i limiti laterali.
- Utilizzare i limiti notevoli (es. $\lim_{x \to 0} \frac{\sin x}{x} = 1$) per risolvere le forme indeterminate nelle definizioni a tratti.

## Errori tipici da segnalare allo studente
1. Confondere una discontinuità eliminabile con una di prima specie (dimenticare che nella prima specie i limiti devono essere finiti ma diversi).
2. Dimenticare di verificare se il punto di studio appartiene al dominio della funzione.
3. Pensare che una funzione possa essere continua anche se il limite destro e sinistro coincidono ma non coincidono con il valore assunto dalla funzione.
4. Trascurare il calcolo dei limiti destro e sinistro separatamente quando la funzione è definita con valore assoluto o tramite funzioni definite a tratti.

## Tipologie di esercizio da generare
- Classificazione di discontinuità in funzioni definite a tratti con punti di raccordo.
- Esercizi basati su funzioni con argomenti esponenziali o logaritmici (es. $2^{-1/x}$) che tendono a infiniti o valori specifici.
- Esercizi di "prolungamento per continuità": trovare il valore da assegnare a una funzione in un punto isolato per renderla continua.
- Analisi teorica su funzioni monotone: determinazione del tipo di salto in punti critici.
