---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
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

## Objekt og klasser

Klasser er ein teknikk for å samla fleire ulike definisjonar,
både variablar og funksjonar (metodar).
Me kan definera ei enkel klasse, med berre variablar, slik:

```{code-cell} ipython3
class Loan:
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
mydebt = Loan()
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

## Tid og dato

+ [ ] **TODO** introduser datetime her

::: {admonition} Merknad
Ein kan sjølvsagt gjera dette like enkelt i eit rekneark.
Det som er nyttig å ha med seg er derimot at tankesettet er det same 
uansett om ein arbeider i eit rekneark eller i eit generelt programmeringsspråk.  
:::


::: {admonition} Oppgåve

Endra dømet over til å skriva ut ein betalingsplan med månadleg forrenting og avdrag.
Du kan velja innbetalingsbeløp sjølv.

:::

## Månadleg sparing

Lat oss sjå på eit litt meir komplisert problem, med månadleg sparing, der sparebeløpa kjem månadleg medan rentene berre kjem årleg.

```{code-cell} ipython3
class Account():
    year = 0
    month = 0
    balance = 0
    interest = 0
    rate = 0.02
    monthly = 0
    
    def __init__(self,x): 
        self.monthly = x
        return
    def monthend(self): 
        interestamount = self.balance * self.rate / 12
        self.interest += interestamount
        self.balance += self.monthly
        self.month += 1
        if self.month == 12: 
            self.yearend()
        return 
    def yearend(self):
        self.balance += self.interest
        self.interest = 0
        self.year += 1
        self.month = 0
        return

myaccount = Account(1000)
for i in range(48):
    myaccount.monthend()
    print( "Saldo: ", myaccount.balance, "\t\tRenter hittil i år:", myaccount.interest )
```

::: {admonition} Oppgåve

Lise sparer 1000 kvar månad til 2% rente, som i dømet over.
Den 1. desember kvart år tek ho ut 5000 kr. til julegåver.
Kor mykje penger har ho på kontoen etter fem år?

Dersom du meiner der manglar opplysingar i oppgåva, kan du gjera dine eigne føresetnader.
:::

