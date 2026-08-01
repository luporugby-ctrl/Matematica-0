---
titolo: Studio di serie a termini di segno variabile
gruppo: Serie numeriche
---
# Studio di serie a termini di segno variabile

## Prerequisiti
Conoscenza delle serie a termini positivi, criteri di convergenza (radice, rapporto, confronto asintotico), limiti di successioni, algebra dei limiti e comportamento delle serie armoniche generalizzate.

## Definizioni e notazione del corso
- **Serie assolutamente convergente**: una serie $\sum_{n=1}^{\infty} a_n$ si dice assolutamente convergente se la serie dei valori assoluti $\sum_{n=1}^{\infty} |a_n|$ è convergente.
- **Serie a segni alterni**: serie della forma $\sum_{n=1}^{\infty} (-1)^n a_n$ (con $a_n$ successione positiva).
- **Serie telescopica**: serie i cui termini sono esprimibili come differenza di due termini consecutivi di una successione, $\sum_{k=1}^{\infty} (a_{k+1} - a_k)$.

## Risultati fondamentali
1. **Teorema della convergenza assoluta**: Se una serie è assolutamente convergente, allora è convergente.
2. **Criterio di Leibniz**: Sia $\sum_{n=1}^{\infty} (-1)^n a_n$ una serie a segni alterni. Se la successione $a_n$ è decrescente e $\lim_{n \to +\infty} a_n = 0$, allora la serie è convergente.
3. **Somma di serie telescopiche**: Per una serie $\sum_{k=1}^{\infty} (a_{k+1} - a_k)$, la somma parziale è $s_n = a_{n+1} - a_1$. La serie converge se $\lim_{n \to +\infty} a_n = a$ (finito) e la somma è $s = a - a_1$.

## Metodi risolutivi usati nel corso
- **Analisi della convergenza assoluta**: Si studia la serie $\sum |a_n|$ mediante i criteri classici (radice, rapporto, confronto). Se converge, la serie originale converge.
- **Applicazione del criterio di Leibniz**: Quando la serie non è a termini positivi e la convergenza assoluta fallisce, si verifica se il termine generale ha segno alternato, se la successione dei moduli è infinitesima e se è decrescente.
- **Scomposizione in fratti semplici**: Tecnica utile per ricondurre una serie a una forma telescopica $\sum (b_n - b_{n+1})$.
- **Studio del parametro $x$**: Nelle serie di potenze o dipendenti da parametri, si isola il valore assoluto per determinare l'intervallo di convergenza assoluta e si analizzano separatamente i casi critici ai bordi dell'intervallo.

## Errori tipici da segnalare allo studente
- Affermare che, se una serie non converge assolutamente, allora è divergente (dimenticando la possibilità che sia convergente in modo semplice, es. serie armonica alternata).
- Applicare il criterio di Leibniz senza verificare che la successione sia effettivamente decrescente.
- Dimenticare di verificare la condizione necessaria di convergenza ($\lim a_n = 0$) prima di applicare i criteri del rapporto o della radice.
- Confondere la serie telescopica $a_{k+1} - a_k$ con altre forme, calcolando erroneamente la somma parziale.

## Tipologie di esercizio da generare
- Determinazione dell'intervallo di convergenza di una serie dipendente da un parametro reale $x$.
- Classificazione della convergenza (assoluta o semplice) di una serie a termini di segno variabile.
- Calcolo della somma esatta di una serie telescopica tramite scomposizione.
- Verifica della convergenza di serie che coinvolgono funzioni trigonometriche o logaritmiche, richiedendo stime asintotiche per il confronto.
