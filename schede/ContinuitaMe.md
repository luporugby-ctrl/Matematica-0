---
titolo: Continuità e invertibilità di funzioni monotone
gruppo: Funzioni, continuita e limiti di funzione
---
# Continuità e funzioni monotone

## Prerequisiti
Conoscenza della definizione di limite, continuità in un punto e in un intervallo, teorema di Weierstrass, teorema dei valori intermedi e definizione di funzione iniettiva/suriettiva.

## Definizioni e notazione del corso
- Una funzione $f: [a, b] \to \mathbb{R}$ è detta monotona se è non decrescente ($f(x_1) \le f(x_2)$ per $x_1 < x_2$) o non crescente ($f(x_1) \ge f(x_2)$ per $x_1 < x_2$).
- Si specifica la distinzione tra monotonia e *stretta* monotonia.
- Notazione per l'immagine: $f([a, b])$ indica l'insieme dei valori assunti dalla funzione nell'intervallo $[a, b]$.

## Risultati fondamentali
1. **Criterio di continuità**: Una funzione monotona $f: [a, b] \to \mathbb{R}$ è continua se e solo se la sua immagine è l'intervallo con estremi $f(a)$ e $f(b)$, ovvero $f([a, b]) = [f(a), f(b)]$ (o $[f(b), f(a)]$).
2. **Lemma di monotonia**: Una funzione $f$ continua e invertibile in un intervallo $[a, b]$ è necessariamente strettamente monotona.
3. **Continuità dell'inversa**: Se $f$ è continua e invertibile in un intervallo $[a, b]$, allora la sua funzione inversa $f^{-1}$ è anch'essa continua.
4. **Criterio di invertibilità**: Una funzione $f$ continua e strettamente monotona in $[a, b]$ è invertibile nell'intervallo.

## Metodi risolutivi usati nel corso
- Per verificare la continuità di una funzione monotona, si confronta l'immagine calcolata tramite i limiti o i valori agli estremi con l'intervallo atteso.
- Per studiare l'invertibilità, si accerta la stretta monotonia (spesso tramite derivata prima, sebbene non esplicitato nelle slide, o analizzando il grafico/segno).
- Per le funzioni definite a tratti, si verifica la continuità nei punti di raccordo e la conservazione della monotonia globale.

## Errori tipici da segnalare allo studente
1. Confondere la continuità di $f$ con la necessaria continuità di $f^{-1}$ quando il dominio non è un intervallo.
2. Pensare che l'invertibilità implichi automaticamente la continuità dell'inversa senza considerare il dominio (es. funzioni non definite su intervalli).
3. Dimenticare di verificare che, per la suriettività (e quindi l'invertibilità), l'immagine della funzione debba coincidere esattamente con il codominio specificato.
4. Confondere la monotonia semplice con la stretta monotonia, necessaria per garantire l'iniettività.

## Tipologie di esercizio da generare
- Esercizi di "Vero o Falso" su proprietà di continuità e monotonia di funzioni definite a tratti.
- Calcolo dell'immagine di una funzione in un dato intervallo e deduzione della sua continuità.
- Analisi di funzioni a tratti per determinare se sono invertibili e se la loro inversa risulta continua.
- Verifica della stretta monotonia per funzioni elementari (es. logaritmiche, esponenziali, radici).
