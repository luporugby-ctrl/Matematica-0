---
titolo: Dominio e trasformazioni grafiche di funzioni
gruppo: Analisi Matematica 1
---
# Dominio e trasformazioni grafiche di funzioni

## Prerequisiti
Conoscenza approfondita dei domini delle funzioni elementari (polinomiali, razionali, esponenziali, logaritmiche, trigonometriche e loro inverse) e proprietà delle operazioni algebriche di base.

## Definizioni e notazione del corso
- Dominio di una funzione $f$: indicato con $D(f)$.
- Funzione composta: la funzione $g \circ f$ è definita per tutti gli $x \in D(f)$ tali che $f(x) \in D(g)$.
- Notazione logica: $\vee$ indica "oppure" (unione di insiemi), $\wedge$ indica "e" (intersezione di insiemi).
- Insieme dei numeri reali: $\mathbb{R}$, sottoinsiemi specifici come $\mathbb{R}^+ = \{x \in \mathbb{R} : x \geq 0\}$.

## Risultati fondamentali
1. Per $f(x) = \sqrt[n]{x}$ con $n$ pari, $D(f) = [0, +\infty)$.
2. Per $f(x) = \log_a(x)$, $D(f) = (0, +\infty)$.
3. Traslazioni:
   - $f(x+a)$ trasla il grafico di $a$ unità a sinistra ($a>0$).
   - $f(x-a)$ trasla il grafico di $a$ unità a destra ($a>0$).
   - $f(x)+a$ trasla il grafico di $a$ unità verso l'alto.
   - $f(x)-a$ trasla il grafico di $a$ unità verso il basso.
4. Simmetrie:
   - $f(-x)$ è il simmetrico di $f(x)$ rispetto all'asse $y$.
   - $-f(x)$ è il simmetrico di $f(x)$ rispetto all'asse $x$.
5. Valore assoluto:
   - $f(|x|)$: mantiene la parte del grafico con $x>0$ e la riflette simmetricamente rispetto all'asse $y$.
   - $|f(x)|$: mantiene la parte del grafico con $f(x)>0$ e riflette la parte negativa rispetto all'asse $x$.

## Metodi risolutivi usati nel corso
- **Studio del dominio:** Si impongono le condizioni di esistenza per ogni funzione componente. Per $f(x) = \frac{p_1(x)}{p_2(x)}$, $p_2(x) \neq 0$. Per le funzioni composte, si costruisce un sistema di disequazioni/condizioni che devono essere verificate simultaneamente ($\wedge$).
- **Trasformazioni grafiche:** Si applicano le traslazioni o simmetrie passo dopo passo, partendo dalla funzione elementare e componendo le trasformazioni nell'ordine corretto.

## Errori tipici da segnalare allo studente
1. Confondere l'ordine di applicazione delle trasformazioni grafiche (es. traslare prima di applicare il valore assoluto).
2. Dimenticare di intersecare le condizioni del dominio nelle funzioni composte, limitandosi solo al dominio della funzione esterna o interna.
3. Errata gestione dei segni nelle traslazioni orizzontali (scambiare $f(x+a)$ con uno spostamento a destra).
4. Errori nel risolvere le disequazioni associate al dominio, specialmente con radici e logaritmi nidificati.

## Tipologie di esercizio da generare
- Determinazione algebrica del dominio di funzioni composte complesse (es. radici di logaritmi, rapporti di funzioni trigonometriche ed esponenziali).
- Riconoscimento del grafico di una funzione a partire dalla sua espressione analitica modificata (traslazioni, riflessioni).
- Scelta dell'espressione analitica corretta a partire da un grafico trasformato.
- Esercizi a risposta multipla su domini di funzioni composte.
