---
titolo: Funzioni reali elementari
gruppo: Funzioni, continuita e limiti di funzione
---
# Funzioni reali elementari

## Prerequisiti
Proprietà algebriche fondamentali, concetti base di insieme, coordinate cartesiane, conoscenza elementare di potenze e radici, nozioni preliminari di iniettività, suriettività e invertibilità.

## Definizioni e notazione del corso
- Funzioni affini: $f(x) = mx + q$.
- Funzioni potenza: $f(x) = x^n$ con $n \in \mathbb{Z}$.
- Funzioni radice: $f(x) = \sqrt[n]{x} = x^{1/n}$ con $n \in \mathbb{N}$.
- Polinomi: $p(x) = \sum_{k=0}^n a_k x^k$.
- Funzioni razionali: rapporto tra polinomi $q(x) = \frac{p_1(x)}{p_2(x)}$.
- Notazione: Dominio, immagine, estremo superiore ($\sup$) e inferiore ($\inf$), parità/disparità, monotonia.

## Risultati fondamentali
1. La funzione affine $f(x) = mx + q$ è invertibile se $m \neq 0$, con inversa $f^{-1}(y) = \frac{y-q}{m}$.
2. Proprietà di parità: $f(-x) = f(x)$ (pari); $f(-x) = -f(x)$ (dispari).
3. Le funzioni potenza $x^{2m}$ (esponente pari positivo) sono iniettive solo se ristrette a $\mathbb{R}^+$, con inversa $x^{1/2m}$.
4. Le funzioni potenza $x^{2m+1}$ (esponente dispari positivo) sono invertibili su tutto $\mathbb{R}$.
5. Una funzione razionale $q(x)$ è definita in $\mathbb{R} \setminus \{x \in \mathbb{R} : p_2(x) = 0\}$.

## Metodi risolutivi usati nel corso
- Studio grafico: determinazione del coefficiente angolare $m$ e dell'intercetta $q$ per funzioni affini, analisi del comportamento asintotico di potenze e polinomi.
- Restrizione del dominio: utilizzo di intervalli specifici (es. $\mathbb{R}^+$) per rendere invertibili funzioni non iniettive (come $x^2$).
- Scomposizione algebrica: fattorizzazione di polinomi per determinare il dominio di funzioni razionali e semplificare espressioni tramite eliminazione di fattori comuni (estensione di funzioni).

## Errori tipici da segnalare allo studente
1. Confondere il dominio di una funzione radice con indice pari (escludendo i negativi) con quello a indice dispari.
2. Considerare invertibile una funzione potenza con esponente pari su tutto $\mathbb{R}$ senza operare una restrizione del dominio.
3. Dimenticare di escludere gli zeri del denominatore dal dominio di una funzione razionale, anche quando il termine può essere semplificato.
4. Interpretare erroneamente la limitatezza: confondere una funzione illimitata superiormente con una che tende a $+\infty$ ovunque.

## Tipologie di esercizio da generare
- Identificazione della funzione a partire dal grafico (es. equazione di una retta passante per due punti).
- Calcolo del dominio di funzioni razionali complesse.
- Verifica delle proprietà di una funzione (parità, invertibilità, limitatezza) dato il suo esponente o espressione analitica.
- Semplificazione di espressioni con radici e potenze (es. $\sqrt[n]{x^n}$).
- Valutazione di funzioni in punti dati per determinarne il comportamento.
