---
titolo: Nozioni preliminari: insiemi e numeri reali
gruppo: Fondamenti di Analisi Matematica
---
# Nozioni preliminari: insiemi e numeri reali

## Prerequisiti
Conoscenza intuitiva delle operazioni aritmetiche di base, capacità di manipolazione algebrica elementare, nozioni base di logica proposizionale (implicazione e doppia implicazione).

## Definizioni e notazione del corso
- **Insiemi**: $a \in A$ (appartenenza), $A \subseteq B$ (inclusione), $\emptyset$ (vuoto), $B \cap C$ (intersezione), $B \cup C$ (unione), $B \setminus C$ (complemento).
- **Numeri**: $\mathbb{N}$ (naturali), $\mathbb{Z}$ (interi), $\mathbb{Q}$ (razionali), $\mathbb{R}$ (reali).
- **Relazioni d'ordine**: $\leq$ (minore o uguale), $\geq$ (maggiore o uguale), $<$ (minore stretto), $>$ (maggiore stretto).
- **Elemento separatore**: dato $A, B \subset \mathbb{R}$ tali che $A \cup B = \mathbb{R}$, $A \cap B = \emptyset$ e $a \leq b \ \forall a \in A, b \in B$, esiste $c$ tale che $a \leq c \leq b$.

## Risultati fondamentali
1. **Assiomi di campo e ordine**: $\mathbb{R}$ è un campo ordinato completo. Valgono le proprietà commutativa, associativa, distributiva, esistenza dell'elemento neutro (0, 1) e dell'inverso/opposto.
2. **Proprietà di Dedekind**: L'assioma di completezza (o di Dedekind) garantisce che non esistano "buchi" in $\mathbb{R}$.
3. **Irrazionalità di $\sqrt{2}$**: Non esiste alcun $a \in \mathbb{Q}$ tale che $a^2 = 2$.
4. **Proprietà di Archimede**: Per ogni $x \in \mathbb{R}$, esiste $n \in \mathbb{N}$ tale che $n > x$.
5. **Legge di annullamento del prodotto**: $ab = 0 \iff a = 0$ oppure $b = 0$.

## Metodi risolutivi usati nel corso
- **Dimostrazione per assurdo**: Tecnica principale per provare l'irrazionalità di numeri come $\sqrt{2}$ o la mancanza dell'elemento separatore in $\mathbb{Q}$. Si nega la tesi e si cercano contraddizioni logiche.
- **Manipolazione di disuguaglianze**: Uso della definizione di $\leq$ e delle proprietà di monotonia (es. moltiplicare per numeri positivi preserva il verso, per negativi lo inverte).
- **Utilizzo delle definizioni di insieme**: Verifica delle appartenenze tramite l'analisi delle condizioni logiche che definiscono un insieme.

## Errori tipici da segnalare allo studente
1. **Confusione tra implicazione e equivalenza**: Scambiare $\implies$ con $\iff$ in passaggi di equazioni o disequazioni.
2. **Assunzione implicita di completezza**: Operare in $\mathbb{Q}$ credendo che ogni sottoinsieme superiormente limitato ammetta estremo superiore nel campo stesso (errore che la dispensa mira a correggere).
3. **Semplificazione algebrica non lecita**: Dividere per espressioni che possono essere nulle senza analizzare il caso.
4. **Uso errato di $\mathbb{N}$**: Dimenticare che in $\mathbb{N}$ non tutte le sottrazioni o le divisioni danno risultati in $\mathbb{N}$.

## Tipologie di esercizio da generare
- Esercizi di teoria degli insiemi: determinare intersezioni, unioni e complementi di insiemi dati per proprietà.
- Dimostrazioni guidate per assurdo: ricalcare la struttura della Proposizione 1 per provare l'irrazionalità di altri radicali (es. $\sqrt{3}, \sqrt{5}$).
- Manipolazione di disuguaglianze: dimostrare disuguaglianze elementari utilizzando gli assiomi di ordinamento e le proprietà dei numeri reali.
- Esercizi di verifica: testare se una data relazione rispetta le proprietà di dicotomia, antisimmetria o transitività.
