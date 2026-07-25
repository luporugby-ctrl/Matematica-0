---
titolo: Studio di monotonia, convessità e flessi
gruppo: Calcolo differenziale
---
# Studio di monotonia, convessità e flessi

## Prerequisiti
Conoscenza del concetto di derivata prima e seconda, calcolo delle derivate di funzioni elementari, studio del segno di disequazioni algebriche e trascendenti, nozioni base di limite.

## Definizioni e notazione del corso
- $f$ è crescente in $[a, b]$ se $\forall x_1, x_2 \in [a, b]$ con $x_1 < x_2 \implies f(x_1) \leq f(x_2)$.
- Una funzione è convessa in $[a, b]$ se il grafico giace sopra la retta tangente in ogni punto $(x_0, f(x_0))$ dell'intervallo.
- Equazione della retta tangente in $x_0$: $y = f(x_0) + f'(x_0)(x - x_0)$.
- Punto di flesso: punto $x_0$ in cui la funzione cambia concavità (da convessa a concava o viceversa).
- Notazioni equivalenti per derivata seconda: $f''(x), \frac{d^2}{dx^2}f(x), D^2f(x)$.

## Risultati fondamentali
1. Criterio di monotonia: $f$ è (de)crescente in $[a, b]$ sse $f'(x) \geq 0$ (oppure $\leq 0$) $\forall x \in (a, b)$.
2. Caratterizzazione costanti: $f$ è costante in $[a, b]$ sse $f'(x) = 0$ $\forall x \in [a, b]$.
3. Criterio di stretta monotonia: $f$ è strettamente (de)crescente sse $f'(x) \geq 0$ (o $\leq 0$) e non si annulla identicamente in alcun intervallo contenuto in $(a, b)$.
4. Criterio di convessità/concavità: Una funzione derivabile due volte è convessa in $[a, b]$ sse $f''(x) \geq 0$ $\forall x \in (a, b)$. Analogamente, è concava sse $f''(x) \leq 0$.

## Metodi risolutivi usati nel corso
- Per la monotonia: calcolare $f'(x)$, risolverne lo studio del segno ($f'(x) > 0$ indica crescita, $f'(x) < 0$ decrescita).
- Per la convessità: calcolare $f''(x)$, risolverne lo studio del segno ($f''(x) > 0$ indica convessità, $f''(x) < 0$ concavità).
- Per punti di flesso: trovare gli annullamenti di $f''(x)$ e verificare il cambio di segno della derivata seconda nell'intorno del punto.

## Errori tipici da segnalare allo studente
- Confondere il segno della derivata prima (monotonia) con quello della derivata seconda (convessità).
- Dimenticare che in un punto di flesso $f''(x)$ deve cambiare segno (non basta che sia $f''(x_0) = 0$).
- Errore nel calcolo delle derivate di prodotti o funzioni composte (es. applicazione errata della regola della catena).
- Includere erroneamente punti di discontinuità o punti dove la funzione non è derivabile nello studio della monotonia tramite il segno della derivata.

## Tipologie di esercizio da generare
- Esercizi a scelta multipla che chiedono di individuare gli intervalli di monotonia di una data funzione $f(x)$.
- Esercizi a scelta multipla che chiedono di determinare gli intervalli in cui una funzione è convessa o concava.
- Quesiti combinati che richiedono di identificare sia la monotonia che la concavità di una funzione in un dominio assegnato.
- Esercizi basati su funzioni trascendenti (esponenziali, logaritmiche, trigonometriche) dove lo studio del segno di $f'(x)$ e $f''(x)$ richiede l'uso di proprietà algebriche.
