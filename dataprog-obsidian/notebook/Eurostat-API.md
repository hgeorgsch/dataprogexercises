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

```{code-cell} ipython3
from pyjstat import pyjstat
import matplotlib.pyplot as plt
import pandas as pd
import requests, json
```

# Eurostat
Eurostat har flere typer web-api:
- **Statistics:** Standard REST-api til
- **sdmx 2.1, sdmx 3:**  Proffe og krafitge standarder for utveksling av statistisk data 
- **catalogue api:** API til å søke gjennom og finne dataset

```{code-cell} ipython3

```

## Statistics
- Vi velger å se på *statistics* apiet

![](https://ec.europa.eu/eurostat/documents/19009692/20123432/structure-rest-request.png/0164d56d-495a-94ec-638d-1af93be0062d?t=1728057499783)

Det er ikke så ulikt ssb sitt web-api. Vi har en url med blant annet tabellnummeret vi vil hente data fra (tabellkode, i dett tilfelle), og bak seperator `?` kommer url-parametre som angir datauttrekk, filtrering språk og format.
Eurostat har også en «statistikkbank» vi kan bla i for å se på dataene og vi kan også her velge å lager en lenke med api-spørringen. I tillegg har vi et *meget nyttig* [verktøy for å bygge spørringer til statistics api-et](https://ec.europa.eu/eurostat/web/query-builder/tool). 



## Tips til bruk

1. Se gjennom tabellen og gjør utvalg på nettsiden til eurostat
    - Hent eventuelt ut «dimensjoner» du trenger og lag spørringen for hånd
3. Du kan under «download» velge å få en URL du bruker med `GET` for å hente dataene
4. Du kan bygge spørringen med [vektøyet](https://ec.europa.eu/eurostat/web/query-builder/tool)

Dersom man vil bla gjennom datasettene, hente ut metadata og bygge spørringen helt fra scratch i python må man ta i bruk det mer avanserte sdmx 3 APIet.
Det er en kraftig standard 

+++



+++

*Oversiktstabeller generert av chat-gpt*

### Filter
| Tema                                | Parameter / mønster                    | Hva det gjør                              | Eksempel                                 | Viktige regler / fallgruver                                                                                                          |
| ----------------------------------- | -------------------------------------- | ----------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Grunnfilter**                     | `<DIM>=<VALUE>`                        | Filtrerer på én dimensjon                 | `geo=NO`                                 | Dimensjonen må finnes i datasettet. Filterparametre er valgfrie. ([European Commission][1])                                          |
| **Flere dimensjoner**               | `&` mellom parametre                   | Kombinerer filtre (AND-logikk)            | `geo=NO&unit=PC_ACT`                     | Returnerer kun observasjoner som matcher **alle** oppgitte filtre. ([European Commission][1])                                        |
| **Flere verdier i samme dimensjon** | Gjenta samme parameter                 | Velger flere kategorier i samme dimensjon | `geo=NO&geo=SE&geo=DK`                   | Dette er standardmåten i Statistics API. ([European Commission][1])                                                                  |
| **“Alle verdier” i en dimensjon**   | **Ikke ta med dimensjonen i filteret** | Henter alle kategorier i den dimensjonen  | *(utelat `geo` helt)*                    | Ingen egen wildcard (`*`) i denne filterstilen; utelat filteret. Filterparametre er valgfrie. ([European Commission][1])             |
| **Filterrekkefølge**                | Valgfri rekkefølge                     | Samme resultat uansett rekkefølge         | `time=2024&geo=NO` vs `geo=NO&time=2024` | Trenger ikke følge dimensjonsrekkefølgen i datasettet. ([European Commission][1])                                                    |
| **Store/små bokstaver**             | Case-insensitive                       | `geo=no` og `geo=NO` fungerer likt        | `unit=pc_act`                            | Eurostat oppgir at dimensjonskoder og verdier er case-insensitive i query. ([European Commission][1])                                |
| **Responsformat (ikke filter)**     | `format=`                              | Styrer format på respons                  | `format=JSON`                            | Ser ut som filter, men er teknisk en query-parameter for responsen. Statistics API leverer JSON-stat 2.0. ([European Commission][2]) |
| **Språk (ikke filter)**             | `lang=`                                | Språk på labels/tekst                     | `lang=EN`                                | Statistics API oppgis å levere EN/FR/DE. Fint å bruke `EN` i undervisning. ([European Commission][2])                                |

[1]: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines/api-statistics?utm_source=chatgpt.com "Detailed guidelines - API Statistics - User guides - Eurostat"
[2]: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-getting-started?utm_source=chatgpt.com "API - Getting started - User guides - Eurostat"

+++

## Spesialfilter

+++

Eurostat har egne spesialfilter på tid og sted (geo) som fungerer litt annerledes enn bare `dimensjon=verdi`
### Tid
| Tema                                       | Parameter                             | Hva det gjør                                  | Eksempel                                    | Viktige regler / fallgruver                                                                                                                          |
| ------------------------------------------ | ------------------------------------- | --------------------------------------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Eksakt tid (alias 1)**                   | `time=`                               | Filtrerer `TIME_PERIOD` på en spesifikk verdi | `time=2024`                                 | `time` og `time_period` adresserer samme tidsdimensjon. ([European Commission][1])                                                                   |
| **Eksakt tid (alias 2)**                   | `time_period=`                        | Samme som `time=`                             | `time_period=2024`                          | Kan brukes om hverandre. ([European Commission][1])                                                                                                  |
| **Fra og med tid**                         | `sinceTimePeriod=`                    | Henter data fra og med gitt periode           | `sinceTimePeriod=2019`                      | Nyttig for “alle nyere data”. ([European Commission][1])                                                                                             |
| **Til og med / frem til tid**              | `untilTimePeriod=`                    | Henter data frem til gitt periode             | `untilTimePeriod=2024`                      | Nyttig for historiske utsnitt. ([European Commission][1])                                                                                            |
| **Siste N perioder**                       | `lastTimePeriod=`                     | Henter de siste N tilgjengelige periodene     | `lastTimePeriod=12`                         | Veldig nyttig når du ikke vet siste måned/kvartal på forhånd. ([European Commission][1])                                                             |
| **Tidsintervall (anbefalt spesialfilter)** | `sinceTimePeriod` + `untilTimePeriod` | Henter intervall                              | `sinceTimePeriod=2015&untilTimePeriod=2024` | Dette er **det eksplisitte unntaket** som er tillatt sammen. ([European Commission][1])                                                              |
| **Flere tidsparametre samtidig**           | (generelt ikke tillatt)               | Avviser kombinasjoner av flere tidsparametre  | f.eks. `time=2024&lastTimePeriod=12`        | Eurostat sier at bruk av mer enn én tidsparameter ikke er akseptert, med unntak av `sinceTimePeriod` + `untilTimePeriod`. ([European Commission][1]) |
| **Ingen tidsfilter**                       | utelat `time` og tidsparametre        | Henter alle tilgjengelige tidsverdier         | *(ingen tidsparameter)*                     | Kan gi store responser; fint å kombinere med `lastTimePeriod`. ([European Commission][1])                                                            |

[1]: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines/api-statistics?utm_source=chatgpt.com "Detailed guidelines - API Statistics - User guides - Eurostat"

### Sted

| Tema                          | Parameter               | Hva det gjør                               | Eksempel                     | Viktige regler / fallgruver                                                                        |
| ----------------------------- | ----------------------- | ------------------------------------------ | ---------------------------- | -------------------------------------------------------------------------------------------------- |
| **Eksplisitte geografikoder** | `geo=`                  | Filtrerer på konkrete geografier           | `geo=NO&geo=SE`              | Enklest og best for nybegynnere. ([European Commission][1])                                        |
| **Geografi etter nivå**       | `geoLevel=`             | Henter geografier etter nivåtype           | `geoLevel=country`           | Spesialparameter for GEO-dimensjonen. ([European Commission][1])                                   |
| **Aggregater**                | `geoLevel=aggregate`    | Henter europeiske aggregater (EU/EA m.fl.) | `geoLevel=aggregate`         | Kan gi EU/EA-aggregater etter Eurostats hvitliste. ([European Commission][1])                      |
| **Landnivå**                  | `geoLevel=country`      | Henter landkoder                           | `geoLevel=country`           | Praktisk hvis du vil vise “alle land” uten å liste `geo=` mange ganger. ([European Commission][1]) |
| **NUTS nivå 1**               | `geoLevel=nuts1`        | Henter NUTS1-regioner                      | `geoLevel=nuts1`             | Regionalt nivå (mer avansert bruk). ([European Commission][1])                                     |
| **NUTS nivå 2**               | `geoLevel=nuts2`        | Henter NUTS2-regioner                      | `geoLevel=nuts2`             | Vanlig i regionalstatistikk. ([European Commission][1])                                            |
| **`geo` + `geoLevel` sammen** | **Ikke tillatt**        | Gir feil                                   | `geo=NO&geoLevel=country`    | Gjensidig utelukkende; Eurostat oppgir at dette gir 400-feil. ([European Commission][1])           |
| **Ingen geofilter**           | utelat `geo`/`geoLevel` | Henter alle geografier i datasettet        | *(ingen geografi-parameter)* | Kan bli mye data; kombiner gjerne med tid/filter på indikator. ([European Commission][1])          |

[1]: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines/api-statistics?utm_source=chatgpt.com "Detailed guidelines - API Statistics - User guides - Eurostat"

+++

Vi begynner med å laste ned lenke rett fra eurostats «statistikkbank»


::: {image} eurostat_lagresporring.png
:align: center
:::
Trykk og velg ut statistikkvariabler i utforskeren, og når du er fornøyd kan du trykke «download» velge format «json_stat» og kopiere «API-lenken»

```{code-cell} ipython3
# Hent fra downloads
url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/lfsq_urgan$defaultview/1.0?compress=false&format=json&lang=en"

dataset = pyjstat.Dataset.read(url)
df = dataset.write("dataframe")
df
```



::: {image} eurostat_kode.png
:align: center
:::


Skal vi bygge API-lenken fra bunnen av, setter vi bare inn datasetkoden inn i url-strukturen slik den er vist helt øverst. Bildet over viser datasetkoden under hovedtittelen på datasettet på redigeringssiden, men det dukker opp de fleste steder. Standardparametere er format (vi anbefaler json) og lang=EN. 

```{code-cell} ipython3
#Bygg selv fra bunn av
# Standard url
url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsq_urgan?format=JSON&lang=EN"


response = requests.get(url)
response.raise_for_status()
dataset = pyjstat.Dataset.read(response.text)
df = dataset.write("dataframe")
df
```

Her ser vi at datasettet inneholder drøye 2.5 millioner rader, og vi kan òg merke at det tar en del tid å laste det ned fra Eurostat.
Dersom vi ikke har behov for alle datene, vil det kunne lønne seg å gjøre filtreringer i spørringen vår, heller enn å laste inn alt og fjerne det vi ikke trenger.

+++

::: {tip} Hvilke data har vi?
En god funksjon å bruke når vi prøver å få oversikt over hvilke data vi har tilgjengelig er:
```python
df["Statistisk variabel"].unique()
```
som gir deg de ulike (unike) verdiene i kolonnen

```{code-cell} ipython3
#df["Age class"].unique()
#df["Country of citizenship"].unique()
#df["Geopolitical entity (reporting)"].unique() 
df
```

Etter å ha sett på innholdet beslutter vi at vi vil ha:

- Data for aldersgruppe 15 til 74 år
- Arbeidsledighet for alle statsborgerskap (totalt)
- Tall for de siste 3 årene
- Tall for alle *land* ingen aggregerte spesialsoner e.l.

Oppgaven blir nå å bruke forskjellige filtreringsmulighetene fra tabellene over til å bygge urlparametere til spørringen.
Tid og geografisk område har en del spesialfilter, `geoLevel = country` gir oss kun land, slik vi ville. 
Dersom vi vil ha de siste 3 årene kunne vi brukt flere av filterene. Vi kan manuelt liste de opp, bruke `sinceTimePeriod` eller `lastTimePeriod`.

For alder og statsborgerskap skal vi bare velge 1 verdi *MEN*: Dataframet vårt har leselige etiketter for kjønn, statsborgerskap osv, mens vi trenger *id* kodene til variabel og verdi. Denne informasjonen ligger i datasettet vi leste inn med pyjstat, og vi kan undersøke det ved å gi ekstraargumentet `naming="id"` når vi skriver det til et dataframe:
```
df_id = dataset.write("dataframe", naming="id")
```

```{code-cell} ipython3
df = dataset.write("dataframe", naming="id")
df
```

I dette tilfellet klarer vi faktisk å lese ut at vi skal filtrere for `age=Y15-74` og `citizen=TOTAL`, men det er ikke sikkert dette alltid er like lett, eller lar seg gjøre. Vi kan i datavisningen til eurostat også trykke «customize your dataset», og lese ut id-kodene vi trenger


::: {image} eurostat_customize.png
:align: center
:::

```{code-cell} ipython3
#Bygg filter, på alder, statsborgerskap og siste 3 år. Be om kun land.

url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsq_urgan?format=JSON&lang=EN"

params = {"age": "Y15-74", "citizen": "total", "lasttimeperiod": 12, "geoLevel": "country"}

response = requests.get(url, params=params)
response.raise_for_status()
dataset = pyjstat.Dataset.read(response.text)
df = dataset.write("dataframe")
```

```{code-cell} ipython3
#Vis
df
```

## Anbefalt: Query builder

Eurostat har som sagt et supert verktøy som lar deg bygge spørringen: [](https://ec.europa.eu/eurostat/web/query-builder/tool)


::: {image} eurostat_tool.png
:align: center
:::

Her velger vi ut filtreringene vi vil ha, og trykker «generate query» for å få en lenke. Merk at denne er annerledes enn url vi fikk fra «Download»-metoden; Den bruker nemlig statistics-apiet, hvilket betyr at vi kan redigere med python som lenger oppe.

```{code-cell} ipython3
# Url bygget med "query builder"
url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsq_urgan?format=JSON&lastTimePeriod=12&geo=BE&geo=BG&geo=CZ&geo=DK&geo=DE&geo=EE&geo=IE&geo=EL&geo=ES&geo=FR&geo=HR&geo=IT&geo=CY&geo=LV&geo=LT&geo=LU&geo=HU&geo=MT&geo=NL&geo=AT&geo=PL&geo=PT&geo=RO&geo=SI&geo=SK&geo=FI&geo=SE&geo=IS&geo=NO&geo=CH&geo=UK&geo=BA&geo=ME&geo=MK&geo=RS&geo=TR&unit=PC&sex=F&sex=M&sex=T&age=Y15-74&citizen=TOTAL&lang=EN"

dataset = pyjstat.Dataset.read(url)
df_tool = dataset.write("dataframe")
df_tool
```

::: {note} Oppgave
1. Lag en funksjon `hent_url_parametere(url)`som bruker `urllib` funksjonene fra fagstoffet om ssb-apiet til å hente ut url-parametere av en lang url
2. Lag en funksjon `hent_endepunkt(url)` som bruker samme bibliotek til å hente ut alt frem til url-parameterene fra en lang url
3. Bruk funksjonene over til å lese inn parametere fra den lange urlen fra query-builder over og gjør noen endringer.
4. Send spørringen med `requests.get` og les det inn med pyjstat til pandas
:::

+++

### Noen raske eksempler

```{code-cell} ipython3
#Plot arbeidsledighet i norden
df1 = df[["Time", "Sex", "Geopolitical entity (reporting)", "value"]].copy()
df1["Time"] = pd.PeriodIndex(df1["Time"], freq="Q")

df1["Geopolitical entity (reporting)"].unique()

nordisk_liste = ["Norway", "Sweden", "Denmark", "Finland", "Iceland"]

df_norden = df1 [  (df1["Sex"] == "Total")
        &(df1["Geopolitical entity (reporting)"].isin(nordisk_liste))
    ]
fig, ax = plt.subplots()
for navn , gruppe in gruppering:
    gruppe.plot(x="Time", y="value", ax=ax, label=navn)

plt.title("Arbeidsledighet i norden")
```

```{code-cell} ipython3
# Arbeidsledighet, stolpe m kjønn for Finland

df_fin = df1 [  ~(df1["Sex"] == "Total")
        &(df1["Geopolitical entity (reporting)"].str.contains("Finl"))
    ]
df_fin.pivot(index="Time", columns="Sex", values="value").plot.bar(stacked=True)
```

# OPPGAVE

::: {note} Konkurser

1. Finn data om åpnede konkurser i norden og less de inn i python gjennom apiet til eurostat.
2. Slå dataene sammen med data om arbeidsledighet i norden
3. Gjør noe egnet statistikk eller visualiseringer av dataene (etter eget ønske)

:::
