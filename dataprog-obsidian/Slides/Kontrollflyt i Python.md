---
tags:
  - lecture/perspective
---

# Kontrollflyt i python

note: 
Jeg håper du har hørt foredraget om  «Imperativ programmering», og at du har arbeidet gjennom noen enkle demonstrasjoner og øvelser i python.
Her skal jeg gå litt nærmere inn i struktur og syntaks i python.

*original:*
Eg håper du har høyrd føredraget om  «Imperativ programmering», og at du har arbeidd gjennom nokre enkle demonstrasjonar og øvingar i python. No skal eg gå litt nærare inn i struktur og syntaks i python.

---

## Demo

1. Finn vevside
2. Velg sprog 
3. Vis bunnen av siden
4. Tast eller lim inn kode


note:
For å kunne se hva som skjer under panseret, skal vi bruke et verktøy som heter *Python Tutor*.
Det er gratis tilgjengelig, så du kan bruke det selv òg, hvis du vil.

1. Vevsiden heter `pythontutor.org`
2. Selv om det heter *Python Tutor*, støttes flere sprog.  Vi velger python.
3. Nederst på siden er en KI-assistent.  Den har ikke jeg prøvd, men det overlater jeg til dere.

Det vi skal gjøre her er å se hvordan *tilstanden* i maskinen endres mens programmet kjører linje for linje.
Dette kan vi gjøre med et verktøy som gjerne kalles *debugger*; der finnes også en *debugger* i Jupyter lab.
*Python Tutor* fungerer litt bedre når vi ønsker å stoppe for hver eneste linje, som vi gjerne gjør når
vi er helt ferske og programmene små.  Vanlige *debuggers* er bedre egnet med litt mer erfaring og litt større
programmer.

4. Vi finner boksen hvor vi kan skrive inn vår egen kode.
5. Vi trykker «Visualize Execution» for å se hva som skjer.


---

## Tilordning 

```
variabel = 5
print( "Variabelen har verdien", variabel )
variabel2 = variabel**2 + 17
variabel3 = variabel2 - 2*variabel
variabel3 = variabel2/2
```

note:
Noe av det mest grunnleggende i imperativ programmering er variabler som vi kan tilordne verdier med likhetstegnet.
Om variabelen ikke er definert i utgangspunktet, blir han opprettet når han blir tilordnet en verdi.
I *Python Tutor* kan vi observere tilstanden med alle de variabler som er definerte til en hver tid.
Vi kan kjøre programmet én linje ad gangen.
Den røde pilen er «program counter» og viser hvilken linje som skal kjøres neste gang.

Når vi trykker «Next» ser vi hva som skjer.  
Vi får en boks som heter «Global frame».
Det er tilstanden til maskinen.
Variabelen `variabel` er blitt en del av tilstanden.

Vi kan fortsette å trykke *next*.
Den grønne pilen viser hva som nettopp er kjørt og den røde viser neste linje.
Når programmet laver *output* ser vi det øverst til høyre.

Hver gang vi tilordner en ny variabel, dukker den opp i *global frame*.
Vi huske selvsagt at vi kan bruke alle slag aritmetiske uttrykk på høyre side i tilordningen.

(vurdering)
+ Bør vi ha hele kodeeksempelet klart på starten?  
+ Klipp og lim hele kodesnutten samlet?
+ Skrive linje for linje?
+ Mulig å starte med linje 1-2, og legge til linje 3-5 før siste avsnitt


---

## Datatypar

```
heiltal = 5
print( type( heiltal ) )
flyttal = 5.0
print( type( flyttal ) )
tekst = "Fem"
print( type( tekst ) )
liste = [ 3, 4, 5, 6, 7 ]
print( type( liste ) )
typ = type( liste )
print( type( typ ) )
```


note:
Verdier kommer i forskjellige typer; *datatyper*.
Noen av de vanligste typene er heltall, flyttall, tegnstreng og liste.
Vi trenger ikke fortelle python hvilken type vi vil ha; det finner den ut av selv, men vi kan sjekke hva slags type en variabel har fått, med `type`-funksjonen.

Det er verd å være bevisst på.  Det skjer ikke sjelden at programmer ikke virker fordi en variabel plutselig har feil datatype.

Merk at typen òg er en verdi, av type *type*, som vi kan bruke som alle andre verdier og f.eks. tilordne til en variabel.
Dermed er det mulig å teste hvilken type variabelen har, om du skulle trenge det.

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
g()
print ( f"b={b}" )
```

note:
Merk at variablar som vert definert eller tilordna inne i funksjonen, ikkje er synlege utanfor. Me seier at funksjonen har sitt eige *scope*.  Dette gjer det mogleg å bruka funksjonar som andre har skrive, utan å risikera at tilstanden i programmet vert endra utan at det er synleg. Me bruker parameter og returverdi for å utveksla data med funksjonskoden.

---

# Lukke til med øvingane

note: 
Ingen lærer å programmere ved å høre på forklaringer.
Den eneste måten er å prøve seg frem, studere eksempler, og bruke programmering på egne problemer.
Det eneste jeg har forsøkt å oppnå her er å peke på *noen* kjerneelementer, for at det skal være lettere å kjenne dem igjen i praksis.
Jeg håper det hjelper når du går i gang med øvelsene, men om det ikke gjær det, så trenger du heller ikke huske det.

Lykke til!
