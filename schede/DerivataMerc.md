---
titolo: Definizione e proprietà fondamentali della derivata
gruppo: Calcolo differenziale
---
# Derivata: definizione e prime proprietà

## Prerequisiti
Conoscenza del calcolo dei limiti di funzioni reali di una variabile reale, nozione di continuità, trigonometria di base (formule di prostaferesi) e algebra elementare.

## Definizioni e notazione del corso
- Rapporto incrementale: $\frac{f(x_0+h)-f(x_0)}{h}$.
- Derivata in un punto $x_0$: $f'(x_0) = \lim_{h \to 0} \frac{f(x_0+h)-f(x_0)}{h}$.
- La derivata è indicata come $f'(x)$, $\frac{d}{dx}f(x)$, o $Df(x)$.
- Derivate destra ($D^+f(x_0)$) e sinistra ($D^-f(x_0)$) definite tramite limiti unilaterali del rapporto incrementale.

## Risultati fondamentali
1. Derivata di costante: $\frac{d}{dx}q = 0$.
2. Derivata di funzione lineare: $\frac{d}{dx}(mx+q) = m$.
3. Derivata di potenza: $\frac{d}{dx}x^2 = 2x$.
4. Derivate trigonometriche: $\frac{d}{dx}\sin x = \cos x$ e $\frac{d}{dx}\cos x = -\sin x$.
5. Algebra delle derivate:
   - Somma/Differenza: $(f \pm g)' = f' \pm g'$.
   - Prodotto: $(f \cdot g)' = f'g + fg'$.
   - Quoziente: $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$ (per $g \neq 0$).

## Metodi risolutivi usati nel corso
- Utilizzo della definizione tramite limite del rapporto incrementale per derivare funzioni base.
- Applicazione delle formule di prostaferesi per semplificare i limiti dei rapporti incrementali di funzioni trigonometriche.
- Applicazione ricorsiva delle regole di derivazione di somma, prodotto e quoziente per funzioni composte da operazioni elementari.

## Errori tipici da segnalare allo studente
1. Confusione tra la derivata del prodotto $(fg)' = f'g + fg'$ e la derivata del quoziente $\frac{f'g - fg'}{g^2}$.
2. Sbagliare il segno nella derivata del coseno, scrivendo $\frac{d}{dx}\cos x = \sin x$ invece di $-\sin x$.
3. Dimenticare di valutare correttamente il limite del rapporto incrementale (es. non semplificare correttamente la $h$ al denominatore).
4. Errata applicazione della regola del quoziente, omettendo il quadrato del denominatore $g^2(x)$.

## Tipologie di esercizio da generare
- Calcolo della derivata di una funzione in un punto generico $x_0$ utilizzando la definizione di limite.
- Calcolo della derivata di espressioni algebriche o trigonometriche semplici usando le regole di somma, prodotto e quoziente.
- Calcolo del valore della derivata di una funzione data (o combinazione di funzioni) in un punto specifico $x_0$.
- Quiz a scelta multipla che richiedono di identificare la corretta espressione della derivata di funzioni base o combinate.
