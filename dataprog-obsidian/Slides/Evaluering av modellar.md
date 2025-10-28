---
tags:
  - lecture/video/perspective
  - stub
---

# Evaluering av modellar

---
<!-- slide template="[[tpl-diagram]]" -->

![[sampling.svg]]

::: credit
:::

note:
Deskriptiv statistikk vs. Statistisk inferens

---

Klassifisering med gode og dårlege utval

---

Testdata og treningsdata

note:
* For å anslå om modellen vår er god, eller om vi overtilpasser den, holder vi gjerne tilbake forskjellige subset av dataene våres:
  * Vi kan feks trekkke ut tilfeldige 20% som ikke brukes til trening av modellen, men til å teste modellen etterpå
* Ellers justerer man på parametre i modellen, forenkler data, straffer kompleksitet og mange andre "triks" for å lage gode modeller

---



![https://i0.wp.com/thaddeus-segura.com/wp-content/uploads/2021/06/Screen-Shot-2021-06-17-at-7.03.33-PM-1.png?resize=532%2C658&ssl=1](https://i0.wp.com/thaddeus-segura.com/wp-content/uploads/2021/06/Screen-Shot-2021-06-17-at-7.03.33-PM-1.png?resize=532%2C658&ssl=1)

![https://www.researchgate.net/publication/357570421/figure/fig2/AS:11431281210648059@1702062985384/Training-and-validation-scheme-for-machine-learning-methods-The-database-is-split-and.tif](https://www.researchgate.net/publication/357570421/figure/fig2/AS:11431281210648059@1702062985384/Training-and-validation-scheme-for-machine-learning-methods-The-database-is-split-and.tif)

---

Preposterous example.


---

Hypotesetest

$H_1$ Systemet svarer rett med sannsyn $> 1-p$

$H_0$ Systemet svarer rett med sannsyn $\le 1-p$

Verste fall gjev forventa feilrate $p$

Gjer me $n$ testart forventar me då $n\cdot p$ feil.

---

Binomialfordelinga

---

Best practice

---

![https://miro.medium.com/v2/resize:fit:720/format:webp/1*lARssDbZVTvk4S-Dk1g-eA.png](https://miro.medium.com/v2/resize:fit:720/format:webp/1*lARssDbZVTvk4S-Dk1g-eA.png)

note:
Vi må da typisk unngå:
* «Overfitting»: Modellen memoriserer kun testdataen vår
* «Underfitting»: Modellen har ikke lært nok
