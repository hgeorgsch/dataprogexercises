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

## Ein kunde

::: {admonition} Oppgåve
Lag ei klasse for ein kunde, og test at ho verkar.
Klassa skal ha ein metode for pen utskrift av kunden.
:::

```{code-cell} ipython3
class Kunde:
    def __init__( self, fornavn, etternavn, fdato, gateadresse, postnummer, kundenummer=None ):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fdato = fdato
        self.gateadresse = gateadresse
        self.postnummer = postnummer
        self.kundenummer = kundenummer
    def show( self ):
        print( str(self) )
        
    def __str__( self ):
        return ( f"{self.fornavn} {self.etternavn}\n" +
            f"Fødselsdato: {self.fdato}\n" +
            f"Kundenummer: {self.kundenummer}\n" +
            f"{self.gateadresse}\n" +
            f"{self.postnummer}\n" )

kunde1 = Kunde( "Ola", "Normann", "2001-03-02", "Borgundvegen 212", 6016 )
print( kunde1 )
kunde1.show()
```

## Eit register

::: {admonition} Oppgåve
Lag ei klasse for eit kunderegister, og test at ho verkar.
Klassa skal ha metodar for å leggja inn ein ny kunde, med
automatisk tildeling av kundenummer, og for å skriva ut alle
kundane i registeret.
:::

```{code-cell} ipython3
class Register:
    def __init__( self ):
        self.reg = []
        self.siste = 0
    def add( self, kunde ):
        self.siste += 1
        kunde.kundenummer = self.siste
        self.reg.append( kunde )
    def __str__( self ):
        return "\n".join( [ str(k) for k in self.reg ] )
reg = Register()
reg.add( kunde1 )
print( reg )
```

```{code-cell} ipython3
kunde2 = Kunde( "Kari", "Normann", "2002-01-12", "Borgundvegen 212", 6016 )
reg.add( kunde2 )
print( reg )
```

## 

+++

## Søk 

::: {admonition} Oppgåve
Utvid registeret med ein metode for å finna ein kunde etter namn.
:::

```{code-cell} ipython3
class RegisterS(Register):
    def search( self, etternavn ):
        return [ k for k in self.reg if k.etternavn == etternavn ] 
regs = RegisterS()
regs.add( kunde1 )
regs.add( kunde2 )
print( regs )
print( regs.search( "Normann" ) )
```

```{code-cell} ipython3
k = regs.search( "Normann" )
print( len( k ) )
```

```{code-cell} ipython3
print( k[1] )
```

```{code-cell} ipython3

```
