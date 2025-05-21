---
tags:
  - lecture/video/perspective
---



---

<!-- slide template="[[tpl-quote]]" -->

![[The_lady_with_the_lamp_Miss_Nightingale_at_Scutari_1854.jpg]]

::: credit
*The Lady with the Lamp*
By Henrietta Rae -  Public Domain
[via Wikimedia commons](https://commons.wikimedia.org/w/index.php?curid=6756261)
:::

note:
Florence Nightingale er kanskje best kjend som
*the lady with the lamp*,
den omsorgfulle sjukepleiaren på det engelske
feltskjukehuset under Krimkrigen.

---

<!-- slide template="[[tpl-quote]]" -->

![[https://upload.wikimedia.org/wikipedia/commons/1/17/Nightingale-mortality.jpg]]

::: credit
Mortality Chart due to Florence Nightingale
:::

note:
Ho er kanskje mindre kjend som statistikar, til tross
for at ho var ein banebrytande pionér.
På feltsjukehuset registrerte ho møysommeleg data m.a.
om kor mange som døydde og kor ofte lækjarane vaska hendene.

**NB!** Ho fann statistiske samanhengar; ikkje årsakssamanhengar.

Kan henda var det slik at når mange pasientar var svært sjuke
og døyande, so hadde ikkje lækjarane tid til å vaske hendene,
slik at mange dødsfall forårsakar dårleg hygiene.

På det punktet lærte helsevitskapane meir utover 1900-talet.
         
Korelasjon versus kausalitet
 
---

<!-- slide template="[[tpl-quote]]" -->

![[dataset2.svg]]

::: credit
:::

note:
Florence Nightingale såg på samanhengen mellomn to variablar,
tala på dødsfall og talet på handvask.

---

<!-- slide template="[[tpl-quote]]" -->

# regresjon

![[reg.svg]]

::: credit
:::

note:
Når slike samanhengar vert studerte kvantitativt, kaller me det
regresjonsanalyse,  kanskje den aller mest sentrale og grunnleggjande
teknikken i statistikk.

---

<!-- slide template="[[tpl-three]]" -->

::: image1
**Adrien-Marie Legendre (1805)**

![[Legendre.jpg]]
:::

::: credit1
By
[Julien-Léopold Boilly](http://www.numericana.com/answer/record.htm#legendre) 
[Public Domain](https://commons.wikimedia.org/w/index.php?curid=6092195)  
:::

::: image2
**Adolphe Quetelet (1796-1874)**
![[Adolphe_Quételet_by_Joseph-Arnold_Demannez.jpg]]
:::

::: credit2
By Joseph-Arnold Demannez.
[Public Domain](https://commons.wikimedia.org/w/index.php?curid=4080229)  
:::

::: image3
**sir Francis Galton ($\sim$ 1885)**
![[Sir_Francis_Galton_by_Charles_Wellington_Furse.jpg]]
:::

::: credit3
By Charles Wellington Furse (died 1904) 
[Public Domain](https://commons.wikimedia.org/w/index.php?curid=6364538)  
:::

note:

Regresjonsanalysa var derimot ikkje utvikla då Florence fekk
gjennombrotet sitt.
Det tok over eitt hundrede år å utvikla.
Ein del av teknikken, minste kvadrats metode, var rett nok skildra av Legendre
i 1805 og godt etablert i astronomi, men då Quetelet innførde statistikk i
samfunnsvitskapane hadde ein stadig ikkje god nok forståing for sannsyn og
usikkerheit til heilt å få det til.
Ofte vert Galton som er rekna som oppfinnaren av regresjon rundt 1885, med
arbeid i genetikk og arvelære.
        
---

<!-- slide template="[[tpl-twocolumn]]" -->

## Ronald Fisher (1890-1962)
::: leftimage
![[Youngronaldfisher2.jpeg]]
:::

::: leftcredit
Ronald Fisher in 1913; from
[Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=42616717)
:::

::: rightimage

![[Irissetosa1.jpg]]
:::

::: rightcredit
Iris Setosa; from
[Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=57593826).
:::

note:
Ein av dei største statistikarane er Ronald Fisher, som m.a.
er kjend for løysing av klassifiseringsproblem.
Datasettet som han brukte for å klassifisera tre ulike artar
av irisblomen vert stadig brukt som referansetest i maskinlæring
i dag.

Datasettet hadde målt lengd og breidd på kron- og begerblada på
ulike individ.  Fisher viste at han kunne finna ein statistisk
modell som seier kva art individet høyrer til, berre ut frå dei fire 
måla.

---

<!-- slide template="[[tpl-quote]]" -->

![[dataset.svg]]

::: credit
:::

---

<!-- slide template="[[tpl-quote]]" -->

![[sep2.svg]]

::: credit
:::


note:
Eg er dårleg på å teikna fire dimensjonar, men dersom han hadde
to mål, kunne det sjå slik ut.

Kvart punkt er eitt individ, og her har me ein blå og ein raud art.

Kvart individ har eitt mål på $x$-aksen og eitt på $y$-aksen,

Fisher delte dei to artane frå kvarandre med ein rett line.
Her ser me ei god og ei dårleg line; Fisher fann ein matematisk
formel for den gode lina.

No kan me måla eit ukjend individ, og raskt sjå kva side av
line individet høyrer heime på, og gjetta på den arten.
Det er ikkje 100%, men me har godt sannsyn.

---

1950-talet
: Maskinlæring *ad hoc*!

1980-talet
: Maskinlæring *er* statistikk.

rundt 2005
: Vektorprosessorer *(GPU)*

siste ti år
: *djupe* evrale nettverk

note:
Rosenblatt (1957) viste fram trening av nevralt nettverk
for å løysa klassifiseringsproblem, men han
justerte vektene manuelt.

Det er fyrst på 1980-talet at ein får effektiv trening
av nevrale nettverk, og skjøner at dette handlar om
usikkerheit og sannsyn.

For tjue år sidan fekk me vektorprosessorar, som fyrst vart
brukte på skjermkort og kom i masseproduksjon til spillkonsoll.
Ein oppdaga derimot ganske raskt at dei var uhyre effektive til
å rekne på store datamengder.

For ti år sidan lossna det verkeleg for nevrale nettverka.
Vektormaskinene gjorde at ein kunne bruka større nettverk og
testa meir og raskare, og ein fann nye nettverksarkitekturar.

Likevel, me hanskast framleis med dei same utfordringane rundt
usikkerheit og sannsyn som har utfordra statistikarane i 200 år.
          
---

+ Statistikk med handrekna formlar.
+ Maskinrekning pga. mange «tunge» rekneoperasjonar 
+ Maskinrekning pga. mange fridomsgradar
+ Maskinrekning pga. store datamengder
+ Maskinrekning fordi lukka formlar ikkje er kjende
    + Iterativ tilnærming

note:
Der er ingen klar grense mellom kva som er maskinlæring
og kva som berre er statistikk.
Eg arbeidde mykje med maskinlæring for 12-15 år sidan.
Då brukte eg hovudsakleg SVM (support vector machines).
Den gongen var SVM stort sett like presise som nevrale
nettverk, og mykje raskare.
Ein kollega av meg argumenterte for at det ikkje
er maskinlæring, fordi SVM har ein lukka formel som
vert rekna ut i eitt steg.

For å illustrera skilnaden kan me bruka eit enklare
døme.  (eller dropp)


---

# Sannsynsmodellar

note:
Uansett om me taler om statistikk eller maskinlæring,
handlar det om å bruka data for å byggja sannsynsmodellar.
Når modellen er bygd kan ein sjå på nokre eigenskaper
i ein situasjon og predikera resten.

Det er dette ChatGPT gjer òg.
Når du skriv inn eit spørsmål, predikerer ChatGPT eit
sannsynleg svar i tråd med den teksta han er trent på.

ChatGPT er en generativ modell; dvs. han genererer ny
tekst, men innerst inne er dette ikkje forskjellig frå 
gamle regresjons- og klassifikasjonsmodellar.
ChatGPT ser på ei kontekst og predikerer den mest 
sannsynlege responsen.
 
---

# Sannsynleg $\neq$ Sann

note:
Det er difor ChatGPT finn opp so mykje misinformasjon.
Sannsynleg har ingenting med sann å gjera.

---

# Semantikk versus Syntaks

note:
Der finst andre typar kunstig intelligens som jobbar med semantikk
der maskinlæring og ChatGPT berre handlar om syntaks.
Mellom anna har me hatt automatiske provmaskiner i fleire tiår.
Dei arbeider med logiske proposisjonar og kan gjennomføra 
logisk deduksjon.
Dette kan ein kombinera med semantiske teknologiar som ikkje berre
identifiserer ord med konsept men ogso relasjonar mellom konsept.

For byggja ein meir sannferdig ChatGPT må ein kanskje finna måtar
å kombinera maskinlæring med semantiske teknologiar.
          
---

# Representative Data

note:

Dersom du skal gjera ein meiningsmåling for å vurdera oppslutning
om ulike politiske parti, so vil du ikkje vera nøydd med å spørja
eit par hundre lærarar som er til stades i dag.

For det fyrste er eit par hundre litt knapt.

For det andre er ikkje lærarar særleg representative for nasjonen
som heilskap.  Industriarbeidarar, lækjarar, lærarar og næringslivsleiarar
har ein tendens til ulike meiningar.

Mange har brukt maskinlæring i tilsetjingsprosessar.
Maskina er trent på representative data frå fortida, der den typiske 
tilsette har vore ein kvit mann med sivilingeniørutdanning frå Trondheim.
Då vil maskina halda fram med å velja kvite menn med 
sivilingeniørutdanning frå Trondheim.

Afrikanske invandrarar, kvinner og musikarar frå Noregs Musikkhøgskule
er akkurat like feil so langt som maskina kan sjå frå data.

---

# Førestillingsevna

note:

Mennesket har ein unik evne til førestilling.
Me kan førestilla oss ei annleis framtid.
Og me kan førestilla oss korleis andre menneske vil oppleva
denne framtida.

Weizenbaum skreiv t.d. at me menneske lærar noko om det 
å vera menneske berre av å veksa opp som menneske og verte
behandla som menneske av andre menneske.

Denne idéen er godt kjend i den tyske og skandinaviske
danningstradisjonen.  Den danske utdanningsfilosofen
Peter Kemp skriv t.d. at der
utdanningsinnhaldet - forklaring - kan skrivast ned
og takast fram når det trengst, finst der eit
danningsinnhald - forståinga - som berre kan formidlast
i direkte møte mellom menneske.

Maskina er god på utdanningsinnhald.

---

# Overraskinga

note:

Mennesket kan difor handtera overrasking.
Me kan finna meining i val som aldri har vore gjort før,
som å tilsetja afrikanske invandrar eller kvinner,
eller musikarar i ein ingeniørjobb,
og vurdera om det er bra for oss.

Maskina kan ikkje det.
Overrasking og nyskaping er støy som bryt med forventinga,
det som statistikken kaller *utliggjarar*.
Der finst ikkje empirisk grunnlag for at nyskapinga er positiv.


---

# Notes

+ Florence Nightingale
+ Utviklinga av statistikk i samfunnsvitskapane
	+ Andre halvdel av 1800-talet
	+ Lineær regresjon
	+ Byggjer på regresjon i astronomi frå starten av 1800-talet
	+ Ny forståing av usikkerheit
+ Fisher i mellomkrigstida
	+ Klassifiseringsproblem
+ Shannons Informasjonsteori på 1940- og 50-talet
+ Bruksområde
	+ Demografi
	+ Val- og meiningsmålingar
	+ Klinisk testing
+ Maskinlæring som sannsynsmodell
	+ Evaluering av maskinlæringsmodellar

