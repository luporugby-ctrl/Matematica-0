# Scheda di sopravvivenza — Primitive immediate

## Livello 0 — Primitive elementari

Tabella speculare a quella delle derivate: leggila al contrario. Ogni primitiva è definita a meno di una costante $c$.

| $f(x)$ | $\int f(x)\,dx$ | Come ricordarla |
|---|---|---|
| $0$ | $c$ | La derivata di una costante è zero: qui si torna indietro. |
| $1$ | $x + c$ | Il caso più semplice. |
| $x^n$ ($n \neq -1$) | $\dfrac{x^{n+1}}{n+1} + c$ | L'esponente sale di 1 e si divide per il nuovo esponente: l'opposto della regola delle derivate. |
| $\dfrac{1}{x}$ | $\log\lvert x \rvert + c$ | Il caso escluso sopra ($n=-1$): qui il valore assoluto è obbligatorio, il logaritmo esiste solo per argomenti positivi. |
| $e^x$ | $e^x + c$ | Come per la derivata: resta se stessa. |
| $a^x$ | $\dfrac{a^x}{\log a} + c$ | Specchio di $\frac{d}{dx}a^x = a^x \log a$: qui si divide invece di moltiplicare. |
| $\sin x$ | $-\cos x + c$ | Il segno meno compare qui, non sul coseno: attenzione, è l'opposto di dove ci si aspetta. |
| $\cos x$ | $\sin x + c$ | Nessun segno, a differenza della primitiva del seno. |
| $\dfrac{1}{\cos^2 x}$ | $\tan x + c$ | Specchio di $\frac{d}{dx}\tan x = \frac{1}{\cos^2 x}$. |
| $\dfrac{1}{1+x^2}$ | $\arctan x + c$ | Specchio della derivata dell'arcotangente. |
| $\dfrac{1}{\sqrt{1-x^2}}$ | $\arcsin x + c$ | Specchio della derivata dell'arcoseno. |

**Attenzione:** $\int \frac{1}{x}dx = \log\lvert x \rvert + c$, non $\log x + c$. Se il dominio dell'esercizio è già $x>0$ il valore assoluto è ridondante ma non è mai sbagliato scriverlo.

## Livello 1 — Le tre mosse quando la primitiva non è immediata

| Situazione | Tecnica | Idea |
|---|---|---|
| Somma o differenza di pezzi immediati | Linearità | $\int (f+g) = \int f + \int g$: si integra pezzo per pezzo. |
| Prodotto di due funzioni "di natura diversa" (polinomio per esponenziale, polinomio per seno, ecc.) | Per parti | $\int f g' = fg - \int f' g$. Scegli come $f$ quella che si semplifica derivando (di solito il polinomio). |
| Funzione composta con un pezzo che è "quasi" la derivata dell'argomento | Sostituzione | Poni $t = g(x)$; se compare $g'(x)\,dx$ nell'integrale, sparisce tutto e resta un integrale immediato in $t$. |

**Come si riconosce la sostituzione al volo:** se vedi $\int g'(x) \cdot h(g(x))\,dx$, cioè la derivata di qualcosa moltiplicata per una funzione di quel qualcosa, è quasi sempre sostituzione. Esempio: $\int 2x \cos(x^2)\,dx$, con $t=x^2$ diventa $\int \cos t\,dt = \sin t + c = \sin(x^2)+c$.

## Le trappole più comuni

1. Dimenticare la costante $c$: due primitive della stessa funzione differiscono sempre per una costante, mai per altro.
2. Scordare il valore assoluto in $\int \frac{1}{x}dx$.
3. Scambiare i segni tra $\int \sin x\,dx = -\cos x + c$ e $\int \cos x\,dx = \sin x + c$: sono opposti a dove ci si aspetterebbe guardando le derivate.
4. Nella sostituzione, dimenticare di cambiare anche $dx$ (non solo l'argomento della funzione).
5. Nell'integrazione per parti, scegliere $f$ e $g'$ al contrario e finire con un integrale più complicato di quello di partenza.
