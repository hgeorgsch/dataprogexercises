# Objektorientert lånekalkulator

Her skal me ta løysinga frå [](Simulering%20av%20kontantstraum) og
visa korleis me kan organisera lånekalkulatoren med klasser og objekt.
Me skal òg bruka typar for tid og dato frå [](Tid%20og%20dato).
Målet er ein meir fleksibel låne- og sparekalkulator, som lett kan
tilpassast ulike låne- og spareformar.

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


```python
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


```python
mydebt = SimpleLoan()
print( f"Eg skuldar {mydebt.balance} kr." )
print( f"Eg må betala {mydebt.balance*mydebt.interest} kr. i renter." )
```

    Eg skuldar 100000 kr.
    Eg må betala 4000.0 kr. i renter.
    

Me kan endra variablane i objektet.
Ei rentenedgang kan me t.d. implementera slik.


```python
mydebt.interest = 0.035
print( f"Eg skuldar {mydebt.balance} kr." )
print( f"Eg må betala {mydebt.balance*mydebt.interest} kr. i renter." )
```

    Eg skuldar 100000 kr.
    Eg må betala 3500.0000000000005 kr. i renter.
    

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


```python
newloan = SimpleLoan()
print(newloan.interest)
```

    0.04
    


```python
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


```python
mydebt = AnnualLoan()
mydebt.printstatement()
mydebt.endyear()
mydebt.printstatement()
```

    Gebyr:		 100
    Renter:		 0
    Nedbetaling:	 9900
    Ny saldo:	 100000
    Gebyr:		 100
    Renter:		 4000.0
    Nedbetaling:	 5900.0
    Ny saldo:	 94100.0
    

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


```python
for i in range(10):
    print( "År", i )
    mydebt.endyear()
    mydebt.printstatement()
    
```

    År 0
    Gebyr:		 100
    Renter:		 3764.0
    Nedbetaling:	 6136.0
    Ny saldo:	 87964.0
    År 1
    Gebyr:		 100
    Renter:		 3518.56
    Nedbetaling:	 6381.4400000000005
    Ny saldo:	 81582.56
    År 2
    Gebyr:		 100
    Renter:		 3263.3024
    Nedbetaling:	 6636.6975999999995
    Ny saldo:	 74945.8624
    År 3
    Gebyr:		 100
    Renter:		 2997.834496
    Nedbetaling:	 6902.1655040000005
    Ny saldo:	 68043.696896
    År 4
    Gebyr:		 100
    Renter:		 2721.74787584
    Nedbetaling:	 7178.252124160001
    Ny saldo:	 60865.44477183999
    År 5
    Gebyr:		 100
    Renter:		 2434.6177908735995
    Nedbetaling:	 7465.382209126401
    Ny saldo:	 53400.06256271359
    År 6
    Gebyr:		 100
    Renter:		 2136.002502508544
    Nedbetaling:	 7763.997497491457
    Ny saldo:	 45636.06506522213
    År 7
    Gebyr:		 100
    Renter:		 1825.4426026088852
    Nedbetaling:	 8074.557397391115
    Ny saldo:	 37561.507667831014
    År 8
    Gebyr:		 100
    Renter:		 1502.4603067132407
    Nedbetaling:	 8397.539693286759
    Ny saldo:	 29163.967974544255
    År 9
    Gebyr:		 100
    Renter:		 1166.5587189817702
    Nedbetaling:	 8733.44128101823
    Ny saldo:	 20430.526693526026
    

Variablane i objektet (`balance` i dette tilfellet) dannar ein **tilstand**.
Objektet har til ein kvar tid ein bestemt tilstand, og metodane kan endra
denne tilstanden.

::: {admonition} Merknad
Som me har sett kan me tilordna objektvariablane utan å bruka metodane i objektet,
men dette er rekna som dårleg praksis.
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


```python
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


```python
loan1 = AnnualLoan2()
loan2 = AnnualLoan2()

print( "Lån 1", loan1.history )
print( "Lån 2", loan2.history )

loan1.endyear()
print( "Oppdatert lån 1" )

print( "Lån 1", loan1.history )
print( "Lån 2", loan2.history )
```

    Lån 1 []
    Lån 2 []
    Oppdatert lån 1
    Lån 1 [100000]
    Lån 2 [100000]
    

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

For å løysa dette problemet må me ha ein metode som opprettar historikkvariabelen i objektet.
Der er ein spesiell metode som vert køyrd når objektet vert instantiert.
Denne kaller me for ein **konstruktør** og i python heiter han `__init__`.
Altso kan me gjera slik:


```python
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


```python
import matplotlib.pyplot as plt
import numpy as np

loan3 = AnnualLoan3()
loan4 = AnnualLoan3()

print( "Lån 3", loan3.history )
print( "Lån 4", loan4.history )

loan3.endyear()
print( "Oppdatert lån 3" )

print( "Lån 3", loan3.history )
print( "Lån 4", loan4.history )

loan_plot = AnnualLoan3()
years = 25
for _ in range(years):
    loan_plot.endyear()

plt.figure()
plt.plot(np.arange(years+1), loan_plot.history)
plt.show()

```

    Lån 3 [100000]
    Lån 4 [100000]
    Oppdatert lån 3
    Lån 3 [100000, 94100.0]
    Lån 4 [100000]
    


    
![png](LoanClass%20copy_files/LoanClass%20copy_19_1.png)
    


No legg me startsaldoen inn i historikken med ein gong, og legg inn
oppdatert saldo like etter at han er oppdatert.  
Dermed får me med saldoen både heilt på starten og heilt på slutten.

::: {admonition} Oppgåve
Test klassa `AnnualLoan3`.  Oppfører historikken seg som han skal,
sjølv om du har fleire instansar samstundes? 
:::

::: {admonition} Oppgåve
Bruk den siste låneklassa iil å plotta saldoen over 25 år,
dvs. køyr `endyear()` 25 gongar og plot `history`.
:::


```python
class AnnualLoan4(AnnualLoan):

    def __init__(self, balance=100000, interest=0.04, fee=100, payment=10000):
        self.balance = balance
        self.interest = interest
        self.fee = fee
        self.payment = payment
        self.history = [self.balance]

    def endyear(self):
        self.interestamount = self.interest*self.balance
        self.oldbalance = self.balance
        self.balance += self.fee
        self.balance += self.interestamount
        self.balance -= self.payment
        self.history.append( self.balance )

newloan = AnnualLoan4(500000, payment=50000) # if the payment is too small, the loan will only increase over time

print(newloan.history)
for _ in range(10):
    newloan.endyear()
print(newloan.history)

plt.Figure()
plt.plot(np.arange(len(newloan.history)), newloan.history)
plt.show()
```

    [500000]
    [500000, 470100.0, 439004.0, 406664.16, 373030.7264, 338051.955456, 301674.03367424, 263840.9950212096, 224494.63482205797, 183574.4202149403, 141017.39702353792]
    


    
![png](LoanClass%20copy_files/LoanClass%20copy_21_1.png)
    


## Parameter i konstruktøren

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
Resten av denne øvinga vert meir open og tidkrevjande.
Det kan henda at du vil ta pause her, og gjera andre gjennomarbeidde døme fyrst.
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

::: {admonition} Merknad
Om programmet vert stort, kan det løna seg å laga ei eiga klasse for 
transaksjon.  Tuppelen (dato,saldo) er ei rask og enkel løysing.
Det fungerer godt so lenge me berre har dato og saldo.
Ei klasse gjer det enklare å leggja til fleire variablar når me finn ut
at me treng transaksjonsbeløp, forklarande tekst, avsendar, osv.
:::


```python
import datetime

class AnnualLoan5(AnnualLoan4):

    def __init__(self, balance=100000, interest=0.04, fee=100, payment=10000, start_date = None):
        super().__init__(balance, interest, fee, payment)

        if start_date is None:
            self.date = datetime.date.today()
        else:
            self.date = start_date
        
        self.history = [(self.date, self.balance)]

    def endyear(self):
        super().endyear()
        self.date = datetime.date(self.date.year + 1, self.date.month, self.date.day) # adds one to the year, 2026 goes to 2027
        self.history[-1] = (self.date, self.balance) # adds the new date and balance as the last values

    def getHistory(self):
        return self.history
    
loan = AnnualLoan5(balance=500000, interest=0.02, fee = 200, payment=30000, start_date=datetime.date(2026, 1, 25))
    
for _ in range(25):
    loan.endyear()

data = loan.getHistory()
print(data)
dates, balances = zip(*data) #zip() in this case, separates the dates from the balances. For more info go through https://realpython.com/python-zip-function/
print(dates)
print(balances)
    
plt.figure()
plt.plot(dates, balances)
```

    [(datetime.date(2026, 1, 25), 500000), (datetime.date(2027, 1, 25), 480200.0), (datetime.date(2028, 1, 25), 460004.0), (datetime.date(2029, 1, 25), 439404.08), (datetime.date(2030, 1, 25), 418392.1616), (datetime.date(2031, 1, 25), 396960.004832), (datetime.date(2032, 1, 25), 375099.20492864), (datetime.date(2033, 1, 25), 352801.1890272128), (datetime.date(2034, 1, 25), 330057.212807757), (datetime.date(2035, 1, 25), 306858.35706391215), (datetime.date(2036, 1, 25), 283195.52420519036), (datetime.date(2037, 1, 25), 259059.4346892942), (datetime.date(2038, 1, 25), 234440.62338308006), (datetime.date(2039, 1, 25), 209329.43585074166), (datetime.date(2040, 1, 25), 183716.02456775648), (datetime.date(2041, 1, 25), 157590.3450591116), (datetime.date(2042, 1, 25), 130942.15196029382), (datetime.date(2043, 1, 25), 103760.9949994997), (datetime.date(2044, 1, 25), 76036.2148994897), (datetime.date(2045, 1, 25), 47756.9391974795), (datetime.date(2046, 1, 25), 18912.077981429087), (datetime.date(2047, 1, 25), -10509.68045894233), (datetime.date(2048, 1, 25), -40519.87406812118), (datetime.date(2049, 1, 25), -71130.2715494836), (datetime.date(2050, 1, 25), -102352.87698047327), (datetime.date(2051, 1, 25), -134199.93452008272)]
    (datetime.date(2026, 1, 25), datetime.date(2027, 1, 25), datetime.date(2028, 1, 25), datetime.date(2029, 1, 25), datetime.date(2030, 1, 25), datetime.date(2031, 1, 25), datetime.date(2032, 1, 25), datetime.date(2033, 1, 25), datetime.date(2034, 1, 25), datetime.date(2035, 1, 25), datetime.date(2036, 1, 25), datetime.date(2037, 1, 25), datetime.date(2038, 1, 25), datetime.date(2039, 1, 25), datetime.date(2040, 1, 25), datetime.date(2041, 1, 25), datetime.date(2042, 1, 25), datetime.date(2043, 1, 25), datetime.date(2044, 1, 25), datetime.date(2045, 1, 25), datetime.date(2046, 1, 25), datetime.date(2047, 1, 25), datetime.date(2048, 1, 25), datetime.date(2049, 1, 25), datetime.date(2050, 1, 25), datetime.date(2051, 1, 25))
    (500000, 480200.0, 460004.0, 439404.08, 418392.1616, 396960.004832, 375099.20492864, 352801.1890272128, 330057.212807757, 306858.35706391215, 283195.52420519036, 259059.4346892942, 234440.62338308006, 209329.43585074166, 183716.02456775648, 157590.3450591116, 130942.15196029382, 103760.9949994997, 76036.2148994897, 47756.9391974795, 18912.077981429087, -10509.68045894233, -40519.87406812118, -71130.2715494836, -102352.87698047327, -134199.93452008272)
    




    [<matplotlib.lines.Line2D at 0x1d2676c6cf0>]




    
![png](LoanClass%20copy_files/LoanClass%20copy_23_2.png)
    


## Modellering

So langt har me fikla på måfå.  
Målet har vore å verta kjent med litt av den
mest grunnleggjenda syntaksen og semantikken i python.
Dersom me skal laga ein brukbar låne- eller sparekalkulator,
løner det seg å ta eit steg tilbake og laga ein modell for kalkulatoren.
Kva skal kalkulatoren kunna gjera?
Korleis skal me som brukar samhandla med han?

Objektorientering er godt egna for å laga fleksibel og gjenbrukbar kode.
Det skal vera råd å gjenbruka det meste av koden for innskotskonti,
serielån og annuitetslån.

Der er ingen fasit når vi modellerer.  
Modellen avheng mykje av kva ein sjølv legg vekt på, og ein må ofte
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
   def addinterest(self,time):
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


```python
class SavingsAccount(AnnualLoan5):
    def __init__(self, balance=0, interest=0.2, start_date = None):
        
        if start_date is None:
            start_date = datetime.date.today()

        super().__init__(balance=balance, interest=interest, fee=0, payment= 0, start_date=start_date)
        self.transactions = []

    def gettransactions(self):
        return self.transactions
        
    def payin(self, amount, date = None):
        if date is None:
            date = self.date 
            
        self.balance += amount
        self.transactions.append((date, amount, "payin"))
        self.history.append((date, self.balance))

    def addinterest(self, date = None):
        if date is None:
            date = self.date
            
        interest_amount = self.balance * self.interest
        self.balance += interest_amount
        self.transactions.append((date, interest_amount, "interest"))
        self.history.append((date, self.balance))

loan = SavingsAccount(balance=10000, interest=0.05, start_date=datetime.date(2026,1,25))
current_date = loan.date 

#the code below might be a bit confusing, so here is the explenation:
# We add some money into the savingsaccount in 10 years, hence range(10)
# each year has 12 months hence range(12)
# we add 1000 each month to the account, and register the payment date
# we update the current date by advancing the date by one month. 
# It is done by using the modulo operator which returns the current month with added 1, unless the current_date is 12, then the month will be set to 0 +1.
# If you wish so, you can try the following calculator to test the logic for finding a new month https://www.calculatorsoup.com/calculators/math/modulo-calculator.php
# Year is updated only when the current month is 12, or december, which means that for most of the year, the equation will be year = current_date.year + 0, beacuse the current date is not 12, which returns 0
# If the current month is 12, then the new year will be year + 1
# and, at the and of the year we add interest

for year in range(10):
    for month in range(12):
        loan.payin(1000, current_date)
        current_date = current_date.replace(month=current_date.month % 12 + 1, year = current_date.year + (current_date.month == 12)) #(current_date.month == 12) can only return 1 or 0
    loan.addinterest(current_date)

dates, balances = zip(*loan.history)

plt.figure()
plt.plot(dates, balances)
plt.xlabel("Dato")
plt.ylabel("Saldo")
plt.title("Saldo over tid")
plt.show()
    
```


    
![png](LoanClass%20copy_files/LoanClass%20copy_25_0.png)
    


## Korrekt renteutrkening.

Korleis kan me no fiksa renteutrekninga, slik at ein betaler rett
rente på innbetalingar midt i ein renteperiode?

Ei mogleg løysing er at `addinterest()` hentar ut alle transaksjonane 
sidan siste renteutrekning frå historikken, og reknar rente for kvar
periode mellom transaksjonane.  
Ein kan lett finna talet på dagar mellom to tidspunkt dersom ein har 
brukt `datetime`-typane, og so kan ein rekna 1/365-del av rentesatsen
per dag.
Sidan rentekapitaliseringa òg er ein transaksjon, 

::: {admonition} Oppgåve
Endra `addinterest()`-metoden slik at han ser på transaksjonane 
sidan førre renteutrekning for å rekna riktig rente.
Du kan bruka ein listekomprehensjon for å finna dei transaksjonane
du treng.
Du må nok bestemma deg for kva renteperioden er (månadleg eller
årleg) for å finna datoen for førre rentebetaling.

Når du har dei aktuelle transaksjonane, kan du laga ei løkke,
og for kvar iterasjon, finna saldoen og talet dagar til neste
transaksjon, og rekna ut rentene for dette.
:::

::: {admonition} Oppgåve
Det vil vera ein føremon om klassa held greie på når rentene
vert lagde til.
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

::: {admonition} Oppgåve
Kva skjer om der er fleire transaksjonar på same dag?
Vert rentene rekna rett om saldoen vert endra fleire
gongar på ein dag?
Lag eit par testar for å sjekka.
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
