---
titolo: Integrazione per sostituzione e sostituzioni speciali
gruppo: Calcolo integrale
---
# Integrazione per sostituzione: sostituzioni speciali

## Prerequisiti
Conoscenza delle tecniche fondamentali di integrazione, capacità di manipolazione algebrica (divisione tra polinomi, scomposizione in fratti semplici) e padronanza delle formule trigonometriche di base.

## Definizioni e notazione del corso
- $R(y, z)$ indica una funzione razionale nelle variabili $y$ e $z$.
- Sostituzioni parametriche (formule di bisezione): $t = \tan \frac{x}{2} \implies x = 2 \arctan t$.
- Identità trigonometriche correlate:
$\cos x = \frac{1-t^2}{1+t^2}$, $\sin x = \frac{2t}{1+t^2}$, $dx = \frac{2}{1+t^2} dt$.

## Risultati fondamentali
1. Per integrali di tipo $R(\cos x, \sin x)$, l'uso della sostituzione $t = \tan \frac{x}{2}$ trasforma l'integrale in una funzione razionale.
2. Per integrali del tipo $R(x, (\frac{ax+b}{cx+d})^{r_1}, \dots, (\frac{ax+b}{cx+d})^{r_n})$, si utilizza la sostituzione $t^N = \frac{ax+b}{cx+d}$, dove $N$ è il minimo comune multiplo dei denominatori degli esponenti $r_i$.
3. Per integrali $R(x, \sqrt{ax^2+bx+c})$, si applicano le sostituzioni di Eulero:
   - Se $a > 0$: $\sqrt{ax^2+bx+c} = \sqrt{a}x + t$ (o varianti basate su $(x+t)^2$).
   - Se $a < 0$: si usano le radici del trinomio per ricondursi a forme standard.

## Metodi risolutivi usati nel corso
- **Razionalizzazione:** Trasformare integrali trigonometrici o irrazionali in integrali di funzioni razionali tramite cambio di variabile.
- **Decomposizione:** Dopo la sostituzione, scomporre la funzione razionale in fratti semplici.
- **Completamento del quadrato:** Essenziale quando, dopo la scomposizione, si presentano denominatori di secondo grado con discriminante negativo, per ricondursi alla forma $\int \frac{1}{y^2+1} dy = \arctan y + c$.
- **Divisione tra polinomi:** Applicata ogni volta che il grado del numeratore è maggiore o uguale a quello del denominatore.

## Errori tipici da segnalare allo studente
1. Dimenticare di trasformare il differenziale $dx$ durante il cambio di variabile.
2. Errata identificazione dell'esponente $N$ nel calcolo del minimo comune multiplo tra le frazioni degli esponenti.
3. Sbagliare la scomposizione in fratti semplici, in particolare nel gestire i fattori irriducibili al denominatore.
4. Non tornare alla variabile originale $x$ dopo aver calcolato l'integrale nella variabile $t$.

## Tipologie di esercizio da generare
- Integrali di funzioni razionali in $\sin x$ e $\cos x$ (es. $1/(1+\sin x)$).
- Integrali contenenti potenze frazionarie della stessa espressione lineare (es. $\sqrt{x}, \sqrt[3]{x}$).
- Integrali di funzioni irrazionali del tipo $R(x, \sqrt{ax^2+bx+c})$.
- Quiz a risposta multipla su passaggi intermedi o risultati finali di sostituzioni speciali.
