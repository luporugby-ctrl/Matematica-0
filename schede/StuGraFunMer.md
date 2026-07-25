---
titolo: Studio qualitativo del grafico di funzioni
gruppo: Calcolo differenziale
---
# Studio qualitativo del grafico di funzioni

## Prerequisiti
Conoscenza delle proprietà delle funzioni elementari (esponenziali, logaritmi, potenze, trigonometriche), calcolo dei limiti, tecniche di derivazione e risoluzione di disequazioni algebriche e trascendenti.

## Definizioni e notazione del corso
- **Insieme di definizione**: $A \subseteq \mathbb{R}$ dove la funzione è definita.
- **Asintoto orizzontale**: retta $y = \ell$ se $\lim_{x \to \infty} f(x) = \ell$.
- **Asintoto obliquo**: retta $y = mx + q$ con $m = \lim_{x \to \infty} \frac{f(x)}{x}$ e $q = \lim_{x \to \infty} (f(x) - mx)$.
- **Asintoto verticale**: retta $x = x_0$ se $\lim_{x \to x_0} f(x) = \infty$.
- **Criterio di monotonia**: $f'(x) \geq 0 \iff f$ crescente; $f'(x) \leq 0 \iff f$ decrescente.
- **Criterio di convessità**: $f''(x) \geq 0 \iff f$ convessa; $f''(x) \leq 0 \iff f$ concava.

## Risultati fondamentali
1. **Ricerca asintoti**: Analisi dei limiti nei punti di accumulazione non inclusi in $A$ o agli estremi del dominio.
2. **Primo criterio massimi/minimi**: Se $f'(x_0) = 0$, $x_0$ è minimo se $f''(x_0) > 0$, massimo se $f''(x_0) < 0$.
3. **Secondo criterio massimi/minimi**: Dato $f'(x_0) = \dots = f^{(n-1)}(x_0) = 0$, se $n$ è pari: $f^{(n)}(x_0) > 0 \implies$ min, $f^{(n)}(x_0) < 0 \implies$ max; se $n$ è dispari: non è un estremo.
4. **Classificazione flessi**:
   - Tangente verticale: continua in $x_0$ ma non derivabile (limiti del rapporto incrementale $\infty$).
   - Tangente orizzontale: $f'(x_0) = 0$ e cambio di concavità.
   - Tangente obliqua: $f'(x_0) \neq 0$ e cambio di concavità.

## Metodi risolutivi usati nel corso
- **Studio del dominio**: Risoluzione del sistema di condizioni di esistenza (denominatori $\neq 0$, argomenti logaritmi $> 0$, basi radici pari $\geq 0$).
- **Sfruttamento simmetrie**: Controllo $f(-x) = \pm f(x)$ per ridurre il dominio di studio.
- **Ricerca asintoti obliqui**: Calcolo separato di $m$ e $q$ per $x \to +\infty$ e $x \to -\infty$, prestando attenzione al segno di $x$ (es. $\sqrt{x^2} = |x|$).
- **Razionalizzazione**: Tecnica fondamentale per risolvere le forme indeterminate del tipo $\infty - \infty$ nel calcolo di $q$.
- **Analisi del segno della derivata**: Risoluzione delle disequazioni associate a $f'(x)$ e $f''(x)$ per determinare crescenza, decrescenza e concavità.

## Errori tipici da segnalare allo studente
1. **Sbagliare la gestione dei moduli**: Dimenticare che $\sqrt{x^2} = |x|$ durante il calcolo del limite per $x \to -\infty$.
2. **Interpretazione errata dei punti stazionari**: Confondere un punto dove la derivata è nulla con un punto di estremo (ignorando i casi di flesso a tangente orizzontale).
3. **Trascurare le condizioni di esistenza**: Dimenticare che la derivata prima stessa può avere un dominio ristretto rispetto alla funzione originale.
4. **Errori nel segno della disequazione**: Errata applicazione della regola dei segni nei prodotti o rapporti che compongono $f'(x)$.

## Tipologie di esercizio da generare
- **Domande a risposta multipla (o vero/falso)**: Analisi di una funzione complessa (es. razionale, esponenziale, logaritmica) chiedendo di identificare correttamente asintoti, estremi relativi, intervalli di monotonia o punti di flesso.
- **Studio completo**: Richiesta di determinazione di tutti i parametri critici (dominio, limiti, derivate) per tracciare il grafico qualitativo di una funzione data.
