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
Me skal altso svara på spørsmålet
*kor raskt betaler ein ned eit bustadlån?*

Som eit døme kan me føresetja
- **Lånebeløp** 100000 kr
- **Rente** 4% årleg og etterskotvis
- **Gebyr** 100kr per år
- **Terminbeløp** 10000 kr per år (inkl. renter, gebyr og avdrag)

## Objekt og klasser

Objekt er ein teknikk for å samla fleire ulike definisjonar, både variablar og funksjonar (metodar).

```{code-cell} ipython3
class Loan:
    interest = 0.04
    fee = 100
    payment = 10000
    balance = 100000
        
mydebt = Loan()
print( f"Eg skuldar {mydebt.balance} kr." )
print( f"Eg må betala {mydebt.balance*mydebt.interest} kr. i renter." )
```

+ [ ] **TODO** introduser datetime her

Her har me definert eit objekt `mydebt` av ei klasse (type) `Loan`.
Objektet `mydebt` er ein konkret instans, *mitt lån*.
Klassa `Loan` er ei generisk sak. Mange andre kan ha liknande lån.
Lat oss sjå kva som skjer med to lån, når me betaler litt ned på det eine.

```{code-cell} ipython3
yourdebt = Loan()
print( "Du skuldar", yourdebt.balance )
mydebt.balance = mydebt.balance - 20000
print( "Eg skuldar", mydebt.balance )
print( "Du skuldar", yourdebt.balance )
```

## Metodar for låneadministrasjon

Objektet som me definerte over inneheld berre variablar.
Lat oss no leggja til metodar (funksjonar), ein for å skriva ut ein slags kontoutskrift, og ein for å oppdatera saldoen med renter og innbetalingar.

```{code-cell} ipython3
class Loan:
    interest = 0.04
    fee = 100
    payment = 10000
    balance = 100000
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

Legg merke til parameteren `self`; det er ein referanse til objektet som eig metoden.
Me innfører òg to nye variablar (`oldbalance` og `interestamount`).  Dei bruker me for å dela data mellom dei to metodane. Tid for å testa.

```{code-cell} ipython3
mydebt = Loan()
mydebt.printstatement()
mydebt.endyear()
mydebt.printstatement()
```

Me kan halda fram og laga nedbetalingsplan fleire år fram i tid, t.d.:

```{code-cell} ipython3
for i in range(10):
    print( "År", i )
    mydebt.endyear()
    mydebt.printstatement()
    
```

## Merknad

Ein kan sjølvsagt gjera dette like enkelt i eit rekneark.
Det som er nyttig å ha med seg er derimot at tankesettet er det same uansett om ein arbeider i eit rekneark eller i eit generelt programmeringsspråk.  
Det er ein føremon for studentane å arbeida med ulike representasjonar av det same algoritmiske tankesettet. Det gjev eit rikare dømemateriale som er grunnlaget for overføring av læring.

+++

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

