---
tags:
  - lecture/video/perspective
  - stub
---

# Evaluering av modellar

note:
Dataanalyse handler ofte om å konstruere modeller, enten det er konvensjonelle, statistiske modeller eller mer komplekse maskinlæringsmodeller.

---
<!-- slide template="[[tpl-diagram]]" -->

![[sampling.svg]]

::: credit
:::

note:
I de fleste tilfeller arbeider vi med datasett som beskriver et begrenset utvalg av en større populasjon.
Skal du gjøre en markedsundersøkelse, kan du kanskje spørre tusen potentielle kunder, men det er umulig å spørre alle potentielle kunder.
Skal du forsøke å forutsi hvor sannsynlig det er at en potentiell lånekunde vil misligholde lånet, må du bruke data om historiske lån. Det er umulig å få data om fremtidige og potentielle lånekunder.

I utvalgsstatistikken må vi skille mellom deskriptiv statistikk, som beskrivere utvalget vårt, og statistisk inferens, som bruker utvalget til å beskrive populasjonen.

Deskriptiv statistikk er relativt enkelt og beskrivelsene av utvalget er eksakte. I noen tilfeller har vi også tilgang til populasjonsdata, som gjøre det mulig med deskriptiv statistikk på populasjonen. Det gjelder gjerne arbeidsledighetsdata, eksportdata og skattetall, som myndighetene registrerer for hele befolkningen.

Statistisk inferens er mer utfordrende, fordi kunnskap om utvalget aldri gir eksakt kunnskap om populasjonen.

---

Klassifisering med gode og dårlege utval

---

Testdata og treningsdata

note:
* For å anslå om modellen vår er god, eller om vi overtilpasser den, holder vi gjerne tilbake forskjellige subset av dataene våres:
  * Vi kan feks trekkke ut tilfeldige 20% som ikke brukes til trening av modellen, men til å teste modellen etterpå
* Ellers justerer man på parametre i modellen, forenkler data, straffer kompleksitet og mange andre "triks" for å lage gode modeller

---




![https://www.researchgate.net/publication/357570421/figure/fig2/AS:11431281210648059@1702062985384/Training-and-validation-scheme-for-machine-learning-methods-The-database-is-split-and.tif](https://www.researchgate.net/publication/357570421/figure/fig2/AS:11431281210648059@1702062985384/Training-and-validation-scheme-for-machine-learning-methods-The-database-is-split-and.tif)

---

![https://i0.wp.com/thaddeus-segura.com/wp-content/uploads/2021/06/Screen-Shot-2021-06-17-at-7.03.33-PM-1.png?resize=532%2C658&ssl=1](https://i0.wp.com/thaddeus-segura.com/wp-content/uploads/2021/06/Screen-Shot-2021-06-17-at-7.03.33-PM-1.png?resize=532%2C658&ssl=1)

note:
Best practice

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
<!-- slide template="[[tpl-diagram]]" -->

![[Underfitting_e_overfitting.png]]

::: credit
By Leomaurodesenv - Own work, CC BY-SA 4.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=103533707)
:::

note:
Vi må da typisk unngå:
* «Overfitting»: Modellen memoriserer kun testdataen vår
* «Underfitting»: Modellen har ikke lært nok

---
<!-- slide template="[[tpl-diagram]]" -->

![[484261_1_En_4_Fig1_HTML.webp]]

::: credit
Montesinos López, O.A., Montesinos López, A., Crossa, J. (2022). Overfitting, Model Tuning, and Evaluation of Prediction Performance. In *Multivariate Statistical Machine Learning Methods for Genomic Prediction*. Springer, Cham. 
[doi:10.1007/978-3-030-89010-0_4](https://doi.org/10.1007/978-3-030-89010-0_4) (Open Access)
:::