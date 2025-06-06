---
tags:
  - lecture/perspective
---

# Kontrollflyt i python

note: 
Jeg håper du har hørt foredraget om  «Imperativ programmering», og at du har arbeidet gjennom noen enkle demonstrasjoner og øvelser i python.
Her skal jeg gå litt nærmere inn i struktur og syntaks i python.

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
3. Nederst på siden er en KI-assistent.  Den har jeg ikke prøvd selv, så det blir opp til dere om dere vil prøve.

Det vi skal gjøre her er å se hvordan *tilstanden* i maskinen endres mens programmet kjører linje for linje.
Verktøy som lar oss gjøre det, kalles gjerne for  *debuggers*.
Der finnes også en *debugger* i Jupyter lab, men *Python Tutor* fungerer litt bedre når vi ønsker å stoppe for hver eneste linje, som vi gjerne gjør når
vi er helt ferske og programmene små.
Vanlige *debuggers* er bedre egnet med litt mer erfaring og litt større
programmer.

4. Midt på siden er der en boks hvor vi kan skrive inn vår egen kode.
5. Når vi har lagt inn kode, trykker «Visualize Execution» for å se hva som skjer.


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
(vis kode)

Noe av det mest grunnleggende i imperativ programmering er variabler som vi kan tilordne verdier med likhetstegnet.
Om variabelen ikke er definert i utgangspunktet, blir han opprettet når han blir tilordnet en verdi.
I *Python Tutor* kan vi observere tilstanden med alle de variabler som er definerte til en hver tid.
Vi kan kjøre programmet én linje ad gangen.
Den røde pilen er «program counter» og viser hvilken linje som skal kjøres neste gang.

(vis tilstand)

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
flyttal = 5.0
tekst = "Fem"
liste = [ 3, 4, 5, 6, 7 ]

print( type( heiltal ) )
print( type( flyttal ) )
print( type( tekst ) )
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
B = liste
C = [ 3, 4, 5, 6, 7 ]

liste[2] = "X"

print(B[2])
print(type(B[2]))
```

note:
Når vi tilordnet en liste, viste *Python Tutor* den som et objekt ved siden av *Global Frame*.
Grunnen til det ser vi dersom vi tilordner den samme listen til flere variabelnavn.
Flere variabler kan peke på det samme objektet.
Vi sier gjerne at variabelen er en *peker* til objektet.

Liste er en sammensatt type, som gjør et vi kan manipulere innholdet i listen også.
Vi bruker klammeparenteser for å vise til en posisjon i listen.  
Når vi endrer verdien i `liste[2]`, er det innholdet i objektet som endres.
Endringen er synlig også via andre pekere til det samme objektet.


---

## Bolske uttrykk  og *if*

```
b = 5
if b > 7: 
   print( "b er stor" )
   b = 0
print( "Denne lina vert køyrd uansett" )   
```

note:
Det andre fundamentale konseptet ved siden av variablar, er kontrollflyt, der ulike delar av programmet blir kjørt, avhengig av tilstanden.
Det enkleste eksempelet er *if*.
Vi ser at programpekeren hopper over linje 3 og 4, fordi `b > 7` er usann.

(endring)
Hvis vi endrer verdien på `b`, kan *if*-blokken bli kjørt.

(annotering)
Kolonet på slutten av *if*-lina innleder en *blokk* som er indentert i forhold til koden før og etter.
Hele blokken blir kjørt om vilkåret for *if* er sant. 
Denne indenteringen må være konsistent, slik at python vet hvilke linjer som hører med til blokken, og hvilke som kommer efterpå.

(annotering)
Vilkåret er et bolsk uttrykk, dvs. et utsagn som kan være enten sant eller usant.

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
print( f"b={b}" )
```

note:
Når vi har *if* kan vi også ha *else*, som innleder en blokk med kolon, på samme måte som *if*.
Denne *else*-blokken blir kjørt når *if*-blokken ikke blir kjørt, og vise versa.
	
---

## Bolske uttrykk og variablar

```
b = 5
test = b > 5

typ = type(test)

if b == 5:
   print ( "Fem" )
b = b == 5
```

note:
Det bolske uttrykket er en egen datatype.
Vi kan faktisk ta det bolske uttrykket og tilordna det til en variabel.
Da ser vi òg at datatypen er `bool`, som er en forkortelse for *Boolean* eller bolsk på norsk, og verdien er usann eller *False*.

Vi skal også merke oss bruken av likheitstegnet, som kan være vanskelig å forstå både i matematikken og i programmering, fordi det har flere ulike betydninger. 
Når vi skriver tilordningen `b = 5` betyr likhetstegnet *ikke* at b er lik 5, men at `b` skal *bli* lik 5. Det er altså en imperativ.
Når vi skal lave et bolsk uttrykk med likhet, bruker vi dobbelt likhetstegn.
Dét gir utsagnet at `b` er lik 5, som kan væra sant eller usant.

Så hva betyr da den siste linjen, `b` er lik `b` er lik 5?

Vi må se på tilordningen først, altså høyre og venstre side av det enkle likhetstegnet.  
Høyresiden er et uttrykk, som her er et bolsk uttrykk med likhet, og verdien av uttrykket havner i variabelen `b` som spesifisert på venstre side.

---

## Løkker 

```
b = 0
while b < 9: 
   print( "No er b lik", b )

```

note:
Med *if* blir blokken kjørt høyst én gang.
Tilsvarende har vi *while* som kjører blokken om igjen så lenge vilkåret er sant.
Det kan være null, én eller mange ganger.
Om utsagnet aldri blir usant, vil programmet aldri ta slutt.

La oss endre litt på programmet, slik at det terminerer.

---

## Løkker 

```
b = 0
while b < 9: 
   print( "No er b lik", b )
   b = b + 2

```

note:
*while* er et eksempel på en løkke, dvs. en gjentagende blokk.

---

## for 

```
for i in [ 0, 2, 4, 6, 8]:
   print( "No er i lik", i )

```

note:
Hvis vi vil at løkken skal kjøre et bestemt antall omganger, er det som regel bedre å bruke *for*.
Legg merke til at *for* automatisk gir opphav til en variabel som blir tilordnet på starten av hver runde.

Vi kan òg huske at alle blokker blir innledet med kolon, både for *if*, *while* og *for*.

---

## Funksjoner

```
def funksjon():
   variabel = "Inne"
   print( f"Dette er funksjonen ({variabel})" )

variabel = "Ute"


funksjon()
print( f"Dette er noko anna ({variabel})" )
funksjon()
```

note:
En litt anden type blokk er funksjonen.
Når vi definerer funksjonen med *def* får kodeblokken et navn, som dukker opp i *Global Frame*.
Blokken blir derimot ikke kjørt.

Vi kaller funksjonen i linje 4, og da ser vi at programpekeren hopper inn i funksjonsblokken, som blir kjørt.
Funksjonen har sin egen *frame*, og det samme variabelnavnet kan ha ulik verdi i den globale og den lokale rammen.
Funksjonen kan ikke endre den globale tilstanden.

Der er to viktige grunner for å lave funksjoner.
Det ene er å unngå unødig gjentagelse av kode.
Det andre er å gjøre koden enklere å lese ved å skille ut blokker som har sine veldefinerte oppgaver.

---

## Funksjonar med returverdi

```
def f(b):
   print( f"Eg fekk {b} inn. No reknar eg" )
   return b**2 + 2*b - 5
r = f(b)
print( r )   
print( type(r))   
```

note:
I matematikken er vi vant til at funksjonar tar en verdi inn og gir en verdi tilbake.
Det kan de også gjøre i python.
Vi definerer parameter i parantensen. 
I eksempelet har vi parameteren `b` som fungerer som en variabel inne i funksjonen.  
Det er ikke god skikk å tilordne ny verdi til en parameter, men det er mulig å gjøre det.

*return*-linjen avslutter funksjonen og definerer returverdien.
Nu kan vi bruke funksjonen i uttrykk på samme måte som variabler eller konstante tall og tegnstrenger.

---

## *None*-typen

```
def foobar():
    print( "Eg heiter foobar." )

r = foobar()

print( type( foobar() ) )

print( type(r) )
```

note:
Teknisk sett har vi en returverdi selv om der ikke er noen `return`-linje, men da er returverdien `None` av `NoneType`-typen.
Denne *None*-typen blir ofte brukt i variabler når riktig verdi er ukjent eller utilgjengelig.

Legg også merke til at funksjonen blir kjørt på nytt i den nestsiste linjen, fordi der er et eksplisitt kall.
I den siste linjen, selv om den på mange måter gjør det samme, bruker vi blott verdien av `r` uten å kjøre funksjonen på nytt.

---

# Lukke til med øvingane

note: 
Ingen lærer å programmere ved å høre på forklaringer.
Den eneste måten er å prøve seg frem, studere eksempler, og bruke programmering på egne problemer.
Det eneste jeg har forsøkt å oppnå her er å peke på *noen* kjerneelementer, for at det skal være lettere å kjenne dem igjen i praksis.
Jeg håper det hjelper når du går i gang med øvelsene, men om det ikke gjør det, så er det kanskje heller ikke så viktig å huske.

Lykke til!
