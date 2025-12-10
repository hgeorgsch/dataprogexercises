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

# Eitt objekt i JSON

::: {admonition} Oppgåve
Fila [](./kundedta1sample.json) inneheld eitt objekt.
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

# Ei liste i JSON

::: {admonition} Oppgåve
Fila [](./kundedta1.json) inneheld ei liste med kundar.
Opna denne fila i ein teksteditor.  
Korleis ser datasettet ut?  Forstår du kva det tyder?
:::

```{code-cell} ipython3
import json

with open("kundedata1.json", 'r') as file:
    kundedata = json.load(file)
print( kundedata )
```

**TODO** under

```{code-cell} ipython3
alle_etternavn = { kunde["etternavn"] for kunde in kundedata }
etternavn_H = {kunde["etternavn"] for kunde in kundedata if kunde["etternavn"][0] == 'H'}
print(etternavn_H)

```

+ Kan bli vanskelig å lese eller for komplisert
+ Dictionary av alle kunder med etternavn som begynner på 'H'

```{code-cell} ipython3
H_klubben = { navn: [kunde["fornavn"] for kunde in kundedata if kunde["etternavn"] == navn] 
             for navn in etternavn_H }

def finnKunde(etternavn):
    treffliste = []
    for kunde in kundedata:
        if etternavn == kunde["etternavn"]:
            treffliste.append(kunde)
    if treffliste == []:
        print(f"Ingen kunder med etternavn '{etternavn}' funndet")
        return None
    else:
        print(f"Vi fant {len(treffliste)} kunder med etternavn '{etternavn}'")
        return treffliste

H_klubben = { navn: finnKunde(navn) for navn in etternavn_H}

with open("kundedata_test.json", 'w') as file:
    json.dump(H_klubben, file)
```

---

## Oppg:

* Bruk komprehensjon til å lage en dictionary som inneholder allekunder med startsaldo større enn 120,000
* Dictionary skal bestå av nøkler som tilsvarer etternavnet til kundene, og verdiene skal være en liste med kundene på samme format som originalt

+ lag liste med rike kunder
+ lag set med etternavnene
+ lag dictionary med kunder { kundensetternavn: [liste med kunder]}

```{code-cell} ipython3
grense = 120e3
rike_kunder = [ kunde for kunde in kundedata if kunde["startsaldo"] > grense]
etternavn_rik = {kunde["etternavn"] for kunde in rike_kunder}
data_rike_kunder = {navn: [kunde for kunde in rike_kunder if kunde["etternavn"] == navn] for navn in etternavn_rik}
```

```{code-cell} ipython3
data_rike_kunder
```
