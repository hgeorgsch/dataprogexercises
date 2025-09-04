---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.2
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Genuttrykk

::: {admonition} Opphavsrett

+ Original oppgåve ved Morten Munthe, Universitetet i Bergen, 2025.
+ Redigert og tilrettelagt av Hans Georg Schaathun, NTNU, 2025, med
  kodeforenkling og utdjuping.

Oppgåva kan brukast fritt under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Datasetta er henta frå [ENCODE](https://www.encodeproject.org/)
med mindre endringar.
Sjå òg
Luo Y, Hitz BC, Gabdank I, Hilton JA, Kagda MS, Lam B, Myers Z, Sud P, Jou J, Lin K, Baymuradov UK, Graham K, Litton C, Miyasato SR, Strattan JS, Jolanki O, Lee JW, Tanaka FY, Adenekan P, O'Neill E, Cherry JM. 
«New developments on the Encyclopedia of DNA Elements (ENCODE) data portal.»
*Nucleic Acids Res.* 2020 Jan 8;48(D1):D882-D889. 
doi: 10.1093/nar/gkz1062. PMID: 31713622; PMCID: PMC7061942.
:::

Denne øvelsen har en dobbel hensikt.
For det første skal den illustrere ulike funksjoner i python, for å analysere
og visualiser data, og skal dermed øve generelle programmerigns- og
databehandlingsferdigheter.
For det andre studerer den sammenhenger i genetiske data, og skal utvikla kompetanse
i biologi på VGS-nivå.

::: {admonition} Læringsutbytter i Biologi

+ Biologi 1:
    - gjere greie for oppbygginga av og funksjonen til sentrale organsystem i kroppen
    - trekkje ut informasjon frå biologiske tekstar, brosjyrar, aviser, bøker og frå Internett, og vurdere korleis informasjonen er underbygd
+ Biologi 2:
    - finne fram til ny kunnskap i biologi frå ulike medium
    - gjere greie for transkripsjon og translasjon av gen og forklare korleis regulering av gen kan styre biologiske prosessar
:::

::: {admonition} Læringsutbytter i Programmering

+ Bli kjent med biblioteket pandas og hvordan det kan brukes til å strukturere
  og visualisere data.

:::

+++

## Celletyper og genregulering

Kroppen vår består av hundrevis av ulike 
[celletyper](https://en.wikipedia.org/wiki/List_of_distinct_cell_types_in_the_adult_human_body)
som utfører spesialiserte oppgaver i kroppen.
Alle celler inneholder det samme DNAet og dermed den samme informasjonen om proteinoppskrifter.
Men celler har ulik funksjon (litt forenklet) fordi de ikke produserer de samme proteinene proteiner.
Det som avgjør hvilke proteiner som skal produseres i de ulike celltypene er definert
av reguleringen av transkripsjon i hver celle og vev.

Sekvenseringen av det humane genom i 2000 var en teknologisk bragd, som på mange måter revolusjonerte molekylærbiologien og genetikkfagene. Etter dette har store ressurser har blitt satt inn på å kartlegge hvordan gener blir regulert i ulike utviklingstrinn og i ulike vev/celletyper.

+++

## Datasettet

Ett prosjekt som har som mål om å forstå «funksjonen» og reguleringen til alle gener i vårt genom
er Encyclopedia of DNA Elements ([ENCODE](https://www.encodeproject.org)).
Dette prosjektet er et stort internasjonalt samarbeid som samler inn og systematiserer data som gir innsikt i hvordan geners transkripsjon reguleres.

I denne øvelsen har vi hentet inn et datasett fra ENCODE prosjektet, nærmere bestemt målinger av mRNA nivå (genuttrykk), fra ulike vev fra menneske og mus.

Som vanlig bruker vi [pandas](https://pandas.pydata.org/docs/)-biblioteket til å håndtere datasettet,
[pyplot](https://matplotlib.org/stable/tutorials/pyplot.html) til plotting,
og [numpy](https://numpy.org/doc/stable/) til noen kvantitative beregninger på 
hele datasett.

```{code-cell} ipython3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```

Last ned de to datafilene
+ [genuttrykk_menneske_data.txt](genuttrykk_menneske_data.txt)
+ [genuttrykk_mus_data.txt](genuttrykk_mus_data.txt)

::: {admonition} Oppgåve
Åpne filene.  Hvorden er de formatert med skilletegn og desimaltegn?
Er begge filene formattert likt?
:::

La oss begynne med å lese inn menneskedata og vise noen rader, f.eks. slik,

```{code-cell} ipython3
data_H = pd.read_csv("genuttrykk_menneske_data.txt", sep=' ')
print(data_H.head(12))   
```

::: {admonition} Oppgave 
1. Hva er de forskjellige typene vev på norsk?
2. Hent inn for dataene for mus på samme måte. Kall datasettet for `data_M`.
3. Er de samme vevene samlet inn fra begge artene?
:::

+++

Vi skal nå fokuserer på enkelte av vevstypene,
og tar vekk søyler "testies", "ovary", "sigmoid", og "adipose".
Det kan vi gjøre med funksjonen `drop`, slik:

```{code-cell} ipython3
data_H = data_H.drop(columns=["testis", "ovary", "sigmoid", "adipose"], axis=1)
```

Hver søyle svarer til en vevstype, bortsett fra søylen `genes`.
Vi kommer til å trenge en liste over vevstypene som vi studerer, uten `genes`, og
det kan vi lage slik.

```{code-cell} ipython3
vev_navn = list(data_H.columns)
vev_navn.remove("genes")
```

::: {admonition} Oppgåve
Dropp dei same søylene frå datasettet for mus.
:::

::: {admonition} Oppgåve
Skriv ut innhaldet av `vev_navn` og samanlikn det med visinga av datasettet over.

Stemmer lista over vevstypar med søylene både for mus og menneske?
:::

::: {hint}
I denne hele oppgaven må vi være detektiver og lese oss opp på funksjoner til ulike gener ved hjelp av ulike databaser på nettet.
Vi anbefaler [www.genecards.org](www.genecards.org) eller [www.proteinatlas.org](www.proteinatlas.org)  for å finne detaljert informasjon om gener og deres proteinprodukt.
I tillegg har wikipedia også ofte gode sider om disse genene/proteinene.
:::

+++

## Dypdykk

Nå skal vi utforske datasettet vårt ved å grave litt i genuttrykksmønstrene. Vi starter å kun se på data fra mennesket.

To av vevene i vårt datasett er hormonproduserende, binyrer (engelsk: adrenal) og bukspyttkjertelen (engelsk: pancreas). En av de viktigste oppgavene til binyrene er å produsere adrenalin, mens en av bukspyttkjertelens viktigste oppgaver er å produsere insulin og glucagon som regulerer glukoseinnholdet i blodet. Produksjon av adrenalin skjer ved kjemisk modifisering (methylering) av noradrenalin. Denne reaksjonen blir katalysert av ensymet phenylethanolamine N-methyltransferase som kodes for av **PNMT**-genet. Glucagon produseres ved å spalte preglucagon, et protein kodet for av genet **GCG**.

+++

For å hente ut de genene vi er interesserte i, can vi bruke `pandas`-funksjonene for å filtrere data, og rett og slett finne de to genene i `genes`-søylen.

```{code-cell} ipython3
r1 = data_H[ data_H["genes"] == "GCG" ]
print(r1) 
r2 = data_H[ data_H["genes"] == "PNMT" ]
print(r2) 
```

Legg merke til at `r1` og `r2` er tabellen eller *data frames* med én rad hver.
Det er ikke det samme som enkeltrader, eller *Series* i `pandas`.
Hvis vi henter ut den ene raden, ser vi forskjellen:

```{code-cell} ipython3
GCG_vals = r1.iloc[0]
PNMT_vals = r2.iloc[0]
print( "Typer:", type(r1), type(r1.iloc[0]) )
print()
print("GCG som serie")
print(GCG_vals)
print()
print("PNMT som serie")
print(PNMT_vals)
```

Nu kan vi bruke `pandas`-funksjonene for å plotte de to genene.
Det blir seende litt forskjellig ut, om vi bruker *Data Frame*-objektet
eller *Series*-objektet, men koden er nesten lik.

```{code-cell} ipython3
plt.figure()
GCG_vals.drop("genes").plot(kind='bar', title="GCG")    # Lager et barplott (histogram) med tittel GCG
plt.ylabel("log2(Genuttrykk)")            # Navn på y-aksen
plt.tight_layout()                        # Dette gjøre at plottet ser ryddigere ut
```

::: {hint}
Merk at vi måtte droppe `genes` før vi plotter. Det er ikke nødvendig når vi plotter en tabell under, men når vi plotter en serie, vil pandas protestere på ikke-numeriske verdier.
:::

```{code-cell} ipython3
plt.figure()
r1.plot(kind='bar', title="GCG")    # Lager et barplott (histogram) med tittel GCG
plt.ylabel("log2(Genuttrykk)")      # Navn på y-aksen
plt.tight_layout()                  # Dette gjøre at plottet ser ryddigere ut
```

::: {admonition} Oppgave
Lag tilsvarende plot for PNMT.  Du velger selv hvilket format du vil ha, og
om du har tid, kan du søke på nett og se om du kan flikke på formateringen
og få finere farger og titler.
:::

::: {admonition} Refleksjon
Virker resultatene logiske utifra det dere kan om produksjonen av disse hormonene?
:::

Det er også mulig å sette sammen de to radene til én tabell og plotte dem sammen.

```{code-cell} ipython3
rs = pd.concat([r1,r2])
print(rs)
```

::: {admonition} Oppgave
Legg til koden for å plotte `rs` på samme måte som `r1` over.
:::


## Mønster

La oss nå se nærmere på noen hovedmønstre i datasettet vårt.
Vi starter med å se på de gener som har høyest uttrykk, dvs. høyest
verdi for vevstypene i datasettet.

Vi laver først en funksjon som finner de 100 sterkeste genene for én
vevstype i ett datasett.  Vi tester den raskt med det samme på et par
vilkårlige eksempler.

```{code-cell} ipython3
def hent_høye_genuttrykk(df, vevstype): 
    sortert_df = df.sort_values(vevstype,ascending=False) # Sorter etter søylen «vevstype»
    genuttrykk_sortert = sortert_df["genes"]          # Kun navn på genene
    gener_høyt = list(genuttrykk_sortert[:100])  # De 100 første (sterkeste) genene
    return gener_høyt
print(hent_høye_genuttrykk(data_H,"pancreas"))
print(hent_høye_genuttrykk(data_H,"brain"))
```

Vi ønsker nu å finne gener som er viktige for alle vevstypene.  I praksis
skal vi identifisere de genere som dukker opp som topp-100 i alle vevstypene.
Der er mange velprøvde teknikker for å finne de elementer er felles for flere lister.
Her skal vi bruke en teknikk som er syntaktisk enkel, og der pythons implementasjon
er regnet for å være god.

Hvis vi ser på listene som mengder, er vi på jakt efter det som i i mengdelæren kalles snitt.
Python har innebygd syntaks for å håndtere mengder og snitt.  Vi kan konvertere listene
til mengder og regne ut snittet slik:

```{code-cell} ipython3
liste1 = (hent_høye_genuttrykk(data_H,"kidney"))
liste2 = (hent_høye_genuttrykk(data_H,"heart"))
mengde1 = set(liste1)
mengde2 = set(liste2)
print(mengde1)
print(mengde2)
snitt = mengde1 & mengde2
print(snitt)
```

Snittoperatoren i python er altså `&`.  
Det går òg an å skrive det som en funksjon, slik:

```{code-cell} ipython3
snitt = set.intersection( mengde1, mengde2 )
print(snitt)
```

::: {admonition} Merknad
Mengder skiller seg fra lister ved at rekkefølgen ikke spiller nogen rolle og
elementer kan opptre bare en gang.
Vi vet at hvert gen bare opptrer én gang i datasettet, så vi taper ingen informasjon her.
Vi er nødt til å se bort fra rekkefølgen, fordi den kan være forskjellig i de to listene.
:::

La oss nu gå videre til å se på alle vevstypene samtidig.
Først laver vi en liste med topp-hundrede for alle vevstypene.
Vi bruke listekomprehensjon for å få det kompakt og lettleselig.

```{code-cell} ipython3
alle_høye_lister = [ hent_høye_genuttrykk(data_H, navn)
                     for navn in vev_navn ]
print("Antall lister: ", len(alle_høye_lister))
print("Lengde første liste: ", len(alle_høye_lister[0]))
```

Her har vi en liste av lister, med alle topp-hundrede-genenene.
For å finne snittet av alle (de indre) listene, trenger vi to triks.
Vi må konvertere alle listene til mengder, og vi må anvende
`set.intersection` på elementene i en liste.
Vi så at `set.intersection` tar flere argumenter, der alle argumentene
er mengder.  Den en liste som ett enkelt argument.
Heldigvis har python et syntakstriks for å pakke opp listen, og sende
alle elementene som argumenter til en funksjon.
Da bruker vi asteriskes `*`, slik:

```{code-cell} ipython3
alle_høye_mengder = [ set(x) for x in alle_høye_lister ]
toppgener = set.intersection( *alle_høye_mengder )
print( toppgener )
```

::: {admonition} Biologioppave 1 
Bruk internet for å finne funksjonen til de seks (?) genene som er høyt uttrykt i alle vev.
Diskuter hva slags funksjoner som er felles for disse genene.
:::

::: {admonition} Oppgave 
Finn de lavest uttrykte genene på samme måte.
1. Begynn med å definere en funksjon `hent_lave_genuttrykk()` tilsvarende `hent_høye_genuttrykk()`.
   Du kan enten sortere omvendt (`ascending=True`) eller ta hundrede elementer fra slutten
   av listen i stedet for begynnelsen.
2. Kopier koden for toppgener og bruk `hent_lave_genuttrykk()` for å finne «bunngener».
:::

+++

::: {admonition} Biologioppave 2 

Legg vekk PCen og diskuter:

1. Hva slags cellefunksjoner forventer vi at styres av gener som ikke varierer mye i genuttrykk mellom ulike celler?
2. Er genene som uttrykkes i alle celler vanligvis lavt eller høyt uttrykt?
:::

+++

Da skal vi bruke koding til å sjekke om dere har tenkt i riktige baner. For å finne gener som varierer mye/lite mellom vev (også referert til som vevsspesifisitet) skal vi nå lage en kode som leter systematisk etter slike gener. Hvis vi tenker algoritmisk på dette problemet trenger vi å gjøre følgende:

- For hvert gen (rad i vår tabell) regn ut et mål på variasjon i genuttrykket (verdiene) mellom vev, dvs kolonner i tabellen
- Lagre dette variasjonsmålet for hver rad
- Bruke verdien for hvor mye variasjon det er i genuttrykkene til å trekke ut de mest/minst varierende genene og visualiser/studer resultatene.

Vi kan legge alle disse målene inn som nye søyler i tabellen, og `pandas` gir oss innebygde funksjoner for å finne gjennomsnitt (`mean`) og standardavvik (`std`). Vi laver nye søyler for disse to, samt variasjonskoeeffisienten som vi definerer som $100\cdot s/\bar x$.

```{code-cell} ipython3
data_H["mean"] = data_H.loc[:,vev_navn].mean(axis=1)
data_H["std"] = data_H.loc[:,vev_navn].std(axis=1)
data_H["varkoef"] = 100*data_H["std"]/data_H["mean"]
data_H
```

Her får vi noe litt rart utifra dataene våre. To av variasjonskoeffisientene blir under null.

```{code-cell} ipython3
data_H[ data_H["varkoef"] < 0 ]
```

::: {admonition} Refleksjon
Se på dataene over.  Hvorfor blir variasjonskoeffisientene negative?
:::

+++

Det virker underlig at genuttrykket kan være negativt, så det er naturlig å tenke at dette skyldes målefeil.
I så fall er det fornuftig å regne dette som ugyldige data, f.eks. ved å sette variasjonskoeffisienten til null.
Det kan vi gjøre slik, og for sikkerhets skyld sjekker vi minimum for å se at der ikke finnes negative verdier igjen.

```{code-cell} ipython3
data_H[ data_H["varkoef"] < 0 ]  = 0
print( data_H["varkoef"].min() )
```

Tilslutt plotter vi et histogram over variasjonskoeffisient til genuttrykket

```{code-cell} ipython3
plt.figure()
plt.hist(data_H["varkoef"], bins=100)
plt.title("Histogram over variasjonskoeffisienter")
plt.xlabel("Variasjonskoeffisientverdi")
plt.ylabel("Antall")
```

::: {admonition} Refleksjon 

Er det vanligst at gener har stor variasjon i genuttrykk mellom vev?

:::

+++

I **biologioppgave 1** og **2** fant vi ut at høyt uttrykte gener ofte er høyt uttrykte i flere vev. Dersom dette er en generell trend foventer vi å se en sammenheng mellom geners ‘vevsspesifisitet’ (som vi har målt som variasjonskoeffisient) og geners uttrykksnivå. Vi plotter variasjonskoeffisienten mot gjenomsnittet (som vi regnet ut for hvert vev over).

```{code-cell} ipython3
plt.figure()
plt.scatter(data_H["mean"], data_H["varkoef"])
plt.xlabel("Gjennomsnittlig vevsuttrykk")
plt.ylabel("Variasjonskoeffisient")
```

Vi skal se på to eksempler på gener som er høyt uttrykt. Beta-aktin (**ACTB**) (se liste over høyt uttrykte gener) og gener som koder for ribosomale proteiner.

La oss legge på informasjon om hvor slike typiske ‘housekeeping genes’ befinner seg i plottet over. Finner først radene som har gener som koder for ribosomale subinuts (disse begynner på ‘**RPS**’) og deretter beta-aktin (**ACTB**).

```{code-cell} ipython3
rps_data = data_H.loc[ data_H["genes"].str.startswith( "RPS", na=False ) ]
print(rps_data)
```

::: {hint}
Dette er antagelig en ny variant av filtrering av datasett.
Vi bruke `str.startswith` for å identifisere gennavn som begynner med en bestemt streng.
Vi må spesifisere `na=False` som eksluderer rader der `genes` er udefinert.
:::

```{code-cell} ipython3
actb_data = data_H.loc[ data_H["genes"].str.startswith( "ACTB", na=False ) ]
print(actb_data)
```

Vi kan nå legge på et nytt lag av informasjon på plottet over der vi uthever disse genene spesifikt

```{code-cell} ipython3
plt.figure()
plt.scatter( data_H["mean"], data_H["varkoef"] )
plt.scatter( rps_data["mean"], rps_data["varkoef"], label='Ribosomale protein-subenheter')
plt.scatter( actb_data["mean"], actb_data["varkoef"] , label='Beta-aktin')
plt.xlabel("Gjennomsnittlig vevsuttrykk")
plt.ylabel("variasjonskoeffisient")
plt.legend()
```

::: {admonition} Biologioppgave 3 

Diskuter hva denne grafen viser og hvorfor det er rimelig at det må være slik

:::

+++

Så langt har vi sett at gener som er høyt uttrykt også oftest varierer lite i genuttrykk mellom vev. Slike gener blir referert til som ‘housekeeping genes’ - og disse er som navnet tilsier involvert i helt basale prosesser i cellen som alle celler må utføre for å overleve.

+++

## Sammenligne mus og mennesker

Her skal vi bruke hele det originale datasettet, med genuttrykk fra både mus og menneske, for å belyse viktige prinsipp innen evolusjon.

::: {admonition} Refleksjon 

Diskuter ut ifra det dere kan om evolusjonsbiologi, om vi vil forvente at genuttrykksmønstrene fra samme vev i menneske og mus er likere hverandre enn de er andre vev i samme art?
:::

Vi starter med å hente inn filen med data fra mus. Mye av denne koden er lik den vi hadde for mennesker i starten av dokumentet.

```{code-cell} ipython3
data_M = pd.read_csv("genuttrykk_mus_data.txt", sep=' ') 
data_M = data_M.drop(columns=["testis", "ovary", "sigmoid", "adipose"], axis=1)
```

Før vi regner på korrelasjon, lager vi alternative tabeller uten den ikke-numeriske `genes`-søylen. Vi dropper også ekstrasøylene som vi la til for mennesker.

```{code-cell} ipython3
vev_H = data_H.drop( columns=[ "genes", "mean", "std", "varkoef" ] )
vev_M = data_M.drop( columns=[ "genes" ] )
```

Nu regner vi ut korrelasjonen mellom mellom menneske og mus, for hver vevstype. Dersom de samme genene er høyt/lavt uttrykt i samme vev i mus og menneske, så vil korrelasjonen være høy.

```{code-cell} ipython3
korrelasjon = vev_H.corrwith(vev_M) 
print("Korrelasjon mellom genuttrykk i menneske og mus\n")
print(korrelasjon)
```

Vi kan vise det samme som et søylediagram.

```{code-cell} ipython3
korrelasjon.plot(kind="bar")
plt.ylim([0, 1])
plt.tight_layout()
```

::: {admonition} Oppgave 

1. Studer likheten mellom vevene i mus og menneske. Hva er grunnen til likheten? Hvorfor er noe vev likere enn annet vev?
2. Hvordan kan dere forklare dette ut ifra evolusjonsprinsipper?
:::

```{code-cell} ipython3

```

```{code-cell} ipython3

```
