---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

+++ {"editable": true, "slideshow": {"slide_type": ""}}

# Store datasett - I Excel

+++ {"editable": true, "slideshow": {"slide_type": "fragment"}}

- Excel er supert helt til filen din har 1,5 mill. rader og kræsjer PC-en din så grundig at sjefen ikke vet om han skal sparke eller ansette på IT

+++ {"editable": true, "slideshow": {"slide_type": "fragment"}}

- Å jobbe med data i Excel er helt supert helt til du må gjøre den samme nedlastingen og opprydding hver mandag morgen i 3 år

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

# **Pan**el**da**ta:
## Pandas 🐼
- Industristandard for dataanalyse
- Behandler enorme mengder data lynraskt
- Relativt lett i bruk til å være et så kraftig verktøy

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

- Pandas leser nesten alt av filer (csv, Excel, SQL, JSON..)
- Pandas+Python lar oss automatisere alt fra innhenting av data, til vasking, sammenslåing, analyse og visualisering

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
import pandas as pd

# Lag en enkel DataFrame på 1-2-3
data = {
    'Navn': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 92, 78],
    'Status': ['Bestått', 'Bestått', 'Vurderes']
}

df = pd.DataFrame(data)
df
```

+++ {"editable": true, "slideshow": {"slide_type": "fragment"}}

- Et dataframe er 2d, og bygget opp av rader og kolonner som av typen pandas `Series`.
- Pythonbiblioteket inneholder ferdig funksjonalitet som lar oss gjøre veldig mye av statistikk og databehandlig.
  - Gruppere, slå sammen data, filtere, deskriptiv statistikk (snitt, standardavvik, korrelasjon osv), plotte osv

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

### Basics: Hente ut kolonner og rader

- Vi henter ut 1 kolonne ved å gi kolonnenavnet i klammeparanteser bak dataframe-variabelen

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
#Henter ut navnekolonnen -> Series   
df["Score"]
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

Vi kan hente ut flere kolonner ved å bruke en kommaseparert liste i klammeparantes, inne i de første klammene

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
#Henter ut Navn og Score kolonner -> Dataframe
df[["Navn", "Score"]]
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

Vi henter ut rader med `df.loc[«radnavn»]`

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
#Hent ut rad 2
df.loc[2]
df.set_index("Navn").loc["Alice"]
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### 

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

`.loc[]` bruker vi også til å velge *både* rader og kolonner

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
# Hent ut rad 0 og 2, og kolonner "Navn" og "Status"
df.loc[[0,2], ["Status", "Navn"]]
df.iloc[0:2] 
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Attributter og metoder
- Et spesifikt objekt som `Dataframe` eksempelet vårt `df`, eller `Series`objektet `df["Score"]` har både attributter og metoder.
- En attributt er litt som en innebygd variabel, mens en metode er som en innebygd funksjon.
- Vi bruker punktum til å hente ut og brukke disse metodene og attributtene:
  

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
#Attributt: En indeks med kolonnenavn
df["Score"].name
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: subslide
---
# .describe() - En funksjon som vi kaller uten argumenter og spytter ut statistikk
df.describe()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: subslide
---
print("Gjennomsnittsscore:", df["Score"].mean()) # Bruker dataseriens innebygde funksjon .mean() som spytter ut gjennomsnitt 
print("Dataseriens navn er: ", df["Score"].name ) #Name er en attributt
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

# Liste over innebygde attributter og metoder
## Series

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

### Series atributter

Dataseriene vi lager har flere *atributter*

| **Attributt**      | **Beskrivelse**                                                                  |
|--------------------|----------------------------------------------------------------------------------|
| `index`            | Indeksen (labels) for Series.                                                    |
| `values`           | Verdiene (data) i Series som en NumPy-array.                                     |
| `name`             | Navnet på Series.                                                                |
| `dtype`            | Datatypen for verdiene i Series.                                                 |
| `size`             | Antall elementer i Series.                                                       |
| `shape`            | Dimensjonaliteten til Series (alltid en enkelt dimensjon).                       |
| `empty`            | Returnerer `True` hvis Series er tom (dvs. ikke har noen elementer).              |
| `nbytes`           | Det totale antallet bytes som forbrukes av elementene i Series.                  |
| `hasnans`          | Returnerer `True` hvis det finnes noen `NaN`-verdier i Series.                   |
| `is_unique`        | Returnerer `True` hvis alle verdiene i Series er unike.                          |
| `is_monotonic`     | Returnerer `True` hvis Series er sortert i stigende rekkefølge.                  |
| `str`              | Gir tilgang til strengmetoder (hvis Series inneholder strenger).                 |
| `dt`               | Gir tilgang til datetime-metoder (hvis Series inneholder datetime-objekter).     |

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

### Series Metoder
En pandas dataserie har mange nyttige innebygde metoder som gjør ting med dataen:

| **Metode**            | **Beskrivelse**                                                                  |
|-----------------------|----------------------------------------------------------------------------------|
| `head(n)`             | Returnerer de første `n` elementene i Series (standard er 5).                     |
| `tail(n)`             | Returnerer de siste `n` elementene i Series (standard er 5).                      |
| `unique()`            | Returnerer unike verdier i Series.                                                |
| `value_counts()`      | Returnerer antall forekomster av unike verdier i Series.                          |
| `describe()`          | Genererer beskrivende statistikk som antall, gjennomsnitt, std, min og maks.      |
| `sum()`               | Returnerer summen av elementene i Series.                                         |
| `mean()`              | Returnerer gjennomsnittet av elementene i Series.                                 |
| `median()`            | Returnerer medianen av elementene i Series.                                       |
| `min()`               | Returnerer minimumsverdien i Series.                                              |
| `max()`               | Returnerer maksimumsverdien i Series.                                             |
| `std()`               | Returnerer standardavviket til Series.                                            |
| `sort_values()`       | Sorterer Series etter verdiene.                                                   |
| `sort_index()`        | Sorterer Series etter indeksen.                                                   |
| `apply(func)`         | Anvender en funksjon element for element på Series.                               |
| `map(func)`           | Mapper verdier i Series ved hjelp av funksjon eller dictionary.                       |
| `dropna()`            | Fjerner `NaN`-verdier fra Series.                                                 |
| `fillna(value)`       | Fyller inn `NaN`-verdier med en spesifisert verdi.                                |
| `astype(dtype)`       | Endrer datatypen til Series til spesifisert datatype.                             |
| `clip(lower, upper)`  | Begrenser verdier til et spesifisert område (nedre og øvre grenser).              |
| `between(left, right)`| Returnerer True for verdier mellom spesifiserte grenser.                          |
| `shift(periods)`      | Skifter verdiene med et spesifisert antall perioder.                             |
| `cumsum()`            | Returnerer den kumulative summen av elementene i Series.                          |
| `cumprod()`           | Returnerer det kumulative produktet av elementene i Series.                       |
| `rolling(window)`     | Gir glidende beregninger med et gitt vindu                                          |
| `expanding()`         | Gir ekspanderende beregninger (f.eks. kumulative beregninger).               |
| `resample(rule)`      | Resampler tidsseriedata i henhold til en spesifisert frekvens.                    |
| `plot()`              | Plotter dataen i Series ved hjelp av Matplotlib.                                  |

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

# Mye....
- Vi begynner ikke å liste om for `Dataframes`
- Her er det lurt å spørre en KI-om hjelp, eller slå opp i [dokumentasjonen](https://pandas.pydata.org/docs/reference/index.html)

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

# CSV og store datasett
- I morgen skal dere jobbe dere gjennom:
[CSV og store datasett](https://iirevu.org.ntnu.no/iira6001/notebooks/Fyrste%20datasett%20med%20CSV.html)
- Målet er å laste inn, «vaske» og plotte valutakurser fra den relativt store csv-filen fra norges bank

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---

```
