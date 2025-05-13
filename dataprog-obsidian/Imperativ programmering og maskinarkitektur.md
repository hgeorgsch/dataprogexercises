---
tags:
  - lecture/video
---

# Imperativ programmering

note: Der er mange måtar å programmera ei datamaskin på. Det paradigmet som ligg til grunn for dette kurset er *imperativ* programmering. Det er det mest kjende paradigmet, men ikkje det einaste.

Me skal prata litt om korleis datamaskina konseptuelt sett verkar. Målet er litt betre innblikk i korleis me tenkjer når me bruker Python til å instruera datamaskina.

---

![[command.webp|600]]

- [ ] Figur: Lisens på *clipart*

note:
Me kaller det for imperativ programmering, fordi me gjev maskina kommandoar, dvs. setningar i grammatisk imperativ.  

Maskina tenkjer ikkje. Det er programmøren som står for all tenkinga. Maskina gjer nøyaktig som kommandert, og programmøren må sjå for seg kva kvar kommando fører til.

---


```python=
b = 5
print(b)
```

note:
Imperativen er tydelag når me skriv t.d. *print* i python. Maskina prentar som ho får beskjed om. Den fyrste lina i koden her er òg ein imperativ, som som me lyt lesa som «lat $b$ vera lik 5». 

Dette skapar ei *tilstandsmaskin*, dvs. ei maskin som til i ein bestemt tilstand til ei kvar tid, og denne tilstanden kan endra seg for kvar instruksjon.  Her er det variabelen `b` som utgjer tilstandsrommet. Før line 1 er `b` i ein udefintert tilstand og etterpå er han i tilstanden 5.

---

```python=
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

Instruksjonane er typisk enkle aritmetiske og logiske operasjonar, som pluss, minus, og, og eller, samt instruksjonar for å hoppa i programmet eller lesa og skriva til minnet eller til eksterne einingar som skjerm og tastatur.

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

---
# Kontrollflyt i python

note: 
Eg håper du har høyrd føredraget om  «Imperativ programmering», og at du har arbeidd gjennom nokre enkle demonstrasjonar og øvingar i python. No skal eg gå litt nærare inn i struktur og syntaks i python.

---

## Tilordning 

```
variabel = 5
```

```
variabel2 = variabel**2 + 17
variabel3 = variabel2 - 2*variabel
variabel3 = variabel2/2
```
<!-- element class="fragment" -->

note:
Noko av det mest grunnleggjande er variablar som me kan tilordna ein verdi med likheitsteiknet. Om variabelen ikkje var definert i utgangspunktet, vert han oppretta når han vert tilordna.

(fragment)
Me har òg tilgang til alle dei vanlege aritmetiske operasjonane.

---
## Datatypar

```
heiltal = 5
flyttal = 5.0
tekst = "Fem"
liste = [ 3, 4, 5, 6, 7 ]
```


```
In [2]: type(variabel)
Out[2]: int

In [3]: type(flyttal)
Out[3]: float

In [4]: type(tekst)
Out[4]: str

In [5]: type(liste)
Out[5]: list
```
<!-- element class="fragment" -->

note:
Variablar kjem i forskjellige typar. Nokon av dei vanlegaste typane er heiltal, flyttal, teiknstreng og liste. Me treng ikkje fortelja python kva type me vil ha; det finn python ut av, men me kan sjekka kva type ein variabel har fått , med `type`- funksjonen.

---

## Samansette datatypar

```
liste = [ 3, 4, 5, 6, 7 ]
print(liste[2])
print(type(liste[2]))
```

```
tekst = "Fem"
print(tekst[2])
print(type(tekst[2]))
```
<!-- element class="fragment" -->

note:
Liste er ein samansett type, som består av fleire element av ein annan type. Me kan henta ut eitt element i lista med klammenotasjon.  Elementa er indeksert frå null, so `liste[2]` gjev det tredje elementet.

(fragment)
Det same gjeld teiknstrengar, sjølv om her har elementa same type.  Python skil ikkje mellom einskildteikn og strengar av fleire teikn.

---
## Bolske uttrykk  og *if*

```
b = 5
if b > 5: 
   print( "b er stor" )
   b = 0
print( "Denne lina vert køyrd uansett" )   
```

note:
Det andre fundamentale konseptet ved sidan av variablar, er kontrollflyt, der ulike delar av programmet vert køyrd, avhengig av tilstanden. Det enklaste dømet er *if*.

(illustrasjon)
Kolonet på slutten av *if*-lina innleier ein *blokk* som er indentert i forhold til koden før og etter. Heile blokken vert køyrd om vilkåret for *if* er sant. Det er viktig at denne indenteringa er konsistent.

(illustrasjon)
Vilkåret er eit bolsk uttrykk, dvs. ei utsegn som kan vera anten sann eller usann.

---

## *if*-*else*

```
b = 5
if b > 5: 
   print( "b er stor" )
   b = 0
else:
   print( "b er liten" )
   b = 10
```

note:
Når me har *if* kan me òg ha *else*, som innleier ein blokk med kolon, på same måte som *if*. Denne *else*-blokken vert køyrd når *if*-blokken ikkje vert køyrd, og vise versa.
	
---

## Bolske uttrykk og variablar

```
In [13]: b = 5
    ...: test = b > 5

In [14]: print(type(test))
<class 'bool'>

In [15]: print(test)
False
```

```
if b == 5:
   print ( "Fem" )
b = b == 5
```
<!-- element class="fragment" -->

note:
Det bolske uttrykket er ein eigen datatype. Me kan faktisk ta det bolske uttrykket og tilordna det til ein variabel. Då kan me òg sjå at datatypen er `bool`, altso bolsk, og verdien er usann eller *False*.

(fragment)
Då kan me òg merka oss bruken av likheitsteikn, som kan vera vanskeleg å forstå både i matematikken og i programmering, fordi det vert brukt i mange ulike tydingar.  Når me skriv tilordninga `b = 5` tyder likheitsteiknet *ikkje* at b er lik 5, men at me *skal la $b$ det verta* 5. Når me skal laga eit boolsk uttrykk med likskap, bruker me dobbelt likheitsteikn.  Det gjev utsegna $b$ er lik 5 som kan vera sann eller usann.

---
## Kontrollflyt 

```
b = 0
while b < 9: 
   print( "No er b lik", b )
```

```
for b in range(9): 
   print( "No er b lik", b )
```
<!-- element class="fragment" -->

note:
Når me bruker *if* vert blokken køyrd høgst éin gong. Tilsvarande har me *while* som køyrer blokken om att so lenge vilkåret er sant. Det kan vera null, ein, eller mange gongar. Om utsegna aldri vert usann, vil programmet aldri stoppa.

*while* er eit døme på ei løkke, dvs. ein gjentakande blokk.  Om me vil at løkka skal køyra eit visst antal omgongar, er det betre å bruka *for*.  Legg merke til at *for* gjev opphav til ein variabel som vert tilordna. I dømet vert $b$ tilordna 0 fyrste gongen, og so 1 og 2 og so vidare opp til 8.  Legg merke til at alle blokkar vert innleidd med kolon.

---

## Funksjonar

```
def funksjon():
   print( "Dette er funksjonen" )

funksjon()
print( "Dette er noko anna" )
funksjon()
```

note:
Eit anna viktig døme på blokkar er funksjonen. Når me definerer funksjonen med *def* får kodeblokken eit namn, men han vert ikkje køyrd då.

Han vert i staden køyrd når funksjonen vert kalt.  Me kan kalla den same funksjonen mange gongar.

Der er to viktige grunnar for å laga funksjonar.  Det eine er å unngå unødig gjentaking av kode. Det andre er for å skilja ut blokkar som har ein veldefinert oppgåve, for at koden skal vera enklare å lesa.

---

## Funksjonar med returverdi

```
def f(b):
   print( f"Eg fekk {b} inn. No reknar eg" )
   return b**2 + 2*b - 5
print( f(b))   
print( type(f(b)))   
```

note:
I matematikken er me vane med at funksjonar tek ein verdi inn og gjev ein verdi ut. Det kan dei òg gjera i python. Då definerer med parameter i parantensen, ($b$ i dømet), som fungerer som ein variabel inne i funksjonen.  Det er ikkje rekna som god skikk å tilordne nye verdiar til parametrane, men det er mogleg.

*return*-lina avsluttar funksjonen og spesifiserer returverdien.  No kan me bruka funksjonen i uttrykk på same måte som variablar eller konstante tal og teiknstrengar.

---

## *None*-typen

```
In [21]: def foobar():
    ...:     print( "Eg heiter foobar." )
    ...: 

In [22]: print( foobar() )
Eg heiter foobar.
None

In [23]: print( type(foobar()) )
Eg heiter foobar.
<class 'NoneType'>
```

note:
Teknisk sett har me ein retur-verdi sjølv om der ikkje er nokon `return`-line, men då er returverdien `None` av `NoneType`-typen.  Denne *None*-typen vert ofte brukt i variablar når riktig verdi er ukjend eller utilgjengeleg.

---

## Lokale og globale variablar

```
b = 5
print ( f"b={b}" )
def g():
   b = 7
   print ( f"b={b}" )

print ( f"b={b}" )
```

note:
Merk at variablar som vert definert eller tilordna inne i funksjonen, ikkje er synlege utanfor. Me seier at funksjonen har sitt eige *scope*.  Dette gjer det mogleg å bruka funksjonar som andre har skrive, utan å risikera at tilstanden i programmet vert endra utan at det er synleg. Me bruker parameter og returverdi for å utveksla data med funksjonskoden.

---

# Lukke til med øvingane

note: 
Ingen lærer å programmera ved å høyra på forklaringar. Den einaste måten er å prøva seg fram, studera døme, og bruka programmering på eigne problem. Det einaste eg har freista på her er å peika på nokre kjerneelement, for at dei skal vera lettare å kjenna igjen i praksis. Eg håper det hjelper når du går i gang med øvingane, men om det ikkje gjer det, so treng du heller ikkje hugsa det.

Lukke til.