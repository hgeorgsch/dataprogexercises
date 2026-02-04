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

# Løysingar til Demo `dict`

Desse oppgåvene er utgangspunktet for ein demonstrasjonsvideo med to 
formål.
Eg skal demonstrera syntaksen for *Dictionaries*, eller `dict`, i 
python, og eg skal vise litt korleis eg tenkjer når eg tek fatt på å skriva
kode.

::: {admonition} Oppgåve
Lag eit kunderegister, der kundane er lagra med for- og etternamn,
kundenummer, fødselsdato, gateadresse og postnummer.

Du treng også
+ ein funksjon for å skriva ut alle kundane i eit godt leseleg format.
+ ein funksjon for å skriva ut éin kunde med eit gjeve namn.
+ ein funksjon for å leggja til ein ny kunde og automatisk generera
  kundenummer.
:::

+++

## En enkelt kunde

```{code-cell} ipython3
kunde1 = { "fornavn" : "Ola",
           "efternavn" : "Normann",
           "kundenummer" : 1,
           "fødselsdato" : "2001-01-01",
           "gateadresse" : "Borgundvegen 112",
           "postnummer" : 6001
}
```

```{code-cell} ipython3
print( kunde1 )
```

```{code-cell} ipython3
def printkunde(kunde):
    print( f'{kunde["kundenummer"]} {kunde["fornavn"]} {kunde["efternavn"]}' )
    print( f'fødd: {kunde["fødselsdato"]}' )
    print( kunde["gateadresse"] )
    print( kunde["postnummer"] )

printkunde( kunde1 )
```

## Utskrift av kunderegister

```{code-cell} ipython3
kundereg = { "Ola Normann" : kunde1 }
```

```{code-cell} ipython3
print( kundereg )
```

```{code-cell} ipython3
def printreg( reg ):
    for navn in reg:
        printkunde( kundereg[navn] )
        print()
```

```{code-cell} ipython3
printreg( kundereg )
```

```{code-cell} ipython3
def printenkunde( reg, navn ):
    printkunde( reg[navn] )
```

```{code-cell} ipython3
printenkunde( kundereg, "Ola Normann" )
```

```{code-cell} ipython3
printenkunde( kundereg, "Kari Normann" )
```

## Legge til kunder

```{code-cell} ipython3
def leggetilkunde( reg, kunde ):
    navn = f'{kunde["fornavn"]} {kunde["efternavn"]}'
    reg[navn] = kunde
```

```{code-cell} ipython3
kunde2 = { "fornavn" : "Kari",
           "efternavn" : "Normann",
           "kundenummer" : 2,
           "fødselsdato" : "2003-02-01",
           "gateadresse" : "Borgundvegen 225",
           "postnummer" : 6002
}
leggetilkunde( kundereg, kunde2 )
```

```{code-cell} ipython3
printreg( kundereg )
```

```{code-cell} ipython3
nr = [ k["kundenummer"] for k in kundereg.values() ]
print(nr)
```

```{code-cell} ipython3
max( nr ) + 1
```

```{code-cell} ipython3
def leggetilkunde( reg, kunde ):
    navn = f'{kunde["fornavn"]} {kunde["efternavn"]}'
    nr = [ k["kundenummer"] for k in reg.values() ]
    nyttnr = max(nr) + 1
    kunde["kundenummer"] = nyttnr
    reg[navn] = kunde
```

```{code-cell} ipython3
kunde3 = { "fornavn" : "Mons",
           "efternavn" : "Hansen",
           "kundenummer" : 3,
           "fødselsdato" : "1965-06-11",
           "gateadresse" : "Spjelkavikvegen 25",
           "postnummer" : 6011
}
leggetilkunde( kundereg, kunde3 )
```

```{code-cell} ipython3
printreg( kundereg )
```

```{code-cell} ipython3
kunde4 = { "fornavn" : "Nina",
           "efternavn" : "Hansen",
           "fødselsdato" : "1966-07-12",
           "gateadresse" : "Spjelkavikvegen 25",
           "postnummer" : 6011
}
leggetilkunde( kundereg, kunde4 )
```

```{code-cell} ipython3
printreg( kundereg )
```

```{code-cell} ipython3
nr = [ k["kundenummer"] for k in kundereg.values() ]
print(nr)
```

```{code-cell} ipython3
max(nr) + 1 
```

```{code-cell} ipython3
kunde5 = { "fornavn" : "Nina",
           "efternavn" : "Olsen",
           "fødselsdato" : "1966-07-12",
           "gateadresse" : "Spjelkavikvegen 25",
           "postnummer" : 6011
}
leggetilkunde( kundereg, kunde5 )
```

```{code-cell} ipython3
printreg( kundereg )
```

```{code-cell} ipython3

```
