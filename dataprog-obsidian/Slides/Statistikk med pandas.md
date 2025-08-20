---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

<!-- slide template="[[tpl-quote-header]]" -->

# Deskriptiv statistikk med pandas

![[Panda_closeup.jpg|480]]

::: credit
By Jcwf, CC BY-SA 3.0, via
[Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=836272)
:::

note:
Statistikk er et område hvor programmering er til stor hjelp, særlig hvis man har analyser som skal gjentas på lignende datasett, f.eks. for ulike perioder, eller datasettene er meget store.

*pandas* er et av de mest populære bibliotekene for å håndtere store datasett i python og inkluderer god støtte for deskriptiv statistikk.

**TODO** Fullfør disposisjon og vurder omfang før målene beskrives
+ **Læringsmål**
	+ Konseptuell oversikt over pandas
		+  Data frame og Series
		+ indeks

---

<!-- slide template="[[tpl-quote-header]]" -->

# *pan*el *da*ta (pandas)


| Varegruppe         |   År | Uke | Vekt (tonn) | Kilopris (kr) |
| :----------------- | ---: | --: | ----------: | ------------: |
| Fersk oppalen laks | 2000 |   1 |        3728 |         30,98 |
| Fersk oppalen laks | 2000 |   2 |        4054 |         31,12 |
| Fersk oppalen laks | 2000 |   3 |        4043 |         31,03 |
| Fersk oppalen laks | 2000 |   4 |        3730 |         30,95 |
| Fersk oppalen laks | 2000 |   5 |        3831 |         31,30 |
| Fersk oppalen laks | 2000 |   6 |        4415 |         32,53 |
| Fersk oppalen laks | 2000 |   7 |        4617 |         32,46 |
| Fersk oppalen laks | 2000 |   8 |        4463 |         32,19 |
| Fersk oppalen laks | 2000 |   9 |        4025 |         32,04 |
| Fersk oppalen laks | 2000 |  10 |        4274 |         32,00 |
| Fersk oppalen laks | 2000 |  11 |        4797 |         33,29 |
| Fersk oppalen laks | 2000 |  12 |        5004 |         33,77 |

::: credit
Utdrag av datasett frå Statistisk Sentralbyrå
:::

note:
*pandas* står for «panel data» som egentlig betyr data som er observert langs en tidsakse.
De samme subjektene er observert på ulike tidspunkt.
Det gir opphav til en tabell, der hver rekke er en observasjon med et bestemt tidspunkt, og hver søyle er en observert egenskap eller variabel.

Der er i og for seg ingen spesiell grunn for at datasettene i pandas må være observert langs en tidsakse. Det sentrale poenget er denne tabellen, med rader som svarer til observasjoner og søyler som svarer til ulike egenskaper som er observert.

Vi har sett at vi kan representere slike datatabeller både i CSV-filer og som regneark, eller vi kan føre dem pent i et rutenett på papir. Vi skal aldri glemme at det er det samme datasettet vi ser på, uansett verktøy. Dataene er uavhengige av representasjonen, som gjør at vi kan velge verktøy efter hvordan vi ønsker å bruke dataene, eller kombinere verktøy, uten at det påvirker innholdet i datasettet.

Datasettet på foilen er eksportdata fra SSB.  Kvantum og kilopris er observert ukentlig. Søylen for varegruppe er unødvendig her, siden alt er samme vare, men dette er bare et utdrag.  Det fullstendige datasettet har rader for andre varegrupper, og er dermed ikke egentlig formattert som paneldata. Radene svarer ikke bare til ulike tidspunkt, men også til ulike varegrupper, men det er en utfordring som vi kan komme tilbake til.

Ordbruken varierer en del mellom fagfelt og anvendelsesdomener. For å unngå forvirring skal vi holde på tabellperspektivet, og tale om rader eller rekker på den ene siden og søyler eller kolonner på den andre.

---

```python
import pandas as pd
df= pd.read_csv("dataset.csv",
                encoding="utf-8",
                sep="\t",
                decimal=",")
```

note:
Vi skal stort sett arbeide med datasett som vi importerter fra andre kilder.
Når vi laster CSV-filer i pandas med `read_csv`-funksjonen kan vi oppgi hvordan filen er formatter. 
Her sier vi at tegnkodingen er UTF-8, at skilletegnet mellom søylene er tabulator, og at komma brukes som desimaltegn. Hvis dette utelates brukes UTF-8, komma som skilletegn og punktum som desimaltegn.

---

<!-- slide template="[[tpl-smalltext]]" -->


```
In [2]: df = pd.read_csv("laksedata.csv",sep=";")

In [3]: print(df)
               varegruppe      uke  Vekt (tonn)  Kilopris (kr)
0      Fersk oppalen laks  2000U01         3728          30.98
1      Fersk oppalen laks  2000U02         4054          31.12
2      Fersk oppalen laks  2000U03         4043          31.03
3      Fersk oppalen laks  2000U04         3730          30.95
4      Fersk oppalen laks  2000U05         3831          31.30
...                   ...      ...          ...            ...
2585  Frosen oppalen laks  2024U39          578          71.97
2586  Frosen oppalen laks  2024U40          987          78.32
2587  Frosen oppalen laks  2024U41          780          73.69
2588  Frosen oppalen laks  2024U42          793          81.90
2589  Frosen oppalen laks  2024U43          677          71.49

[2590 rows x 4 columns]
```

::: credit
:::

note:
Resultatet av `read_csv` kalles en *data frame*. I tillegg til rådataene fra filen, inneholder en *data frame* gjerne en del metadata. Bl.a. vil pandas indeksere både rekker og søyler.  Når vi viser vår *data frame* med `print`, ser vi at radene har fått nummer. Søylene hadde overskrifter som vises som indeks.

Vi vil stort sett bruke numerisk indeks på radene og *label*-indeks på søylene, men dette er ingen begrensning. Søylene har en numerisk indeks, som vi kan bruke, selv om den normalt ikke vises når der finnes en *label*. Vi kan også definere *labels* på rekkene, selv om det sjelden er praktisk med tusenvis av rekker.

Med pandas kan vi manipulere våre *data frames* på mange ulike måter.  Vi kan ta utsnitt av datasettet, definere nye søyler, sette sammen datasett, finne gjennomsnitt og standardavvik og tegne plott.

---

<!-- slide template="[[tpl-smalltext]]" -->

# Indeksering

```python
In [7]: col = df["kr/kg"]

In [8]: col
Out[8]: 
0       30.98
1       31.12
2       31.03
3       30.95
4       31.30
        ...  
2585    71.97
2586    78.32
2587    73.69
2588    81.90
2589    71.49
Name: kr/kg, Length: 2590, dtype: float64

In [9]: type(col)
Out[9]: pandas.core.series.Series

```

::: credit
:::
note:
Indeksering er kritisk for å hente utsnitt av data.  Den enkleste formen for indeksering er den samme som for *dictionaries*, med klamme-parenteser.
Vi bruker klammeparenteser og *label*.

Resultatet er en ny datatype, *Series*, som er den andre sentrale typen i pandas-verden, ved side av *DataFrame*.

Der *DataFrame* er en todimensjonal tabell, er *Series* éndimensjonal som en liste. Hvis vi bare observerer én variabel, kan det være naturlig å bruke *Series*. Når vi observerer flere variabler, trenger vi *DataFrame*.

Til forskjell fra vanlige lister inneholder derimot *Series* metadata, og vi ser at indeksene vises med `print`, som de gjør for *DataFrame*.

---

<!-- slide template="[[tpl-smalltext]]" -->

# Indeksering

```python
In [10]: df1 = df[["Tonn","kr/kg"]]

In [11]: df1
Out[11]: 
      Tonn  kr/kg
0     3728  30.98
1     4054  31.12
2     4043  31.03
3     3730  30.95
4     3831  31.30
...    ...    ...
2585   578  71.97
2586   987  78.32
2587   780  73.69
2588   793  81.90
2589   677  71.49

[2590 rows x 2 columns]

In [12]: type(df)
Out[12]: pandas.core.frame.DataFrame
```

::: credit
:::
note:
Vi kan ogzå be om flere søyler samtidig, ved å oppgi en liste med *labels*.  Det er meget nyttig når vi har et overdrevent komplekst datasett, og bare noen søyler er interessante.

---
<!-- slide template="[[tpl-smalltext]]" -->

# .loc og .iloc

```
In [38]: df.loc[2]
Out[38]: 
varegruppe    Fersk oppalen laks
uke                      2000U03
Tonn                        4043
kr/kg                      31.03
Name: 2, dtype: object

In [39]: df.iloc[2]
Out[39]: 
varegruppe    Fersk oppalen laks
uke                      2000U03
Tonn                        4043
kr/kg                      31.03
Name: 2, dtype: object
```

::: credit
:::

note:
Når vi skal indeksere på rader, bruker vi notasjonen `loc` og `iloc`. De er ganske like, men `iloc` er ment for numerisk indeksering og `loc` for *labels*.

Vi skal merke oss at `.loc` og `.iloc` ikke er funksjoner.
De følges av klammeparenteser som for anden indeksering, og
ikke av runde paranteser som funksjoner bruker.

---
<!-- slide template="[[tpl-smalltext]]" -->

# Slices

```
In [40]: df.iloc[2:4]
Out[40]: 
           varegruppe      uke  Tonn  kr/kg
2  Fersk oppalen laks  2000U03  4043  31.03
3  Fersk oppalen laks  2000U04  3730  30.95

In [41]: df.loc[2:4]
Out[41]: 
           varegruppe      uke  Tonn  kr/kg
2  Fersk oppalen laks  2000U03  4043  31.03
3  Fersk oppalen laks  2000U04  3730  30.95
4  Fersk oppalen laks  2000U05  3831  31.30

In [42]: 
```

::: credit
:::

note:
Ofte indekserer vi får å ta et utvalg av rader, det som gjerne kalles
*slicing*.  Den enkleste formen for dette er ved å oppgi et spenn av
indekser med kolon, slik som vi også kan gjøre med lister.

Her oppfører `loc` og `iloc` seg forskjellig.  `loc` tar med sluttindeksen
i spennet, mens `iloc` gjør det ikke.

---

+ `[]` - søyler
+ `.loc[]` - rader
+ `.iloc[]` - rader
+ `.loc[2:10,"Tonn"]`

note:
Beklager.  Dette blir lett rotete, og det kommer til å bli litt 
prøving og feiling, før dere blir fortrolige med *data frames*.
For å oppsummere, bruker pandas tre forskjellige indekseringsformater.
Bare klammeparenteser for søyler og `loc` og `iloc` for rader.
I tillegg kan `loc` brukes til å indeksere på både rader og søyler
samtidig.

Prinsippene er stort sett de samme som for å indeksere andre typer objekter, 
men fordi pandas ønsker å gjøre det enkelt å bruke både tallindeks og *labels*, og
å indeksere både rader og søyler, trengs disse ekstra variantene med `loc` og `iloc`.

---
<!-- slide template="[[tpl-smalltext]]" -->
# Filtrering
```
In [52]: df2 = df[ df["varegruppe"] == "Fersk oppalen laks" ]

In [53]: df2
Out[53]: 
              varegruppe      uke   Tonn  kr/kg
0     Fersk oppalen laks  2000U01   3728  30.98
1     Fersk oppalen laks  2000U02   4054  31.12
2     Fersk oppalen laks  2000U03   4043  31.03
3     Fersk oppalen laks  2000U04   3730  30.95
4     Fersk oppalen laks  2000U05   3831  31.30
...                  ...      ...    ...    ...
1290  Fersk oppalen laks  2024U39  29238  73.23
1291  Fersk oppalen laks  2024U40  26543  69.70
1292  Fersk oppalen laks  2024U41  25180  72.76
1293  Fersk oppalen laks  2024U42  25561  76.02
1294  Fersk oppalen laks  2024U43  24910  77.59

[1295 rows x 4 columns]
```

::: credit
:::

---

## Pandas DataFrame

* `data` variabelen vi fyller dataframen vår med kan ha flere former:
 - 2d-array
 - dictionary -> `{col0: [data0], col1: [data1], ...}`
 - pandas Series

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
import pandas as pd
import numpy as np
data1 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(data1)
df1 = pd.DataFrame(data1, columns=["høyde", "vekt", "omkrets"], index=range(2,5))
df1
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
data2 = {"BNP": [1,2,3,4], "levealder": [88,88,99,102], 
         "styresett": ["demokrati", "diktatur", "demokrati", "monarki"]}
df2 = pd.DataFrame(data2, index=["Norge", "Uganda", "Sverige", "England"])
df2
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
indeks = ["BNP", "levealder", "styresett"]
serie1 = pd.Series([1,88,"demokrati"], name="Norge", index =indeks )
serie2 = pd.Series([2,88,"diktatur"], name="UGanda", index=indeks)
df3 = pd.DataFrame([serie1, serie2])
df3
```

---

## Manipulere Frame/Series

Vi vil kanskje kunne trenge å:
* Forandre indeks, navn på serie, eller navn på kolonner
* Legge til rad, eller kolonne til dataframe
* Bytte om på rad/kolonne
* Fjerne rad eller kolonne

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
data_land = ["England", "Norge", "Sverige"]
land = pd.Series(data_land)

#Forandre/hente navn på serie med min_serie.name
land.name = "land"

indeks = ["GB", "NO", "SE"]

#Hent eller sett en series index med min_sere.index
land.index= indeks
land["NO"] = "Danmark"

#land.index[1] = "DK" Vi må skifte hele indeksen
indeks = ["GB", "DK", "SE"]
land.index = indeks

#Vi legger til nye element på samme måte som i dictionaries
land["NOO"]= "Norge" # Legg til nytt element.

land = land.rename({"NOO": "NU"}) #Skift navn 
#Merk at .rename() ikke skifter navnet, men returnerer en ny Serie med skiftet
land.rename({"NU": "NO"}, inplace=True) #inplace=True gjør "fikser" på dette
land
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
data_innbyggere = [56, 6, 10]
land_innbyggere = pd.Series(data_innbyggere, name="innbyggere", index=indeks)

df_land = pd.DataFrame([land, land_innbyggere])
df_land = df_land.T # Bytter om på kolonner/rader (Transponerer)
df_land = df_land.rename(columns=({'land': 'navn'})) #Nytt navn til kolonne
df_land.loc['DK', 'navn'] = "Island" #Skifter landenavn til island
df_land.loc['DK', 'innbyggere'] = 0.4 #antall innbyggere til 0.4
df_land.rename(index={'DK': 'IS'}, inplace=True) #Nytt navn på indeks "DK"
df_land.loc["NO", "innbyggere"] = 5 # Oppdaterer data

df_land.loc["DK"] = ["Danmark", 6] #Legg til ny rad
df_land.loc["DE"] = {"navn": "Tyskland"} #Legg til rad med manglende data
df_land.loc["DE", "innbyggere"] = 80 #Oppdater data
df_land
```

+++ {"slideshow": {"slide_type": "slide"}}

### Oppg 5:
Ta utgangpunkt i tabellen over for å lage tabellen under
![oppg5](img/df_oppg5v2.png)

les [her](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html) for å finne ut hvordan du legger til en kolonne med `insert`

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
df_land.rename(columns=({"innbyggere": "populasjonsstørrelse"}), inplace=True)
df_land.drop(index=['NO'], inplace=True)
df_land.insert(2,"arbeidsledighet", ["1.0%","4.9%","3.2%","1.6%","12.5%" ])
df_land.loc["DE", "populasjonsstørrelse"]  = 83
df_land.loc["US"] = ["USA", 300, "50%"]
df_land
```

---

### Oppg 6
Hva er gjennomsnittlig arbeidsledighet til landene over?

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
arbeids_ledighet = df_land["arbeidsledighet"]
arbeidsledighet_formatert = [float(s[:-1]) for s in arbeids_ledighet]
gjennomsnitt = sum(arbeidsledighet_formatert)/len(arbeidsledighet_formatert)
print(f"Gjennomsnittlig arbeidsledighet er {round(gjennomsnitt,1)}%")
```


---
## Utdjupin


* Når vi behandler store mengder data og data fra ulike kilder trenger vi å ha kontroll på hvordan dataen vår representeres internt i datamaskinen
```python
data = np.array([..... ], dtype=«numpy datatype»)
```
* `numpy` har flere ulike datatyper vi kan bruke


| **Type**       | **Name**     | **Description**                                                   |
| -------------- | ------------ | ----------------------------------------------------------------- |
| Integer        | `int8`       | Integer (-128 to 127)                                             |
| Integer        | `int16`      | Integer (-32,768 to 32,767)                                       |
| Integer        | `int32`      | Integer (-2,147,483,648 to 2,147,483,647)                         |
| Integer        | `int64`      | Integer (-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807) |
| Unsigned Int   | `uint8`      | Unsigned integer (0 to 255)                                       |
| Unsigned Int   | `uint16`     | Unsigned integer (0 to 65,535)                                    |
| Unsigned Int   | `uint32`     | Unsigned integer (0 to 4,294,967,295)                             |
| Unsigned Int   | `uint64`     | Unsigned integer (0 to 18,446,744,073,709,551,615)                |
| Floating Point | `float16`    | Half precision floating point                                     |
| Floating Point | `float32`    | Single precision floating point                                   |
| Floating Point | `float64`    | Double precision floating point                                   |
| Complex Number | `complex64`  | Complex number (real and imaginary as `float32`)                  |
| Complex Number | `complex128` | Complex number (real and imaginary as `float64`)                  |
| Boolean        | `bool_`      | Boolean (True or False)                                           |
| String         | `string_`    | Fixed-size string data                                            |
| Unicode String | `unicode_`   | Fixed-size Unicode string data                                    |

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

### DataFrame-data
* Merk at dersom vi forandrer datavariabelen, forandres også pandas serien
* Vi sier at dataframen inneholder «refererer» til data som er lagret et annet sted
* Dersom dette ikke er ønskelig kan vi bruke `copy=True` når vi lager serien
* Av og til vil vi ha en kopi som ikke forstyrrer «datakilden»
* Av og til vil vi ikke gjøre det slik -- det er raskere og bruker mindre minne

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
dataserie = pd.Series(data, name=navn, index=indeks, copy=True)
print(dataserie)
data[2]=66
dataserie
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}


## Metoder

* Pandas Series objekter har flere nyttige *metoder*

+++ {"editable": true, "slideshow": {"slide_type": "fragment"}}

| **Metode**            | **Beskrivelse**                                                                  |
|-----------------------|----------------------------------------------------------------------------------|
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

---

# Notar


+ *Basert på førelesingsnotat frå veke 41/2024.  Sjå nokre andre notat og oppslagstabellar i [[Pandas-Series-DataFrames-JH]]*
+ [[Døme med pickle]]
* Pandas er et bibliotek for python for å manipulere og analysere data
	* me brukte det fyrst i [[Fyrste datasett med CSV]]
* Vi importerer pandas med som regel med `import pandas as pd`
* Pandas er bygd på numpy, så man trenger ofte også å bruke numpy
	
* Vi bruker pandas til å laste inn eller lage datasett
    - Rydde opp i data
    - Få det over på annet format
    - Gjøre statistikk
    - Plotte data
* Dersom vi mangler noe data for en indeks bruker vi `np.NaN`som data
    
---
<img src="img/dfnavn1.jpg" width="550">


![dataframe_indeksnavn](img/dfnavn2.png)

---

```{code-cell} ipython3
sdata = {"frukt": ["epler", "pærer", "moreller", "rips"], "produksjon": [12,23,1,9], "subsidiert": [True, False, True, False], "pris": [10, 25, 40, 5]}
df_bilde = pd.DataFrame(sdata)
df_bilde
```

```{code-cell} ipython3
---
slideshow:
  slide_type: skip
---
sdata2 = { "produksjon": [12,23,1,9], "subsidiert": [True, False, True, False], "pris": [10, 25, 40, 5]}
df_bilde2 = pd.DataFrame(sdata2, index = ["epler", "pærer", "moreller", "rips"])
df_bilde2
```


---

### Oppgave 1:

* Lag dataserien under i pandas:
![oppg1](img/series_oppg1.png)

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
data = np.array([187,177,195,159], dtype="float64")
indeks = ["Per", "Pål", "Espen", "Askeladd"]
navn = "EventyrfigurHøyde"
dataserie = pd.Series(data, name=navn, index=indeks, copy=True)
dataserie
```

