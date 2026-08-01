---
titolo: Limiti di funzioni, teorema ponte e continuità
gruppo: Successioni e limiti
---
# Limiti di funzioni, teorema ponte e continuità

## Prerequisiti
Conoscenza della definizione di limite per successioni numeriche, proprietà degli insiemi (intervalli) e concetti base di funzioni reali di variabile reale.

## Definizioni e notazione del corso
- **Punto di accumulazione**: $x_0$ è di accumulazione per $D(f)$ se $\forall \delta > 0, (B_\delta(x_0) \setminus \{x_0\}) \cap D(f) \neq \emptyset$.
- **Limite (definizione $\varepsilon-\delta$)**: $\lim_{x \to x_0} f(x) = \ell$ se $\forall \varepsilon > 0, \exists \delta > 0 : \forall x \in D(f), 0 < |x - x_0| < \delta \implies |f(x) - \ell| < \varepsilon$.
- **Intorno destro/sinistro**: $B_r^+(x_0) = \{x \in \mathbb{R} : x_0 < x < x_0 + r\}$ e $B_r^-(x_0) = \{x \in \mathbb{R} : x_0 - r < x < x_0\}$.
- **Continuità**: $f$ è continua in $x_0$ se $\lim_{x \to x_0} f(x) = f(x_0)$.

## Risultati fondamentali
1. **Teorema Ponte**: Il limite $\lim_{x \to x_0} f(x) = \ell$ sussiste se e solo se per ogni successione $\{x_n\} \subseteq D(f) \setminus \{x_0\}$ tale che $x_n \to x_0$, si ha $f(x_n) \to \ell$.
2. **Unicità del limite**: Se il limite esiste, è unico.
3. **Teoremi di confronto**: Si estendono le proprietà dei limiti di successioni (Teorema dei carabinieri, permanenza del segno) ai limiti di funzioni.
4. **Continuità delle elementari**: Tutte le funzioni elementari ($|x|, x^\alpha, a^x, \log_a x, \sin x, \cos x, \tan x$) sono continue nel loro dominio.
5. **Algebra dei limiti**: La somma, il prodotto e il quoziente di funzioni continue sono continui nel proprio dominio.

## Metodi risolutivi usati nel corso
- **Verifica formale**: Utilizzo delle definizioni $\varepsilon-\delta$ o $M-\delta$ per dimostrare l'esistenza di un limite specifico (es. maggiorazione di $|f(x) - \ell|$ tramite la distanza $|x-x_0|$).
- **Continuità a tratti**: Per funzioni definite a pezzi, la continuità in un punto di raccordo richiede l'uguaglianza dei limiti destro, sinistro e del valore della funzione nel punto.
- **Utilizzo del limite di successioni**: Sfruttare il Teorema Ponte per negare l'esistenza di un limite (trovando due successioni che divergono a valori diversi).

## Errori tipici da segnalare allo studente
1. Confondere il punto di accumulazione con un punto generico del dominio (la definizione di limite prescinde dal valore di $f$ in $x_0$).
2. Dimenticare di verificare la continuità nei punti di raccordo in funzioni definite a tratti.
3. Sbagliare la stima di $\delta$ in funzione di $\varepsilon$ durante le verifiche formali (es. non gestire correttamente il termine $|x+x_0|$).
4. Assumere che il limite esista sempre senza verificare l'uguaglianza dei limiti unilateri.

## Tipologie di esercizio da generare
- Esercizi di verifica formale (scelta multipla o dimostrazione): dato $f(x)$, individuare la corretta espressione formale che definisce il limite (es. "$\forall \varepsilon > 0, \exists \delta > 0 : \dots$").
- Esercizi di analisi della continuità: dato $f(x)$ definito a tratti (es. funzioni trigonometriche o algebriche), stabilire se la funzione è continua in punti critici.
- Esercizi di classificazione: verificare la continuità di funzioni in intervalli chiusi o aperti.
