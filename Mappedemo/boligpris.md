---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Innledning

Boligmarkedet er en sentral del av norsk økonomi, og boligprisene har hatt betydelig vekst de siste tiårene. Samtidig påvirkes kjøpekraften av generell prisstigning i økonomien, målt gjennom konsumprisindeksen (KPI). For boligkjøpere er det derfor interessant å forstå ikke bare nominell prisutvikling, men også hvordan boligpriser utvikler seg relativt til inflasjon.

## Problemstilling

Hvordan har boligprisene i Norge utviklet seg sammenlignet med konsumprisindeksen, og hva sier dette om reell prisvekst i boligmarkedet?

```{code-cell} ipython3
import pandas as pd

df1 = pd.read_csv("1060.csv", sep=";", encoding="latin1")
print(df1.columns.tolist())
display(df1.head())
```

### Forklaring

Jeg har importert datasettet `1060.csv` fra Statistisk sentralbyrå med informasjon om boligprisindekser. Datasettet starter på 1992K1 fordi Statistisk sentralbyrå begynte å publisere prisindekser for brukte selveierboliger tidlig på 1990-tallet, etter kraftige prisfall i boligmarkedet på slutten av 1980- og starten av 1990-tallet. Dette gir en historisk oversikt over boligprisutviklingen i Norge fra en tid med store markedsendringer.

```{code-cell} ipython3
import matplotlib.pyplot as plt

bpi = df1[df1["statistikkvariabel"] == "Prisindeks for brukte boliger"]
bpi = bpi[bpi["boligtype"] == "00 Alle boligtyper"]
bpi = bpi[bpi["region"] == "TOTAL Hele landet"]
bpi = bpi.copy()

def formatertid(streng):
    return streng.replace("K", "Q")

bpi["kvartal"] = bpi["kvartal"].map(formatertid)
bpi["kvartal"] = pd.PeriodIndex(bpi["kvartal"], freq="Q")
bpi = bpi.set_index("kvartal")

prisidx = list(bpi.columns)[-1]
bpi[prisidx] = bpi[prisidx].replace("..", None)
bpi[prisidx] = bpi[prisidx].str.replace(",", ".")
bpi[prisidx] = bpi[prisidx].astype(float)
bpi = bpi.rename(columns={prisidx: "prisindeks"})

idxs_bpi = list(bpi.columns)[0:3] 
bpi = bpi.drop(labels=idxs_bpi, axis=1)

display(bpi)
bpi["prisindeks"].plot(title="Boligprisindeks - brukte boliger, alle typer for hele landet")
plt.xlabel("Kvartal")
plt.ylabel("Prisindeks")
plt.show()
```

### Forklaring

Datasettet **filtreres** først for statistikkvariabelen "Prisindeks for brukte boliger", boligtypen `"00 Alle boligtyper"` og regionen `"TOTAL Hele landet"`. Dette gir en oversikt over de generelle boligprisene i Norge på nasjonalt nivå, uten at tallene påvirkes av lokale variasjoner eller spesifikke boligtyper.

En **kopi** av datasettet lages for å lage en ny *dataframe* slik at man unngår advarsler når verdier endres. Kvartalene omformes til et Pandas `PeriodIndex` med frekvens "Q" (kvartal), slik at de kan brukes som **tidsindeks** i plottet.

Kolonnen med prisindeksen renses: manglende verdier ("..") settes til `None` (NaN), desimalskilletegn endres fra komma til punktum, og verdiene konverteres til flyttall (`float`). Kolonnen får navnet `"prisindeks"` for enklere bruk i videre analyser og plotting.

Til slutt vises/**plottes** tabellen og utviklingen av boligprisindeksen i et linjediagram. Dette viser den langsiktige trenden i boligmarkedet, med jevn prisvekst og enkelte mindre nedgangsperioder.


+++

Videre kan det være interessant å se på hvilke kvartal som hadde høyest og lavest **prosentvis endring**.

```{code-cell} ipython3

bpi["vekst"] = bpi["boligprisindeks"].pct_change() * 100

lav_endring = bpi["vekst"].idxmin()
lav_endring_verdi = bpi["vekst"].min()
print(f"Kvartalet med lavest prisvekst var {lav_endring}, med en endring på {lav_endring_verdi:.1f}%")

hoy_endring = bpi["vekst"].idxmax()
hoy_endring_verdi = bpi["vekst"].max()
print(f"Kvartalet med høyest prisvekst var {hoy_endring}, med en endring på {hoy_endring_verdi:.1f}%")
```

### Forklaring

En ny kolonne `vekst` beregnes med metoden `pct_change()`, som regner ut prosentvis endring fra forrige kvartal. Verdien multipliseres med 100 for å få prosent.  

Deretter identifiseres kvartalet med lavest og høyest prisvekst ved å bruke `idxmin()` og `idxmax()`, og verdiene printes ut som prosenter med én desimal, `1f}%`.  

Kvartalet med høyest prosentvis prisvekst i BPI var i andre kvartal i 1999, med en økning på 8,1%. Dette kan ha vært drevet av høy etterspørsel etter bolig, lave renter og generelt optimistiske økonomiske utsikter på slutten av 1990-tallet.  

Kvartalet med lavest prisvekst var siste kvartal i 2008, med en nedgang på 7,0%. Dette kvartalet sammenfaller med finanskrisen, som førte til økt usikkerhet i økonomien, strammere kredittforhold og lavere kjøpekraft, som alle bidro til fall i boligprisene.  

Dette viser at kvartalsvise svingninger i boligprisene ofte reflekterer større samfunnsøkonomiske hendelser, og at den reelle prisveksten i boligmarkedet påvirkes av både kortsiktige og langsiktige faktorer som renter, kreditt og økonomisk tillit.

```{code-cell} ipython3
df2 = pd.read_csv("1086.csv", sep=";", encoding="latin1")
print(df2.columns.tolist())
display(df2.head())
```

### Forklaring

Koden leser inn datasettet `1086.csv` som er en **csv-fil** av en tabell hentet fra SSB, som inneholder tall for **konsumprisindeksen** (KPI). Denne indeksen måler endringer i prisnivået på varer og tjenester som husholdninger kjøper, og brukes som et mål på **inflasjon**.
Ved å bruke `pd.read_csv("1086.csv", sep=";", encoding="latin1")` importeres datafilen, mens `print(df2.columns.tolist())` viser kolonnenavnene og `display(df2.head())` viser de første radene i tabellen for å få oversikt over strukturen.
Datasettet danner dermed grunnlaget for å analysere prisutviklingen i Norge over tid.
Fra tabellen ser man at **basisåret** (året hvor indeksen er 100) er 2015. Statistikken går helt tilbake til 1979 og måles **månedlig**. 
For at KPI skal kunne sammenlignes med BPI, er det viktig å undersøke om begge indeksene har samme basisår, altså 2015, siden dette ikke var presisert i datasettet om BPI. 

```{code-cell} ipython3
bpi_per_aar = bpi["prisindeks"].groupby(bpi.index.year).mean()
basisaar = (bpi_per_aar - 100).abs().idxmin()
print(f"Basisåret er {basisaar}, med en gjennomsnittlig prisindeks på {bpi_per_aar.loc[basisaar]:.1f}")
```

### Forklaring

Koden beregner **gjennomsnittlig boligprisindeks per år** ved å gruppere kvartalsdataene i `bpi` etter år med `groupby(bpi.index.year)` og finne gjennomsnittet med `.mean()`. Variabelen `bpi_per_aar` inneholder dermed ett gjennomsnittstall for hvert år. Deretter finner koden hvilket år som har en gjennomsnittlig prisindeks nærmest 100 med `(bpi_per_aar - 100).abs().idxmin()`, og lagrer dette som `basisaar`. 
Koden bekrefter at basisåret for BPI er 2015 i likhet med KPI, og de kan sammenlignes videre. 

+++

Som nevnt måles KPI månedlig, mens BPI måles kvartalvis. De har altså en tidsindeks med **ulik frekvens**. For å sammenligne dem vil man helst ha hver variabel kun én gang per periode. Det er også hensiktsmessig å kun se på KPI fra 1992, selv om dataene går lenger tilbake. 

```{code-cell} ipython3
kpi = df2[df2["statistikkvariabel"] == "Konsumprisindeks (2015=100)"]
kpi = kpi[kpi["måned"] >= "1992M01"]
kpi = kpi.copy()

kpi["måned"] = kpi["måned"].str.replace("M", "-")
kpi["kvartal"] = pd.PeriodIndex(kpi["måned"], freq="Q")

kpi = kpi.set_index("måned")

idxs_kpi = list(kpi.columns)[0:2] 
kpi = kpi.drop(labels=idxs_kpi, axis=1)

kpidx = list(kpi.columns)[0]
kpi[kpidx] = kpi[kpidx].str.replace(",", ".")
kpi[kpidx] = kpi[kpidx].astype(float)

kpi_kvartal = kpi.groupby("kvartal").mean()
kpi_kvartal = kpi_kvartal.rename(columns={kpidx: "konsumprisindeks"})

display(kpi_kvartal.round(2))

kpi_kvartal["konsumprisindeks"].plot(title="Konsumprisindeks kvartalsvis")
plt.xlabel("Kvartal")
plt.ylabel("Konsumprisindeks")
plt.show()
```

### Forklaring

Datasettet **filtreres** først slik at det kun inneholder statistikkvariabelen `"Konsumprisindeks (2015=100)"`, og observasjonene begrenses til perioden fra og med `1992M01`. Dette gjøres for å gjøre datasettet sammenlignbart med BPI-dataene, som også starter i 1992. En **kopi** av datasettet lages for å unngå advarsler når verdier endres.

Deretter omformes månedsformatet ved å erstatte `“M” med “-”`, slik at verdiene får et gyldig **datotidformat**. En ny kolonne med kvartal opprettes basert på månedskolonnen ved hjelp av `PeriodIndex` med kvartalsfrekvens. Dette gjør det mulig å gruppere dataene på kvartalsnivå. Kolonnen “måned” settes som indeks for å tydeliggjøre tidsdimensjonen.

Unødvendige kolonner som `"kode"` og `"statistikkvariabel"` fjernes fordi de ikke lenger er relevante etter filtreringen. Dette gjør datasettet ryddigere og enklere å bruke videre. Verdiene omformes konsumprisindeksen slik at komma erstattes med punktum, og datatypen konverteres til flyttall (`float`) for å kunne beregne **gjennomsnitt per kvartal**.

Gjennomsnittlig konsumprisindeks per kvartal beregnes deretter ved hjelp av `groupby("kvartal").mean()`, og kolonnen gis navnet `"konsumprisindeks"` for enklere referanse. Til slutt vises den ferdige tabellen avrundet til to desimaler og plottes i et linjediagram som viser utviklingen i konsumprisindeksen kvartalsvis fra 1992 til i dag.
Plottet viser en tydlig og jevn økning i KPI. 

```{code-cell} ipython3
df = pd.merge(bpi, kpi_kvartal, how='outer', on="kvartal")
display(df.round(2))

df.plot(title="BPI og KPI kvartalsvis")
plt.xlabel("Kvartal")
plt.ylabel("Prisindeks")
plt.show()
```

### Forklaring

Datasettene for boligprisindeks (`bpi`) og konsumprisindeks per kvartal (`kpi_kvartal`) **slås sammen** med `.merge()` basert på felles kolonne `"kvartal"`. Argumentet `how='outer'` sikrer at alle kvartaler fra begge datasett inkluderes, selv om det mangler data i ett av dem. Resultatet er en samlet *dataframe* med både BPI og KPI per kvartal.

Deretter plottes alle numeriske kolonner mot kvartal i et linjediagram. Plottet viser hvordan boligprisene og konsumprisene har utviklet seg over tid.  

Fra plottet kan man se at boligprisene (BPI) har hatt en **kraftigere** og mer **volatil** økning sammenlignet med konsumprisindeksen (KPI), som stiger **jevnere** over tid. Dette illustrerer at boligmarkedet har større svingninger enn generelle konsumpriser.

+++

Videre kan man lage et **spredringsplott** for å se om det er en **korrelasjon** mellom de to indeksene. 

```{code-cell} ipython3
df.plot.scatter("boligprisindeks", "konsumprisindeks")
plt.title("Sammenheng mellom boligprisindeks og konsumprisindeks")
plt.xlabel("BPI")
plt.ylabel("KPI")
plt.show()
```

### Forklaring

Koden lager et **spredningsplott** som viser sammenhengen mellom boligprisindeks (`BPI`) og konsumprisindeks (`KPI`) for hvert kvartal. Hver prikk i plottet representerer et kvartal, med boligpriser på x-aksen og konsumprisindeksen på y-aksen.  

Fra plottet kan man observere en klar **positiv sammenheng/korrelasjon**: når KPI øker, stiger også BPI. Dette betyr at boligpriser og den generelle prisutviklingen i økonomien ofte beveger seg i samme retning.   

+++

Dette kan kvantifiseres ved å beregne **korrelasjonen** mellom de to indeksene, og man kan også se på **kovariansen** for å måle hvordan de endrer seg i forhold til hverandre.

```{code-cell} ipython3
indekser = df[["boligprisindeks", "konsumprisindeks"]]

korrelasjon = indekser.corr()
print("Korrelasjon mellom BPI og KPI:")
print(korrelasjon)

kovarians = indekser.cov()
print("\nKovarians mellom BPI og KPI:")
print(kovarians)
```

### Forklaring

Koden velger først kolonnene `"boligprisindeks"` og `"konsumprisindeks"` fra datasettet `df` for å kunne sammenligne dem. Deretter beregnes **korrelasjonen** med `.corr()`, som viser hvor tett BPI og KPI beveger seg sammen. En verdi nær 1 indikerer sterk positiv korrelasjon, dvs. at når konsumprisindeksen stiger, stiger også boligprisindeksen.  

Videre beregnes **kovariansen** med `.cov()`, som viser hvor mye de to indeksene varierer sammen i samme enheter som indeksene. Positiv kovarians betyr at BPI og KPI i gjennomsnitt beveger seg i samme retning, mens negativ kovarians ville indikert motsatt bevegelse.  

Tallene fra korrelasjon - og kovarianstabellen bekrefter at BPI og KPI har en **sterk positiv sammenheng**, noe som støtter observasjonen fra spredningsplottet om at boligprisene i stor grad følger den generelle prisutviklingen i økonomien.

+++

## Avslutning og refleksjon

Analysen viser at boligprisene i Norge (BPI) har steget betydelig fra 1992 til i dag, med en langsiktig vekst som overgår utviklingen i konsumprisindeksen (KPI). Dette indikerer at boligmarkedet har hatt en reell prisvekst over perioden, altså at boligprisene har økt mer enn den generelle prisstigningen i samfunnet. Både spredningsplott og beregning av korrelasjon og kovarians viser at BPI og KPI beveger seg i samme retning, men BPI har større volatilitet, noe som reflekterer at boligmarkedet påvirkes av flere faktorer enn konsumprisene alene

Som student i økonomi og nylig boligkjøper har jeg funnet oppgaven svært interessant. Det har vært spennende å se hvor mye boligprisene har steget siden 1992, samtidig som analysen av konsumprisindeksen gir innsikt i hvordan prisutvikling på varer og tjenester påvirker kjøpekraften, særlig nå som jeg selv skal kjøpe flere varer.  

I tillegg har arbeidet med oppgaven styrket mine programmeringskunnskaper. Programmet kombinerer praktisk økonomisk forståelse med tekniske ferdigheter, noe som er nyttig både for studier og fremtidige karriereplaner innen økonomi og rådgivning.


```{code-cell} ipython3

```
