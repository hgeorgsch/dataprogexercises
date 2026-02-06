---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Løysingar frå Demo Klasser og Objekt

Desse oppgåvene er utgangspunktet for ein demonstrasjonsvideo som skal
illustrera bruken av klasser og objekt i python.
Oppgåva er den same som me tidlegare brukte for å demonstrera `dict`, men
denne gongen skal me tenkja objektorientert.

::: {admonition} Hovudmål
Lag eit objektorientert kunderegister, der kundane er lagra 
med for- og etternamn,
kundenummer, fødselsdato, gateadresse og postnummer.
:::

+++

## Ein kunde

::: {admonition} Oppgåve
Lag ei klasse for ein kunde, og test at ho verkar.
Klassa skal ha ein metode for pen utskrift av kunden.
:::

```{code-cell} ipython3
class Kunde:
    def __init__(self, fornavn, etternavn, fdato, gateadresse, postnummer, kundenummer=None):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fdato = fdato
        self.gateadresse = gateadresse
        self.postnummer = postnummer
        self.kundenummer = kundenummer
    def __str__(self):
        return f"{self.fornavn} {self.etternavn}\nKundenummer: {self.kundenummer}\n{self.gateadresse}\n{self.postnummer}\n"
    def getEtternavn( self ):
        return self.etternavn
kunde1 = Kunde( "Ola", "Normann", "2002-12-10", "Borgundvegen 202", 6016 )
print( kunde1 )
```

## Eit register

::: {admonition} Oppgåve
Lag ei klasse for eit kunderegister, og test at ho verkar.
Klassa skal ha metodar for å leggja inn ein ny kunde, med
automatisk tildeling av kundenummer, og for å skriva ut alle
kundane i registeret.
:::

```{code-cell} ipython3
class KundeRegister:
    def add(self, kunde):
        self.siste += 1
        kunde.kundenummer = self.siste
        self.reg.append( kunde )
    def __str__(self):
        return "\n".join(  [ str(x) for x in self.reg ] )
    def __init__(self):
        self.reg = []
        self.siste = 0
reg = KundeRegister()
reg.add( kunde1 )
print( reg )
```

```{code-cell} ipython3
kunde2 = Kunde( "Kari", "Normann", "2003-03-10", "Borgundvegen 202", 6016 )
reg.add( kunde2 )
print( reg )
```

## Søk 

::: {admonition} Oppgåve
Utvid registeret med ein metode for å finna ein kunde etter namn.
:::

```{code-cell} ipython3
class KundeRegister:
    def add(self, kunde):
        self.siste += 1
        kunde.kundenummer = self.siste
        self.reg.append( kunde )
    def __str__(self):
        return "\n".join(  [ str(x) for x in self.reg ] )
    def __init__(self):
        self.reg = []
        self.siste = 0
    def search(self,navn):
        return [ x for x in self.reg if x.etternavn == navn ] 
reg = KundeRegister()
reg.add( kunde1 )
reg.add( kunde2 )
print( reg.search( "Jensen" ) )
```

```{code-cell} ipython3
res =  reg.search( "Normann" ) 
for x in res:
    print(x)
```

```{code-cell} ipython3

```
