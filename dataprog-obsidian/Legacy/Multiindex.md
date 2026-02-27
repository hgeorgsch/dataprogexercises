---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.18.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Multi-index

* Når vi har fått lest inn, vasket og preppet dataene våres skal vi gjøre noe med de
* Typisk trenger vi og trekke ut forskjellige deler av dataene - og visualisere de, eller kjøre noe statistikk på de (sum, average osv)
* Når det kommer til å velge ut data har vi sett på:
  * Velge ut rader og kolonner med `.loc[]`
  * Filtrere data med uttrykk som `df[df["alder"] > 25]`
* En annen nyttig måte, er å strukturere dataene med flere nivå på indeks eller kolonnekategorier, og gjøre utvalg og slice på disse




```python
import pandas as pd
import requests, json
from pyjstat import pyjstat
```

```python
url = "https://data.ssb.no/api/pxwebapi/v2/tables/07459/data?lang=no&valueCodes[Region]=K-3101,K-3103,K-3105,K-3107,K-3110,K-3112,K-3114,K-3116,K-3118,K-3120,K-3122,K-3124,K-3201,K-3203,K-3205,K-3207,K-3209,K-3212,K-3214,K-3216,K-3218,K-3220,K-3222,K-3224,K-3226,K-3228,K-3230,K-3232,K-3234,K-3236,K-3238,K-3240,K-3242,K-0301,K-3301,K-3303,K-3305,K-3310,K-3312,K-3314,K-3316,K-3318,K-3320,K-3322,K-3324,K-3326,K-3328,K-3330,K-3332,K-3334,K-3336,K-3338,K-3401,K-3403,K-3405,K-3407,K-3411,K-3412,K-3413,K-3414,K-3415,K-3416,K-3417,K-3418,K-3419,K-3420,K-3421,K-3422,K-3423,K-3424,K-3425,K-3426,K-3427,K-3428,K-3429,K-3430,K-3431,K-3432,K-3433,K-3434,K-3435,K-3436,K-3437,K-3438,K-3439,K-3440,K-3441,K-3442,K-3443,K-3446,K-3447,K-3448,K-3449,K-3450,K-3451,K-3452,K-3453,K-3454,K-3901,K-3903,K-3905,K-3907,K-3909,K-3911,K-4001,K-4003,K-4005,K-4010,K-4012,K-4014,K-4016,K-4018,K-4020,K-4022,K-4024,K-4026,K-4028,K-4030,K-4032,K-4034,K-4036,K-4201,K-4202,K-4203,K-4204,K-4205,K-4206,K-4207,K-4211,K-4212,K-4213,K-4214,K-4215,K-4216,K-4217,K-4218,K-4219,K-4220,K-4221,K-4222,K-4223,K-4224,K-4225,K-4226,K-4227,K-4228,K-1101,K-1103,K-1106,K-1108,K-1111,K-1112,K-1114,K-1119,K-1120,K-1121,K-1122,K-1124,K-1127,K-1130,K-1133,K-1134,K-1135,K-1144,K-1145,K-1146,K-1149,K-1151,K-1160,K-4601,K-4602,K-4611,K-4612,K-4613,K-4614,K-4615,K-4616,K-4617,K-4618,K-4619,K-4620,K-4621,K-4622,K-4623,K-4624,K-4625,K-4626,K-4627,K-4628,K-4629,K-4630,K-4631,K-4632,K-4633,K-4634,K-4635,K-4636,K-4637,K-4638,K-4639,K-4640,K-4641,K-4642,K-4643,K-4644,K-4645,K-4646,K-4647,K-4648,K-4649,K-4650,K-4651,K-1505,K-1506,K-1508,K-1511,K-1514,K-1515,K-1516,K-1517,K-1520,K-1525,K-1528,K-1531,K-1532,K-1535,K-1539,K-1547,K-1554,K-1557,K-1560,K-1563,K-1566,K-1573,K-1576,K-1577,K-1578,K-1579,K-1580,K-5001,K-5006,K-5007,K-5014,K-5020,K-5021,K-5022,K-5025,K-5026,K-5027,K-5028,K-5029,K-5031,K-5032,K-5033,K-5034,K-5035,K-5036,K-5037,K-5038,K-5041,K-5042,K-5043,K-5044,K-5045,K-5046,K-5047,K-5049,K-5052,K-5053,K-5054,K-5055,K-5056,K-5057,K-5058,K-5059,K-5060,K-5061,K-1804,K-1806,K-1811,K-1812,K-1813,K-1815,K-1816,K-1818,K-1820,K-1822,K-1824,K-1825,K-1826,K-1827,K-1828,K-1832,K-1833,K-1834,K-1835,K-1836,K-1837,K-1838,K-1839,K-1840,K-1841,K-1845,K-1848,K-1851,K-1853,K-1856,K-1857,K-1859,K-1860,K-1865,K-1866,K-1867,K-1868,K-1870,K-1871,K-1874,K-1875,K-5501,K-5503,K-5510,K-5512,K-5514,K-5516,K-5518,K-5520,K-5522,K-5524,K-5526,K-5528,K-5530,K-5532,K-5534,K-5536,K-5538,K-5540,K-5542,K-5544,K-5546,K-5601,K-5603,K-5605,K-5607,K-5610,K-5612,K-5614,K-5616,K-5618,K-5620,K-5622,K-5624,K-5626,K-5628,K-5630,K-5632,K-5634,K-5636,K-21-22,K-23,K-Rest&valueCodes[Kjonn]=2,1&valueCodes[Alder]=F00-09,F10-19,F20-29,F30-39,F40-49,F50-59,F60-69,F70-79,F80-89,F90-99&valueCodes[Tid]=1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025&valueCodes[ContentsCode]=Personer1&codelist[Region]=agg_KommSummer&outputValues[Region]=aggregated&codelist[Alder]=agg_TiAarigGruppering&outputValues[Alder]=aggregated"
url = r"https://data.ssb.no/api/pxwebapi/v2/tables/07459/data?lang=no&valueCodes[Region]=K-3101,K-3103,K-3105,K-3107,K-3110,K-3112,K-3114,K-3116,K-3118,K-3120,K-3122,K-3124,K-3201,K-3203,K-3205,K-3207,K-3209,K-3212,K-3214,K-3216,K-3218,K-3220,K-3222,K-3224,K-3226,K-3228,K-3230,K-3232,K-3234,K-3236,K-3238,K-3240,K-3242,K-0301,K-3301,K-3303,K-3305,K-3310,K-3312,K-3314,K-3316,K-3318,K-3320,K-3322,K-3324,K-3326,K-3328,K-3330,K-3332,K-3334,K-3336,K-3338,K-3401,K-3403,K-3405,K-3407,K-3411,K-3412,K-3413,K-3414,K-3415,K-3416,K-3417,K-3418,K-3419,K-3420,K-3421,K-3422,K-3423,K-3424,K-3425,K-3426,K-3427,K-3428,K-3429,K-3430,K-3431,K-3432,K-3433,K-3434,K-3435,K-3436,K-3437,K-3438,K-3439,K-3440,K-3441,K-3442,K-3443,K-3446,K-3447,K-3448,K-3449,K-3450,K-3451,K-3452,K-3453,K-3454,K-3901,K-3903,K-3905,K-3907,K-3909,K-3911,K-4001,K-4003,K-4005,K-4010,K-4012,K-4014,K-4016,K-4018,K-4020,K-4022,K-4024,K-4026,K-4028,K-4030,K-4032,K-4034,K-4036,K-4201,K-4202,K-4203,K-4204,K-4205,K-4206,K-4207,K-4211,K-4212,K-4213,K-4214,K-4215,K-4216,K-4217,K-4218,K-4219,K-4220,K-4221,K-4222,K-4223,K-4224,K-4225,K-4226,K-4227,K-4228,K-1101,K-1103,K-1106,K-1108,K-1111,K-1112,K-1114,K-1119,K-1120,K-1121,K-1122,K-1124,K-1127,K-1130,K-1133,K-1134,K-1135,K-1144,K-1145,K-1146,K-1149,K-1151,K-1160,K-4601,K-4602,K-4611,K-4612,K-4613,K-4614,K-4615,K-4616,K-4617,K-4618,K-4619,K-4620,K-4621,K-4622,K-4623,K-4624,K-4625,K-4626,K-4627,K-4628,K-4629,K-4630,K-4631,K-4632,K-4633,K-4634,K-4635,K-4636,K-4637,K-4638,K-4639,K-4640,K-4641,K-4642,K-4643,K-4644,K-4645,K-4646,K-4647,K-4648,K-4649,K-4650,K-4651,K-1505,K-1506,K-1508,K-1511,K-1514,K-1515,K-1516,K-1517,K-1520,K-1525,K-1528,K-1531,K-1532,K-1535,K-1539,K-1547,K-1554,K-1557,K-1560,K-1563,K-1566,K-1573,K-1576,K-1577,K-1578,K-1579,K-1580,K-5001,K-5006,K-5007,K-5014,K-5020,K-5021,K-5022,K-5025,K-5026,K-5027,K-5028,K-5029,K-5031,K-5032,K-5033,K-5034,K-5035,K-5036,K-5037,K-5038,K-5041,K-5042,K-5043,K-5044,K-5045,K-5046,K-5047,K-5049,K-5052,K-5053,K-5054,K-5055,K-5056,K-5057,K-5058,K-5059,K-5060,K-5061,K-1804,K-1806,K-1811,K-1812,K-1813,K-1815,K-1816,K-1818,K-1820,K-1822,K-1824,K-1825,K-1826,K-1827,K-1828,K-1832,K-1833,K-1834,K-1835,K-1836,K-1837,K-1838,K-1839,K-1840,K-1841,K-1845,K-1848,K-1851,K-1853,K-1856,K-1857,K-1859,K-1860,K-1865,K-1866,K-1867,K-1868,K-1870,K-1871,K-1874,K-1875,K-5501,K-5503,K-5510,K-5512,K-5514,K-5516,K-5518,K-5520,K-5522,K-5524,K-5526,K-5528,K-5530,K-5532,K-5534,K-5536,K-5538,K-5540,K-5542,K-5544,K-5546,K-5601,K-5603,K-5605,K-5607,K-5610,K-5612,K-5614,K-5616,K-5618,K-5620,K-5622,K-5624,K-5626,K-5628,K-5630,K-5632,K-5634,K-5636,K-21-22,K-23,K-Rest&valueCodes[Kjonn]=2,1&valueCodes[Alder]=F00-09,F10-19,F20-29,F30-39,F40-49,F50-59,F60-69,F70-79,F80-89,F90-99&valueCodes[Tid]=1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025&valueCodes[ContentsCode]=Personer1&codelist[Region]=agg_KommSummer&outputValues[Region]=aggregated&codelist[Alder]=agg_TiAarigGruppering&outputValues[Alder]=aggregated"
response = requests.get(url)
# Det nye API-et oppfører seg ikke alltid
print("Status:", response.status_code)
```

```python
# Annen metode
# Dataset: https://www.ssb.no/statbank/table/07459/tableViewLayout1/
url = "https://www.ssb.no/statbank/sq/10116061"

response = requests.get(url)
# Send spørring
print("Status", response.status_code)
```

```python
# Les inn dataset til pandas
dataset = pyjstat.Dataset.read(response.text)
df = dataset.write("dataframe")

```

```python
df["år"] = pd.PeriodIndex(df["år"], freq="Y")
df
# Vask, filtrer og pivoter
df = df.pivot(index=["region", "år"], columns=["kjønn", "alder"], values="value")
df
```

## Multiindex fra pivot

* I cellen over har vi en indeks med to nivåer: region->år OG kolonneoverskrifter i to nivåer: kjønn->aldersgruppe
* Dette kalles multiindekser og de kan være litt tricky slå opp i

<!-- #region -->
### Utdrag av opplsagsmetoder (KI-generert)


| Metode                                 | Forklaring                                           | Eksempel (kode)                                                 | Resultat (forklart)                            |
| :------------------------------------- | :--------------------------------------------------- | :-------------------------------------------------------------- | :--------------------------------------------- |
| **Direkte oppslag med `loc`**          | Bruk tuppel (nivå1, nivå2) for å hente en rad        | `df.loc[('Oslo', 2020)]`                                 | Raden der *nivå 1 = 'Oslo'* og *nivå 2 = 2020* |
| **Oppslag på første nivå**             | Bruk bare første nivå for å hente *alle undernivåer* | `df.loc['Oslo']`                                         | Alle rader for byen *Oslo*                     |
| **Oppslag på flere nøkler (liste)**    | Bruk liste for å hente flere etiketter               | `df.loc[(['Oslo', 'Bergen'], 2020)]`                     | Rader for *Oslo* og *Bergen* i *2020*          |
| **`xs()` (cross section)**             | Hent verdier fra ett nivå med `level`-argument       | `df.xs('Oslo', level='By')`                              | Alle rader der *By = 'Oslo'*, uansett år       |
| **`xs()` på indre nivå**               | Bruk nivå 2 uten å måtte angi hele tuppelen          | `df.xs(2020, level='År')`                                | Alle byer i *2020*                             |
| **Flere nivå samtidig (xs med tuple)** | Angi begge nivå                                      | `df.xs(('Oslo', 2020))`                                  | Samme som `df.loc[('Oslo', 2020)]`             |
| **`loc` med slice**                    | Hent ut et område fra indeksen                       | `df.loc[('Oslo', 2019):('Oslo', 2021)]`                  | Alle rader mellom 2019–2021 for Oslo           |
| **`IndexSlice`**                       | Praktisk måte å slice på tvers av nivåer             | `idx = pd.IndexSlice; df.loc[idx['Oslo', 2019:2021], :]` | Samme som over, men mer lesbart                |


<!-- #endregion -->

* Ved enkle direkte oppslag, eller oppslag kun i ytterste nivå bruker vi gjerne `.loc[]` som vanlig (eller med tupler)

```python
# Slå opp på Ålesund 1987 og plot barplott av aldersfordeling av menn
df.loc[("Ålesund", "1987"), "Menn"].plot.bar()
```

```python
# # Slå opp på Ålesund 1987 og plot barplott av aldersfordeling av menn og kvinner
df.loc[("Ålesund", "1987"), :].plot.bar()
# Ikke helt slik vi vil ha det...
```

```python

```

### Stack / Unstack
* `plot.bar()`lager bar plot med indeks langs x, og stolper av alle kolonnene
* Vi kan bruke `stack` og `unstack` til å kjapt smelte/pivotere

```python
df.loc[("Ålesund", "1987"), :].unstack(0).plot.bar() # unstack(0) flytter nivå 0 opp langs kolonnene
unstakked = df.loc[("Ålesund", "1987"), :].unstack(0)
```

```python
# Stack Flytter kolonnene ned til index igjen (men er nå i innerste nivå)
unstakked.stack()
```

```python

```

## Slicing 
* Å «slice» betyr å «skjære ut» litt data - litt som å skjære ut en kakebit
* Typisk "slicer" vi alle år fra "1985" til, men ikke med, "2000" og aller kommuner fra "A" til (men ikke med) "R"
* Med multiindex bør dette gjøres med `pd.IndexSlice`

```python
idx = pd.IndexSlice

#Slice fra Forbokstav og år, og i kolonner med idx
df.loc[idx["E":"R", "1990":"2001"], idx["Kvinner", "0-9 år"]]
```

<!-- #region -->
* Pass på at indexer er *sortert* om du vil slice

  
  `df.sort_index()`
<!-- #endregion -->

### Krysstabell `.xs()`

* En praktisk funksjon å kunne er .xs (crosstable)
* Den velger ut 1 eller flere verdier over mange nivå, slår sammen og dropper nivå som ikke er i bruk
* Du kan gjøre det samme med `.loc` og `IndexSlice`, men det er ofte ryddigere med `.xs()`
* Standard er krysstabell langs indeks (axis=0), men vi kan bruke kolonner med (axis=1)

```python
# Velg ut data for 60-69-åringer i 2006 for alle kommuner
df_utdrag = df.xs("2006", level=1).xs("60-69 år", level=1, axis=1)

#Sjekk kjønnsrate og plot med histogram

df_utdrag["rate"] = df_utdrag["Menn"]/(df_utdrag["Menn"]+df_utdrag["Kvinner"])
df_utdrag["rate"].plot.hist(bins=20)

df_utdrag.idxmax()
```
