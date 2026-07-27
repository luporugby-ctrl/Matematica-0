# Scheda di sopravvivenza — Limiti e trigonometria

## 1. I valori chiave (la bussola)

| $x$ | $\sin x$ | $\cos x$ | $\tan x$ | $\arctan x$ |
|---|---|---|---|---|
| $0$ (0°) | $0$ | $1$ | $0$ | $0$ |
| $\pi/2$ (90°) | $1$ | $0$ | non esiste ($\to \pm\infty$) | $\approx 1{,}00$ |
| $\pi$ (180°) | $0$ | $-1$ | $0$ | $\approx 1{,}26$ |
| $+\infty$ | oscilla tra $-1$ e $1$ | oscilla tra $-1$ e $1$ | non esiste | $\pi/2$ |
| $-\infty$ | oscilla tra $-1$ e $1$ | oscilla tra $-1$ e $1$ | non esiste | $-\pi/2$ |

**Da ricordare:** seno e coseno all'infinito non hanno limite perché continuano a oscillare.
L'arcotangente invece si appiattisce: $\arctan x \to \pi/2$ per $x \to +\infty$.

## 2. Le sostituzioni rapide (quando il blocco $t \to 0$)

Valgono **solo** se l'argomento $t$ tende a $0$. Se $t$ non tende a zero, non si applicano.

| Blocco | Si comporta come |
|---|---|
| $\sin t$ | $t$ |
| $\tan t$ | $t$ |
| $\arcsin t$ | $t$ |
| $\arctan t$ | $t$ |
| $\log(1+t)$ | $t$ |
| $e^t - 1$ | $t$ |
| $1 - \cos t$ | $\dfrac{1}{2}t^2$ |

**Come si usa:** dentro una forma indeterminata $\frac{0}{0}$, se riconosci uno di questi blocchi
lo sostituisci con la sua versione semplice e il limite spesso si scioglie da solo.

**Attenzione:** l'ultima riga è l'unica che non dà $t$, ma $\frac{1}{2}t^2$. È l'errore più comune.

## 3. Le proprietà fondamentali da avere in memoria

| Categoria | Formula | A cosa serve |
|---|---|---|
| Relazione trigonometrica | $\tan x = \dfrac{\sin x}{\cos x}$ | Trasformare le tangenti in seni e coseni |
| Ibrido esponenziale | $A^B = e^{B \log A}$ | La stampella "e" quando hai la $x$ sia sotto che sopra |
| Logaritmi: sottrazione | $\log A - \log B = \log \dfrac{A}{B}$ | Trasformare due logaritmi in una sola frazione |
| Logaritmi: esponente | $k \log A = \log A^k$ | Portare un coefficiente sopra come potenza (e viceversa) |
| Limite di Nepero | $\lim_{x \to \pm\infty} \left(1 + \dfrac{1}{x}\right)^x = e$ | Il valore base dell'esponenziale all'infinito |
