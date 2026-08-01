---
titolo: Integrali Impropri: Calcolo e Convergenza
gruppo: Calcolo integrale
---
# Integrali Impropri

## Prerequisiti
Calcolo di integrali definiti e indefiniti, tecniche di integrazione (parti, sostituzione, decomposizione in fratti semplici), limiti di funzioni, sviluppo in serie di Taylor/Maclaurin, studio di domini e continuità.

## Definizioni e notazione del corso
- Si definisce integrale improprio il limite del valore dell'integrale calcolato su un intervallo limitato $[a, b]$, per $b \to +\infty$ o per $a$ che tende a un punto di singolarità dove la funzione non è definita.
- Notazione per il limite: $\lim_{b \to +\infty} \int_a^b f(x)dx$.
- Uso della notazione di Landau $o(\cdot)$ per il confronto locale tra funzioni.

## Risultati fondamentali
1. **Teorema del confronto asintotico**: Date $f, g$ positive, se $\lim_{x \to x_0} \frac{f(x)}{g(x)} = \ell \in (0, +\infty)$, allora $\int f(x)dx$ e $\int g(x)dx$ hanno lo stesso carattere di convergenza.
2. **Convergenza assoluta**: Se l'integrale del valore assoluto $\int |f(x)|dx$ converge, allora converge anche l'integrale di $f(x)dx$.
3. **Criterio di integrazione**: La funzione $\frac{1}{x^\alpha}$ è integrabile vicino a $0$ se $\alpha < 1$ e integrabile a $+\infty$ se $\alpha > 1$.

## Metodi risolutivi usati nel corso
- **Scomposizione**: Se il dominio di integrazione presenta punti di singolarità interni, l'integrale va spezzato in più parti: $\int_a^b = \lim_{c \to s^-} \int_a^c + \lim_{c \to s^+} \int_c^b$.
- **Sostituzione**: Uso di cambi di variabile (es. $t^2 = x$ o $t = \sqrt{x-a}$) per ricondurre l'integrale a forme note, spesso razionali o che coinvolgono l'arcotangente.
- **Fratti semplici**: Scomposizione di funzioni razionali per via algebrica tramite coefficienti indeterminati.
- **Analisi asintotica**: Studio del comportamento della funzione tramite sviluppi di Taylor per determinare la convergenza senza calcolare la primitiva.

## Errori tipici da segnalare allo studente
1. **Dimenticare i punti di singolarità**: Non analizzare il dominio di integrazione prima di calcolare l'integrale, ignorando punti in cui la funzione non è definita o diverge.
2. **Uso errato del confronto asintotico**: Applicare il confronto asintotico senza verificare che le funzioni siano positive (o non negative) nell'intervallo considerato.
3. **Errore nel calcolo del limite**: Non gestire correttamente la forma indeterminata risultante dal limite degli estremi di integrazione (es. errori nel calcolo di $\lim_{b \to +\infty} \log(\dots)$).

## Tipologie di esercizio da generare
- Calcolo esplicito di un integrale improprio tramite calcolo della primitiva e limite.
- Esercizio sulla determinazione di un parametro ($n \in \mathbb{N}$ o $a \in \mathbb{R}$) affinché l'integrale converga.
- Verifica della convergenza (senza calcolare l'integrale) tramite criteri di confronto o confronto asintotico.
- Studio della convergenza assoluta di integrali impropri con funzioni trigonometriche.
