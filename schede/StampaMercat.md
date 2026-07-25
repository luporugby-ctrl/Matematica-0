---
titolo: Limiti di successioni ed ordini di infinito
gruppo: Successioni e limiti
---
# Limiti di successioni ed ordini di infinito

## Prerequisiti
Conoscenza delle proprietà delle potenze, logaritmi, esponenziali, funzioni trigonometriche elementari, nozioni basilari di estremo superiore/inferiore e la definizione formale di limite.

## Definizioni e notazione del corso
- La successione viene indicata come $x_n$.
- Parte intera di un numero reale: $[x]$ è il più grande intero minore o uguale a $x$.
- Simbologia: $\not\exists$ indica l'assenza di limite.
- Gerarchia tra infiniti: $\log n \ll n^b \ll a^n \ll n! \ll n^n$ (con $b>0, a>1$).

## Risultati fondamentali
1. **Limite notevole potenze**: $\lim_{n\to +\infty} a^n = +\infty$ se $a>1$; $0$ se $-1 < a < 1$; $\not\exists$ se $a \le -1$.
2. **Radice n-esima**: $\lim_{n\to +\infty} \sqrt[n]{a} = 1$ per ogni $a > 0$ e $\lim_{n\to +\infty} \sqrt[n]{n^b} = 1$ per ogni $b \in \mathbb{R}$.
3. **Limiti trigonometrici**: $\lim_{n\to +\infty} \sin x_n = 0$ e $\lim_{n\to +\infty} \cos x_n = 1$ se $x_n \to 0$. Fondamentale il limite notevole $\lim_{n\to +\infty} \frac{\sin x_n}{x_n} = 1$ con $x_n \to 0$.
4. **Teorema sulle successioni monotone**: Ogni successione monotona ammette limite. Se è limitata, il limite è finito.
5. **Criterio del rapporto**: Se $a_n > 0$ e $\lim_{n\to +\infty} \frac{a_{n+1}}{a_n} = b < 1$, allora $\lim_{n\to +\infty} a_n = 0$.

## Metodi risolutivi usati nel corso
- **Teorema dei carabinieri**: Utilizzato per stringere la successione tra due funzioni note aventi lo stesso limite.
- **Riconduzione a forme note**: Trasformazione in $e^{b \log a}$ per gestire le forme indeterminate $1^{\infty}, 0^0, (+\infty)^0$.
- **Gerarchia degli infiniti**: Confronto tra la velocità di crescita delle funzioni per risolvere limiti di rapporti (es. logaritmi vs polinomi vs esponenziali).
- **Razionalizzazione**: Tecnica per eliminare le differenze tra radici (es. $\sqrt{n+1} - \sqrt{n-1}$).

## Errori tipici da segnalare allo studente
1. Considerare che una successione non limitata tenda sempre a $+\infty$ (errore su successioni oscillanti come $(-1)^n n$).
2. Applicare il criterio del rapporto quando il limite è uguale a $1$ (caso inconcludente).
3. Sbagliare il segno invertendo le disuguaglianze quando si passa ai reciproci.
4. Non verificare le ipotesi (es. $a_n > 0$) prima di applicare il criterio del rapporto.

## Tipologie di esercizio da generare
- Calcolo di limiti di successioni contenenti radici n-esime e potenze di $n$.
- Confronto di infiniti mediante gerarchie o criteri del rapporto.
- Calcolo di limiti contenenti funzioni trigonometriche (con $x_n \to 0$).
- Esercizi basati sull'uso di limiti notevoli, in particolare $\frac{\sin x_n}{x_n}$ e le forme indeterminate del tipo $1^\infty$.
- Analisi del comportamento di successioni basate su combinazioni di logaritmi e polinomi.
