---
title: Om å læra frå data
tags:
  - lecture/video/perspective
  - topic/machinelearning
css:
  - css/templates.css
---

# Om å læra frå data

---

<!-- slide template="[[tpl-quote]]" -->

![[The_lady_with_the_lamp_Miss_Nightingale_at_Scutari_1854.jpg]]

::: credit
*The Lady with the Lamp*
By Henrietta Rae -  Public Domain
[via Wikimedia commons](https://commons.wikimedia.org/w/index.php?curid=6756261)
:::

note:
Florence Nightingale er kanskje best kjent som
*the lady with the lamp*,
den omsorgsfulle sykepleiersken på det engelske
feltskjukehuset under Krimkrigen.

---

<!-- slide template="[[tpl-quote]]" -->

![[Nightingale-mortality.jpg]]

::: credit
Mortality Chart due to Florence Nightingale
:::

note:
Hun er kanskje mindre kjent som statistiker, til tross
for at hun var en banebrytende pionér.
I 1858 ble hun som første kvinne medlem av *Royal Statistical Society*.

På feltsjukehuset registrerte hun møysommelig data.
Bl.a. talte hun hvor mange pasienter som døde og hvor ofte
legene vasket hendene.

Hun fant en statistisk sammenheng, som hun brukte til å argumentere for bedre hygiene. Hun møtte  dronning Victoria personlig, og fikk anledning til på påvirke politikken gjennom statistikk. Reformene hun skape i sykestellet er et av de aller første eksemplene på at data blir brukt systematisk til å ta beslutninger.

Det skal innrømmes at selv om Florence gjettet på at dårlig håndhygiene
fører til flere dødsfall, er ikke dét noe som vi kan lese ut fra datamaterialet.
Kan hende er det slik at når mange pasientar er syke og 
døende, så har legene mindre tid til å vaske hendene.
Altså at mange døende pasienter er årsak til dårlig hygiene.

Årsakssammenhengene ble forklart av legevidenskaben efter Florence Nightingale sin tid.

---

<!-- slide template="[[tpl-quote]]" -->

![[DARPA_Big_Data.jpg]]

::: credit
By DARPA - Defense Advanced Research Projects Agency (DARPA), Public Domain,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=25685422)
:::

note:
Når vi går i gang med å studere stordata med hjelp av programmering og kunstig intelligens,
er det viktig å huske på at vi egentlig ikke gjør noget andet enn Florence Nightingale.
Vi gjør det blott i større skala, med flere variabler og flere datapunkter.
Hun kunne telle og tegne for hånd.
Når vi går til store data trenger vi maskiner til å gjøre eselarbeidet for oss.

Liksom Florence Nightingale, kan hverken KI eller vi finne årsakssammenhenger gjennom data alene.
Som dataanalytikere, statistikere og KI-eksperter må vi nøye oss med å påvise korrelasjon,
og overlate kausalitet til andre fagfelter.
Kunnskap om korrelasjon gir like fullt en nyttig pekepinn på hvor man kan lete efter kausalitet.
 
---

<!-- slide template="[[tpl-quote]]" -->

![[regdata.svg]]

::: credit
Figur frå øvinga [Lineær regresjon](notebook/Linear%20Regression%20in%20SciKitLearn).
:::

note:
Florence Nightingale så på samanhengen mellom to variabler,
antall dødsfall og antall håndvask.

Figuren viser ikke hennes data, men et andet datasett der vi har en variabel `x` som vi kan observere og en anden variabel `y` som vi ønsker å forutsi før vi kan observere den. Hvert punkt viser et observert par x/y som hører sammen.

---

<!-- slide template="[[tpl-quote]]" -->


![[regmodel.svg]]

::: credit
[Lineær regresjon](notebook/Linear%20Regression%20in%20SciKitLearn) (døme frå øvinga).
:::

note:
Når vi studerer en slik samanheng kvantitativt, kaller vi det
regresjonsanalyse,  som er en av de aller mest sentrale og grunnleggende
teknikkene i statistikk.

Lineær regresjon prøver å beskrive `y` som en lineær funksjon av `x`.
Dette datasettet viser bare svak sammenheng.
Gjennomsnittlig `y`-verdi synker noe med økende `x`,
men det er tilfeldig variasjon som dominereri bildet.

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
**Adolphe Quetelet <br> (1796-1874)**
![[Adolphe_Quételet_by_Joseph-Arnold_Demannez.jpg]]
:::

::: credit2
By Joseph-Arnold Demannez.
[Public Domain](https://commons.wikimedia.org/w/index.php?curid=4080229)  
:::

::: image3
**sir Francis Galton <br> ($\sim$ 1885)**
![[Sir_Francis_Galton_by_Charles_Wellington_Furse.jpg]]
:::

::: credit3
By Charles Wellington Furse (died 1904) 
[Public Domain](https://commons.wikimedia.org/w/index.php?curid=6364538)  
:::

note:
Regresjonsanalysen var derimot ikke utviklet da Florence fikk sitt
gjennombrudd.
Tilfeldighet og sannsynlighet er rett og slett krevende konsepter å håndtere, 
og det tok mange generasjoner å oppnå tilstrekkelig forståelse til å kunne utvikle pålitelige teknikker.

Det var enklest i fysikken. 
Legendre skildre  minste kvadraters metode allerede i 1805, og astronomene tok raskt teknikken i bruk for å beregne planetbaner.
Fordelen med fysikk er at de teoretiske modellene er godt funderte og har relativt få variabler.

Samfunnsvidenskabene er vanskeligere, fordi der alltid er flere faktorer enn dem vi klarer å holde regning med.
Da Quetelet innførte statistikk i samfunnsvidenskabene utover 1800-tallet,
hadde man ennu ikke tilstrekkelig forståelse av  sannsynlighet og usikkerhet til helt å lykkes.

Mange regner  Galton som som oppfinneren av regresjon rundt 1885, med
arbeide i genetikk og arvelære.
        
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
En anden av de store pionerene i statistikk er Ronald Fisher, som bl.a.
er kjent for løsninger på klassifiseringsproblemer.
Datasettet som han brukte for å klassifisere tre ulike arter
av irisblomsten blir stadig brukt som referansetest i maskinlæring
i dag.

Datasettet inneholder lengde og bredde på kron- og begerblad på
ulike individ av blomsten.
Fisher viste at han kunne finne en statistisk modell som sier 
hvilken art et individ tilhører, bare ut fra disse fire målene..

---

<!-- slide template="[[tpl-quote]]" -->

![[fisher.svg]]

::: credit
Eigen figur, sjå [[Fisher Linear Discriminant in sklearn]].
:::

note:
Jeg er dårlig på å tegne i fire dimensjoner, men dersom vi bare tar
målene på begerbladene, kan det se slik ut.

Hvert punkt er ett individ,
med lengde på x-aksen og bredde på y-aksen.
Hver art har så sin farve, og vi kan se at de ulike artene
*typisk sett* har ulike mål.

---

<!-- slide template="[[tpl-quote]]" -->

![[fishersep.svg]]

::: credit
Eigen figur, sjå [[Fisher Linear Discriminant in sklearn]].
:::


note:
Fisher delte artene fra hverandre med rette linjer.
Her ser vi Fishers løsning for å skille *Iris Setosa* fra andre iris-varianter.

Når vi siden måla et ukjent individ, kan vi raskt se hvilken side av
linjen det faller på.
Modellen er ikke perfekt.  Vi ser f.eks. ett setosaeksemplar på feil side av linjen.
Det er likevel en god modell, som virker med god sannsynlighet. 

Mye av det arbeidet vi gjør i maskinlæring er ett av disse to problemene, 
enten regresjon eller klassifisering.

Den lineære modellen har bare én *vekt*, som definerer stigningstallet på skillelinjen. Dagens dype nevrale nettverk kan ha milliarder av vekter. Dess flere vekter, dess mer komplekse sammenhenger kan beskrives, men flere vekter krever også flere datapunkter og ikke minst mer strøm til beregningen.

I tillegg til vektene har modellen et konstantledd, *bias*, som forteller hvor linjen krysser `y`-aksen.

---

1950-talet
: Maskinlæring *ad hoc*!

1980-talet
: Maskinlæring *er* statistikk.

rundt 2005
: Vektorprosessorar *(GPU)*

rundt 2010-2015
: *djupe* nevrale nettverk

note:
Historien om maskinlæring og kunstig intelligens begynner på 1940- og 50-tallet, samtidig med at de første generelle og programmerbare datamaskinene ble tatt i bruk.
Rosenblatt viste frem trening av nevrale nettverk
for å løse klassifiseringsproblemer i 1957, men den gangen
justerte han vektene manuelt.

Det er først på 1980-tallet at man får effektive treningsalgoritmer
for nevrale nettverk, og skjønner at maskinlæring må bygge
statistikk og forståelsen av usikkerhet og sannsynlighet. 

For tyve år siden fikk vi billige vektorprosessorer, som først 
ble brukt i skjermkort og ble masseproduksert til spillkonsoller.
Man oppdaget derimot ganske raskt at de var uhyre effektive til
å regne på store datamengder.  
Matematikken i nevrale nettverk er langt på vei den samme som i 3D-grafikk.

For ti-femten år siden løsnet det virkelig for nevrale nettverk.
Vektormaskinene gjorde at man kunne bruke større nettverk og 
større datasett, og 
teste flere og større modeller på kortere tid.
Det hjalp frem nye og mer komplekse nettverksarkitekturer.

Likevel står vi overfor de samme utfordringene rundt
usikkerhet og sannsynlighet som statistikerne har strevd med i 200 år.
          
---

<!-- slide template="[[tpl-quote]]" -->

![[Human_computers_-_Dryden.jpg]]

::: credit
NACA High Speed Flight Station Computer Room (1949)
by
[NACA (NASA)](http://www.dfrc.nasa.gov/Gallery/Photo/Places/HTML/E49-54.html),
- Dryden Flight Research Center Photo Collection - 
Public Domain, via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=885426).
:::

note:
Der er ingen klar grense mellom hva som er maskinlæring
og hva som bare er statistikk.
Eksperter kan gjerne være uenige om hvor grensen går.
Kan hende er den store forskjellen mellom modeller
som kan regnes for hånd og modeller som krever maskiner.

Bildet viser noen av NASAs *computers* i 1949 - altså
personer som regner.

---

<!-- slide template="[[tpl-quote]]" -->

![[iris-pdf.svg]]

::: credit
Egen figur basert på iris-datasettet.
:::

note:
Uansett om vi tenker statistikk eller maskinlæring,
handler det om å bruke data for å bygge sannsynlighetsmodeller.
Figuren viser mulige sannsynlighetsfordelinger for kronbladbredden på *Iris Setosa* i blått og *Iris Versicolor* i orange, basert på datasettet.

Vi ser den statistiske forskjellen.  Hvis kronbladet er mer enn tre centimeter bredt er det mest sannsynlig *versicolor*, men det er langt fra sikkert.

---

<!-- slide template="[[tpl-quote]]" -->

![[Artificial_Intelligence_Word_Cloud.png]]

::: credit
By Madhav-Malhotra-003 - Own work, CC0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=127185596)
:::

note:
Det er akkurat det samme ChatGPT eller MicroSoft Copilot gjør.
Store sprogmodeller er sannsynlighetsmodeller for tekst.
Når du skriver inn et spørsmål, predikerer ChatGPT et
sannsynlig svar i tråd med den tekstkorpusen den er trent på.

Vi kaller ChatGPT for er en generativ modell; dvs. han genererer ny
tekst, men innerst inne er dette ikke forskjellig fra 
gamle regresjons- og klassifikasjonsmodeller.
ChatGPT ser på en kontekst og predikerer den mest 
sannsynlige responsen.
 
---

# Sannsynleg $\neq$ Sann

note:
Det er derfor ChatGPT og andre sprogmodeller kan hallusinere.
Sannsynlig har ingenting med sann å gjøre.

---

<!-- slide template="[[tpl-quote]]" -->

![[Simple_random_sampling.png]]

::: credit
By Dan Kernler - Own work, CC BY-SA 4.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=36506020)
:::

note:
Der er mange utfordringer når man skal lære fra data. 
En av de største er å finne data som er *representative* for det man ønsker å lære noe om.

Ingen prøver å spå resultatene til stortingsvalget ved å spørre bare et par tusen mennesker på Søre Sunnmøre. Vi vet at det ville gi en helt anden modell enn om vi spurte folk i Lofoten eller Drammen.

Det er mange som glemmer denne lærdommen når de tar i bruk maskinlæring og kunstig intelligens. Et velkjent eksempel er ansettelsesprosesser, der man har trent maskinlæringsmodeller på data fra historiske ansettelsesprosesser, og ikke på data som er representative for den fremtiden man ønsker seg.  

Hvis man tidligere bare har ansatt etnisk norske menn med sivilingeniørgrad fra Trondhjem, får vi en maskinlæringsmodell som sier at dét er normalen. Kvinner, afrikanere og musikere fremstår alle som like usannsynlige og blir dermed valgt bort, blott fordi de var sjeldne i treningsutvalget.


---

<!-- slide template="[[tpl-quote]]" -->

![[2010_Utopien_arche04.jpg]]

::: credit
By Efthymios Warlamis - Own work, Daskunstmuseum, 2007-01-05, CC BY-SA 3.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=16899707)
:::

note:
Da ChatGPT ble allment tilgjengelig i 2022 fremsto det som et mirakel fra fremtiden, som et orakel som vi ikke er ment å forstå.

Det er ikke sant.

 Mange av prinsippene bak maskinlæring er over hundrede år gamle, og selv om vi i dag har regnekraft og datamengder som kan ta pusten fra oss, er vi like sårbare for de gamle fallgrubene.
 Modellene representerer bare den fortiden som de er trent på.
 Skal vi skape den fremtiden vi ønsker oss, må vi ta ansvar selv.
