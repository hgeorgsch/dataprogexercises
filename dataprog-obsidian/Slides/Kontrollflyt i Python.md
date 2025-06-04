---
tags:
  - lecture/perspective
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
g()
print ( f"b={b}" )
```

note:
Merk at variablar som vert definert eller tilordna inne i funksjonen, ikkje er synlege utanfor. Me seier at funksjonen har sitt eige *scope*.  Dette gjer det mogleg å bruka funksjonar som andre har skrive, utan å risikera at tilstanden i programmet vert endra utan at det er synleg. Me bruker parameter og returverdi for å utveksla data med funksjonskoden.

---

# Lukke til med øvingane

note: 
Ingen lærer å programmera ved å høyra på forklaringar. Den einaste måten er å prøva seg fram, studera døme, og bruka programmering på eigne problem. Det einaste eg har freista på her er å peika på nokre kjerneelement, for at dei skal vera lettare å kjenna igjen i praksis. Eg håper det hjelper når du går i gang med øvingane, men om det ikkje gjer det, so treng du heller ikkje hugsa det.

Lukke til.
