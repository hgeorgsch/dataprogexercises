---
tags:
  - lecture/perspective
---

# Kontrollflyt i python


(ansikt) Jeg håper du har hørt foredraget om  «Imperativ programmering», og at du har arbeidet gjennom noen enkle demonstrasjoner og øvelser i python.
Her skal jeg gå litt nærmere inn i struktur og syntaks i python.

For å kunne se hva som skjer under panseret, skal vi bruke et verktøy som heter *Python Tutor*.
Det er gratis tilgjengelig, så du kan bruke det selv òg, hvis du vil.

(tutor)
1. Dette er en vevside: `pythontutor.com`
2. Selv om det heter *Python Tutor*, støttes flere sprog.  Vi velger python.
3. Nederst på siden er en KI-assistent.  Den har jeg ikke prøvd selv, så det blir opp til dere om dere vil prøve.
4. Midt på siden kan vi taste inn vår egen kode.

```
variabel = 5
print( "Variabelen har verdien", variabel )

variabel2 = variabel**2 + 17
variabel3 = variabel2 - 2*variabel
variabel3 = variabel2/2
```

(klipp)
(tutor)
1. Når vi har lagt inn kode, trykker vi «Visualize Execution» for å se hva som skjer.

(ansikt+kode)
*Python Tutor* lar oss overvåke tilstanden mens vi kjører programmet linje for linje.
 Verktøy som lar oss gjøre det, kalles gjerne for  *debuggers*. Der finnes også en *debugger* i Jupyter lab, men *Python Tutor* fungerer litt bedre når vi ønsker å stoppe for hver eneste linje, som vi gjerne gjør når vi er helt ferske og programmene små. Vanlige *debuggers* er bedre egnet med litt mer erfaring og litt større programmer.

(tutor)
1.  Noe av det mest grunnleggende i imperativ programmering er variabler som vi kan tilordne verdier med likhetstegnet.
2.  Om variabelen ikke er definert i utgangspunktet, blir han opprettet når han blir tilordnet en verdi.
3. Når vi kjører linje med «next», ser vi at varaibelen dukker opp i tilstanden Global Frame
4. Observerer tilastand med variabler definert til en hver tid.
5.  I tillegg til variablene har vi «program counter» 
6. Det vises som den røde pilen i koden, og marekrer nest linje som skal kjøre
7. Den grønne pilen viser hva som nettopp er kjørt 

(tutor)
1. Vi kan fortsette å trykke *next*.
2. Når programmet laver *output* ser vi det øverst til høyre.
3. Hver gang vi tilordner en ny variabel, dukker den opp i *global frame*.
4. Vi huske selvsagt at vi kan bruke alle slag aritmetiske uttrykk på høyre side i tilordningen.

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
print( typ, type( typ ) )
```


(tutor)
La oss ta et nytt eksempel.
«Edit Code»

(klipp)

(tutor)
«Visualize Code»

(kode+ansikt)
Variabler og verdier kommer i forskjellige typer; *datatyper*.
Noen av de vanligste typene er heltall, flyttall, tegnstreng og liste.

Vi trenger ikke fortelle python hvilken type vi vil ha; det finner den ut av selv, men vi kan sjekke hva slags type en variabel har fått, med `type`-funksjonen.

(tutor)
1. La oss se hva som skjer når vi trykker «Next».
2. Les type-navn

(kode+ansikt)
Det er verd å være bevisst på.  Det skjer ikke sjelden at programmer ikke virker fordi en variabel plutselig har feil datatype.

(tutor)
1. Merk at typen òg er en verdi, av type *type*, som vi kan bruke som alle andre verdier og f.eks. tilordne til en variabel.
2. Dermed er det mulig å teste hvilken type variabelen har, om du skulle trenge det.
3. La oss se litt nærmere på lister.
4. «Edit Code»

---

## Samansette datatypar

```
liste = [ 3, 4, 5, 6, 7 ]
B = liste
C = [ 3, 4, 5, 6, 7 ]

liste[2] = "X"

print(B[2], type(B[2]))
print(C[2], type(C[2]))
```

(klipp)

(tutor )
1. «Visualise Code»
2. «Next»
3. Når vi tilordnet en liste, viste *Python Tutor* den som et objekt ved siden av *Global Frame*.
4. Grunnen til det ser vi dersom vi tilordner den samme listen til flere variabelnavn.
5. Flere variabler kan peke på det samme objektet.
6. Vi sier gjerne at variabelen er en *peker* til objektet.

7. Liste er en sammensatt type, som gjør et vi kan manipulere innholdet i listen også.
8. Vi bruker klammeparenteser for å vise til en posisjon i listen.  
9. Når vi endrer verdien i `liste[2]`, er det innholdet i objektet som endres.
10. Endringen er synlig også via andre pekere til det samme objektet.
11. Vi kan også se at hvert element i listen er en verdi med sin egen type


---

## Bolske uttrykk  og *if*

```
b = 5
if b > 7: 
   print( "b er stor" )
   b = 0
print( "Denne lina vert køyrd uansett" )   
```
(klipp)

(kode+ansikt)
Det andre fundamentale konseptet ved siden av variablar, er kontrollflyt, der ulike delar av programmet blir kjørt, avhengig av tilstanden.
Det enkleste eksempelet er *if*.

(tutor)
1. Når vi kjører koden, ser vi at programpekeren hopper over linje 3 og 4, fordi `b > 7` er usann.
2. Den siste linjen står utenfor blokken og blir kjørt uansett.

(endring)
Hvis vi endrer verdien på `b`, kan *if*-blokken bli kjørt.

(annotering) Kolonet på slutten av *if*-lina innleder en *blokk* som er indentert i forhold til koden før og etter.
Hele blokken blir kjørt om vilkåret for *if* er sant. 

(annotering) Denne indenteringen må være konsistent, slik at python vet hvilke linjer som hører med til blokken, og hvilke som kommer efterpå.

(annotering) Vilkåret er et bolsk uttrykk, dvs. et utsagn som kan være enten sant eller usant.

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

(klipp)

(tutor) Når vi har *if* kan vi også ha *else*, som innleder en blokk med kolon, på samme måte som *if*.
Denne *else*-blokken blir kjørt når *if*-blokken ikke blir kjørt, og vise versa.
	
---

## Bolske uttrykk og variablar

```
a = 5
b = a > 5

t = type(b)

if a == 5:
   print ( "Fem" )
a = a == 5
```

(klipp)

(ansikt)
Det bolske uttrykket i *if*-satsen er en verdi på samme måte som tallverdier, strenger og lister.
Det har også sin egen datatype.
Vi kan faktisk ta det bolske uttrykket og tilordna det til en variabel.

(tutor)
1. Vi kan la a være lik 5
2. og b være lik «a > 5»
3. b dukker opp i global frame med verdien usann eller *False*.
4. Vi kan la t typen til b
5. Da ser vi at datatypen er `bool`,  som er en forkortelse for *Boolean* eller bolsk på norsk,

(ansikt)
1. Vi skal også merke oss bruken av likheitstegnet, som kan være vanskelig å forstå både i matematikken og i programmering, fordi det har flere ulike betydninger. 
2. Når vi skriver tilordningen `b = 5` betyr likhetstegnet *ikke* at b er lik 5, men at `b` skal *bli* lik 5. Det er altså en imperativ.

(tutor)
1. Når vi skal lave et bolsk uttrykk med likhet, bruker vi dobbelt likhetstegn.
2. Dét gir utsagnet at `a` er lik 5, som kan væra sant eller usant.

3. Så hva betyr da den siste linjen, `b` er lik `b` er lik 5?

4. Vi må se på tilordningen først, altså høyre og venstre side av det enkle likhetstegnet.  
5. (annotering) Høyresiden er et uttrykk, som her er et bolsk uttrykk med likhet,
6. og verdien av uttrykket havner i variabelen `b` som spesifisert på (annotering) venstre side.

---

## Løkker 

```
b = 0
while b < 9: 
   print( "No er b lik", b )

```

(klipp)

(tutor)
1. Med *if* blir blokken kjørt høyst én gang.
2. Tilsvarende har vi *while* som kjører blokken om igjen så lenge vilkåret er sant.
3. Det kan være null, én eller mange ganger.
4. Om utsagnet aldri blir usant, vil programmet aldri ta slutt.

La oss endre litt på programmet, slik at det terminerer.

(klipp)

```
b = 0
while b < 9: 
   print( "No er b lik", b )
   b = b + 2

```

(ansikt)
1. *while* er et eksempel på en løkke, dvs. en gjentagende blokk.
2. Løkker er helt kritiske i imperativ programmering,
3. enten vi skal bla gjennom rad for rad i et datasett, eller gjenta en simulering periode for periode.

---

## for 

```
for i in [ 0, 2, 4, 6, 8]:
   print( "No er i lik", i )

```

(klipp)

(tutor)
Hvis vi vil at løkken skal kjøre et bestemt antall omganger, er det som regel bedre å bruke *for*.
Legg merke til at *for* automatisk gir opphav til en variabel som blir tilordnet på starten av hver runde.

(annotering) Vi kan òg huske at alle blokker blir innledet med kolon, både for *if*, *while* og *for*.

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

(klipp)

(tutor)
1. En litt anden type blokk er funksjonen.
2. Når vi definerer funksjonen med *def* får kodeblokken et navn, som dukker opp i *Global Frame*.
3. Blokken blir derimot ikke kjørt.  Program counter hopper over hele blokken.
4. Koden efter blokken blir kjørt

5. Vi kaller funksjonen i linje 5, og da ser vi at programpekeren hopper inn i funksjonsblokken, som blir kjørt.
6. Funksjonen har sin egen *frame*, og det samme variabelnavnet kan ha ulik verdi i den globale og den lokale rammen.
7. Funksjonen kan ikke endre den globale tilstanden.

(ansikt)
Der er to viktige grunner for å lave funksjoner.
Det ene er å unngå unødig gjentagelse av kode.
Det andre er å gjøre koden enklere å lese ved å skille ut blokker som har sine veldefinerte oppgaver.

Programmer som er skrevet uten bruk av funksjoner blir rask uleselige, når de bikker 50-100 linjer.
Det lønner seg å tenke over hvilke oppgaver som er såpass veldefinerte at de kan skrives som en funksjon med et lettfattelig navn.

Funksjonen som vi nettopp så, skriver bare ut en streng på skjermen.
I matematikken er vi vant til at funksjonar tar en verdi inn og gir en verdi tilbake.
Det kan de også gjøre i python.
La oss ta et eksempel på det.


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

(klipp)

(tutor)
Vi definerer parameter i parantesen. 
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

(klipp)

(tutor)
1. Teknisk sett har vi en returverdi selv om der ikke er noen `return`-linje, men da er returverdien `None` av `NoneType`-typen.
2. Denne *None*-typen blir ofte brukt i variabler når riktig verdi er ukjent eller utilgjengelig.

3. Legg også merke til at funksjonen blir kjørt på nytt i den nestsiste linjen, fordi der er et eksplisitt kall.
4. I den siste linjen, selv om den på mange måter gjør det samme, bruker vi blott verdien av `r` uten å kjøre funksjonen på nytt.

---

# Lukke til med øvingane

(ansikt)
1. Ingen lærer å programmere ved å høre på forklaringer.
2. Den eneste måten er å prøve seg frem, studere eksempler, og bruke programmering på egne problemer.
3. Det eneste jeg har forsøkt å oppnå her er å peke på *noen* kjerneelementer, for at det skal være lettere å kjenne dem igjen i praksis.
4. Jeg håper det hjelper når du går i gang med øvelsene, men om det ikke gjør det, så er det kanskje heller ikke så viktig å huske.

Lykke til!
