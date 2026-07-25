---
titolo: Funzioni reali elementari: Trigonometria
gruppo: Analisi delle funzioni
---
# Funzioni reali elementari: Trigonometria

## Prerequisiti
Conoscenza della geometria del piano, delle proprietà del triangolo rettangolo, della circonferenza e dei concetti base di funzione (dominio, codominio, iniettività, suriettività, invertibilità).

## Definizioni e notazione del corso
- Circonferenza goniometrica: circonferenza centrata nell'origine con raggio $r=1$.
- Radiante: misura dell'arco di circonferenza unitaria. Relazione fondamentale: $\pi = 180^\circ$.
- Funzioni trigonometriche: definite tramite le coordinate $(cos \theta, \sin \theta)$ del punto $P$ sulla circonferenza.
- Relazione pitagorica: $(cos \theta)^2 + (\sin \theta)^2 = 1$.
- Periodicità: $f(x+kT) = f(x)$.

## Risultati fondamentali
1. Identità fondamentale: $\cos^2 x + \sin^2 x = 1$.
2. Formule di addizione/sottrazione:
   $\sin(x_1 \pm x_2) = \sin x_1 \cos x_2 \pm \sin x_2 \cos x_1$
   $\cos(x_1 \pm x_2) = \cos x_1 \cos x_2 \mp \sin x_1 \sin x_2$
3. Formule di duplicazione:
   $\sin(2x) = 2 \sin x \cos x$
   $\cos(2x) = \cos^2 x - \sin^2 x$
4. Formule di bisezione (derivate da 6 e 7):
   $\cos^2 x = \frac{1 + \cos(2x)}{2}, \quad \sin^2 x = \frac{1 - \cos(2x)}{2}$
5. Formule di prostaferesi e Werner (es. $\sin x_1 \cdot \sin x_2 = \frac{1}{2}[\cos(x_1 - x_2) - \cos(x_1 + x_2)]$).

## Metodi risolutivi usati nel corso
- Restrizione del dominio: per invertire funzioni non iniettive (es. $cos|_{[0, \pi]}$ o $\sin|_{[-\pi/2, \pi/2]}$).
- Uso della circonferenza goniometrica per individuare graficamente simmetrie, parità/disparità e segni delle funzioni.
- Risoluzione di equazioni trigonometriche mediante scomposizione o identità.
- Analisi grafica tramite trasformazioni: traslazioni e confronti di grafici (es. confronto tra $\sin x$ e $\cos x$).

## Errori tipici da segnalare allo studente
1. Dimenticare le condizioni di esistenza per le funzioni $\tan x$ ($x \neq \pi/2 + k\pi$) e $\cot x$ ($x \neq k\pi$).
2. Confondere gli intervalli di invertibilità (es. usare tutto $\mathbb{R}$ per definire l'arcoseno).
3. Errata applicazione delle formule di bisezione, specialmente nel segno della radice.
4. Non considerare la periodicità durante la risoluzione di equazioni o disequazioni trigonometriche.

## Tipologie di esercizio da generare
1. Risoluzione di disequazioni trigonometriche in intervalli limitati (es. $[- \pi, \pi]$).
2. Semplificazione di espressioni trigonometriche complesse usando formule di addizione e sottrazione.
3. Analisi grafica: identificazione del grafico di funzioni composte (es. $h(x) = \max\{\sin x, \cos x\}$).
4. Calcolo di valori trigonometrici dato un vincolo su un quadrante (es. dato $\sin x$, calcolare $\cot(2x)$).
5. Risoluzione di equazioni goniometriche parametriche o algebriche.
