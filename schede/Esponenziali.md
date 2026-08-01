---
titolo: Funzioni elementari, valore assoluto e funzioni a tratti
gruppo: Funzioni, continuita e limiti di funzione
---
# Funzioni elementari, valore assoluto e funzioni a tratti

## Prerequisiti
Conoscenza delle proprietà delle potenze con esponente razionale e base reale positiva. Capacità di manipolazione algebrica di espressioni contenenti radici e potenze.

## Definizioni e notazione del corso
- La funzione esponenziale $f(x) = a^x$ è definita per $a \in \mathbb{R}^+ \setminus \{0, 1\}$.
- Il logaritmo $\log_a(x)$ è definito come l'inverso dell'esponenziale: $a^x = y \iff \log_a(y) = x$.
- Valore assoluto: $f(x) = |x| = \begin{cases} x & \text{se } x \ge 0 \\ -x & \text{se } x < 0 \end{cases}$.
- Funzione caratteristica di un insieme $A$: $\chi_A(x) = \begin{cases} 1 & \text{se } x \in A \\ 0 & \text{se } x \notin A \end{cases}$.

## Risultati fondamentali
1. Proprietà esponenziali: $a^b \cdot a^c = a^{b+c}$, $(a^b)^c = a^{b \cdot c}$.
2. Invertibilità: Esponenziali e logaritmi sono invertibili, con $a^{\log_a(x)} = x$ e $\log_a(a^x) = x$.
3. Proprietà logaritmiche: $\log_a(x_1 \cdot x_2) = \log_a(x_1) + \log_a(x_2)$, $\log_a(x^b) = b \log_a(x)$, $\log_b(x) = \frac{\log_a(x)}{\log_a(b)}$.
4. Disequazioni valore assoluto: $|x| \le r \iff -r \le x \le r$.
5. Disuguaglianza triangolare: $|x_1 + x_2| \le |x_1| + |x_2|$.
6. Funzioni a tratti: Una funzione definita su una partizione $A_k$ si esprime come $f(x) = \sum_{k=1}^n f_k(x) \chi_{A_k}(x)$.

## Metodi risolutivi usati nel corso
- Uso della monotonia (crescente se $a > 1$, decrescente se $0 < a < 1$) per risolvere disequazioni esponenziali e logaritmiche.
- Scomposizione di funzioni definite a tratti tramite l'uso delle funzioni caratteristiche.
- Verifica di parità/disparità tramite la sostituzione $f(-x)$ e confronto con $f(x)$.
- Analisi del grafico per determinare inf, sup e iniettività/suriettività.

## Errori tipici da segnalare allo studente
1. Confondere le proprietà delle potenze con quelle dei logaritmi (es. $\log(a+b) = \log a + \log b$ è errato).
2. Dimenticare il vincolo $x > 0$ nella definizione di logaritmo o trascurare il dominio naturale.
3. Errata gestione dei segni nelle disuguaglianze con valore assoluto (es. $|x| \le r$ non equivale a $x \le r$ e $x \ge r$).
4. Applicare le proprietà di base degli esponenziali ignorando che per $0 < a < 1$ la disuguaglianza inverte il verso.

## Tipologie di esercizio da generare
- Manipolazione algebrica di espressioni con potenze e logaritmi applicando le proprietà fondamentali.
- Risoluzione di disequazioni o confronto di espressioni esponenziali/logaritmiche basato sulla monotonia.
- Analisi qualitativa di funzioni a tratti (determinazione di sup/inf, parità, invertibilità).
- Espressione analitica di funzioni definite a tratti o mediante grafici utilizzando la funzione caratteristica $\chi_A(x)$.
- Verifica di proprietà (pari/dispari, monotonia) su funzioni date.
