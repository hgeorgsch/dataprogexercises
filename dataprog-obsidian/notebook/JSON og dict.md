---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  name: dataprog
  language: python
  display_name: dataprog
---

# JSON og `dict`

Det er ofte nyttig å kunna lagra ein datastruktur på fil,
og lasta han inn att.  Dette kan gjerast på mange måtar.
Nokon er spesifikke for eit bestemt program, t.d. kan python
lagra kva som helst i sitt *pickle*-format, men dette er ikkje
nyttig for andre program.

Eit meir portabelt format er JSON -- *JavaScript Object Notation* --
som er godt egna til å lagra `dict`-strukturar og lister av `dict`.
Her skal me sjå nokre døme.

## Eitt objekt i JSON

::: {admonition} Oppgåve
Fila [](./kundedata1sample.json) inneheld eitt objekt.
Opna denne fila i ein teksteditor.  
Kva slags data inneheld ho?  Kva representerer objektet?
:::

For å lasta JSON-filer i python, bruker me `json`-biblioteket,
slik.

```{code-cell} ipython3
import json

file = open("kundedata1sample.json", 'r')
kunde = json.load(file)
file.close()
print( kunde )
```

Her bruker me `open()` for å opna fila.  Funksjonen tek filnamnet
og ein modus, som her er `r` for *read*.  Dvs. me har opna fila
å lesa og ikkje skriva.
Når fila er opna, kan me lesa ho med `json`-biblioteket.
Til slutt bør me passa på å lukka fila.

::: {admonition} Refleksjon
Korleis ser objektet frå `kundedata1sample.json` ut i python?
Kva slags objekt er det?
:::

Koden over kan me skriva på ein annan måte, med `with`, slik:

```{code-cell} ipython3
import json

with open("kundedata1sample.json", 'r') as file:
   kunde = json.load(file)
print( kunde )
```

Det som skjer her er akkurat det same som i det fyrste kodedømet,
men `with` startar ein blokk og lukkar fila automatisk når blokken
er slutt.  Det er lett å gløyma å lukka fila, og det kan verta eit
problem i store program.

## Ei liste i JSON

::: {admonition} Oppgåve
Fila [](./kundedata1.json) inneheld ei liste med kundar.
Opna denne fila i ein teksteditor.  
Korleis ser datasettet ut?  Forstår du kva det tyder?
:::

```{code-cell} ipython3
import json

with open("kundedata1.json", 'r') as file:
    kundedata = json.load(file)
print( f"Type:  {type(kundedata)}" )
print( f"Lengd: {len(kundedata)}" )
```

::: {admonition} Oppgåve
Kva slags data har du i `kundedata`?
Skriv ut innhaldet av variabelen med `print` eller `display`.
Kva fungerer best, `print` eller `display`?
:::

## Studera store datasett

Det er ikkje lett å verta klok på utskrifta av store datasett.
Me har 2000 oppslag der kvart oppslag inneheld samansett informasjon.
Eit enkelt triks er å indekssera eit enkelt element for å sjå kva type
det er.

```{code-cell} ipython3
display( kundedata[-1] )
```

Negative indeksar tel frå slutten av lista, so indeks -1 er siste element.

::: {admonition} Oppgåve
Kva slags struktur og type har elementet som me skreiv ut over?
Skriv ut eit anna vilkårleg element.  Har det same struktur?
:::

For å få oversikt over heile lista, kan det vera nyttig å skriva ut 
berre litt informasjon om kvart element.
T.d. kan me sjå på etternamn.

```{code-cell} ipython3
alle_etternavn = [ kunde["etternavn"] for kunde in kundedata ]
print(alle_etternavn)
print(len(alle_etternavn))
```

Over såg me på ei liste med etternamn.
Me kan gjera denne lista om til ei mengd, slik:

```{code-cell} ipython3
set_etternavn = set( alle_etternavn )
print(len(set_etternavn))
```

::: {admonition} Refleksjon
Kvifor er der færre element i megnda `set_etternavn` enn i lista
`alle_etternavn`?
Lag gjerne ein blokk som viser innhaldet i `set_etternavn` om det hjelper.
:::

Det er ofte nyttig å filtrera, for å finna element med særlege eigenskapar.
T.d. kan me finna kundar med etternamn på H.

```{code-cell} ipython3
etternavn_H = { kunde["etternavn"] for kunde in kundedata if kunde["etternavn"][0] == 'H' }
print(etternavn_H)
```

## Meir komplisert døme

Det kan vera nyttig å sjå på alle kundane med same etternamn.

::: {admonition} Oppgåve
Korleis vil du definera ein variabel med alle kundane som heiter Humblen?
:::

Du kan løysa oppgåva raskt med listekomprehensjon, og der er ikkje noko galt i
det.
Dersom me skal gjera liknande oppgåver og studera fleire namn er det derimot
enklast om me har ein funksjon.  T.d.

```{code-cell} ipython3
def finnKunde(etternavn):
   return [ kunde for kunde in kundedata if kunde["etternavn"] == etternavn ]
print( finnKunde( "Humblen" ) )
```

::: {admonition} Refleksjon
Kva gjer funksjonen `finnKunde`?
:::

Me kan kombinera teknikkar for å laga nøsta datastrukturer.
T.d. kan me laga ein `dict` med alle kundane på H, sortert
etter etternamn.

```{code-cell} ipython3
H_klubben = { navn: finnKunde(navn) for navn in etternavn_H }
```

Her har me brukt komprehensjon på `dict`, med et oppslag for kvart namn på H.

::: {admonition} Refleksjon
Korleis ser innhaldet i `H_klubber` ut?
Me har ikkje skrive det ut fordi det fyller so mykje på sida, men du
må gjerna prøva sjølv.
:::

Me kunne laga ein `dict` berre for å telja kundane med same etternamn.

```{code-cell} ipython3
htal = { navn: len(finnKunde(navn)) for navn in etternavn_H }
print( htal )
```

Dersom me vil ha resultatet på fil, kan me bruka `json`-biblioteket slik.

```{code-cell} ipython3
with open("kundedata_test.json", 'w') as file:
    json.dump(H_klubben, file)
```

Her bruker me `open()` som før, men med `w` for *write* i staden for `r` for *read*.


::: {admonition} Oppgåve

* Bruk komprehensjon til å lage en dictionary som inneholder allekunder med startsaldo større enn 120,000
* Dictionary skal bestå av nøkler som tilsvarer etternavnet til kundene, og verdiene skal være en liste med kundene på samme format som originalt

+ lag liste med rike kunder
+ lag set med etternavnene
+ lag dictionary med kunder { kundensetternavn: [liste med kunder]}

:::

```{code-cell} ipython3

```
