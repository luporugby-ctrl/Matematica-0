# Scheda di sopravvivenza — Serie: quale criterio uso?

## 1. Il primo controllo, sempre

Prima di scegliere un criterio, verifica la condizione necessaria:
$$\lim_{k \to \infty} a_k = 0$$

**Se non vale:** la serie diverge, punto. Non serve altro.
**Se vale:** non dice ancora nulla sulla convergenza, si passa ai criteri veri e propri.

## 2. La mappa dei criteri (serie a termini positivi)

| Come si presenta il termine generale $a_k$ | Criterio da provare | Cosa guardare |
|---|---|---|
| Confrontabile a occhio con una serie nota (geometrica, armonica) | Confronto diretto | $a_k \leq b_k$ definitivamente, con $\sum b_k$ di carattere noto |
| Rapporto complicato ma "somigliante" a $k^p$ per $k \to \infty$ | Criterio degli infinitesimi (confronto asintotico) | $\ell = \lim_{k\to\infty} k^p a_k$: se $p>1$ e $\ell$ finito, converge; se $p\leq 1$ e $\ell \neq 0$, diverge |
| Fattoriali, potenze $k$-esime ($a^k$, $k^k$) | Criterio del rapporto | $\ell = \lim \dfrac{a_{k+1}}{a_k}$: $\ell<1$ converge, $\ell>1$ diverge, $\ell=1$ non dice nulla |
| Tutto elevato alla $k$ (es. $\left(\frac{k}{k+1}\right)^{k^2}$) | Criterio della radice | $\ell = \lim \sqrt[k]{a_k}$: stesse soglie del rapporto |
| Termine decrescente, non facile da confrontare | Criterio di condensazione di Cauchy | Stesso carattere di $\sum 2^k a_{2^k}$ |

**Attenzione:** rapporto e radice con $\ell = 1$ non sono falliti, sono inconcludenti: bisogna cambiare criterio, non concludere "non convergente".

## 3. Se la serie non è a termini positivi

| Situazione | Cosa fare |
|---|---|
| Segno alterno, es. $\sum (-1)^k a_k$ con $a_k \geq 0$ | Criterio di Leibniz: se $a_k$ è decrescente e $a_k \to 0$, la serie converge |
| Segno qualsiasi, non alterno in modo regolare | Studia $\sum \lvert a_k \rvert$ con i criteri della sezione 2 |

**Da ricordare:** se $\sum \lvert a_k \rvert$ converge, allora $\sum a_k$ converge di sicuro (convergenza assoluta implica convergenza). Il contrario non è vero: una serie può convergere senza convergere assolutamente (es. $\sum \frac{(-1)^k}{k}$).

## 4. L'ordine consigliato quando non sai da dove iniziare

1. Condizione necessaria ($a_k \to 0$?). Se fallisce, hai finito.
2. Il termine è a segno alterno? Prova Leibniz.
3. Altrimenti guarda la forma: fattoriali o potenze $k$-esime → rapporto o radice; rapporto di polinomi o forme miste → confronto asintotico.
4. Se niente si applica in modo pulito, cerca un confronto diretto con una serie nota.
