---
titolo: Integrazione di funzioni razionali fratte
gruppo: Calcolo integrale
---
# Integrazione di funzioni razionali

## Prerequisiti
Conoscenza della divisione tra polinomi, fattorizzazione di polinomi (radici reali e complesse), calcolo di derivate, tecniche base di integrazione (integrali immediati e sostituzione).

## Definizioni e notazione del corso
- Funzione razionale: rapporto tra polinomi $f(x)/g(x)$.
- Grado di un polinomio $P(x)$: indicato solitamente come $n$ o $m$.
- Divisione euclidea: $f(x) = q(x) \cdot g(x) + r(x)$, da cui $\frac{f(x)}{g(x)} = q(x) + \frac{r(x)}{g(x)}$ con $\text{deg}(r) < \text{deg}(g)$.
- Radici reali e complesse: le radici di $g(x)$ determinano la forma della decomposizione in fratti semplici.

## Risultati fondamentali
1. Linearità dell'integrale per scomporre il problema in parti elementari.
2. Decomposizione in fratti semplici: ogni funzione razionale con $\text{deg}(f) < \text{deg}(g)$ si può scrivere come somma di termini del tipo:
   - $\frac{A}{(x-r)^k}$ (radici reali)
   - $\frac{B(2x+b_1) + C}{(x^2+b_1x+b_0)^k}$ (radici complesse, usando la derivata del denominatore).
3. Integrazione dei fratti semplici:
   - $\int \frac{A}{x-r} dx = A \ln|x-r| + c$
   - $\int \frac{1}{y^2+1} dy = \arctan(y) + c$ (richiede completamento del quadrato).

## Metodi risolutivi usati nel corso
1. **Verifica dei gradi:** Se $\text{deg}(f) \geq \text{deg}(g)$, eseguire la divisione tra polinomi.
2. **Scomposizione del denominatore:** Trovare le radici di $g(x)$.
3. **Determinazione dei coefficienti:** Imporre l'uguaglianza tra la funzione originale e la somma dei fratti semplici; risolvere il sistema lineare risultante (spesso per confronto di coefficienti o assegnazione di valori particolari).
4. **Completamento del quadrato:** Per denominatori di secondo grado con $\Delta < 0$, manipolare il denominatore per ricondursi alla forma $\int \frac{1}{y^2+1} dy$.

## Errori tipici da segnalare allo studente
1. Dimenticare la divisione tra polinomi quando il grado del numeratore è maggiore o uguale a quello del denominatore.
2. Sbagliare la forma della scomposizione in fratti semplici (es. non considerare le potenze decrescenti $(x-r)^k$ o mancare il termine lineare al numeratore per le radici complesse).
3. Errore nel completamento del quadrato (es. dimenticare il fattore di normalizzazione costante fuori dall'integrale).
4. Confusione nei segni durante la risoluzione del sistema per i coefficienti $A, B, C$.

## Tipologie di esercizio da generare
- Esercizi di divisione tra polinomi: calcolo esplicito di quoziente e resto.
- Integrali con denominatori di secondo grado: casi con $\Delta > 0$, $\Delta = 0$, $\Delta < 0$.
- Integrali con denominatori di grado superiore: fattorizzazione richiesta per arrivare a fratti semplici.
- Domande a risposta multipla con 4 opzioni di risoluzione, dove l'integrando presenta gradi misti e diverse tipologie di radici al denominatore.
