---
title: Bias i maskinlæring
tags:
  - lecture/video/perspective
  - topic/machinelearning
css:
  - css/templates.css
---
# Kunstig Intelligens

note:
Kunstig intelligens er et uungåelig tema når vi går inn i dataanalyse, men kunstig intelligens er mye rart. En begrepsavklaring er på sin plass.

---
<!-- slide template="[[tpl-flex]]" -->

![[dartmouth1956.jpeg]]

::: credit
Foto: Margareth Minsky
:::

note:
Selve ordet *Artificial Intelligence* ble brukt første gang i 1956, på det legendariske arbeidsseminaret på Dartmouth College i 1956.  John McCarthy hadde idéen og klarte å skaffe finansiering til å samle ti unge og lovende forskere i to måneder for å finne ut hvordan man kan programmere maskiner til å tenke som mennesker.

Flere av deltagerne ble de fremste på feltet utover 60- og 70-tallet, som Simon og Newall, og Marvin Minsky.

---
<!-- slide template="[[tpl-twocolumn]]" -->

::: rightimage
![[Plato_Silanion_Musei_Capitolini_MC1377.png]]
:::

::: rightcredit
Platon
:::

::: leftimage
![[The_lady_with_the_lamp_Miss_Nightingale_at_Scutari_1854.jpg]]
:::

::: leftcredit
*The Lady with the Lamp*
By Henrietta Rae -  Public Domain
[via Wikimedia commons](https://commons.wikimedia.org/w/index.php?curid=6756261)
:::

note:
Like siden starten har der vært to paradigmer innenfor kunstig intelligens.
Regelbasert KI som bygger på Platons forståelse av fornuften og maskinlæring som gjør som Florence Nightingale gjorde.

Platon hevdet at all kunnskap kan formuleres som universelle regler. Håndtverk basert på erfaring eller poesi basert på inspirasjon er blott vilkårlig fumling. 
Dette synet på  kunnskap har dominert vestlig tenkning i over 2000 år.

Det fine med universelle regler er at de er lette å programmere.
Hvis vi først *kan* formulere en universell regel, er det en smal sak å oversette regelen til python-kode. 

---
<!-- slide template="[[tpl-twocolumn]]" -->

::: rightimage
![[Herbert-A-Simon-1978.jpg]]
:::

::: rightcredit
By Rochester Institute of Technology - News & Events 1981 at the RIT Digital Archive, 
Public Domain,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=115626765)
:::

::: leftimage
![[Allen_Newell.jpg]]
:::

::: leftcredit
By [Stanford Magazine](https://stanfordmag.org/contents/if-you-love-what-computers-can-do-thank-these-folks),
Fair use,
via [Wikimedia Commons](https://en.wikipedia.org/w/index.php?curid=63421113)
:::

note:
Herbert Simon og Allen Newell deltok bare to uker på Dartmouth-seminaret, men de stjal på mange måter showet med sin *General Problem Solver* eller GPS.
Problemløsning var for dem bare beregninger på logiske utsagn, og programmet deres kunne søke gjennom regelsamlinger for å finne alle mulige logiske konsekvenser.
Slik implementerte de en algoritme som først ble formulert av Aristoteles.

---
<!-- slide template="[[tpl-twocolumn]]" -->

::: rightimage
![[Marvin_Minsky_at_OLPCb_(3x4_cropped).jpg]]
:::

::: rightcredit
Marvin Minsky, foto Sethwoodworth at English Wikipedia. 
CC BY 3.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=170239489)
:::

::: leftimage
![[Frank_Rosenblatt.jpg]]
:::

::: leftcredit
Frank Rosenblatt.
Foto: Anonymous - [Heinz Nixdorf MuseumsForum](https://blog.hnf.de/frank-rosenblatt-und-das-perceptron/),
CC BY-SA 4.0, via
[Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=163187420)
:::

note:
Den som store fanebæreren for maskinlæring var Frank Rosenblatt, med sitt arbeide på perseptroner på slutten av 1950-tallet.  Forskningsmidlene på 1960-tallet gikk derimot i all hovedsak til dem som fulgte i Simon og Newell sine fotspor.  Han ble kraftig kritisert av Marvin Minsky.

Rosenblatt endte opp med depresjon og i 1971 ble båten hans ble funnet drivende og forlatt på sjøen.  Offisielt omkom han i en båtulykke.

Minskys kritikk var at Rosenblatts maskinlæring bare virket på leketøyseksempler.
At det samme også var tilfellet for regelbasert kunstig intelligens, unnlot Minsky å snakke om.
Det gikk derimot ikke mange årene før man måtte erkjenne at KI ikke var en stor suksess, og feltet gikk inn i en lang AI-vinter.

---
<!-- slide template="[[tpl-flex]]" -->

::: credit
By D Wells - File:Iris_Pairs_Plot.png with some minor modifications, CC BY-SA 4.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=112294469)
:::

note:
Da vinteren tok slutt var det maskinlæring som fikk sin renaissanse, med en ny forståelse bygd på statistikk.

Statistikken gav et teoretisk fundament for å se på maskinlæring som pålitelig kunnskap, selv der det ikke er mulig å formulere generelle regler.  Platon ville neppe vært enig, men det virker for oss.

---
<!-- slide template="[[tpl-flex]]" -->

![[Ontology.jpg]]

:::  credit
By Lia Veja ([Semantic Cora]()https://semantic-cora.org/index.php/File:Ontology.jpg),
CC BY-SA 4.0, via
[Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=79753999)
:::

note:
Det er derimot ikke slik at regelbasert KI er helt borte.
Den regelbaserte intelligensen har en viktig egenskap som maskinlæringen mangler, nemlig sematikk. 
Når vi formulerer logiske utsagn i problemløseren til Simon og Newell, bruker vi meningsbærende symboler. Utsagnene kan faktisk beskrive egenskaper ved verden rundt oss. I maskinlæring er dataene ribbet for kontekst og mening.

Problemet med semantisk KI er kjøretiden, som gjerne vokser eksponentielt i antall regler som blir brukt. Hvis problemområdet er tilstrekkelig avgrenset, kan man likevel oppnå resultater. 


---

+ Prediksjonsmodeller
+ Ontologier
+ Generativ KI

note:
Så hvilke former for kunstig intelligens er det da vi står igjen med i dag?

Det vi snakker om i dataanalyse er i all hovedsak prediksjonsmodeller, dvs. maskinlæring anvendt på et avgrenset og veldefinert problem.
Når vi vet nøyaktig hva vi ønsker å løse, og har mulighet for å samle nok data på ett og samme problem, er det mulig ikke bare å trene men også teste presise modeller.

Regelbasert KI bygger gjerne på ontologier, dvs. systemer av begreper og relasjoner mellom dem.  Forutsetningen for å kunne regne på semantisk er at vi først har definert meningsfulle begreper å regne på. 

Generativ KI er det som er mest kjent, både med store sprogmodeller og generativ KI for bilder og musikk.  I prinsippet er det også prediksjonsmodeller. En stor sprogmodell predikerer neste ord i en tekst, basert på forutgående kontekst.  Slik er svaret fra sprogmodellen blott et gjennomsnitt av tekst som den er trent på. Der er ingen semantikk bak ordene som brukes.

---

# Slutt

note:
Faren med KI er at vi tar det i bruk på nye problemer uten å forstå dem godt nok til å vurdere om KI-modellene gir fornuftige svar.  Det er derfor jeg mener at det er så viktig å se maskinlæring som en gren av statistikk og dataanalyse, der vi har verktøyene for kvantitativ testing.

Uansett hvordan vi snur og vender på det, så er KI et verktøy og det er brukeren som har ansvaret for resultatet.  Aldri verktøyet.

Takk for oppmerksomheten.