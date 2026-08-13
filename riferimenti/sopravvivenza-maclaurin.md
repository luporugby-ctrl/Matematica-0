# Scheda di sopravvivenza — Sviluppi di Maclaurin delle funzioni elementari

## 0. La formula generale

$$f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(0)}{k!} x^k + o(x^n), \qquad x \to 0$$

**Vale solo per $x \to 0$.** Se l'argomento della funzione non tende a zero (es. $\sin(x-1)$ per $x \to 1$ va bene, ma $\sin x$ per $x \to 3$ no), lo sviluppo non si applica direttamente: bisogna prima centrare l'argomento con una sostituzione ($t = x-1$, ecc.).

## 1. La tabella degli sviluppi notevoli

| $f(x)$ | Sviluppo di Maclaurin | Resto |
|---|---|---|
| $e^x$ | $1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!} + \cdots + \dfrac{x^n}{n!}$ | $o(x^n)$ |
| $\sin x$ | $x - \dfrac{x^3}{3!} + \dfrac{x^5}{5!} - \cdots$ | $o(x^{2k+2})$ |
| $\cos x$ | $1 - \dfrac{x^2}{2!} + \dfrac{x^4}{4!} - \cdots$ | $o(x^{2k+1})$ |
| $\tan x$ | $x + \dfrac{x^3}{3} + \dfrac{2x^5}{15} + \cdots$ | $o(x^6)$ |
| $\log(1+x)$ | $x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \dfrac{x^4}{4} + \cdots$ | $o(x^n)$ |
| $(1+x)^\alpha$ | $1 + \alpha x + \dfrac{\alpha(\alpha-1)}{2!}x^2 + \dfrac{\alpha(\alpha-1)(\alpha-2)}{3!}x^3 + \cdots$ | $o(x^n)$ |
| $\dfrac{1}{1-x}$ | $1 + x + x^2 + x^3 + \cdots + x^n$ | $o(x^n)$ |
| $\dfrac{1}{1+x}$ | $1 - x + x^2 - x^3 + \cdots + (-1)^n x^n$ | $o(x^n)$ |
| $\arctan x$ | $x - \dfrac{x^3}{3} + \dfrac{x^5}{5} - \cdots$ | $o(x^{2k+2})$ |
| $\arcsin x$ | $x + \dfrac{x^3}{6} + \dfrac{3x^5}{40} + \cdots$ | $o(x^6)$ |
| $\sinh x$ | $x + \dfrac{x^3}{3!} + \dfrac{x^5}{5!} + \cdots$ | $o(x^{2k+2})$ |
| $\cosh x$ | $1 + \dfrac{x^2}{2!} + \dfrac{x^4}{4!} + \cdots$ | $o(x^{2k+1})$ |

**Casi particolari utili di $(1+x)^\alpha$:**

| $\alpha$ | Funzione | Sviluppo troncato al second'ordine |
|---|---|---|
| $-1$ | $\dfrac{1}{1+x}$ | $1 - x + x^2 + o(x^2)$ |
| $\tfrac{1}{2}$ | $\sqrt{1+x}$ | $1 + \dfrac{x}{2} - \dfrac{x^2}{8} + o(x^2)$ |
| $-\tfrac{1}{2}$ | $\dfrac{1}{\sqrt{1+x}}$ | $1 - \dfrac{x}{2} + \dfrac{3x^2}{8} + o(x^2)$ |

## 2. Come si sceglie l'ordine di troncamento

**Regola pratica:** tronca all'ordine minimo che ti fa comparire un termine diverso da zero dopo le cancellazioni. Se il primo tentativo produce $0/0$ ancora indeterminato, alza l'ordine di uno o due e ricalcola.

**Attenzione al termine "principale":** se stai calcolando un limite del tipo $\frac{f(x)}{g(x)}$ e sia $f$ che $g$ iniziano con lo stesso ordine (es. entrambi partono da $x$), non basta il primo ordine: serve andare avanti finché numeratore e denominatore non si "distinguono".

## 3. Le sostituzioni e composizioni

- **Cambio di variabile:** per sviluppare $f(x^2)$, $f(-x)$, $f(2x)$ ecc. si sostituisce direttamente nella tabella nota, senza ricalcolare le derivate da zero. Esempio: $\cos(x^2) = 1 - \dfrac{x^4}{2!} + o(x^4)$.
- **Prodotto di sviluppi:** si moltiplicano i polinomi troncando al grado voluto e scartando i termini di grado superiore (che finiscono dentro l'$o$).
- **Occhio all'ordine dell'$o$ dopo la sostituzione:** se $t = x^2$ e lo sviluppo di $f(t)$ è valido a meno di $o(t^n)$, dopo la sostituzione diventa $o(x^{2n})$, non $o(x^n)$.

## 4. Gli errori tipici da segnalare allo studente

1. **Troncamento troppo basso:** fermarsi a un ordine che non elimina l'indeterminazione, lasciando un $0/0$ apparente.
2. **Applicare lo sviluppo fuori da $x \to 0$:** usare direttamente la tabella quando l'argomento non tende a zero, senza prima centrare con una sostituzione.
3. **Sommare o-piccoli di ordine diverso senza tenere il minimo:** $o(x^2) + o(x^3) = o(x^2)$, non $o(x^3)$ né $o(x^5)$.
4. **Dimenticare il segno alterno** negli sviluppi di $\sin x$, $\log(1+x)$, $\arctan x$ (coefficienti a segni alterni) rispetto a quelli di $e^x$, $\cosh x$ (tutti positivi).
5. **Confondere $\log(1+x)$ con $\log x$:** lo sviluppo di Maclaurin vale solo per $\log(1+x)$; $\log x$ non è nemmeno definito (né derivabile con Taylor) in $x=0$.
