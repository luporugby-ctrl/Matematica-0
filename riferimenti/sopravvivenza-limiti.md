# Scheda di sopravvivenza — Limiti e trigonometria

## 0. Tabella degli angoli notevoli

**Primo quadrante — quella da sapere a memoria:**

| Gradi | Radianti | $\sin$ | $\cos$ | $\tan$ |
|---|---|---|---|---|
| $0°$ | $0$ | $0$ | $1$ | $0$ |
| $30°$ | $\pi/6$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{3}}{3}$ |
| $45°$ | $\pi/4$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $1$ |
| $60°$ | $\pi/3$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{1}{2}$ | $\sqrt{3}$ |
| $90°$ | $\pi/2$ | $1$ | $0$ | non esiste |

**Trucco per ricordarla:** al numeratore di $\sin$ metti in ordine $\sqrt{0}, \sqrt{1}, \sqrt{2}, \sqrt{3}, \sqrt{4}$ (tutto diviso $2$): viene $0, \tfrac12, \tfrac{\sqrt2}{2}, \tfrac{\sqrt3}{2}, 1$. Per $\cos$ leggi la stessa fila al contrario. La $\tan$ e sempre $\sin/\cos$, non serve impararla a parte.

**Gli altri quadranti — stessi valori, cambia solo il segno:**

| Gradi | Radianti | $\sin$ | $\cos$ | $\tan$ |
|---|---|---|---|---|
| $120°$ | $2\pi/3$ | $\dfrac{\sqrt{3}}{2}$ | $-\dfrac{1}{2}$ | $-\sqrt{3}$ |
| $135°$ | $3\pi/4$ | $\dfrac{\sqrt{2}}{2}$ | $-\dfrac{\sqrt{2}}{2}$ | $-1$ |
| $150°$ | $5\pi/6$ | $\dfrac{1}{2}$ | $-\dfrac{\sqrt{3}}{2}$ | $-\dfrac{\sqrt{3}}{3}$ |
| $180°$ | $\pi$ | $0$ | $-1$ | $0$ |
| $210°$ | $7\pi/6$ | $-\dfrac{1}{2}$ | $-\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{3}}{3}$ |
| $225°$ | $5\pi/4$ | $-\dfrac{\sqrt{2}}{2}$ | $-\dfrac{\sqrt{2}}{2}$ | $1$ |
| $240°$ | $4\pi/3$ | $-\dfrac{\sqrt{3}}{2}$ | $-\dfrac{1}{2}$ | $\sqrt{3}$ |
| $270°$ | $3\pi/2$ | $-1$ | $0$ | non esiste |
| $300°$ | $5\pi/3$ | $-\dfrac{\sqrt{3}}{2}$ | $\dfrac{1}{2}$ | $-\sqrt{3}$ |
| $315°$ | $7\pi/4$ | $-\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $-1$ |
| $330°$ | $11\pi/6$ | $-\dfrac{1}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $-\dfrac{\sqrt{3}}{3}$ |
| $360°$ | $2\pi$ | $0$ | $1$ | $0$ |

**Il segno si ricorda dal quadrante:** in I quadrante tutto positivo, in II solo $\sin$, in III solo $\tan$, in IV solo $\cos$ (frase mnemonica: "Tutti Studenti Tengono Coraggio").

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
