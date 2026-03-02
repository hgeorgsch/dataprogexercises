---
tags:
  - lecture/video/perspective
  - topic/machinelearning
  - lecture/stub
css:
  - css/templates.css
---

<!-- slide template="[[tpl-titleslide]]" -->
# Evaluering av modellar

![[mlloan.svg]]

note:
Dataanalyse handler ofte om å konstruere modeller,
enten det er konvensjonelle, statistiske modeller eller
mer komplekse maskinlæringsmodeller.

Modeller er aldri perfekte, men de kan gjøre større eller
mindre feil.

Når vi evaluerer modeller må vi egentlig stille vi to spørsmål.
Det ene er deskriptivt.
Hvor store og hvor sannsynlige er feilene?

Det andre er normativt.
Hvor stor og hvor hyppige feil kan vi akseptere?

Vi skal nøye oss med å diskutere det deskriptive spørsmålet.
Det normative spørsmålet må man ta i hvert enkelt tilfelle for seg.

---
<!-- slide template="[[tpl-diagram]]" -->

![[sampling.svg]]

::: credit
:::

note:
Konteksten vår er statistisk inferens eller maskinlæring, der vi
konstruerer modellen ut fra et utvalg, men ønsker å bruke den til
å beskrive populasjonen.

Dvs. at når vi evaluerer modellen, er det feilene den gjør på populasjonen
som er interessant.  Det er ikke godt nok at beskrivelsen er feilfri på
utvalget, for det er ikke det den skal brukes til.

---
<!-- slide template="[[tpl-diagram]]" -->

![[eval01.svg]]

::: credit
:::

note:
La oss ta et klassifiseringseksempel.  Vi kan forestille oss at vi deler
kundenemassen opp i gode eller blå kunder og dårlige, røde kunder.
Her har vi bare to observerte variabler.  Kanskje det er inntekt og formue.
selv om skalaen frå pluss til minus tyve er meningsløs.  Det spiller ingen
rolle, for problemet er generelt.

Så med tanke på modellen, er hver kunde blott et punkt $(x,y)$.
Modellen er den grønne, stiplede linjen som deler rommet i to.
Den sier at en kunde på undersiden av linjen, antagelig er rød.
Gode kunder er ventet på oppsiden.

Modellen er konstruert ut fra det utvalget som er vist i figuren, og
vi ser at den fungerer perfekt.

Så langt.

---
<!-- slide template="[[tpl-diagram]]" -->

![[eval02.svg]]

::: credit
:::

note:
Hvis vi hadde sett hele populasjonen, kan det tenkes at det hadde
sett slik ut.  Dette er ganske pene og homogene populasjoner, og 
modellen gjør bare to feil.

---
<!-- slide template="[[tpl-diagram]]" -->

![[eval03.svg]]

note:
Utvalget kunne like gjerne være hentet fra denne populasjonen, og her ser 
vi ikke bare at modellen gjør et betydelig antall feil, men også at der finnes
bedre modeller.  Vi kunne ha tegnet linjen vannrett og ikke på skrå.

Når vi ser på utvalget er det umulig å se hvilken av de to populasjoner det
er hentet fra.


---
<!-- slide template="[[tpl-diagram]]" -->

![[sampling2.svg]]

note:
Løsningen er å bruke flere utvalg.
Det er usannsynlig at en dårlig modell vil fungere dårlig på et 
tilfeldig utvalg.  

Dvs. tilfeldig utvalg betyr her et utvalg som ikke bare er tilfeldig,
men som også ikke har vært brukt tidligere i tilpassingen av modellen.

Prinsippet er det samme som Karl Popper la ned for videnskablig forskning 
på begynnelsen av 1900-tallet.
Gode modeller og teorier er åpne for falsifisering.
Vi kan alltid prøve å motbevise dem, ved å prøve dem i nye sammenhenger.
Hvis teorien skal være generell, så må den holde i et hvert tilfeldig
valgt nytt spesialtilfelle.  

---
<!-- slide template="[[tpl-quote]]" -->

![[Training-and-validation-scheme-for-machine-learning-methods-The-database-is-split-and.png]]

::: credit
[Imbalzano *et al* 2022](https://www.mdpi.com/2077-0383/11/1/219)
:::

note:
I maskinlæring er det vanlig å dele datasettet opp i to eller tre utvalg.
For å vurdere kvaliteten på modellen, holder vi gjerne tilbake en del av datasettet.
En vanlig tommelfingerregel er å ta 20% av radene til testing, og resten til trening.

Dette gir oss ett treningssett som vi mater gjennom algoritmen for å lave en
modell.  Testsettet er i prinsippet er uavhengig av modellen, og når
vi mater det gjennom modellen, kan vi se hvordan den gjør det på datapunkter
som ikke var tilgjengelige for treningsalgoritmen.
har man et treningssett som brukes til å lave modellen, og tilpasse 
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
<!-- slide template="[[tpl-flex]]" bg="white"-->

![[Heading_nyhetsbrev_uke-43-Maskiner-som-tenker.jpg]]

::: credit
Illstrasjon frå Kagge forlag.
:::

note:
Vi skal merke oss at denne standardoppskriften fra maskinlæring er langt fra de standarder som brukes i mer etablerte statistiske disipliner.

Inga Strümke formulerer dette godt i sin bestselger av en bok.
Når vi samler inn ett datasett og deler det i to eller tre, så har vi ikke egentlig
uavhengige utvalg.  Alle utvalgene er samlet inn med de samme metodene fra den
samme konteksten.  Det er sjelden vi kan samle tilfeldige utvalg som er representative
for hele verden.

I klinkiske forsøk i medisin er kravene strengere.  Der krever man uavhengige tester på
utvalg som er uavhengig innsamlet.

Det er en god idé å tenke gjennom dette konkret for hvert enkelt anvendelsesområde
når man skal trene og ta i bruk en maskinlæringsmodell.  

Denne utfordringen er dog for stor til å løse her, og vi har andre utfordringer
å se på.

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

Sett at vi har en modell.  La oss si en modell for lånetilsagn.

+ Så sier jeg at denne har jeg testet.
+ Testane viser at vi tjener penger på 100% av de lån som er tildelt vha modellen.
+ Så sier jeg at jeg har testet på *to* lånesøknader.

Hva tror du om testen?

---

| | Sannsyn |
| :- | -: |
| Feil | $p$ |
| Rett svar | $1-p$ |
| To rette testar | $(1-p)^2$ |

note:
La oss si at modellen har et faktisk feilsannynlighet $p$.
Vi vet selvsagt ikke hva $p$ er.

Sannsynligheten for et godt svar fra modellen er da $1-p$,
og hvis vi gjør to uavhengige tester, er sannsynligheten for
100% rett lik $(1-p)^2$.

---
<!-- slide template="[[tpl-twocolumn]]" bg="white"-->

::: leftimage
| | Sannsyn | Døme |
| :- | -: | -: |
| Faktisk feilsannsyn | $p$ | 50% |
| Sannsyn for rett svar | $1-p$ | 50% |
| Sannsyn for to rette testar | $(1-p)^2$ | 25% |
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
Sett nu at alt modellen gjør er å kaste mynt og kron.
Kron gir lån og mynt gir ikke.
Dvs. at riktig og galt svar fra modellen er like sannsynlig,
uansett hva det riktige svaret måtte være.

$$ p = 0{,}5 $$

Sannsynligheten for to riktige myntkast er da 25%.
Vår tullete modell har dermed 25% sannsynlighet for å få perfekt
vurdering ...

Vi skjønner at utvalget er for lite.
Det er ikke like lett å se hvor stort utvalget må være for å være stort nok.

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

::: credit
:::

note:
Når vi gjør en hypotesetest bestemmer vi et signifikansnivå, f.eks. 5%, og vi forkaster nullhypotesen når det observerte resultatet er mer usannsynlig enn signifikansnivået.

Vi har merket dette i figuren.  Det lyseblå området har sannsynlighet under 5%.  Dvs. at hvis vi observerer null eller én feil, kan vi konkludere med at feillsannsynligheten er høyst 10%, på et signifikansnivå på 5%.  

Problemet med hypotesetester er at vi trenger gode marginer for å konkludere med noe som helst. Vi begrenser risikoen for at vi stoler på et system som ikke er godt nok, men der er stor risiko for å forkaste et system som kunne vært brukt. I kritiske operasjoner, som f.eks. nye medisiner og vaksiner, er det nettopp slik vi vil ha det.

---
<!-- slide template="[[tpl-diagram]]" -->

![[hyp2.svg]]

::: credit
:::

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
