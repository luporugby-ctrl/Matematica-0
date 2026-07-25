---
titolo: Calcolo dei limiti mediante Teoremi di de l'Hôpital
gruppo: Calcolo differenziale
---
# Calcolo dei limiti mediante Teoremi di de l'Hôpital

## Prerequisiti
Conoscenza del concetto di limite di una funzione, continuità, derivazione di funzioni elementari, Teorema di Rolle e calcolo dei limiti notevoli.

## Definizioni e notazione del corso
Il corso adotta la notazione standard per le funzioni $f(x)$ e $g(x)$. Si definisce forma indeterminata una situazione in cui il limite del rapporto $f(x)/g(x)$ non è immediatamente deducibile dai limiti dei singoli componenti (es. $0/0$ o $\infty/\infty$).

## Risultati fondamentali
1. **Teorema di Cauchy:** Siano $f, g$ continue in $[a, b]$ e derivabili in $(a, b)$ con $g'(x) \neq 0$. Esiste $x_0 \in (a, b)$ tale che:
   $$\frac{f(b) - f(a)}{g(b) - g(a)} = \frac{f'(x_0)}{g'(x_0)}$$
2. **Primo Teorema di de l'Hôpital (caso $0/0$):** Siano $f, g$ continue in $[a, b]$, derivabili in $[a, b] \setminus \{x_0\}$ con $g'(x) \neq 0$. Se $f(x_0) = g(x_0) = 0$ e $\lim_{x\to x_0} \frac{f'(x)}{g'(x)} = L$, allora:
   $$\lim_{x\to x_0} \frac{f(x)}{g(x)} = \lim_{x\to x_0} \frac{f'(x)}{g'(x)} = L$$
3. **Secondo Teorema di de l'Hôpital (caso $\infty/\infty$):** Analogamente al primo, se $\lim_{x\to a} f(x) = \lim_{x\to a} g(x) = \infty$, allora il limite del rapporto delle funzioni è uguale al limite del rapporto delle derivate, se quest'ultimo esiste.

## Metodi risolutivi usati nel corso
- Verifica preliminare delle ipotesi: prima di applicare de l'Hôpital, accertarsi che il limite si presenti come forma indeterminata del tipo $0/0$ o $\infty/\infty$.
- Derivazione iterata: se il limite del rapporto delle derivate è ancora una forma indeterminata, è possibile riapplicare il teorema (derivata seconda, terza, ecc.).
- Cambio di variabile: utile per ricondurre limiti a $\infty$ a limiti in $0^+$ (es. $z = 1/x$).
- Manipolazione algebrica: trasformare le forme $\infty - \infty$ o $0 \cdot \infty$ in rapporti prima di procedere.

## Errori tipici da segnalare allo studente
1. **Applicazione indiscriminata:** Applicare de l'Hôpital quando il limite non è una forma indeterminata (es. ottenere un risultato errato per un limite che è finito).
2. **Confusione con la regola del prodotto:** Derivare il rapporto $f/g$ usando la regola $(f/g)' = (f'g - fg')/g^2$ anziché derivare separatamente numeratore e denominatore.
3. **Mancata verifica delle ipotesi:** Non controllare che $g'(x) \neq 0$ in un intorno del punto o che il limite del rapporto delle derivate esista effettivamente.

## Tipologie di esercizio da generare
- Calcolo di limiti in forme $0/0$ che richiedono una o più applicazioni del teorema.
- Limiti con funzioni trascendenti (logaritmi, esponenziali, funzioni trigonometriche).
- Limiti presentati in forma indeterminata $0 \cdot \infty$ o $\infty - \infty$ da ricondurre alla forma di rapporto.
- Esercizi con parametro $\alpha$ che richiedono l'uso del teorema per determinare il comportamento asintotico.
