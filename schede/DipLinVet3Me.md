---
titolo: Sistemi di vettori, dipendenza lineare e sottospazi
gruppo: Algebra Lineare
---
# Dipendenza lineare e sottospazi generati

## Prerequisiti
Conoscenza della struttura di spazio vettoriale $V$ su un campo $K$ e delle operazioni di somma tra vettori e prodotto per uno scalare.

## Definizioni e notazione del corso
- **Sistema di vettori**: Una $n$-upla non ordinata di elementi di $H \subseteq V$, indicata come $S = [v_1, \dots, v_n]$.
- **Dipendenza lineare**: Il vettore $v$ dipende linearmente da $S$ se esistono scalari $k_i \in K$ tali che $v = \sum_{i=1}^n k_i v_i$.
- **Sottospazio generato**: $\langle S \rangle$ è l'intersezione di tutti i sottospazi di $V$ contenenti $S$; coincide con l'insieme di tutti i vettori che dipendono linearmente da $S$.
- **Notazione**: Si usa la parentesi quadra $[v_1, \dots, v_n]$ per i sistemi di vettori e la notazione $\langle S \rangle$ per il sottospazio generato.

## Risultati fondamentali
1. Ogni vettore del sistema $S$ dipende linearmente da $S$.
2. Il vettore nullo $0$ dipende linearmente da qualsiasi sistema.
3. Se $T \subseteq S$, allora $\langle T \rangle \subseteq \langle S \rangle$.
4. $\langle T \rangle = \langle S \rangle$ se e solo se ogni vettore di $T$ dipende linearmente da $S$ e viceversa.
5. Se $v \in S$, allora $\langle S - v \rangle = \langle S \rangle$ se e solo se $v$ dipende linearmente da $S - v$.

## Metodi risolutivi usati nel corso
- **Verifica di dipendenza lineare**: Impostare l'equazione $v = \sum k_i v_i$ e verificare l'esistenza di scalari $k_i$.
- **Tecnica della doppia inclusione**: Per provare l'uguaglianza $\langle S \rangle = \langle T \rangle$, si dimostra che ogni generatore di $S$ è in $\langle T \rangle$ e ogni generatore di $T$ è in $\langle S \rangle$.
- **Semplificazione di sistemi**: Rimuovere vettori dal sistema che siano combinazioni lineari degli altri per trovare sistemi equivalenti.

## Errori tipici da segnalare allo studente
1. Confondere l'appartenenza di un vettore a un insieme con la sua dipendenza lineare dal sistema di generatori.
2. Dimenticare che il vettore nullo appartiene a ogni sottospazio generato.
3. Non verificare correttamente la condizione di unicità nella combinazione lineare quando richiesto dal problema.
4. Applicare le proprietà dell'inclusione tra spazi senza aver prima verificato che il sistema di generatori sia effettivamente contenuto nell'altro.

## Tipologie di esercizio da generare
- Data una lista di vettori (o matrici), stabilire se un dato vettore (o matrice) appartiene al sottospazio da essi generato.
- Confrontare due sistemi di generatori $S$ e $T$ per verificare se generano lo stesso sottospazio o se uno è contenuto nell'altro.
- Verificare la dipendenza lineare di vettori/matrici dato un sistema di riferimento.
- Identificare se un sottospazio definito da condizioni (es. $a+c=0$) è generato da un dato insieme di matrici.
