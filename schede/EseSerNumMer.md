---
titolo: Studio di convergenza di serie numeriche
gruppo: Successioni e serie numeriche
---
# Studio di convergenza di serie numeriche

## Prerequisiti
Conoscenza approfondita dei limiti di successioni, gerarchia degli infiniti, algebra dei logaritmi e degli esponenziali, nozione di serie numerica come somma dei termini di una successione.

## Definizioni e notazione del corso
- Serie numerica: $\sum_{n=k}^{\infty} a_n$
- Condizione necessaria di convergenza: $\lim_{n \to +\infty} a_n = 0$
- Convergenza assoluta: la serie $\sum_{n=k}^{\infty} |a_n|$ è convergente.
- Convergenza semplice: la serie $\sum_{n=k}^{\infty} a_n$ converge, ma non necessariamente quella dei moduli.
- La notazione dei limiti è standard, solitamente $n \to +\infty$.

## Risultati fondamentali
1. **Condizione necessaria**: se $\sum a_n$ converge, allora $\lim_{n \to +\infty} a_n = 0$. Se il limite è diverso da zero, la serie non converge.
2. **Criterio del rapporto**: se $\lim_{n \to +\infty} \frac{a_{n+1}}{a_n} = L$, allora:
   - $L < 1$: la serie converge.
   - $L > 1$: la serie diverge.
3. **Criterio della radice**: se $\lim_{n \to +\infty} \sqrt[n]{a_n} = L$, allora:
   - $L < 1$: la serie converge.
   - $L > 1$: la serie diverge.
4. **Criterio degli infinitesimi** (confronto asintotico): se $a_n \sim \frac{c}{n^\alpha}$ per $n \to +\infty$, la serie converge se $\alpha > 1$ e diverge se $\alpha \leq 1$. Spesso applicato calcolando $\lim_{n \to +\infty} n^\alpha a_n = L \neq 0$.
5. **Criterio di Leibniz**: per serie a segno alterno $\sum (-1)^n b_n$ (con $b_n \geq 0$), la serie converge se $b_n$ è infinitesima e decrescente.

## Metodi risolutivi usati nel corso
- **Verifica preliminare**: calcolare sempre il limite del termine generale. Se non è 0, concludere la divergenza (per serie a termini positivi) o l'irregolarità.
- **Confronto asintotico**: usare gli sviluppi o i limiti notevoli per trovare il comportamento asintotico del termine generale e ricondursi a una serie armonica generalizzata $\sum \frac{1}{n^\alpha}$.
- **Studio della convergenza assoluta**: per serie a segno alterno, studiare la serie dei valori assoluti $\sum |a_n|$ usando i criteri per serie a termini positivi. Se converge, la serie converge assolutamente (e quindi anche semplicemente).
- **Applicazione di Leibniz**: se la serie dei moduli non converge, verificare le ipotesi di monotonia e annullamento per il criterio di Leibniz.

## Errori tipici da segnalare allo studente
1. Dimenticare che la condizione $\lim_{n \to +\infty} a_n = 0$ è solo necessaria e non sufficiente per la convergenza.
2. Applicare il criterio del rapporto o della radice quando il limite $L=1$, caso in cui i criteri risultano inconcludenti (necessario passare al confronto asintotico).
3. Sbagliare il segno o la monotonia nel criterio di Leibniz: la decrescenza è un requisito fondamentale non sempre ovvio.
4. Confondere la serie armonica $\sum \frac{1}{n}$ (divergente) con la serie armonica generalizzata $\sum \frac{1}{n^\alpha}$ con $\alpha > 1$ (convergente).

## Tipologie di esercizio da generare
- Studio della convergenza di serie a termini positivi tramite criterio del rapporto o radice.
- Studio della convergenza di serie a termini positivi tramite criterio del confronto asintotico (limiti di $n^\alpha a_n$).
- Studio della convergenza assoluta e semplice di serie a segno alterno.
- Verifica della condizione necessaria per serie dove il limite del termine generale è non nullo.
