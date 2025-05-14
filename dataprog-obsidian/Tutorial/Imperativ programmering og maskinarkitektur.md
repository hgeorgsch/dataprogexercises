---
tags:
  - lecture/video
---

# Imperativ programmering

note: Der er mange måtar å programmera ei datamaskin på. Det paradigmet som ligg til grunn for dette kurset er *imperativ* programmering. Det er det mest kjende paradigmet, men ikkje det einaste.

Me skal prata litt om korleis datamaskina konseptuelt sett verkar. Målet er litt betre innblikk i korleis me tenkjer når me bruker Python til å instruera datamaskina.

---

![[command-DALLE.webp]]

![[export/Imperativ programmering og maskinarkitektur/assets/command.webp]]

- [x] Figur: Lisens på *clipart* ✅ 2025-05-14
- [x] Kan genere med feks DALL-E (command-DALLE.webp, command-DALLE-alt.webp) ✅ 2025-05-14
- [ ] Kan DALL-E o.l ta imot et fargekart vi bruker i digital profil / brand?
- [ ] Inkluder grafikk frå DALL-E

note:
Me kaller det for imperativ programmering, fordi me gjev maskina kommandoar, dvs. setningar i grammatisk imperativ.  

Maskina tenkjer ikkje. Det er programmøren som står for all tenkinga. Maskina gjer nøyaktig som kommandert, og programmøren må sjå for seg kva kvar kommando fører til.

---


```python
b = 5
print(b)
```

note:
Imperativen er tydelag når me skriv t.d. *print* i python. Maskina prentar som ho får beskjed om. Den fyrste lina i koden her er òg ein imperativ, som som me lyt lesa som «lat $b$ vera lik 5». 

Eit kritisk kjenneteikn i imperativ programmering er *tilstand* . Tilordning `b=5` endrar tilstand på maskina. Før line 1 er `b`uderfinert, når me kjem til line 2 har `b` ein verdi, 5, og altso ein annan tilstand. Resultatet av *print* i line 2 avheng heilt openbert av kva tilstand maskina har.

- [x] Her skulle det kanskje vært en slide om hva vi mener med en tilstandsmaskin før det ses på mer ved turingmaskina? ✅ 2025-05-14

---

```python
b = 5
print(b)
b = 10
print(b)
```

note:
Tilstanden vert enno tydlegare i dette dømet.  Dei to *print*-linene er identiske, men dei gjev ikkje same resultat, fordi *tilstaden* åt maskina er forskjellig. Fyrste gongen har `b` tilstanden 5, og *print* skriv ut 5. Andre gongen er tilstanden 10, og det er 10 som vert skrive ut.

---

<split even>
::: block
![[Alan_Turing_(1951).jpg|400]]

Alan Turing 1951 ([by Elliott & Fry](https://www.computerhistory.org/timeline/1949/) Public Domain)
:::


::: block
![[Alonzo_Church.jpg|400]]

Alonzo Church
([By Princeton University, Fair use](https://en.wikipedia.org/w/index.php?curid=6082269))
:::

</split>

note: Teorien for datamaskiner og programmering vart hovudsakleg utarbeidd på 1930-talet, om lag ti år før ein fyrst bygde maskiner som faktisk kunne køyra programma. Church og Turing definterte kvart sitt paradigme. Dei er ekvivalente i den forstand at dei kan *oppnå* det same, sjølv om ein tenkjer forskjellig.

Turingmaskina er den mest kjende modellen, og den som ligg til grunn for imperativ programmering, der me kommanderer maskina og seier nøyaktig hva ho skal gjera.  Church sin $\lambda$-kalkyle ligg til grunn for det som me i dag kaller *funksjonell programmering*, der me definerer kva eigenskaper resultatet av programmer skal ha, utan å seia korleis ein oppnår det.

Båe modellane var abstrakte matematiske konsept, men det er Turing sin modell som best svarer til dei elektroniske maskinene som ein tok til å byggja utover 1940-talet.  Imperativ programmering er stadig det dominerande tankesettet, og difor det som me vil bruka tid på her.

---
## Turingmaskina

![[Turing_Machine_Model_Davey_2012.jpg|600]]

Turing Machine, reconstructed by Mike Davey as seen at Go Ask ALICE at Harvard University ([Rocky Acosta](https://commons.wikimedia.org/wiki/User:Arttechlaw "User:Arttechlaw") - Own work)

note: 
Turingmaskina er som sagt ein abstrakt og matematisk modell. Biletet viser ein rekonstruert modell. 

Maskina har eit papirband som er rulla opp på to spoler som kan dra bandet att og fram gjennom lesehodet i midten. Papirbandet er minnet i maskina og delt i diskrete posisjonar der kvar posisjon kan innehalad eitt teikn.

Turingmaskina er ei *tilstandsmaskin*.  Dvs. til ei kvar tid er maskina i ei bestemt tilstand. Det som maskina gjer avheng både av tilstanda og kva som står på bandet. 

---

<!-- slide bg="white" -->

![[turinginstruction.svg|600]]

note:
På kvart tidssteg ser maskina tilstanden sin og eitt teikn på bandet. Dette avgjer både den nye tilstanden og kva teikn som vert skrive til bandet. I tillegg kan bandet flytta eit steg til høgre eller venstre. Turingmaskina har ein fast oppslagstabell, som gjev resultatet for ein gjeven tilstand og eit gjeve teikn på bandet. Same tilstand og teikn gjev *alltid* same resultat.

Denne maskina er sjølvsagt absurd enkel.  Ho må òg vera uhyrleg treig sidan det tek lang tid å leita gjennom bandet. Likevel viser Turing at ho i prinsippet kan løysa mange komplekse problem.  

Alt me treng er eit minne som me kan bla igjennom og ein operasjon som verkar på to inputtverdiar, tilstanden og verdien fra bandet.

---

<!-- slide bg="white" -->
## von Neumann-arkitekturen

![[neumann.svg|1200]]

note:
Desse elementa kjenner me igjen i  John von Neumann sin arkitektur frå 1945, som har vorte førande for den praktiske konstruksjonen av datamaskiner.

Papirremsa er vorte til *Random Access Memory*, eller RAM. *Random Access* tyder at maskina kan lesa og skriva til ein kvan posisjon, utan å bruka tid på å leita langs remsa.

Sjølve prosesseringseininga er vorten meir kompleks. Kontrolleininga held styr på programmet og kva instruksjon den logiske og aritmetiske eininga skal utføra neste gong.  Tilstanden er ikkje lenger éin atomær verdi, men fleire register der kvart register inneheld ein verdi.

Instruksjonane er typisk enkle aritmetiske og logiske operasjonar, som pluss, minus, og, og eller, samt instruksjonar for å hoppa i programmet eller lesa og skriva til minnet.

I tillegg er maskina kobla til det me gjerne kaller *perifere einingar*, eller *input/output devices* i figuren. Det omfatter skjerm, for *output*, og tastatur for *input*, men kan òg vera nettverksgrensesnitt eller harddisk. Du la kanskje merke til at turingmaskina ikkje hadde nokon mekanisme for å kommunisera med omverda. I praksis må den logiske eininga ha instruksjonar for å senda og motta data til og frå perifere einingar.

- [x] Kanskje noen ord om hva input/output device er ✅ 2025-05-14

---

![[Classic_shot_of_the_ENIAC.jpg]]

[By Unidentified U.S. Army photographer](https://commons.wikimedia.org/w/index.php?curid=978770) Public Domain 

note:
Dei fyrste programmørane måtte koda programmet nøyaktig som prosessoren les det, ikkje som nullar og einarar, men som elektrisitet som er anten av eller på, ved hjelp av brytarar og koblingsbrett. Biletet viser ENIAC som er rekna som den fyrste generelle, programmerbare, elektroniske datamaskina, og som kom i drift i 1945.

---

- **ca. 1947/49** Assembler-språk
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
For å gjera programmeringa enklare, har me utvikla programmeringsspråk. Andre generasjon programmeringsspråk kom allereie på 1940-talet og er kjent som *assembler*-språk.  Der bruker ein nøyaktig dei same primitive instruksjonane som CPU-en bruker, men ein kan definera variablar og subrutinar.

Ein av dei største nyvinningane i tredje generasjon-språka som kom frå slutten av 1950-talet var å gjera dei uavhengige av prosessorarkitekturen. Ulike mikroprosessorar har ikkje det same instruksjnonssettet, og eit *assembly*-program kan berre brukast på den maskintypen det er skrive for.

Der finst tusenvis av programmeringsspråk, som er meir eller mindre utbreidde, og meir eller mindre egna til ulike oppgåver. Utviklinga handlar i stor grad om å gjera det enklare å handtera komplekse problem og datastrukturar. Fjerde generasjon-språk er gjerne tilpassa spesifikke anvendingsdomene.

Python, som kom i 1991, er eit tredjegenerasjonspråk. Det vert brukt til alle slags oppgåver, men det er særleg populært fordi det gjev tilgang til gode og gratis bibliotek til numerisk analyse, statistikk og maskinlæring. 

Sjølv om me stadig får nye programmeringsspråk treng CPUen stadig den same maskinkoden. Når me skriv eit program i python, bruker me eit anna program, kalt ein *interpreter* eller *tolk*, som les programmet og omset det til maskinkode.  Jupyter Notebook bruker ein sokalla *kernel* til denne tolkejobben, og der finst *kernels* for andre språk en *python*.

---

<!-- slide bg="white" -->

![[state.svg|900]]


note:
Ein instruksjon som *print* er i verkelegheit uhyre komplisert. Talverdiar må omsetjasts til teiknstrengar.  Adressa til terminalen må finnast. Kvart teikn må kopierast frå registeret til terminalen. Feil kan oppstå og må evt. handterast. Det er godt me har tredjegenerasjonsspråk so me slepp å tenkja på desse detaljane.

Det grunnleggjande prinsippet er likevel det same som Turing og von Neumann la til grunn for tre mannsaldrar sidan.  Gjennom programmet gjev me imperativar til CPUen, som utfører ordren avhengig av tilstanden sin. Somme instruksjonar oppdaterar variablar i tilstanden. Somme instruksjonar kommuniserer med verda utanfor maskina.  CPUen har òg ein programpeikar som viser til neste instruksjon i programmet. Normalt går peikaren frå ei line til neste, men ikkje alltid. I *for*-løkka kan peikaren hoppa tilbake for å gjenta linene i løkka.

Denne same modellen ligg til grunn for all imperativ programmering. Det som gjer programmering krevjande, er at programmøren må kunna forutseia kva som skjer på CPUen, og ikkje minst kva tilstand maskina kan enda opp i.  Det er lett å oversjå moglege tilstandar, og skriva programmet slik at det berre verkar dei vanlegaste situasjonane.

