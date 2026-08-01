# Scheda di sopravvivenza — Studio di funzione: la checklist

Segui l'ordine. Ogni passo usa i risultati del precedente, saltarne uno di solito costa punti nel grafico finale.

## 1. Dominio

Escludi: denominatori nulli, argomenti negativi di radici pari, argomenti non positivi di logaritmi, argomenti fuori $[-1,1]$ per arcoseno/arcocoseno.

**Da ricordare:** il dominio non è un dettaglio preliminare, è quello che decide dove ha senso fare tutto il resto.

## 2. Simmetrie e periodicità

| Controllo | Cosa dice |
|---|---|
| $f(-x) = f(x)$ | Funzione pari, grafico simmetrico rispetto all'asse $y$: basta studiare $x \geq 0$. |
| $f(-x) = -f(x)$ | Funzione dispari, simmetrico rispetto all'origine. |
| $f(x+T) = f(x)$ | Periodica di periodo $T$: basta un solo periodo. |

Se nessuna delle tre vale, si passa oltre senza perdere tempo.

## 3. Segno e intersezioni con gli assi

Risolvi $f(x) > 0$, $f(x) = 0$ e calcola $f(0)$ (se $0$ è nel dominio). Serve per sapere dove il grafico sta sopra o sotto l'asse $x$ prima ancora di conoscerne la forma.

## 4. Limiti agli estremi del dominio e asintoti

Calcola il limite di $f$ a $\pm\infty$ e in ogni punto escluso dal dominio (o di frontiera).

| Tipo di asintoto | Condizione |
|---|---|
| Verticale in $x_0$ | $\lim_{x \to x_0} f(x) = \pm\infty$ |
| Orizzontale | $\lim_{x \to \pm\infty} f(x) = L$ finito |
| Obliquo ($y=mx+q$) | Solo se non c'è quello orizzontale: $m = \lim_{x\to\pm\infty}\frac{f(x)}{x}$, poi $q = \lim_{x\to\pm\infty}(f(x)-mx)$; asintoto reale solo se entrambi i limiti sono finiti |

## 5. Derivata prima: monotonia e punti critici

Calcola $f'(x)$, studia il segno di $f'(x) > 0$ (funzione crescente). I punti dove $f'(x)=0$ o non esiste sono candidati a massimo, minimo o flesso a tangente orizzontale/verticale: il segno di $f'$ prima e dopo il punto dice quale.

**Attenzione:** $f'(x_0)=0$ non basta per dire che $x_0$ è un massimo o un minimo. Serve controllare come cambia il segno di $f'$ attorno al punto (o il segno di $f''$).

## 6. Derivata seconda: concavità e flessi

Studia il segno di $f''(x)$: positivo vuol dire convessa (concava verso l'alto), negativo concava verso il basso. Dove $f''(x)=0$ e cambia segno, c'è un flesso.

## 7. Il grafico

Metti insieme tutto: dominio, segno, asintoti, punti di massimo/minimo/flesso con i relativi valori di $f$. Il grafico deve essere coerente con ognuno dei passi precedenti — se un pezzo non torna, è lì che c'è l'errore, non nel disegno finale.

## L'ordine da non invertire mai

Segno e limiti (passi 3-4) **prima** delle derivate (passi 5-6): senza sapere dove la funzione tende a $\pm\infty$ o a un asintoto, un massimo trovato con $f'$ non si sa nemmeno se sia globale o solo locale.
