---
titolo: Tecniche di integrazione: per parti e sostituzione
gruppo: Calcolo integrale
---
# Tecniche di integrazione: per parti e sostituzione

## Prerequisiti
Conoscenza delle regole di derivazione (in particolare derivata del prodotto e funzioni composte), nozioni base di primitive e integrali indefiniti elementari.

## Definizioni e notazione del corso
- Fattore finito ($f(x)$) e fattore differenziale ($g'(x)$) nel metodo per parti.
- Differenziale della variabile: $dx = g'(t)dt$ in caso di sostituzione.
- La costante di integrazione è indicata con $c$.

## Risultati fondamentali
1. Formula di integrazione per parti: $\int f(x)g'(x)dx = f(x)g(x) - \int f'(x)g(x)dx$.
2. Estensione per integrali definiti: $\int_{a}^{b} f(x)g'(x)dx = [f(x)g(x)]_{a}^{b} - \int_{a}^{b} f'(x)g(x)dx$.
3. Formula di sostituzione: $\int f(x)dx = \int f(g(t))g'(t)dt$ dove $x=g(t)$.
4. Per integrali definiti con sostituzione: $\int_{a}^{b} f(x)dx = \int_{g^{-1}(a)}^{g^{-1}(b)} f(g(t))g'(t)dt$.

## Metodi risolutivi usati nel corso
- **Integrazione per parti**: utilizzata per prodotti di funzioni di natura diversa (es. trascendente per algebrica). La scelta dei fattori deve semplificare l'integrale risultante.
- **Integrazione ciclica**: nel caso di prodotti come $e^x \sin x$, si applica la formula due volte per tornare all'integrale di partenza e risolvere l'equazione algebrica risultante.
- **Integrazione per sostituzione**: si opera un cambio di variabile per ricondurre l'integrale a una forma nota o a una funzione razionale. È cruciale il calcolo del corretto differenziale $dx$.
- **Scomposizione di funzioni razionali**: dopo la sostituzione, si ricorre spesso al metodo dei fratti semplici per risolvere integrali di funzioni razionali.

## Errori tipici da segnalare allo studente
1. Sbagliare la scelta del fattore differenziale nel metodo per parti, rendendo l'integrale più complesso anziché più semplice.
2. Dimenticare di moltiplicare per il fattore correttivo derivante dal differenziale $dx$ durante il cambio di variabile.
3. Non gestire correttamente il segno meno nell'integrale della formula per parti.
4. Mancato ritorno alla variabile $x$ (se non si lavora con estremi di integrazione definiti).

## Tipologie di esercizio da generare
1. Integrali di prodotti (es. $x \cdot \text{funzione trascendente}$, $\log x$, $\arctan x$).
2. Integrali ciclici (es. $e^x \sin x$, $e^x \cos x$).
3. Integrali risolvibili tramite sostituzione diretta o sostituzione "logaritmica" (es. $\frac{f'(x)}{f(x)}$).
4. Integrali di funzioni esponenziali che si riconducono a funzioni razionali tramite la sostituzione $t = e^x$.
