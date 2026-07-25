---
titolo: Uniforme continuità e Teorema Fondamentale del Calcolo
gruppo: Calcolo integrale
---
# Uniforme continuità e Teorema Fondamentale del Calcolo

## Prerequisiti
- Definizione di limite di una funzione in un punto.
- Definizione di continuità puntuale di una funzione.
- Calcolo differenziale di base (concetto di derivata).
- Somme di Riemann e integrale definito come limite di somme.

## Definizioni e notazione del corso
- **Uniforme continuità**: $f: (a, b) \to \mathbb{R}$ è uniformemente continua se:
  $\forall \varepsilon > 0, \exists \delta(\varepsilon) > 0 : \forall x, x' \in (a, b) \text{ tali che } |x - x'| < \delta, \text{ allora } |f(x) - f(x')| < \varepsilon$.
  La differenza fondamentale rispetto alla continuità classica è che $\delta$ dipende solo da $\varepsilon$, non dal punto $x$.
- **Funzione integrale**: $F(x) = \int_{a}^{x} f(t) dt$.
- **Primitiva**: $F(x)$ è primitiva di $f(x)$ se $F'(x) = f(x)$ per ogni $x \in [a, b]$.

## Risultati fondamentali
1. **Teorema di Heine-Cantor**: Se $f$ è continua in un intervallo chiuso e limitato $[a, b]$, allora $f$ è uniformemente continua in $[a, b]$.
2. **Integrabilità delle funzioni continue**: Se $f$ è continua in $[a, b]$, allora $f$ è integrabile secondo Riemann in $[a, b]$.
3. **Teorema Fondamentale del Calcolo**: Se $f$ è continua in $[a, b]$, la funzione integrale $F(x) = \int_{a}^{x} f(t) dt$ è derivabile e risulta $F'(x) = f(x)$.
4. **Caratterizzazione delle primitive**: Se $F$ e $G$ sono primitive di $f$ nello stesso intervallo, allora $G(x) = F(x) + c$ per una costante $c \in \mathbb{R}$.
5. **Formula fondamentale**: $\int_{a}^{b} f(x) dx = G(b) - G(a)$, dove $G$ è una qualsiasi primitiva di $f$.

## Metodi risolutivi usati nel corso
- **Verifica dell'uniforme continuità**: Per funzioni non uniformemente continue su intervalli aperti, si utilizzano limiti del rapporto incrementale o analisi del comportamento all'infinito/frontiera. Per intervalli chiusi, si invoca il Teorema di Heine-Cantor.
- **Calcolo dell'integrale definito**: Si cerca una primitiva $G(x)$ della funzione integranda e si calcola la differenza tra i valori agli estremi dell'intervallo.
- **Relazione tra derivata e primitiva**: Per verificare se $F(x)$ è una primitiva di $f(x)$, si deriva $F(x)$ e si confronta il risultato con $f(x)$.

## Errori tipici da segnalare allo studente
1. Confondere la continuità puntuale con l'uniforme continuità (l'uniforme continuità è una proprietà "globale" dell'intervallo).
2. Dimenticare la costante arbitraria $c$ quando si scrive l'insieme di tutte le primitive di una funzione.
3. Sbagliare la derivazione della funzione integrale: il Teorema Fondamentale afferma che la derivata di $\int_{a}^{x} f(t) dt$ è esattamente $f(x)$.
4. Invertire gli estremi dell'integrazione o il segno nella formula di calcolo $G(b) - G(a)$.

## Tipologie di esercizio da generare
- Esercizi teorici di scelta multipla sull'uniforme continuità (es. "Data $f(x)$, è uniformemente continua in $I$?").
- Esercizi di verifica: "Date $f(x)$ e $g(x)$, verificare se $g$ è una primitiva di $f$".
- Esercizi di calcolo diretto di integrali definiti mediante ricerca della primitiva (es. funzioni polinomiali, trigonometriche, esponenziali).
- Esercizi concettuali sulla relazione tra $f$ e le sue primitive.
