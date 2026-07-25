---
titolo: Calcolo delle derivate di funzioni elementari
gruppo: Calcolo differenziale
---
# Derivate delle funzioni elementari

## Prerequisiti
- Conoscenza delle funzioni elementari (polinomi, esponenziali, logaritmi, funzioni trigonometriche).
- Concetto di limite e continuità.
- Definizione di derivata e di rapporto incrementale.
- Operazioni algebriche di base e proprietà dei logaritmi/esponenziali.

## Definizioni e notazione del corso
- La derivata di una funzione $f$ in $x$ è indicata con la notazione $\frac{d}{dx}f(x)$.
- L'esponenziale in base $a$ è legato al numero di Nepero $e$ dalla relazione $a^x = e^{x \log a}$.
- La derivazione di funzioni inverse segue il teorema: se $f$ è invertibile e derivabile, allora $\frac{d}{dy}f^{-1}(y) = \frac{1}{f'(f^{-1}(y))}$.

## Risultati fondamentali
1. Derivata di potenza generica ($n \in \mathbb{N}$ o $b \in \mathbb{R}$): $\frac{d}{dx}x^b = b x^{b-1}$.
2. Derivata di esponenziali e logaritmi: $\frac{d}{dx}e^x = e^x$, $\frac{d}{dx}a^x = a^x \log a$, $\frac{d}{dx}\log x = \frac{1}{x}$.
3. Derivate trigonometriche inverse: $\frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1-x^2}}$, $\frac{d}{dx}\arccos x = -\frac{1}{\sqrt{1-x^2}}$, $\frac{d}{dx}\arctan x = \frac{1}{1+x^2}$.
4. Regola di derivazione di una funzione composta (catena): $\frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)$.
5. Regola della derivata di una funzione del tipo $f(x)^{g(x)}$: $\frac{d}{dx}f(x)^{g(x)} = f(x)^{g(x)} \cdot \frac{d}{dx}(g(x) \log f(x))$.

## Metodi risolutivi usati nel corso
- Applicazione ricorsiva delle regole di derivazione per somma, prodotto e quoziente.
- Uso del cambio di variabile o della scomposizione in funzioni elementari per gestire composizioni complesse.
- Trasformazione in forma esponenziale per funzioni con variabile sia nella base che nell'esponente ($f(x)^{g(x)} \to e^{g(x) \log f(x)}$).

## Errori tipici da segnalare allo studente
1. Confusione tra la derivata di $x^n$ ($nx^{n-1}$) e quella di $a^x$ ($a^x \log a$).
2. Dimenticare la derivata della parte interna quando si applica la regola della catena (derivata della funzione composta).
3. Sbagliare i segni nelle derivate di $\arccos x$ o nella derivata del quoziente.
4. Applicare le formule delle potenze a funzioni del tipo $f(x)^{g(x)}$ ignorando la dipendenza della base dalla variabile.

## Tipologie di esercizio da generare
- Calcolo della derivata di funzioni razionali fratte (uso della regola del quoziente).
- Derivazione di funzioni composte annidate (es. $\log(\sin(x^3))$).
- Derivazione di funzioni con incognita alla base e all'esponente (es. $x^x$, $(x+\arctan x)^x$).
- Derivazione di espressioni contenenti funzioni trigonometriche e inverse.
- Applicazione delle regole di derivazione a funzioni irrazionali e prodotti di funzioni elementari.
