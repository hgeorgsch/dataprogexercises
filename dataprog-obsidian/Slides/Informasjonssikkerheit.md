---
title: Informasjonssikkerheit
author: Hans Georg Schaathun
date: Mai 2026
tags:
  - lecture/video/perspective
css:
  - css/templates.css
---

# Informasjonssikkerheit

![[sec01.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Intet kurs i databehandling eller programmering bør avsluttes uten å komme inn på informasjonssikkerhet.


---

![[protect.png]]

![[sec02.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Sikkerhet handler i bunn og grunn bare om én ting.  
Om å verne om det som vi helst ikke vil miste.

Alt vi gjør, og alt vi ikke gjør, har betydning for sikkerheten, på en eller anden måte.

Når vi går ut av huset, tar vi en risiko.  Vi kan bli truffet av en taksten som faller eller påkjørt av bussen.

Blir vi inne tar vi også en risiko.  Det sies at de fleste ulykker skjer på kjøkkenet.

Det samme gjelder når vi bruker data.  Når vi lagrer data, er der alltid en risiko for at de kommer i gale hender.  Lagrer vi dem ikke, mister vi tilgangen til dem.

Slike stadige risikovurderinger tilhører brukerne, og kan ikke overlates til
sikkerhetseksperter som ikke vet hvordan data brukes.

---
<!-- slide template="[[tpl-twocolumn]]" -->


::: leftimage
![[calamity.png]]
:::

::: leftcredit
:::

::: rightimage
![[slyfox.png]]
:::

::: rightcredit
:::

![[sec03.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Sikkerhet handler om to ganske forskjellige utfordringer.
På engelsk skiller man vanemessig mellom *security* og *safety*.
På norsk *kan* vi skille mellom sikkerhet og trygghet, men like ofte bruker vi sikkerhet om alt.

På den ene siden har vi trygghet for ulykker som inntreffer tilfeldig.
På den andre siden har vi sikkerhet mot fiender som aktivt ønsker å tilrane seg verdier på vår bekostning, eller kanskje bare skade oss uten skjellig grunn.

Tilfeldige hendelser er det enkleste å forholde seg til.  Klarer vi å forhindre 50% av hendelsene, har vi redusert risikoen med 50%.

---

![[kurios119.jpg]]

![[sec04.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Slik er det ikke med skurken.  De er slu, og hvis vi hindrer 50% av angrepene, vil angriperne oppdage det og flytte innsatsen for å utnytte andre sårbarheter. 
Der vil alltid være skurker som aktivt søker efter vårt svakeste punkt.

---
<!-- slide template="[[tpl-flex]]" -->

![[treasure.png]]

::: credit
:::

![[sec05.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Sikkerhet er ingen absolutt størrelse; det er alltid relativt til de verdier vi ønsker å beskytte.

I informasjonssikkerhet kan vi snakke om informasjonsverdier.  Data kan ha verdi som kunnskapskilde eller som forretningshemmeligheter. Penger, i våre dager, er også stort sett data i et informasjonssystem og sjelden gull eller sølv. Det kan være vanskelig å sette ord på faktiske verdier, fordi de ofte er abstrakte, men det gjør ikke tapet mindre reelt, enten det er økomisk tap, ødelagt rykte eller juridisk ansvar.

---
<!-- slide template="[[tpl-flex]]" bg="white" -->

![[kit.svg]]

::: credit
:::

![[sec06.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Informasjonsverdier som blir stjålet eller kommer på avveie er ikke det eneste
som bekymrer oss.
Dersom dét var det eneste som bekymret oss, ville det tryggeste være bare å slette og ødelegge alt sammen.  Ingenting blir hemmeligere enn det som alle har glemt.

Derfor snakker vi gjerne om tre forskjellige sider ved sikkerhet, 

+ Konfidentialitet handler om at informasjon ikke skal være tilgjengelig for uvedkommende.
+ Tilgjengelighet handler om at informasjonen *skal* være tilgjengelig for oss som trenger den.
+ Integritet handler om at vi må kunne stole på at informasjonen er korrekt.

Til sammen blir dette det som gjerne kalles KIT-triangelet.
Det er farlig å bli så opphengt i én side av trianglet at vi glemmer en anden.
Når vi fortsetter skal vi derfor alltid huske at informasjonsverdier er utsatt for trusler fra alle de tre kantene.

---
<!-- slide template="[[tpl-flex]]" bg="white" -->

![[infosecorg.svg]]
::: credit
:::

![[sec07.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Utgangspunktet for effektiv sikring er god forståelse av hva som
skal sikres og hva det skal sikres mot.  

Vi har snakket om informasjonsverdier.  Når vi arbeider med dataanalyse,
er det først og fremst datasettene vi jobber med som er relevant.

Disse datasettene er eid av noen.  I figuren er det kalt en organisasjon,
men det kan være en person.  Eierskapet kan òg være tvetydig.  
En bedrift vil forvalte kundedata og har kanskje eierskap til databasen,
men hver enkelt kunde har eierskap til sine personopplysninger.
Man kan også sitte på data som man har kjøpt fra en dataleverandør,
uten at man har løyve til å dele disse data videre.

Verdiene er utsatt for trusler, det kan være konkurrenter som vil ha
forretningdshemmeligheter eller svindlere som vil ha fatt i persondata.
Det kan være fremmede makter som spionerer på enkeltpersoner.

Dersom en trusel blir realisert, fører det til skade på organisasjonen.
Den mest vanlige skaden er kanskje tap av rykte og tillit som følge av
innbrudd og mulig tap av data.

Før man tar i bruke en datakilde, er det nyttig å sette ord på verdiene
man risikerer og truslene man står overfor.

---
<!-- slide template="[[tpl-flex]]" bg="white" -->

![[ontology.svg]]
::: credit
:::

![[sec08.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Når vi vet hva vi står overfor, er det nyttig å gå videre og vurdere
hva vi kan gjøre med det.

Trusler, når vi ser bort fra ulykker, kommer av motstandere med et
bevisst ønske om å gjøre skade.  Hvem er disse motstanderne?

Motstanderne vil utnytte sårbarheter, ikke bare i datasystemet men også
i vår bruk av systemet og dataene.  Lar vi døren stå ulåst?  
Har vi passordet på en gul lapp på skjermen?
Sender vi data i ukryptert epost? 

Først når vi setter ord på sårbarhetene, gir det mening å snakke om
kontroller som er egnet til å redusere sårbarhet.

Grunnen til at jeg bruker tid på dette er at disse vurderingene ikke
kan gjøres generelt eller uten inngående kjennskap til virksomheten.  
Brukerne er en del av systemet og dermed en del av løsningen.

---
<!-- slide template="[[tpl-flex]]" -->

![[Beaumaris_Castle_(48281071296).jpg]]

::: credit
By Tom Parnell from Scottish Borders, Scotland - Beaumaris Castle, CC BY-SA 2.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=80472330)
:::

![[sec09.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Tradisjonelt har vi ofte lagt borgmodellen til grunn for sikkerhet.

Vi får ekspertene til å bygge høye og solide murer rundt oss, og så velger vi å stole blindt på dem som er innenfor murene. Truslene forutsettes å være utenfor.

---
<!-- slide template="[[tpl-flex]]" -->

![[Castell_Beaumaris_Castle,_Ynys_Mon_(Anglesey),_Wales_05.jpg]]

::: credit
By Llywelyn2000 - Own work, CC BY-SA 4.0, 
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=137373162)
:::

![[sec10.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Vi kan gjerne ha flere lag med mur, der hver mur representerer et nytt sikkerhetsnivå, men det samme prinsippet og det samme problemet ligger til grunn på hvert nivå.
Vi må ha full kontroll på dem som kommer inn i borgen og kunne stole 100% på dem.

Borgporten er en sårbarhet.  Er vi slepphendte risikerer vi å tape konfidentialitet og integritet, og er vi strenge risikerer vi å tape tilgjengelighet.

Hver gang noen slippes inn, og hver gang noen tar med noe ut, risikerer vi å gjøre feil.

Informasjonssystemer er ofte bygd rundt dette tankesettet, der de store aktører forvalter tilgangen til skyløsninger. Som databrukere må vi derimot huske på at hver gang vi henter data ut, utnytter vi en åpning i muren, og eksponerer dataene utenfor.  Da må vi ta ansvar selv.

Enda mer kontroversielt er det når vi legger data inn i borgen. Hvis det er våre egne data, er det opp til oss om vi vil stole på borgherren. Når vi ønsker å studere data om andre mennesker, er det deres personvern vi setter på spill.


---
## Slutt

![[sec11.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Personvern er dog en så stor utfordring at det fordrer et foredrag for seg selv.

Takk for nå.
