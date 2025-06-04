---
tags:
  - lecture/video
---

# Imperativ programmering

note:
Der er mange måter å programmere en datamaskin på.
Det paradigmet som ligger til grunn for dette kurset kaller vi gjerne for *imperativ* programmering.
Det er det mest kjente paradigmet, men ikke det eneste.

Vi skal snakke litt om hvordan datamaskina konseptuelt sett virker.
Målet er bedre innblikk i hvordan vi tenker når vi bruker Python til
å instruere datamaskinen.

*original*: Der er mange måtar å programmera ei datamaskin på. Det paradigmet som ligg til grunn for dette kurset er *imperativ* programmering. Det er det mest kjende paradigmet, men ikkje det einaste.

Me skal prata litt om korleis datamaskina konseptuelt sett verkar. Målet er litt betre innblikk i korleis me tenkjer når me bruker Python til å instruera datamaskina.

---

<!-- slide template="[[tpl-quote]]" -->

![[command-DALLE.webp]]

::: credit
Bilete frå DALL-E (kunstig intelligens)
:::

note:
Vi kaller det for imperativ programmering fordi vi gir maskinen kommandoer, dvs. setninger i grammatisk imperativ.  

Maskinen tenker ikke.
Det er programmøren som står for all tenkingen.
Maskinen gjør nøyaktig som kommandert, og programmøren må se for seg hva hver kommando vil føre til.

*original:*
Me kaller det for imperativ programmering, fordi me gjev maskina kommandoar, dvs. setningar i grammatisk imperativ.  

Maskina tenkjer ikkje. Det er programmøren som står for all tenkinga. Maskina gjer nøyaktig som kommandert, og programmøren må sjå for seg kva kvar kommando fører til.

---

```python
b = 5
print(b)
```

note:
Imperativen er tydelig når vi skriver t.eks. *print* i python.
Maskinen prenter som han får beskjed om.
Den første kodelinjen her er også en imperativ, som som vi kan lese som «la `b` være lik 5». 

Et kritisk kjennetegn i imperativ programmering er *tilstand*.
Tilordningen `b=5` endrer tilstand på maskinen.
Før linje 1 er `b` udefinert, når vi kommer til linje 2 har `b` verdien 5, og dermed en anden tilstand.
Resultatet av *print* i line 2 avhenger helt åbenbart av hvilken tilstand maskinen -- eller `b` -- har.

*original:*
Imperativen er tydeleg når me skriv t.d. *print* i python. Maskina prentar som ho får beskjed om. Den fyrste lina i koden her er òg ein imperativ, som som me lyt lesa som «lat $b$ vera lik 5». 

Eit kritisk kjenneteikn i imperativ programmering er *tilstand* . Tilordning `b=5` endrar tilstand på maskina. Før line 1 er `b` udefinert, når me kjem til line 2 har `b` ein verdi, 5, og altso ein annan tilstand. Resultatet av *print* i line 2 avheng heilt openbert av kva tilstand maskina har.

---

```python
b = 5
print(b)
b = 10
print(b)
```

note:
Tilstanden blir enda tydligere i dette eksempelet.
De to *print*-linjene er identiske, men de gir ikke samme resultat, fordi *tilstaden* i maskinen er forskjellig.
Første gang har `b` tilstanden 5, og *print* skriver ut 5.
Den andre gangen er tilstanden 10, og det er 10 som blir skrevet ut.

*original:*
Tilstanden vert enno tydlegare i dette dømet.  Dei to *print*-linene er identiske, men dei gjev ikkje same resultat, fordi *tilstaden* åt maskina er forskjellig. Fyrste gongen har `b` tilstanden 5, og *print* skriv ut 5. Andre gongen er tilstanden 10, og det er 10 som vert skrive ut.

---

<!-- slide template="[[tpl-twocolumn]]" -->

::: leftimage
![[Alan_Turing_(1951).jpg|400]]
:::

::: leftcredit
Alan Turing 1951 ([by Elliott & Fry](https://www.computerhistory.org/timeline/1949/) Public Domain)
:::

::: rightimage
![[Alonzo_Church.jpg|400]]
:::

::: rightcredit
Alonzo Church
([By Princeton University, Fair use](https://en.wikipedia.org/w/index.php?curid=6082269))
:::


note:
Teorien for datamaskiner og programmering ble lang på vei utarbeidet på 1930-talet, cirka ti år før man først bygde maskiner som faktisk kunne kjøre programmene.
Church og Turing definerte hvert sitt paradigme. De er ekvivalente i den forstand at de kan *oppnå* det samme, selv om tankesettet er meget forskjellig.

Turingmaskinen er den mest kjente modellen, og den som ligger til grunn for imperativ programmering, der vi kommanderer maskinene og sier nøyaktig hva den skal gjøre i hvilken rekkefølge.
Church sin λ-kalkyle ligger til grunn for det som vi i dag kaller *funksjonell programmering*, der vi heller definerer hvilke egenskaper resultatet av programmet skal ha, utan å si hvordan den skal komme frem til det.

Begge modellene var abstrakte matematiske konsepter, men det er Turing sin modell som best svarer til dei elektroniske maskinene som man tok til å bygge utover 1940-talet.
Imperativ programmering er stadig det dominerende tankesettet, og derfor er det det vi skal bruke tid på her.

*original:*
Teorien for datamaskiner og programmering vart hovudsakleg utarbeidd på 1930-talet, om lag ti år før ein fyrst bygde maskiner som faktisk kunne køyra programma. Church og Turing definterte kvart sitt paradigme. Dei er ekvivalente i den forstand at dei kan *oppnå* det same, sjølv om ein tenkjer forskjellig.

Turingmaskina er den mest kjende modellen, og den som ligg til grunn for imperativ programmering, der me kommanderer maskina og seier nøyaktig hva ho skal gjera.  Church sin $\lambda$-kalkyle ligg til grunn for det som me i dag kaller *funksjonell programmering*, der me definerer kva eigenskaper resultatet av programmer skal ha, utan å seia korleis ein oppnår det.

Båe modellane var abstrakte matematiske konsept, men det er Turing sin modell som best svarer til dei elektroniske maskinene som ein tok til å byggja utover 1940-talet.  Imperativ programmering er stadig det dominerande tankesettet, og difor det som me vil bruka tid på her.

---

<!-- slide template="[[tpl-quote]]" -->

## Turingmaskina

![[Turing_Machine_Model_Davey_2012.jpg]]

::: credit
Turing Machine, reconstructed by Mike Davey as seen at Go Ask ALICE at Harvard University ([Rocky Acosta](https://commons.wikimedia.org/wiki/User:Arttechlaw "User:Arttechlaw") - Own work)
:::

note: 
Turingmaskinen er som sagt en abstrakt og matematisk modell. Bildet viser en rekonstruert og fysisk modell. 

Maskinen har et papirbånd som er rullet opp på to spoler som drar båndet fram og tilbake gjennom lesehodet i midten.
Dette båndet er minnet i maskinen.
Det er delt i diskrete posisjonar der hver posisjon kan inneholde ett tegn.

Turingmaskinen er en *tilstandsmaskin*.  Dvs. til en hver tid er maskinen i en bestemt tilstand. Det som maskinen gjør avhenger både av tilstanden og det som står på båndet. 

*original:*
Turingmaskina er som sagt ein abstrakt og matematisk modell. Biletet viser ein rekonstruert modell. 

Maskina har eit papirband som er rulla opp på to spoler som kan dra bandet att og fram gjennom lesehodet i midten. Papirbandet er minnet i maskina og delt i diskrete posisjonar der kvar posisjon kan innehalad eitt teikn.

Turingmaskina er ei *tilstandsmaskin*.  Dvs. til ei kvar tid er maskina i ei bestemt tilstand. Det som maskina gjer avheng både av tilstanda og kva som står på bandet. 

---

<!-- slide template="[[tpl-diagram]]" -->

![[turinginstruction.svg]]
::: credit
:::

note:
På hver tidssteg ser maskinen tilstanden sin og ett tegn på båndet. Dette avjør både den nye tilstanden og hvilket tegn som blir skrevet på båndet.
I tillegg kan båndet flytte et steg til høyre eller til venstre.
Turingmaskinen har en fast oppslagstabell som definerer resultatet for en gitt tilstand og et gitt tegn på båndet.
Samme tilstand og tegn gir *alltid* samme resultat.

Denne maskinen er selvsagt absurd enkel.
Den må òg være uhyre treg siden det tar lang tid å lete gjennom båndet efter riktig posisjon. 
Likevel viser Turing at den i prinsippet kan løse mange komplekse problemer.  

Alt vi trenger er et minne som vi kan bla igjennom og en operasjon som virker på to inputtverdier, tilstanden og verdien fra båndet.
Ennu i dag regner vi turingmaskinen som målestokk for hva som overhode er mulig å beregne.

*original:*
På kvart tidssteg ser maskina tilstanden sin og eitt teikn på bandet. Dette avgjer både den nye tilstanden og kva teikn som vert skrive til bandet. I tillegg kan bandet flytta eit steg til høgre eller venstre. Turingmaskina har ein fast oppslagstabell, som gjev resultatet for ein gjeven tilstand og eit gjeve teikn på bandet. Same tilstand og teikn gjev *alltid* same resultat.

Denne maskina er sjølvsagt absurd enkel.  Ho må òg vera uhyrleg treig sidan det tek lang tid å leita gjennom bandet. Likevel viser Turing at ho i prinsippet kan løysa mange komplekse problem.  

Alt me treng er eit minne som me kan bla igjennom og ein operasjon som verkar på to inputtverdiar, tilstanden og verdien fra bandet.

---

<!-- slide template="[[tpl-diagram]]" -->

**von Neumann-arkitekturen**

![[neumann.svg|1200]]

::: credit
:::

note:
Elementene fra turingmaskinen kjenner vi igjen i John von Neumann sin arkitektur fra 1945.
Hans modell er blitt førende for praktisk konstruksjon av datamaskiner.

Papirremsen er blit til *Random Access Memory*, eller RAM. *Random Access* betyr at maskinen kan lese og skrive på en hvilken som helst posisjon, utan å bruke tid på å lete langs remsen

Selve prosesseringsenheten er blitt mer kompleks. 
Kontrollenheten holder styr på programmet og hvilken instruksjon den logiske og aritmetiske enheten skal utføre neste gang.
Tilstanden er ikke lenger én atomær verdi, men flere registre der hvert register inneholder en verdi.

Instruksjonene er typisk enkle aritmetiske og logiske operasjoner, som pluss, minus, *og* og *eller*, samt instruksjoner for å hoppe i programmet eller lese og skrive til minnet.

I tillegg er maskina koblet til det vi gjerne kaller *perifere enheter*, eller *input/output devices* i figuren.
Det omfatter skjerm for *output*, og tastatur for *input*, men kan òg være nettverksgrensesnitt eller harddisk.
Du la kanskje merke til at turingmaskinen ikke hadde noen mekanisme for å kommunisere omverdenen.
I praksis må den logiske enheten ha instruksjoner for å sende og motta data til og fra perifere enheter.

Et hovedpoeng i von Neumann-arkitekturen er at det samme RAM-minnet blir brukt både til de data som programmet arbeider på og til selve programmet.

*original:*
Desse elementa kjenner me igjen i  John von Neumann sin arkitektur frå 1945, som har vorte førande for den praktiske konstruksjonen av datamaskiner.

Papirremsa er vorte til *Random Access Memory*, eller RAM. *Random Access* tyder at maskina kan lesa og skriva til ein kvan posisjon, utan å bruka tid på å leita langs remsa.

Sjølve prosesseringseininga er vorten meir kompleks. Kontrolleininga held styr på programmet og kva instruksjon den logiske og aritmetiske eininga skal utføra neste gong.  Tilstanden er ikkje lenger éin atomær verdi, men fleire register der kvart register inneheld ein verdi.

Instruksjonane er typisk enkle aritmetiske og logiske operasjonar, som pluss, minus, og, og eller, samt instruksjonar for å hoppa i programmet eller lesa og skriva til minnet.

I tillegg er maskina kobla til det me gjerne kaller *perifere einingar*, eller *input/output devices* i figuren. Det omfatter skjerm, for *output*, og tastatur for *input*, men kan òg vera nettverksgrensesnitt eller harddisk. Du la kanskje merke til at turingmaskina ikkje hadde nokon mekanisme for å kommunisera med omverda. I praksis må den logiske eininga ha instruksjonar for å senda og motta data til og frå perifere einingar.

---

<!-- slide template="[[tpl-quote]]" -->

![[Classic_shot_of_the_ENIAC.jpg]]

::: credit
[By Unidentified U.S. Army photographer](https://commons.wikimedia.org/w/index.php?curid=978770) Public Domain 
:::

note:
De første programmørene måtte kode programmet nøyaktig som prosessoren leser det, ikke som nuller og enere, men som elektrisitet som er enten av eller på, ved hjelp av brytere og koblingsbrett.
Bildet viser ENIAC som er regnet som den første generelle, programmerbare, elektroniske datamaskinen, og som kom i drift i 1945.

*original:*
Dei fyrste programmørane måtte koda programmet nøyaktig som prosessoren les det, ikkje som nullar og einarar, men som elektrisitet som er anten av eller på, ved hjelp av brytarar og koblingsbrett. Biletet viser ENIAC som er rekna som den fyrste generelle, programmerbare, elektroniske datamaskina, og som kom i drift i 1945.

---

- **1947/49** Assembler-språk
- **1957** Fortran
- **1958** LISP
- **1962** Simula
- **1972** C
- **1980** C++
- **1991** Python
- **1993** R
- **1995** Java
- **2000** C\#
- **2002** Scratch

note:
For å gjøre programmeringen enklere, har vi utviklet ulike programmeringssprog.
Andre generasjon programmeringssprog kom allerede på 1940-talet og er kjent som *assembler*-sprog.
Der bruker man nøyaktig de samme primitive instruksjonene som CPU-en bruker, men man kan definere variabler og subrutiner, i stedet for å måtte referere til minne- og registeradresser.

En av de største nyvinningene i tredje generasjon-sprogene som kom fra slutten av 1950-talet var å gjøre dem mer uavhengige av prosessorarkitekturen. Ulike mikroprosessorer har ikke det samme instruksjnonssettet, og et *assembly*-program kan bare brukes på den maskintypen det er skrevet for.

Der finnes tusenvis av programmeringssprog, som er mer eller mindre utbredd, og mer eller mindre egnet til ulike oppgaver.
Utviklingen handler i stor grad om å gjøre det enklere å håndtere komplekse problem, sammensatte programmer og store datastrukturer. Fjerde generasjon-sprog er gjerne tilpasset spesifikke anvendelsesdomener.

Python, som først kom i 1991, er et tredjegenerasjonsprog.
Det blir brukt til alle slags oppgaver, men det er særlig populært fordi det gir tilgang til gode og gratis bibliotek til numerisk analyse, statistikk og maskinlæring. 

*original:*
For å gjera programmeringa enklare, har me utvikla programmeringsspråk. Andre generasjon programmeringsspråk kom allereie på 1940-talet og er kjent som *assembler*-språk.  Der bruker ein nøyaktig dei same primitive instruksjonane som CPU-en bruker, men ein kan definera variablar og subrutinar.

Ein av dei største nyvinningane i tredje generasjon-språka som kom frå slutten av 1950-talet var å gjera dei uavhengige av prosessorarkitekturen. Ulike mikroprosessorar har ikkje det same instruksjnonssettet, og eit *assembly*-program kan berre brukast på den maskintypen det er skrive for.

Der finst tusenvis av programmeringsspråk, som er meir eller mindre utbreidde, og meir eller mindre egna til ulike oppgåver. Utviklinga handlar i stor grad om å gjera det enklare å handtera komplekse problem og datastrukturar. Fjerde generasjon-språk er gjerne tilpassa spesifikke anvendingsdomene.

Python, som kom i 1991, er eit tredjegenerasjonspråk. Det vert brukt til alle slags oppgåver, men det er særleg populært fordi det gjev tilgang til gode og gratis bibliotek til numerisk analyse, statistikk og maskinlæring. 

Sjølv om me stadig får nye programmeringsspråk treng CPUen stadig den same maskinkoden. Når me skriv eit program i python, bruker me eit anna program, kalt ein *interpreter* eller *tolk*, som les programmet og omset det til maskinkode.  Jupyter Notebook bruker ein sokalla *kernel* til denne tolkejobben, og der finst *kernels* for andre språk en *python*.

---

<!-- slide bg="white" -->

<!-- slide template="[[tpl-diagram]]" -->

![[state.svg|900]]

::: credit
:::


note:
En instruksjon som *print* er i virkeligheten uhyre komplisert.
Tallverdier må oversettes til tegnstrenger.
Adressen tl terminalen må finnes.
Hvert tegn må kopieres fra registeret til riktig posisjon på terminalen.
Feil kan oppstå og må håndteres fornuftig når det skjer. 
Det er godt vi har tredjgegenerasjonssprog så vi slipper å tenke på alle disse detaljene selv.

Det grunnleggende prinsippet er likevel det samme som Turing og von Neumann la til grunn for tre mannsaldre sidan.
Gjennom programmet gir vi imperativer til CPUen, som utfører ordren avhengig av tilstanden sin.
Noen instruksjoner oppdaterer variabler i tilstanden.
Andre kommuniserer med verden utenfor maskinen.
CPUen har òg en programpeiker som viser til neste instruksjon i programmet.
Normalt går pekeren frå en linje til neste, men ikke alltid.
I *for*-løkken kan hopper pekere tilbake til starten av løkken for å gjenta de samme kodelinjene med en ny tilstand.

Denne samme modellen ligger til grunn for all imperativ programmering.
Det som gjør programmering krevende, er at programmøren må kunne forutsi hva som skjer på CPUen, og ikke minst hvilken tilstand maskinen kan ende opp i.
Det er lett å overse mulige tilstander, og skrive programmet slik at det bare virker i de vanligste situasjonene.

*original:*
Ein instruksjon som *print* er i verkelegheita uhyre komplisert. Talverdiar må omsetjasts til teiknstrengar.  Adressa til terminalen må finnast. Kvart teikn må kopierast frå registeret til terminalen. Feil kan oppstå og må evt. handterast. Det er godt me har tredjegenerasjonsspråk so me slepp å tenkja på desse detaljane.

Det grunnleggjande prinsippet er likevel det same som Turing og von Neumann la til grunn for tre mannsaldrar sidan.  Gjennom programmet gjev me imperativar til CPUen, som utfører ordren avhengig av tilstanden sin. Somme instruksjonar oppdaterar variablar i tilstanden. Somme instruksjonar kommuniserer med verda utanfor maskina.  CPUen har òg ein programpeikar som viser til neste instruksjon i programmet. Normalt går peikaren frå ei line til neste, men ikkje alltid. I *for*-løkka kan peikaren hoppa tilbake for å gjenta linene i løkka.

Denne same modellen ligg til grunn for all imperativ programmering. Det som gjer programmering krevjande, er at programmøren må kunna forutseia kva som skjer på CPUen, og ikkje minst kva tilstand maskina kan enda opp i.  Det er lett å oversjå moglege tilstandar, og skriva programmet slik at det berre verkar dei vanlegaste situasjonane.

---

# Slutt

note:
Jeg håper at dette konseptuelle overblikket er nyttig når dere setter
dere ned for å programmere, men vi skal ikke dvele ved det.
Det er først når dere kjenner at dere har kontroll med hva maskinen 
gjør at dere vet at dere har forstått det.
