---
titolo: Verifica di sottospazi vettoriali in $\mathbb{R}^n$
gruppo: Algebra Lineare
---
# Verifica di sottospazi vettoriali

## Prerequisiti
Conoscenza della struttura di spazio vettoriale, in particolare di $\mathbb{R}^n$, e delle proprietà fondamentali delle operazioni di somma tra vettori e prodotto per uno scalare.

## Definizioni e notazione del corso
Un sottoinsieme $V' \subseteq V$ (dove $V$ è uno spazio vettoriale su $\mathbb{R}$) è un sottospazio vettoriale se soddisfa le seguenti condizioni:
1. Contiene l'elemento neutro: $0_V \in V'$.
2. È chiuso rispetto alla somma: $\forall v, w \in V', v + w \in V'$.
3. È chiuso rispetto al prodotto per uno scalare: $\forall \alpha \in \mathbb{R}, \forall v \in V', \alpha \cdot v \in V'$.
La notazione utilizzata per i vettori è la tupla canonica, es. $(a, b, c) \in \mathbb{R}^3$.

## Risultati fondamentali
1. Il vettore nullo di $\mathbb{R}^n$ è $(0, 0, \dots, 0)$.
2. Se un insieme $V'$ è definito da equazioni lineari omogenee (es. $a+b+c=0$), allora $V'$ è un sottospazio vettoriale.
3. Se un insieme $V'$ contiene condizioni non lineari (es. prodotto tra componenti) o termini noti non nulli (es. $a=2$), allora generalmente non è un sottospazio vettoriale poiché fallisce il test dell'elemento neutro o la chiusura rispetto alle operazioni.

## Metodi risolutivi usati nel corso
Per verificare se $V'$ è sottospazio di $V$:
1. **Test del vettore nullo**: Sostituire le componenti nulle nelle equazioni definitorie. Se l'equazione non è soddisfatta (es. $0 \neq 1$), l'insieme non è un sottospazio.
2. **Test della chiusura rispetto al prodotto**: Prendere un generico vettore $v \in V'$ e moltiplicarlo per $\alpha \in \mathbb{R}$. Verificare se il risultante $\alpha v$ soddisfa ancora le equazioni di $V'$.
3. **Test della chiusura rispetto alla somma**: Prendere due vettori generici $v, w \in V'$ e sommarli. Verificare se $v+w$ soddisfa le equazioni definitorie originali.

## Errori tipici da segnalare allo studente
1. Dimenticare di verificare la presenza del vettore nullo: è la condizione più rapida per escludere un sottoinsieme.
2. Confondere la chiusura rispetto agli scalari (es. $\alpha \in \mathbb{R}$) con restrizioni non permesse (es. verificare la stabilità solo per $\alpha \in \mathbb{N}$ o $\alpha \in \mathbb{Q}$ non rende l'insieme uno spazio vettoriale su $\mathbb{R}$).
3. Sbagliare la verifica della somma: non sommare correttamente le componenti o non controllare se la somma mantiene la relazione richiesta.
4. Non riconoscere che equazioni non omogenee (termine noto diverso da zero) escludono sempre la presenza del vettore nullo.

## Tipologie di esercizio da generare
1. Data una condizione del tipo $f(a, b, c) = 0$ (o sistema di equazioni), determinare se l'insieme dei vettori che la soddisfano è un sottospazio di $\mathbb{R}^3$ o $\mathbb{R}^4$.
2. Esercizi con condizioni non lineari (es. $ab=c$ o $a=2$) per allenare lo studente a identificare rapidamente i controesempi.
3. Esercizi con condizioni che coinvolgono coefficienti o combinazioni lineari (es. $a+b+2d = a+3c = 0$) per verificare la chiusura sotto operazioni.
