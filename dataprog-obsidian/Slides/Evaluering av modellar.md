---
tags:
  - lecture/video/perspective
  - topic/machinelearning
  - lecture/stub
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
<!-- slide template="[[tpl-twocolumn]]" bg="white"-->

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

| | Sannsyn |
| :- | -: |
| Feil | $p$ |
| Rett svar | $1-p$ |
| To rette testar | $(1-p)^2$ |

---

| | Sannsyn | Døme |
| :- | -: | -: |
| Faktisk feilsannsyn | $p$ | 50% |
| Sannsyn for rett svar | $1-p$ | 50% |
| Sannsyn for to rette testar | $(1-p)^2$ | 25% |


note:
Preposterous example.


---

# Hypotesetest

$H_1$ Systemet svarer rett med sannsyn $> 1-p$

$H_0$ Systemet svarer rett med sannsyn $\le 1-p$

note:
Verste fall gjev forventa feilrate $p$

Gjer me $n$ testart forventar me då $n\cdot p$ feil.

---
<!-- slide template="[[tpl-diagram]]" -->

![[hyp0.svg]]

::: credit
$p_e=0.1$; $n=100$ testar
:::

note:
Sett at me godtek 10% feil, og at me har 50 datapunkt å testa på.
Hypotetisk kan me gå ut frå at systemet har feilsannsyn 0,1, og plotta sannsynsfordelinga for feiltalet når me testar på 50 datapunkt.

Det ser slik ut.

Ikkje uventa ligg tyngdepunktet på 5 feil, som svarer til 10% av 50 testar.  Det er om lag like sannsynleg å få fleire eller færre feil.  Om me observerer 4% feil, altso to feil, tyder ikkje det at feilsannsynet er 4%.  Det er faktisk 11% sannsyn for å sjå to eller færre feil når feilsannsynet er 10%.

---
<!-- slide template="[[tpl-diagram]]" -->

![[hyp1.svg]]

note:
Når vi gjør en hypotesetest bestemmer vi et signifikansnivå, f.eks. 5%, og vi forkaster nullhypotesen når det observerte resultatet er mer usannsynlig enn signifikansnivået.

Vi har merket dette i figuren.  Det lyseblå området har sannsynlighet under 5%.  Dvs. at hvis vi observerer null eller én feil, kan vi konkludere med at feillsannsynligheten er høyst 10%, på et signifikansnivå på 5%.  

Problemet med hypotesetester er at vi trenger gode marginer for å konkludere med noe som helst. Vi begrenser risikoen for at vi stoler på et system som ikke er godt nok, men der er stor risiko for å forkaste et system som kunne vært brukt. I kritiske operasjoner, som f.eks. nye medisiner og vaksiner, er det nettopp slik vi vil ha det.

---
<!-- slide template="[[tpl-diagram]]" -->

![[hyp2.svg]]

note:
Vi kan få mer presise tester hvis vi gjør flere forsøk.  Vi ser i figuren at dess større $n$ er, dess mer konsentrasjon for vi rundt forventet feiltall.  Da trenger ikke feilsannsynligheten være så mye mindre enn de postulerte 10% før det er mest sannsynlig at testen lar oss forkaste nullhypotesen.

Den samme vurderingen gjelder om vi estimerer feilsannsynligheten.  Dess større $n$, dess mindre usikkerhet i estimatet.


---

# Overlæring og underlæring

note:
Vi skal ta ett -- eller to -- begreper til: overlæring og underlæring.

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

---

# Slutt

note:
