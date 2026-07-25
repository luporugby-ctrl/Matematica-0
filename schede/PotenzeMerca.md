---
titolo: Limiti notevoli di potenze, esponenziali e logaritmi
gruppo: Analisi Matematica 1
---
# Limiti notevoli di potenze, esponenziali e logaritmi

## Prerequisiti
Conoscenza delle definizioni di limite, operazione con le forme indeterminate, algebra dei logaritmi e degli esponenziali, proprietà delle potenze e delle radici, comportamento asintotico di polinomi.

## Definizioni e notazione del corso
- Il numero di Nepero è indicato come $e$.
- Si utilizza la notazione $\log_a x$ per il logaritmo in base $a$.
- Si sfrutta il teorema ponte per estendere i limiti dalle successioni alle funzioni.
- Per il calcolo di limiti di funzioni esponenziali complesse, si usa l'identità $f(x)^{g(x)} = e^{g(x)\log(f(x))}$.

## Risultati fondamentali
1. Limiti di esponenziali: $\lim_{x\to +\infty} a^x = +\infty$ (se $a>1$) oppure $0$ (se $0 < a < 1$).
2. Comportamento di frazioni polinomiali: per $x\to +\infty$, il limite di $\frac{p(x)}{q(x)}$ è dettato dai gradi $r$ e $s$ dei polinomi; se $r=s$ il limite è il rapporto tra i coefficienti direttivi.
3. Gerarchia degli infiniti: $\lim_{x\to +\infty} \frac{\log_a x}{x^b} = 0$ e $\lim_{x\to +\infty} \frac{x^b}{a^x} = 0$ (per $a>1, b>0$).
4. Numero di Nepero: $\lim_{x\to \pm\infty} (1 + \frac{a}{x})^x = e^a$.
5. Logaritmi e esponenziali notevoli: 
   - $\lim_{x\to 0} \frac{\log_a(1+x)}{x} = \frac{1}{\log a}$
   - $\lim_{x\to 0} \frac{a^x - 1}{x} = \log a$
   - $\lim_{x\to 0} \frac{(1+x)^a - 1}{x} = a$

## Metodi risolutivi usati nel corso
- Messa in evidenza del termine di grado massimo (per polinomi o radici) o dell'esponenziale dominante (per funzioni miste).
- Manipolazione algebrica per ricondursi ai limiti notevoli citati sopra.
- Cambio di variabile (es. $y = 1/x$ per limiti a infinito, $y = a^x-1$ per esponenziali).
- Scomposizione dei polinomi o uso di prodotti notevoli (es. cubi di binomi) per risolvere forme $0/0$.
- Razionalizzazione per gestire differenze tra radici.

## Errori tipici da segnalare allo studente
- Confusione nel segno di $\sqrt{x^{2n}} = |x|$: dimenticare che per $x\to -\infty$, $|x| = -x$.
- Sbagliare la gerarchia degli infiniti, dando priorità al polinomio rispetto all'esponenziale.
- Applicare i limiti notevoli in modo meccanico senza verificare che l'argomento tenda effettivamente a $0$ (es. nel caso di $f(x) \to 0$, usare $\frac{\log(1+f(x))}{f(x)} \to 1$).
- Errore nel calcolo del limite di una differenza ($\infty - \infty$) trattandola come un limite di rapporto senza prima manipolare l'espressione.

## Tipologie di esercizio da generare
- Calcolo di limiti di funzioni razionali fratte per $x\to \pm\infty$.
- Limiti che coinvolgono la forma indeterminata $\infty - \infty$ risolti mediante raccoglimento.
- Limiti di funzioni esponenziali o logaritmiche che richiedono l'uso dei limiti notevoli.
- Limiti di funzioni del tipo $f(x)^{g(x)}$ con forme indeterminate come $0^0$ o $1^\infty$.
- Esercizi di scelta multipla che richiedono di identificare il valore corretto del limite tra quattro opzioni fornite.
