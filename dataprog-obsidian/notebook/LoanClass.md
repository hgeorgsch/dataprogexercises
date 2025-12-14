---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  name: python3
  display_name: Python 3 (ipykernel)
  language: python
---

# Objektorientert lånekalkulator

Her skal me ta løysinga frå [](Simulering%20av%20kontantstraum) og
visa korleis me kan organisera lånekalkulatoren med klasser og objekt.
Me skal òg bruka typar for tid og dato frå [](Tid%20og%20dato).
Målet er å svara på spørsmålet
*kor raskt betaler ein ned eit bustadlån?*

Som eit døme kan me føresetja
- **Lånebeløp** 100000 kr
- **Rente** 4% årleg og etterskotvis
- **Gebyr** 100kr per år
- **Terminbeløp** 10000 kr per år (inkl. renter, gebyr og avdrag)

::: {admonition} Merknad
Ein kan sjølvsagt laga ein lånekalkulator like enkelt i eit rekneark.
Dersom du er dyktig med rekneark, må du akseptera at det tek tid før du
kan klara det same i python.
På den andre sida er det nytt om du kan sjå at utrkeningane som trengst
er dei same, uansett kva verkty du bruker.
:::

## Objekt og klasser

Klasser er ein teknikk for å samla fleire ulike definisjonar,
både variablar og funksjonar (metodar).
Me kan definera ei enkel klasse, med berre variablar, slik:

```{code-cell} ipython3
class SimpleLoan:
    interest = 0.04
    fee = 100
    payment = 10000
    balance = 100000
```

Ei **klasse** er ein datatype.  Når me bruker klassa, lagar med ein variabel
med typen.  Me seier at me instantierer typen.
Verdien av ei klassetype kaller me for eit **objekt**
For å instantiera typen bruker me klassenamnet som ein funksjon, med
parentesar, slik:

```{code-cell} ipython3
mydebt = SimpleLoan()
print( f"Eg skuldar {mydebt.balance} kr." )
print( f"Eg må betala {mydebt.balance*mydebt.interest} kr. i renter." )
```

Me kan endra variablane i objektet.
Ei rentenedgang kan me t.d. implementera slik.

```{code-cell} ipython3
mydebt.interest = 0.035
print( f"Eg skuldar {mydebt.balance} kr." )
print( f"Eg må betala {mydebt.balance*mydebt.interest} kr. i renter." )
```

::: {admonition} Refleksjon
Kva har endra seg i lånet over?
:::

::: {admonition} Oppgåve
Instantier eit nytt lån `newloan`.
Sjekk kva rentenivå det nye lånet får?
:::

::: {admonition} Merknad
Klassevariablane som er definert under `class` tener som initialverdiar
for objektvariablane som me kan definera på kvar instans.
:::

## Metodar 

Den fyrste klassa vår hadde berre variablar.
Me kunne like gjerne ha brukt ein `dict`.
Klasser kan òg ha funksjonar, som lèt oss samla typen og operasjonar
på typen på éin plass, slik at koden vert ryddigare.
Lat oss ta eit døme på metodar som oppdaterer og skriv ut saldoen
på lånet.

```{code-cell} ipython3
class AnnualLoan(SimpleLoan):
    interestamount = 0
    
    def endyear(self):
        self.interestamount = self.interest*self.balance
        self.oldbalance = self.balance
        self.balance += self.fee
        self.balance += self.interestamount
        self.balance -= self.payment
    def printstatement(self):
        repayment = self.payment - self.fee - self.interestamount
        print( "Gebyr:\t\t", self.fee )
        print( "Renter:\t\t", self.interestamount )
        print( "Nedbetaling:\t", repayment )
        print( "Ny saldo:\t", self.balance )
```

Det fyrste me skal leggja merke til her er notasjonen `AnnualLoan(SimpleLoan)`
i den fyrste lina.  Dette tyder at den nye klassa, `AnnualLoan`, skal
arva den eksisterende klassa, `SimpleLoan`.  Dvs. at alle eigenskapane
som vart definerte i `SimpleLoan` òg gjeld for `AnnualLoan` med mindre
dei vert redefinert der.

::: {admonition} Merknad
Arv er ein av dei viktigaste eigenskapane ved objektorientert programmering.
Det lèt oss definera klasser som liknar på kvarandre, utan å måtte gjenta
den koden som er lik.
:::

Funksjonar som er definert i ei klasse kaller me som regel **metodar**.
Me ser at dei er definert med `def` som andre funksjonar, men 
definisjonen står inni klassa (blokken).
Der er eit par ting som er spesielt med metodar.
Alle metodar treng ein parameter `self` som refererer til objektet som eig
metoden.
Denne parameteren skal ikkje vera med når me kaller metoden.
Lat oss sjå korleis me instantierer eit lån, sjekker saldo, oppdaterer
etter eitt år, og sjekker saldo igjen.

```{code-cell} ipython3
mydebt = AnnualLoan()
mydebt.printstatement()
mydebt.endyear()
mydebt.printstatement()
```

Metodane som er definerte i klassa vert eigenskapar ved instansen, slik at
me kan kalla metode frå objektet som `mydebt.endyear()`.
Det ser ut som om me har gløymt parameteren self, men det har me ikke.
Parameteren `self` får verdien `mydebt`, etter objektet som metoden vert
kalt frå.

Går me tilbake til definisjonen av `endyear()`, ser me korleis saldoen
(`balance`) vert oppdatert med gebyr, rente og innbetaling.
Tilsvarande vil `printstatement()` henta verdiar frå objektet (`self`)
og skriva dei ut.

Me kan halda fram og laga nedbetalingsplan fleire år fram i tid, t.d.:

```{code-cell} ipython3
for i in range(10):
    print( "År", i )
    mydebt.endyear()
    mydebt.printstatement()
    
```

Variablane i objektet (`balance` i dette tilfellet) dannar ein tilstand.
Objektet har til ein kvar tid ein bestemt tilstand, og metodane kan endra
denne tilstanden.

::: {admonition} Merknad
Som me har sett kan ein endra tilstanden ved å oppdatera objektvariablane
utan å bruka metodane i objektet, men dette er rekna som dårleg praksis.
Metodar som tek seg av tilstandsoppdatering kan òg sjekka for feil og sjå
til at tilstanden er konsistent.  Ved å la all oppdatering gå gjennom
utvalde metodar, er det enklare å unngå feil.
:::

## Konstruktøren

Det vil vera nyttig om låneobjekte kan hugsa transaksjonane og saldoen
år for år.  Dette krev litt omtanke.
Me kunne tenkja oss at me lagar ei klassevariabel `history` som me
instantierer med ei tom liste, der me legg til saldoen kvart år,
t.d. slik:

```{code-cell} ipython3
class AnnualLoan2(AnnualLoan):
    history = []

    def endyear(self):
        self.history.append( self.balance )
        self.interestamount = self.interest*self.balance
        self.oldbalance = self.balance
        self.balance += self.fee
        self.balance += self.interestamount
        self.balance -= self.payment
```

Denne klassa arvar `AnnualLoan` har dermed same `printstatement()`, men ho
har si eiga variant av `endyear()`, med éi ekstra line som oppdaterer
`self.history`.  
Lat oss testa dette.

```{code-cell} ipython3
loan1 = AnnualLoan2()
loan2 = AnnualLoan2()

print( "Lån 1", loan1.history )
print( "Lån 2", loan2.history )

loan1.endyear()
print( "Oppdatert lån 1" )

print( "Lån 1", loan1.history )
print( "Lån 2", loan2.history )
```

::: {admonition} Refleksjon
Kva er det som skjer her?  Skal verkeleg `loan1` og `loan2` ha same historikk?
:::

Me er nøydde til å skilja mellom klasse- og objektvariablar.
Ei variabel som er definert direkte i klassa, slik som me har gjort,
høyrer til klassa.
Når me gjer `self.history.append( ... )` oppdaterer båe objekta den
same klassevariabele.

Dette har ikkje vore noko problem før no.  Når me bruker tilordning, som i
`self.balance += self.fee` vert der oppretta ein *ny* variabel i objektet,
og denne vert brukt i staden for klassevariabelen. 

For å løysa dette problemet må me ha ein metode som opprettar objektvariabelen.
Der er ein spesiell metode som vert køyrd når objektet vert instantiert.
Denne kaller me for ein **konstruktør** og i python heiter han `__init__`.
Altso kan me gjera slik:

```{code-cell} ipython3
class AnnualLoan3(AnnualLoan):

    def __init__(self):
        self.history = [ self.balance ]
    def endyear(self):
        self.interestamount = self.interest*self.balance
        self.oldbalance = self.balance
        self.balance += self.fee
        self.balance += self.interestamount
        self.balance -= self.payment
        self.history.append( self.balance )
```

No legg me startsaldoen inn i historikken med ein gong, og legg inn
oppdatert saldo like etter at han er oppdatert.

::: {admonition} Oppgåve
Testa klassa `AnnualLoan3`.  Oppfører historikken seg som han skal,
sjølv om du har fleire instansar samstundes? 
:::

::: {admonition} Oppgåve
Bruk den siste låneklassa iil å plotta saldoen over 25 år,
dvs. køyr `endyear()` 25 gongar og plot `history`.
:::

## Parameter i kosntruktøren

Det er naturleg å gjera alle klassevariablane om til objektvariablar.
Det er òg naturleg om me kan velja startsaldo og rentesats når me 
oppretter lånet.
Dette kan ein fint gjera ved å ha fleire parameter i konstruktøren,
som her:

```python
class AnnualLoan3(AnnualLoan):

    def __init__(self,balance=1000000):
        self.balance = balance
        self.history = [ self.balance ]
    ...
newloan = AnnualLoan3(500000)
```

Dei ekstra parametrane gjev me som argument når me instantierer eit objekt.

::: {admonition} Oppgåve
Oppdater låneklassa slik at alle låneparametrane kan setjast gjennom konstruktøren.
:::

::: {admonition} Merknad
Resten av denne øvinga vert meir open.  Det kan henda at du vil ta pause her,
og gjera andre gjennomarbeidde døme fyrst.
:::

## Tid og dato

Lånekalkulatoren vår er svært primitiv og grovkorna.
T.d. har me ikkje dato saldoane i historikken.
Her vore det naturleg å bruka `datetime`-typen som me har sett
før (sjå [](Tid%20og%20dato)).

::: {admonition} Oppgåve
Legg inn datering i klassa, slik at historikken inneheld dato for kvar saldo.

1.  Konstrukturøren må ta ein parameter for utbetalingsdato.
2.  Objektet må ha ein «dags dato», dvs. datoen for siste oppdatering av lånet.
3.  Historikken skal lagra både saldo og dato for saldoen.  Dette kan ein gjera
    ved at kvart element er ein tuppel (dato,saldo).
4.  Metoden for `endyear` må sjølvsagt finna rett dato, ved å sjekka dags dato og
    finna fyrste nyttår.
:::

::: {admonition} Oppgåve
Bruk den nye daterte klassa til å plotta saldoen over 25 år med dato på $x$-aksen.
:::

## Modellering

So langt har me fikla på måfå.  
Målet har vore å verta kjent med litt av den
mest grunnleggjenda syntaksen og semantikken i pytjhon.
Dersom me skal laga ein brukbar låne- eller sparekalkulator,
løner det seg å ta eit steg tilbake og laga eoin modell for kalkulatoren.
Kva skal kalkulatoren kunna gjera?
Korleis skal me som brukar samhandla med han?

Objektorientering er godt egna for å laga fleksibel og gjenbrukbar kode.
Det skal vera råd å gjenbruka det meste av koden for innskotskonti,
serielån og annuitetslån.

Der er ingen fasit når vi modellerer.  
Modellen avheng mykje av kva me legg vekt på, og ein må ofte
gjennom fleire rundar med prøving og feiling.
Lat oss starta med nokre av metodane som me treng.
+ me treng ein metode som reknar ut og kapitaliserer renter og evt. gebyr.
  So langt har det vore `endyear()`, men mange lån vert forrenta månadleg.
+ me må ha ein metode for innskot eller nedbetaling.  Hittil har det vore
  `endyear()` men det er fornuftig å skilja nedbetaling frå forrenting.
  Det er ikkje alle konti der det skjer samstundes.
+ me treng ein metode for å henta ut ei transaksjonsoversikt, som kan
  brukast m.a. til plotting.

Eit fyrste utkast kan sjå slik ut:

```python
class Account():
   def __init__(self,amount,time,interest=0.05,fee=0):
      pass
   def payin(self,amount,time):
      """Registrer ein ny transaksjon med beløpet `amount` på tidspunkt `time`.
      Oppdater saldoen.
      """
      pass
   def addinterest(self,time=None):
      """Rekn ut rentene og evt. gebyr og registrer dei som ein transaksjon.
      Oppdater saldoen.
      """
      pass
   def gettransactios(self,time):
      """Returner ei liste med transaksjonar, der kvar transaksjon er ein
      tuppel (tidspunkt,beløp,ny saldo).
      """
      pass
```

Her har me ikkje programmert nokon av metodane;
`pass` tyder «gjer ingenting», men gjer at definisjonen er gyldig.
Her har me teke med *docstrings* dvs. ei slags brukarrettleiing som
ein teiknstreng i starten av kvar metode.  
Tidlegare har me skrive slike forklaringar utanfor kodeblokken, men
når kodeblokkane blir lange, som klassedefinisjonar ofte er, kan det
vera greitt å ha dokumentasjonen i koden.

Metodane som er definerte her dannar *grensesnittet* til klassa.
Me kaller det gjerne eit API for *Application Programing Interface*.
Når APIet fyrst er fastsett, kan ein skriva resten av programmet.
Endringar i implementasjonen av metodane påverkar ikkje resten
av programmet so lenge APIet ligg fast.

## Ei naïv løysing


Me har ei ny utfordring når me skil innskot frå rentekapitalisering.
Når saldoen varierer i gjennom renteperioden, må ein rekna renter for
delar av belopet på delar av perioden.

Det er derimot ein god idé, når ein programmerer, å laga ei naïv 
løysing fyrst, og so forbetra ho etter kvart.  Difor skal me sjå
bort frå rentedagar i den fyrste implementasjon.

::: {admonition} Oppgåve
Skriv konstruktøren `__init__` for klassa.  
Bruk ein egna type frå [](Tid%20og%20dato) til tidspunktet.
Start ei ny liste med transaksjonar.
:::

::: {admonition} Oppgåve
Skriv `gettransactions`-metoden som returnerer lista med transaksjonar.
:::

::: {admonition} Oppgåve
Skriv `payin`-metoden som lagar ein transaksjon og oppdaterer
saldoen.
:::

::: {admonition} Oppgåve
Skriv `addinterest`-metoden som lagar ein transaksjon og oppdaterer
saldoen.
:::

::: {admonition} Oppgåve
Lag eit testdøme med månadleg sparing og årleg rente.
Hent ut transaksjonane og plott saldoen som ein funksjon av tida.
:::

::: {hint}
Du kan bruka ei løkke som kaller `payin` og `addinterest` utan at
denne løkka treng vera ein del av klassa.
:::

## Korrekt renteutrkening.

Korleis kan me no fiksa renteutrekninga, slik at ein betaler rett
rente på innbetalingar midt i ein renteperiode?

Ei mogleg løysing er at `addinterest()` hentar ut alle transaksjonane 
sidan siste renteutrekning frå historikken, og reknar rente for kvar
periode mellom transaksjonane.  
Ein kan lett finna talet på dagar mellom to tidspunkt dersom ein har 
brukt `datetime`-typane, og so kan ein rekna 1/365-del av rentesatsen
per dag.

::: {admonition} Oppgåve
Endra `addinterest()`-metoden slik at han ser på transaksjonane 
sidan førre renteutrekning for å rekna riktig rente.
Du bør kunna bruka ein listekomprehensjon for å finna dei 
transaksjonane du treng.
Du må nok bestemma deg for kva renteperioden er (månadleg eller
årleg) for å via kor langt tilbake du skal gå.
:::

::: {admonition} Oppgåve
Det vil vera ein fordel om klassa held greie på kor ofte rentene
vert kapitaliserte.
Skriv om `addinterest` slik at han legg til renter for kvar periode
frå siste transaksjon til datoen som er gjeven som parameter til
metoden.
:::

::: {admonition} Oppgåve
Med endringa for forrige oppgåve, kan du gjera renteutrekningane
automatisk.
Skriv om `payin()` slik at rentene vert oppdatert før det nye innskotet
vert innbetalt.
Det kan du få til ved å kalla `addinterest()` frå `payin()`.
Test for å sjekk at det vert rett.
:::

::: {admonition} Oppgåve
Lise sparer 1000 kvar månad til 2% rente.
Den 1. desember kvart år tek ho ut 5000 kr. til julegåver.
Kor mykje penger har ho på kontoen etter fem år?

Bruk sparekalkulatoren til å rekna ut svaret.
:::

## Avslutting

Eg reknar med at oppgåvene over har vore krevjande.
Der er fleire ting ein må kunna for å få dette til.
1.  Ein må vita korleis renter faktisk vert rekna ut i røynda.
2.  Ein må kunna programmera løkker og gjentekne operasjonar, *og*
    kunna kontrollera dei mot reglane som gjeld i røynda.
3.  Ein må kunne gjera utrekningane på enkle døme for hand eller i 
    andre verkty, slik at ein kan kontrollera at programmet reknar
    rett på nokre enkle testar.

