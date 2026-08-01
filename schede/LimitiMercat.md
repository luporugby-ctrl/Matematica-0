---
titolo: Limiti e proprietà delle successioni numeriche
gruppo: Successioni e limiti
---
# Limiti e proprietà delle successioni numeriche

## Prerequisiti
Conoscenza basilare dell'insieme dei numeri naturali $\mathbb{N}$ e reali $\mathbb{R}$, valore assoluto, manipolazione algebrica di espressioni polinomiali e razionali, concetto di funzione.

## Definizioni e notazione del corso
- **Successione:** Funzione $a: \mathbb{N} \to \mathbb{R}$, $n \mapsto a_n$. Il simbolo $a_n$ indica il valore che la successione assume in $n$, non la funzione stessa.
- **Limite finito ($a_n \to a$):** $\forall \epsilon > 0, \exists n_0 \in \mathbb{N} : |a_n - a| < \epsilon, \forall n > n_0$.
- **Limite infinito:** 
  - $a_n \to +\infty$ se $\forall M > 0, \exists n_0 \in \mathbb{N} : a_n > M, \forall n > n_0$.
  - $a_n \to -\infty$ se $\forall M > 0, \exists n_0 \in \mathbb{N} : a_n < -M, \forall n > n_0$.
- **Successione limitata:** $\exists M \in \mathbb{R} : |a_n| \leq M, \forall n \in \mathbb{N}$.
- **Definitivamente:** Una proprietà vale definitivamente se esiste un indice $n_0$ tale che la proprietà è vera per ogni $n > n_0$.
- **Sottosuccessione:** Definita tramite una successione strettamente crescente di indici $n_k$.

## Risultati fondamentali
1. **Unicità del limite:** Se una successione ammette limite, questo è unico.
2. **Permanenza del segno:** Se $a_n \to a > 0$, allora $a_n$ è definitivamente strettamente positiva.
3. **Convergenza e limitatezza:** Ogni successione convergente è limitata.
4. **Prodotto con infinitesima:** Il prodotto di una successione limitata per una infinitesima ($b_n \to 0$) è una successione infinitesima.
5. **Teorema del confronto (Carabinieri):** Se $a_n \leq b_n \leq c_n$ e $a_n, c_n \to a$, allora $b_n \to a$.
6. **Ereditarietà del limite:** Ogni sottosuccessione di una successione convergente converge allo stesso limite.

## Metodi risolutivi usati nel corso
- **Calcolo dei limiti:** Si utilizzano i teoremi sulle operazioni algebriche tra limiti (somma, differenza, prodotto, quoziente).
- **Risoluzione di frazioni algebriche:** Per $\lim_{n \to +\infty} \frac{P(n)}{Q(n)}$, si raccoglie il termine di grado massimo sia al numeratore che al denominatore.
- **Teorema del confronto:** Si applica maggiorando/minorando la successione con termini di cui è noto il limite (es. usando la limitatezza di $\sin n$ o $\cos n$).
- **Verifica con definizione ($\epsilon, n_0$):** Utilizzo algebrico della disuguaglianza del valore assoluto per determinare l'indice soglia $n_0$.

## Errori tipici da segnalare allo studente
1. **Confusione tra limiti e forme indeterminate:** Tentare di sommare o sottrarre infiniti di segno opposto senza ricondurre il limite a una forma determinata.
2. **Uso improprio del confronto:** Applicare il teorema del confronto ignorando che la successione "testimone" deve convergere allo stesso valore.
3. **Mancata verifica delle condizioni:** Applicare il limite del quoziente senza verificare che il denominatore non sia nullo.
4. **Scambio di quantificatori:** Non comprendere che l'indice $n_0$ dipende dal valore $\epsilon$ (o $M$) scelto.

## Tipologie di esercizio da generare
1. **Calcolo di limiti:** Determinare il limite di successioni razionali fratte (es. $\frac{an^k + \dots}{bn^m + \dots}$).
2. **Analisi teorica:** Date due successioni, stabilire la verità di affermazioni riguardanti la convergenza, il limite o la limitatezza (vero/falso).
3. **Applicazione dei teoremi:** Esercizi che richiedono l'uso del teorema del confronto o delle proprietà algebriche su successioni generiche.
4. **Verifica di limiti:** Dimostrare che una successione converge a un valore dato usando la definizione formale $\epsilon - n_0$.
