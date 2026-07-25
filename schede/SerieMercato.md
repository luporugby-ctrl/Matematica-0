---
titolo: Serie numeriche a termini positivi
gruppo: Successioni e serie numeriche
---
# Serie numeriche a termini positivi

## Prerequisiti
Conoscenza della definizione di limite di una successione, proprietà delle successioni monotone, nozione di serie numerica come limite della successione delle somme parziali $s_n$, conoscenza delle serie geometriche e delle serie armoniche generalizzate.

## Definizioni e notazione del corso
- Serie a termini (non negativi) positivi: serie $\sum_{k=1}^{\infty} a_k$ dove $a_k \geq 0$ per ogni $k$.
- Carattere della serie: poiché la successione delle somme parziali $s_n$ è monotona crescente, la serie può solo convergere a un valore finito o divergere a $+\infty$.
- Condizione necessaria di convergenza: $\lim_{k \to \infty} a_k = 0$.

## Risultati fondamentali
1. **Teorema di convergenza:** Una serie a termini non negativi non può essere indeterminata.
2. **Criterio del confronto:** Siano $\sum a_k$ e $\sum b_k$ serie a termini positivi. Se $a_k \leq b_k$ definitivamente, allora $\sum b_k$ convergente implica $\sum a_k$ convergente, e $\sum a_k$ divergente implica $\sum b_k$ divergente.
3. **Criterio di Cauchy (Condensazione):** Se $a_k$ è una successione positiva decrescente, la serie $\sum a_k$ ha lo stesso carattere della serie $\sum 2^k a_{2^k}$.
4. **Criterio degli infinitesimi:** Data $\sum a_k$, se esiste $\ell = \lim_{k \to \infty} k^p a_k$, allora per $p > 1$ e $\ell \neq +\infty$ la serie converge; per $p \leq 1$ e $\ell \neq 0$ la serie diverge.
5. **Criterio del rapporto:** Se $\ell = \lim_{n \to \infty} \frac{a_{n+1}}{a_n}$, allora $\ell < 1 \implies$ convergente, $\ell > 1 \implies$ divergente.
6. **Criterio della radice:** Se $\ell = \lim_{n \to \infty} \sqrt[n]{a_n}$, allora $\ell < 1 \implies$ convergente, $\ell > 1 \implies$ divergente.

## Metodi risolutivi usati nel corso
- **Confronto asintotico:** Utilizzare il criterio degli infinitesimi per confrontare la serie data con serie armoniche note.
- **Stima per confronto:** Maggiorare il termine generale con serie geometriche o armoniche convergenti/divergenti.
- **Uso dei limiti notevoli:** Per calcolare i limiti richiesti dai criteri del rapporto, della radice o degli infinitesimi, spesso manipolando espressioni con fattoriali o potenze.

## Errori tipici da segnalare allo studente
1. Tentare di applicare il criterio del rapporto o della radice quando il limite $\ell$ è uguale a $1$ (il criterio non è risolutivo).
2. Dimenticare di verificare la condizione necessaria di convergenza ($a_k \to 0$) prima di applicare i criteri di convergenza.
3. Confondere il verso delle disuguaglianze nel criterio del confronto (es. pensare che se $\sum a_k$ converge allora $\sum b_k$ converge anche se $a_k \leq b_k$).
4. Applicare erroneamente il criterio di Cauchy a successioni che non sono decrescenti.

## Tipologie di esercizio da generare
- **Domande a risposta multipla:** Quesiti sul carattere di serie con parametri o sulla validità di disuguaglianze tra somme parziali.
- **Studio del carattere:** Esercizi in cui lo studente deve determinare, tramite i criteri citati, se una serie numerica (con fattoriali, potenze, logaritmi) converge o diverge.
- **Analisi di convergenza con parametri:** Determinare per quali valori del parametro $x$ o $p$ una data serie risulta convergente.
