# Scheda di sopravvivenza — Derivate

## Livello 0 — Derivate elementari

| $f(x)$ | $f'(x)$ | Come ricordarla |
|---|---|---|
| $q$ (costante) | $0$ | Un numero fermo non varia: pendenza zero. |
| $x$ | $1$ | Cresce di uno ogni uno. |
| $mx + q$ (retta) | $m$ | Resta solo il coefficiente angolare. |
| $x^2$ | $2x$ | L'esponente scende davanti. |
| $x^3$ | $3x^2$ | L'esponente scende e la potenza cala di 1. |
| $x^n$ | $n\,x^{n-1}$ | Regola generale: porti $n$ davanti e togli 1 all'esponente. |
| $\sqrt{x}$ | $\dfrac{1}{2\sqrt{x}}$ | E $x^{1/2}$: stessa regola delle potenze, con $n = \frac12$. |
| $\dfrac{1}{x}$ | $-\dfrac{1}{x^2}$ | E $x^{-1}$: sempre la regola delle potenze, con $n = -1$. |
| $\sin x$ | $\cos x$ | Il seno diventa coseno. |
| $\cos x$ | $-\sin x$ | Il coseno diventa **meno** seno. Il segno e l'errore piu frequente. |
| $\tan x$ | $\dfrac{1}{\cos^2 x}$ | Si ricava dal quoziente $\frac{\sin x}{\cos x}$, non serve impararla a memoria. |
| $e^x$ | $e^x$ | L'unica funzione che resta se stessa. Per questo $e$ e ovunque. |
| $a^x$ | $a^x \log a$ | Come $e^x$, ma con la spia $\log a$ davanti. Se $a = e$, $\log e = 1$ e torna il caso sopra. |
| $\log x$ | $\dfrac{1}{x}$ | Vale solo per $x > 0$, dove il logaritmo esiste. |
| $\arctan x$ | $\dfrac{1}{1+x^2}$ | Denominatore sempre positivo: l'arcotangente cresce sempre. |
| $\arcsin x$ | $\dfrac{1}{\sqrt{1-x^2}}$ | Esplode in $x = \pm 1$, cioe agli estremi del dominio. |

## Livello 1 — Regole operative

| Operazione | Derivata |
|---|---|
| $(f + g)'$ | $f' + g'$ |
| $(f - g)'$ | $f' - g'$ |
| $(f \cdot g)'$ | $f'g + fg'$ |
| $\left(\dfrac{f}{g}\right)'$ | $\dfrac{f'g - fg'}{g^2}$ |
| $[\,f(g(x))\,]'$ | $f'(g(x)) \cdot g'(x)$ |

**Somma e differenza:** si deriva ogni pezzo per conto suo, mantenendo il segno.

**Prodotto:** derivata del primo per il secondo non derivato, piu il primo non derivato per la derivata del secondo.

**Quoziente:** al numeratore $f'g - fg'$ — l'ordine conta, non e simmetrico come il prodotto. Al denominatore il secondo al quadrato.

**Catena (funzione composta):** e la regola che userai piu di tutte. Si deriva la funzione esterna
lasciando dentro l'argomento com'e, poi si moltiplica per la derivata dell'argomento.
Esempi: $[\sin(3x)]' = \cos(3x)\cdot 3$, $[e^{x^2}]' = e^{x^2}\cdot 2x$, $[\log(5x+1)]' = \dfrac{5}{5x+1}$.

## Livello 2 — Tecniche algebriche per il rapporto incrementale

Servono quando la derivata va calcolata **dalla definizione**, cioe risolvendo
$$f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$$

| Tecnica | Formula | Quando serve |
|---|---|---|
| Quadrato di binomio | $(a+b)^2 = a^2 + 2ab + b^2$ | Sviluppare $(x_0 + h)^2$ nel rapporto incrementale. |
| Differenza di quadrati | $a^2 - b^2 = (a-b)(a+b)$ | Scomporre e semplificare le forme $\frac{0}{0}$. |
| Raccoglimento a fattor comune | $\dfrac{h\,(2x_0 + h)}{h} = 2x_0 + h$ | Semplificare la $h$ al denominatore: e il passaggio che sblocca tutto. |
| Prostaferesi (seno) | $\sin x - \sin x_0 = 2\sin\dfrac{x-x_0}{2}\cos\dfrac{x+x_0}{2}$ | Trasformare una differenza di seni in prodotto. |
| Prostaferesi (coseno) | $\cos x - \cos x_0 = -2\sin\dfrac{x-x_0}{2}\sin\dfrac{x+x_0}{2}$ | Trasformare una differenza di coseni in prodotto. |
| Limite notevole | $\lim_{t \to 0} \dfrac{\sin t}{t} = 1$ | Chiudere il limite dopo la prostaferesi. |
| Angoli notevoli | $\sin\dfrac{\pi}{2} = 1$, $\cos \pi = -1$, $\sin\dfrac{\pi}{3} = \dfrac{\sqrt{3}}{2}$ | Sostituzione finale nei conti numerici. |

## Le trappole che costano piu punti

1. Dimenticare il meno in $(\cos x)' = -\sin x$.
2. Invertire il numeratore del quoziente: e $f'g - fg'$, non $fg' - f'g$.
3. Fermarsi alla funzione esterna e non moltiplicare per la derivata dell'argomento: $[\sin(3x)]'$ non e $\cos(3x)$, manca il $3$.
4. Applicare la regola delle potenze a $a^x$: li la $x$ e all'esponente, non alla base, e la derivata e $a^x \log a$.
5. Derivare $\log x$ senza controllare che il dominio sia $x > 0$.
