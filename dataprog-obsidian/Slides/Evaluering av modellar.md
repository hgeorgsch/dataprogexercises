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
<!-- slide template="[[tpl-diagram]]" -->

![[mlloan.svg]]
::: credit
:::

note:
Hva mener vi med en modell.

---
<!-- slide template="[[tpl-diagram]]" -->

![[eval01.svg]]

note:
Utval

---
<!-- slide template="[[tpl-diagram]]" -->

![[eval02.svg]]

note:
Positiv test

---
<!-- slide template="[[tpl-diagram]]" -->

![[eval03.svg]]

note:
Negativ test

---
<!-- slide template="[[tpl-quote]]" -->

![[Training-and-validation-scheme-for-machine-learning-methods-The-database-is-split-and.png]]

::: credit
[Imbalzano *et al* 2022](https://www.mdpi.com/2077-0383/11/1/219)
:::

note:
For å vurdere kvaliteten på modellen, holder vi gjerne tilbake en del av datasettet.
Ofte fjerner man tilfeldig 20% av radene, som da ikke brukes til trening.
Dette gir oss et lite datasett som i prinsippet er uavhengig av modellen.

Slik har man et treningssett som brukes til å lave modellen, og tilpasse 
vektene, og et treningssett som brukes til å teste hvor god modellen er.

---
<!-- slide template="[[tpl-quote]]" -->

![https://i0.wp.com/thaddeus-segura.com/wp-content/uploads/2021/06/Screen-Shot-2021-06-17-at-7.03.33-PM-1.png?resize=532%2C658&ssl=1](https://i0.wp.com/thaddeus-segura.com/wp-content/uploads/2021/06/Screen-Shot-2021-06-17-at-7.03.33-PM-1.png?resize=532%2C658&ssl=1)

::: credit
:::

note:
Ofte trener man flere forskjellige modeller og prøver seg frem med ulike
design og varierer såkalte hyperparametre.  Da er det ikke nok å validere
maskinlæringen, men òg det designet som vi tilpasser manuelt.

Derfor er det vanlig å ha to testsett, gjerne kalt valideringssett og
testsett.  Da bruker man valideringssettet til å evaluere hver enkelt
modell som man trener, og når man er ferdig og velger den man synes er
best, bruker man testsettet til å kontrollere at denne modellen faktisk
er god nok.

Merk at det er det samme prinsippet som ligger til grunn den automatiske
maskinlæringen som tilpasser vektene i modelle og den modelle designprosessen
som velger algoritme og tilpasser designparametrene.  I begge tilfeller 
prøver vi oss frem til vi finner noe som passer med datasettet, og vi vet
ikke om det generaliserer før vi tester på uavhengige data.

---
<!-- slide template="[[tpl-twocolumn]]" -->

::: leftimage
![[mlloan.svg]]
:::

::: leftcredit
:::

::: rightimage
![[Coin_Toss_(3635981474).jpg]]
:::

::: rightcredit
By ICMA Photos - Coin Toss,
CC BY-SA 2.0, via
[Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=71147286)
:::

note:
Sett nu at vi har en modell.  La oss si en modell for lånetilsagn.

+ Så sier jeg at denne har jeg testet.
+ Testane viser at vi tjener penger på 100% av tildelte lån.
+ Så sier jeg at jeg har testet på *to* lånesøknader.

Hva tror du om testen?

---

<!-- slide template="[[tpl-twocolumn]]" -->

::: leftimage
+ Faktisk feilsannsyn $p$
+ Sannsyn for rett svar $1-p$
+ Sannsyn for to rette testar $(1-p)^2$
:::

::: leftcredit
:::

::: rightimage
# Til dømes
+ Faktisk feilsannsyn 50%
+ Sannsyn for rett svar 50%
+ Sannsyn for to rette testar 25%
:::

::: rightcredit
:::

note:
Preposterous example.


---

Hypotesetest

$H_1$ Systemet svarer rett med sannsyn $> 1-p$

$H_0$ Systemet svarer rett med sannsyn $\le 1-p$

Verste fall gjev forventa feilrate $p$

Gjer me $n$ testart forventar me då $n\cdot p$ feil.

---
<!-- slide template="[[tpl-diagram]]" -->

![[hyp0.svg]]

---
<!-- slide template="[[tpl-diagram]]" -->

![[hyp1.svg]]

---
<!-- slide template="[[tpl-diagram]]" -->

![[hyp2.svg]]

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
