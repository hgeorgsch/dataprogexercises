---
tags:
  - lecture/video/perspective
  - machine-learning
  - stub
---

# Tema å dekkja

1. Klassifikasjon av bilete
2. Klassifikasjon av numeriske data
    + https://www.kaggle.com/datasets/anishdevedward/loan-approval-dataset
3. Regresjon
4. Tidsrekkjer
    + ikkje prioritert - krev meir tid

# Utdrag frå førelesing 2024

## Typer læring

* I hovedtrekk ofte to typer:
  * «Supervised learning»: Algoritmen eller modellen lærer fra input/output data (vi vet hva "resultatet" skal være)
  * «Unsupervised learning»: Algoritmen eller modellen finner mønstre i data vi ikke "kjenner" i utgangspunktet

+++

## Hovedmål

* Målet med «læringen» er at den opplærte modellen vår skal «funke» på data vi ikke har sett før
* Dersom den gjør det sier vi at modellen generaliserer bra

Vi må da typisk unngå:
* «Overfitting»: Modellen memoriserer kun testdataen vår
* «Underfitting»: Modellen har ikke lært nok

+++

![https://miro.medium.com/v2/resize:fit:720/format:webp/1*lARssDbZVTvk4S-Dk1g-eA.png](https://miro.medium.com/v2/resize:fit:720/format:webp/1*lARssDbZVTvk4S-Dk1g-eA.png)

+++

# Testdata og treningsdata
* For å anslå om modellen vår er god, eller om vi overtilpasser den, holder vi gjerne tilbake forskjellige subset av dataene våres:
  * Vi kan feks trekkke ut tilfeldige 20% som ikke brukes til trening av modellen, men til å teste modellen etterpå
* Ellers justerer man på parametre i modellen, forenkler data, straffer kompleksitet og mange andre "triks" for å lage gode modeller

+++

![https://www.researchgate.net/publication/357570421/figure/fig2/AS:11431281210648059@1702062985384/Training-and-validation-scheme-for-machine-learning-methods-The-database-is-split-and.tif](https://www.researchgate.net/publication/357570421/figure/fig2/AS:11431281210648059@1702062985384/Training-and-validation-scheme-for-machine-learning-methods-The-database-is-split-and.tif)

+++

![https://i0.wp.com/thaddeus-segura.com/wp-content/uploads/2021/06/Screen-Shot-2021-06-17-at-7.03.33-PM-1.png?resize=532%2C658&ssl=1](https://i0.wp.com/thaddeus-segura.com/wp-content/uploads/2021/06/Screen-Shot-2021-06-17-at-7.03.33-PM-1.png?resize=532%2C658&ssl=1)

