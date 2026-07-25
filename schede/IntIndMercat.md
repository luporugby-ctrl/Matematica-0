---
titolo: Introduzione all'integrale indefinito
gruppo: Calcolo integrale
---
# Calcolo dell'integrale indefinito

## Prerequisiti
Conoscenza approfondita delle derivate delle funzioni elementari e delle regole di derivazione (in particolare derivata di somma, prodotto per costante e funzione composta). Capacità di manipolazione algebrica di base.

## Definizioni e notazione del corso
L'integrale indefinito di una funzione continua $f(x)$ è l'insieme di tutte le sue primitive, indicato con:
$$\int f(x)dx = F(x) + c$$
dove $F(x)$ è una primitiva e $c$ è una costante arbitraria. 
Convenzione: si distingue nettamente tra integrale definito (un numero) e indefinito (un insieme di funzioni).

## Risultati fondamentali
1. Linearità dell'integrale: $\int (f(x) + g(x))dx = \int f(x)dx + \int g(x)dx$ e $\int \alpha f(x)dx = \alpha \int f(x)dx$.
2. Potenze: $\int x^b dx = \frac{x^{b+1}}{b+1} + c$ per $b \neq -1$.
3. Logaritmo: $\int \frac{1}{x} dx = \log |x| + c$.
4. Esponenziale: $\int e^x dx = e^x + c$.
5. Trigonometriche: $\int \sin x dx = -\cos x + c$, $\int \cos x dx = \sin x + c$, $\int \frac{1}{\cos^2 x} dx = \tan x + c$.
6. Funzioni composte: $\int f(x)^b \cdot f'(x) dx = \frac{f(x)^{b+1}}{b+1} + c$ e $\int \frac{f'(x)}{f(x)} dx = \log |f(x)| + c$.

## Metodi risolutivi usati nel corso
* **Riconoscimento immediato**: Applicazione diretta delle formule per le primitive elementari.
* **Decomposizione in somma**: Riscrivere l'integrando come somma di più termini (es. aggiungendo e sottraendo costanti al numeratore di una frazione razionale).
* **Riconoscimento di derivate di funzioni composte**: Riscrivere l'integrale nella forma $f(x)^b \cdot f'(x)$ o $\frac{f'(x)}{f(x)}$ per facilitare l'integrazione.
* **Manipolazione trigonometrica**: Utilizzo di identità fondamentali ($\sin^2 x + \cos^2 x = 1$) o formule di duplicazione per ricondursi a forme integrabili.

## Errori tipici da segnalare allo studente
1. Dimenticare la costante arbitraria $c$ nel risultato finale.
2. Applicare la regola della potenza $\int x^b dx$ anche quando $b = -1$.
3. Sbagliare il segno nell'integrazione di funzioni trigonometriche ($\int \sin x dx$ vs $\int \cos x dx$).
4. Non riconoscere la necessità della derivata della funzione interna ($f'(x)$) quando si tenta di integrare una funzione composta.
5. Confondere l'integrale del prodotto di funzioni con il prodotto degli integrali.

## Tipologie di esercizio da generare
* Quesiti a scelta multipla che richiedono di identificare la primitiva corretta di una funzione elementare.
* Calcolo di integrali indefiniti che richiedono una semplice manipolazione algebrica (es. $\int \frac{x}{x+1} dx$).
* Riconoscimento della formula per l'integrazione di funzioni composte: data $f(x)$, identificare l'integrale della forma $f(x)^b \cdot f'(x)$.
* Esercizi basati su identità trigonometriche per ridurre espressioni complesse (es. $\int \tan^2 x dx$ o $\int \sin^2 x dx$).
