---
titolo: Limiti notevoli di funzioni trigonometriche
gruppo: Successioni e limiti
---
# Limiti notevoli di funzioni trigonometriche

## Prerequisiti
Conoscenza delle funzioni elementari (trigonometriche, logaritmiche, esponenziali), definizioni di limite di successione e funzione, e capacità di manipolazione algebrica delle espressioni.

## Definizioni e notazione del corso
Il corso utilizza il "Teorema ponte" per estendere i limiti dalle successioni alle funzioni. Si definisce la funzione come il rapporto di termini che tendono a zero o a infinito.
Simboli chiave:
- Rapporto fondamentale: $\lim_{x\to 0} \frac{\sin x}{x} = 1$
- Relazione trigonometrica: $\sin^2 x + \cos^2 x = 1$
- Limite per funzioni limitate: $\lim_{x\to \infty} (\text{limitata} \cdot \text{infinitesima}) = 0$

## Risultati fondamentali
1. $\lim_{x\to 0} \sin x = 0$
2. $\lim_{x\to 0} \cos x = 1$
3. $\lim_{x\to 0} \frac{\sin x}{x} = 1$
4. $\lim_{x\to 0} \frac{1-\cos x}{x^2} = \frac{1}{2}$
5. $\lim_{x\to 0} \frac{\tan x}{x} = 1$
6. $\lim_{x\to 0} \frac{\arcsin x}{x} = 1$ e $\lim_{x\to 0} \frac{\arctan x}{x} = 1$
7. Limiti asintotici di funzioni periodiche (es. $\sin x$ per $x \to \infty$ non esiste).

## Metodi risolutivi usati nel corso
- **Manipolazione algebrica:** Riscrivere l'espressione (es. moltiplicare e dividere per termini necessari) per isolare i limiti notevoli.
- **Scomposizioni:** Utilizzo della relazione fondamentale per passare dal coseno al seno.
- **Cambiamento di variabile:** Porre $y = g(x)$ per ricondurre il limite a una forma nota, verificando che $y \to 0$ quando $x \to x_0$.
- **Scomposizione di limiti di prodotto:** Calcolare il limite di ciascun fattore separatamente se il limite del prodotto è determinato.

## Errori tipici da segnalare allo studente
1. **Applicazione scorretta:** Tentare di applicare un limite notevole quando la variabile non tende al valore corretto (es. $x \to \pi$ invece di $x \to 0$).
2. **Manipolazioni errate:** Dimenticare le potenze nel denominatore, ad esempio trattare $1-\cos x$ come se fosse equivalente a $x$ anziché a $x^2/2$.
3. **Limite del prodotto:** Assumere che il limite di un prodotto sia sempre il prodotto dei limiti senza prima verificare che i singoli limiti esistano finiti.
4. **Argomenti composti:** Sbagliare l'argomento di una funzione composta durante il cambio di variabile, ignorando il valore a cui tende la funzione interna.

## Tipologie di esercizio da generare
- Calcolo di limiti di funzioni razionali contenenti termini trigonometrici ($\sin, \cos, \tan, \arcsin, \arctan$).
- Limiti che presentano forme indeterminate del tipo $0/0$ richiedenti l'uso di limiti notevoli.
- Limiti di funzioni esponenziali o logaritmiche che coinvolgono argomenti trigonometrici.
- Esercizi basati su cambiamenti di variabile per eliminare forme indeterminate.
- Verifica del limite di funzioni prodotto (infinitesima $\cdot$ limitata).
