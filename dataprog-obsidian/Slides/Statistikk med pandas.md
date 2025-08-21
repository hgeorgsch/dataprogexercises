---
tags:
  - lecture/video/perspective
  - statistics
  - pandas
---


<!-- slide template="[[tpl-quote-header]]" -->

# Deskriptiv statistikk med pandas

![[Panda_closeup.jpg|480]]

::: credit
By Jcwf, CC BY-SA 3.0, via
[Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=836272)
:::

note:
(Sjå òg [[Notar til Statistikk med pandas]])

Statistikk er et område hvor programmering er til stor hjelp, særlig hvis man har analyser som skal gjentas mange ganger på lignende datasett, f.eks. for ulike perioder, eller datasettene er meget store og sammensatte.

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

Vi skal bruke det samme datasettet gjennom hele foredraget.  Der er bare
to varegrupper, observert med eksportvolum og kilopris hver uke i
1295 uker.

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
<!-- element class="fragment" -->

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

- `[]` - søyler
- `.loc[]` - rader
- `.iloc[]` - rader
- `.loc[2:10,"Tonn"]`

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

note:
Ved siden av indeksering, trenger vi ofte å hente ut delmengder av datasettet etter bestemte kriterier. Jeg sa innledningsvis at eksportdatasettet vårt ikke egentlig er paneldata. Vi har forskjellige observasjoner på samme tidspunkt.

For å gå videre med et rent og pent eksempel på paneldata, kan vi hente ut et datasett for bare én varegruppe. Igjen bruker vi klammeparenteser, men i stedet for en indeks, gir vi et kriterium, f.eks. at varegruppen i datasettet må være lik «fersk oppalen laks».

---

<!-- slide template="[[tpl-smalltext]]" -->


```python
df2 = df[ df["varegruppe"] == "Fersk oppalen laks" ]
```


<p class="fragment">

```
In [41]: x = df["varegruppe"] == "Fersk oppalen laks"

In [42]: x
Out[42]:
0        True
1        True
2        True
3        True
4        True
        ...
2585    False
2586    False
2587    False
2588    False
2589    False
Name: varegruppe, Length: 2590, dtype: bool

In [43]: type(x)
Out[43]: pandas.core.series.Series
```

</p>

::: credit
:::

note:
Filtreringsnotasjonen som vi brukte er egentlig et spesialtilfelle
av *bolsk indeksering*.

Hvis vi evaluerer uttrykket 
`df["varegruppe"] == "Fersk oppalen laks"`,
ser vi at dette er et *Series*-objekt med bolske verdier.
Vi sammeligner rett og slett hvert element i serien på venstre side
med strengen på høyre side.

Når vi bruker en bolsk serie til å indeksere, får vi med de
elementene som svarer til sann i serien og dropper dem som
som svarer til usann.

Dette er en kraftfull finesse, men det tar en del 

---

# Datatypar

```
In [57]: df.dtypes
Out[57]: 
varegruppe     object
uke            object
Tonn            int64
kr/kg         float64
dtype: object

```

note: 
Hver søyle i en  *data frame*  har en datatype.  Til forskjell fra lister, tillater ikke pandas oss å blande ulike datatyper i samme søyle eller serie. Dette gjør at vi alltid kan behandle hele søyler på en konsistent måte. Vi kan bruke `dtypes`-attributten til å se hvilke datatyper søylene har.

Det er de numeriske søylene som er interessante i statistikk.  I eksportdatasettet vårt er det volumet i tonn og kiloprisen i kroner. Ukenummeret er en streng som samler år og uke, og den er vanskelig å regne på.  Vi kan bruke indeksen, som forsåvidt nummererer ukene kronologisk i vårt tilfelle.  Det er mulig å skille år og uke i ukestrengen, men det får vi ta en anden gang.

---

<!-- slide template="[[tpl-header]]" -->
# Deskriptiv statistikk

```
In [55]: df.describe()
Out[55]: 
               Tonn        kr/kg
count   2590.000000  2590.000000
mean    6782.083398    44.835591
std     7373.273168    21.268257
min       60.000000    17.460000
25%      565.750000    27.722500
50%     1717.500000    39.005000
75%    13357.750000    58.517500
max    29238.000000   123.280000
```

::: credit
:::

note:
Den enkleste måten å få ut en statistisk oppsummering av datasettet er `describe()`-metoden.
Vi får en oppsummering av hver av de numeriske søylene, med antall rader,
gjennomsnitt eller *mean*, standardavvik eller std for *standard deviation*, minimum, maksimum, samt 25de, 50de og 75de persentil.

---

```
In [38]: df1["kr/kg"].min()
Out[38]: 17.46

In [39]: df1["Tonn"].max()
Out[39]: 29238

In [40]: df1["Tonn"].mean()
Out[40]: 12937.647104247104

In [41]: df1["Tonn"].std()
Out[41]: 5730.168860496539
```

note:
Hvis vi skal bruke statistiske størrelser i videre beregninger, så er det enkleste å trekke ut en enkelt søyle og bruke metoder på *Series*-objektet i stedet.  

Der finnes metoder for alle de vanlige statistikkene som brukes.  Det er bare å slå opp i dokumentasjonen for å finne flere.

---

![[df1plot.svg]]

```python
import matplotlib.pyplot as plt
plt.plot( df1["kr/kg"] )
```

note:
Søylene i datasettet er det grunnleggende objektet for dataanalyse.
Hver søyle er en serie med observasjoner av samme variabel.

Vi kan hente ut slike enkeltsøyler og bruke dem i funksjoner fra andre
biblioteker, f.eks. kan vi bruke *pyplot* til å plotte.
I bildet har vi plottet kiloprisen for fersklaks.

---

![[df2plot.svg]]

```python
import matplotlib.pyplot as plt
plt.plot( df1["kr/kg"] )
plt.plot( df2["kr/kg"] )
```

note:
Vi må likevel være varsomme, fordi indeksen er en del av serieobjektet
i pandas.
Hvis vi har flere serier, skjer det ofte at disse indeksene ikke er
kompatible.
Det skjer typisk når indeksen blott viser til rekkenummer i datasettet,
og ikke er direkte knyttet til tidspunkt eller andre fysiske størrelser.

Her har vi plottet kiloprisen for fersklaks og frossenlaks, men $x$-aksen
viser ikke tidspunkt, men indeksen i det opprinnelige datasettet, der
frossenlaksen kom efter fersklaksen, selv om den var observert i samme 
periode.

---

![[dfplot.svg]]

```python
df1 = df1.reset_index()
df2 = df2.reset_index()
```

note:
Vi har muligheten til å endre indeksene, f.eks. ved
`reset_index()`-funksjonen som renummererer rekkene.
Det fungerer i dette tilfellet, fordi fersk- og frossenlaks
er observert på nøyaktig samme tidspunkter.

---

<!-- slide template="[[tpl-smalltext]]" -->

# Fletting av *data frames*

- `merge()` - horisontal sammenstilling
- `concat()` - vertikal sammenstilling

note:
Reindeksering vil være nyttig i mange sammenhenger, men skal vi 
en mer robust løsning, må vi bruke ukenummer som nøgle når
vi sammenligner seriene.

Dette kan gjøres på mange måter.  En teknikk som ofte trengs er
å flette sammen flere ulike datasett til én dataframe.
*pandas* har to funksjoner til dette:

`concat()` forutsetter at radene er unike, og legger sammen alle
radene fra begge datasettene under hverandre.

`merge()` forutsetter at radene i de to datasettene overlapper
og representerer de samme tidspunkter eller objekter, og 
kombinerer alle søylene fra begge datasettene side om side.

---

<!-- slide template="[[tpl-smalltext]]" -->

```
In [30]: join = df1.merge(df2,on="uke")

In [31]: join
Out[31]: 
            varegruppe_x      uke  Tonn_x  ...         varegruppe_y Tonn_y  kr/kg_y
0     Fersk oppalen laks  2000U01    3728  ...  Frosen oppalen laks    383    32.54
1     Fersk oppalen laks  2000U02    4054  ...  Frosen oppalen laks    216    33.63
2     Fersk oppalen laks  2000U03    4043  ...  Frosen oppalen laks    633    36.06
3     Fersk oppalen laks  2000U04    3730  ...  Frosen oppalen laks    393    34.27
4     Fersk oppalen laks  2000U05    3831  ...  Frosen oppalen laks    453    33.91
...                  ...      ...     ...  ...                  ...    ...      ...
1290  Fersk oppalen laks  2024U39   29238  ...  Frosen oppalen laks    578    71.97
1291  Fersk oppalen laks  2024U40   26543  ...  Frosen oppalen laks    987    78.32
1292  Fersk oppalen laks  2024U41   25180  ...  Frosen oppalen laks    780    73.69
1293  Fersk oppalen laks  2024U42   25561  ...  Frosen oppalen laks    793    81.90
1294  Fersk oppalen laks  2024U43   24910  ...  Frosen oppalen laks    677    71.49

[1295 rows x 7 columns]
```

note: 
La oss se hva vi trenger i vårt tilfelle.
Vi har fersklaks i df1 og frossenlaks i df2, begge observert på de samme tidspunktene eller ukene.
Dvs. at uke-søylen identifiserer radene, og rader med samme uke hører sammen.
Det må dermed være riktig å flette på uke, og vi bruke `on="uke"` som parameter til `merge`.

Siden de to tabellene har de samme søylenavnene, har pandas lagt til underscore-x og -y for å skille søylene fra de to tabellene.  Det er dog ikke så lett å se siden vi har flere søyler enn det som får plass på skjermen.  Men varegruppene er nu overflødige, så vi kan droppe dem.

---

<!-- slide template="[[tpl-smalltext]]" -->

```
In [33]: join0 = join.drop( columns=[ "varegruppe_x", "varegruppe_y" ] )

In [34]: join0
Out[34]: 
          uke  Tonn_x  kr/kg_x  Tonn_y  kr/kg_y
0     2000U01    3728    30.98     383    32.54
1     2000U02    4054    31.12     216    33.63
2     2000U03    4043    31.03     633    36.06
3     2000U04    3730    30.95     393    34.27
4     2000U05    3831    31.30     453    33.91
...       ...     ...      ...     ...      ...
1290  2024U39   29238    73.23     578    71.97
1291  2024U40   26543    69.70     987    78.32
1292  2024U41   25180    72.76     780    73.69
1293  2024U42   25561    76.02     793    81.90
1294  2024U43   24910    77.59     677    71.49

[1295 rows x 5 columns]
```


note:
*Data frame* har en metode `drop()` for å kvitte seg med overflødige søyler.
Der er også en `rename()`-metode som vi kunne ha brukt for å få mer informative søylenavn.

---

![[dfplot.svg]]

```python
plt.plot( join0["kr/kg_x"] )
plt.plot( join0["kr/kg_y"] )
plt.savefig( "join.png" )
```

note:
Nu kan vi være helt sikre på at tidspunktene er de samme når vi sammenligner kiloprisene for fersk og frossen laks.

Dette blir ennu viktigere å tenke på når vi  sammenligner data fra ulike kilder.
I dette tilfellet visste vi at vi hadde alle observasjonene på hvert tidspunkt, men når dataene kommer fra ulike kilder, er det ofte ikke tilfellet.

---

<!-- slide template="[[tpl-quote]]" -->

<table>
<tr> <th>Indeks</th> <th>Venstre</th> <th>Høgre</th></tr>
<tr> <td> Venstre</td>
     <td style="background: yellow ;"> </td>
     <td style="background: grey ;"> </td>
</tr>
<tr> <td> Felles</td>
     <td style="background: yellow ;"> </td>
     <td style="background: yellow ;"> </td>
</tr>
<tr> <td> Høgre</td>
     <td style="background: grey ;"> </td>
     <td style="background: yellow ;"> </td>
</tr>
</table>

::: credit
:::

note:
Vi trenger selvsagt å tenke på hva man gjør når man mangler data.
Sett at vi skal flette en venstre og en høyre tabell som har noen
felles og noen unike rader.

*pandas* lar oss definere en flettestrategi, med en *how*-parameter.

---

<!-- slide template="[[tpl-small2]]" -->

::: leftimage

# *Inner join*
<table>
<tr> <th>Indeks</th> <th>Venstre</th> <th>Høgre</th></tr>
<tr> <td> Venstre</td>
     <td style="background: red ;"> Droppa </td>
     <td style="background: gray ;"> </td>
</tr>
<tr> <td> Felles</td>
     <td style="background: yellow ;"> </td>
     <td style="background: yellow ;"> </td>
</tr>
<tr> <td> Høgre</td>
     <td style="background: grey ;"> </td>
     <td style="background: red ;"> Droppa </td>
</tr>
</table>

# *Left join*
<table>
<tr> <th>Indeks</th> <th>Venstre</th> <th>Høgre</th></tr>
<tr> <td> Venstre</td>
     <td style="background: yellow ;"> </td>
     <td style="background: green ;"> NaN </td>
</tr>
<tr> <td> Felles</td>
     <td style="background: yellow ;"> </td>
     <td style="background: yellow ;"> </td>
</tr>
<tr> <td> Høgre</td>
     <td style="background: grey ;"> </td>
     <td style="background: red ;"> Droppa </td>
</tr>
</table>

:::
::: leftcredit
:::

::: rightimage

# *Outer join*
<table>
<tr> <th>Indeks</th> <th>Venstre</th> <th>Høgre</th></tr>
<tr> <td> Venstre</td>
     <td style="background: yellow ;"> </td>
     <td style="background: green ;"> NaN </td>
</tr>
<tr> <td> Felles</td>
     <td style="background: yellow ;"> </td>
     <td style="background: yellow ;"> </td>
</tr>
<tr> <td> Høgre</td>
     <td style="background: green ;"> NaN</td>
     <td style="background: yellow ;"> </td>
</tr>
</table>

# *Right join*
<table>
<tr> <th>Indeks</th> <th>Venstre</th> <th>Høgre</th></tr>
<tr> <td> Venstre</td>
     <td style="background: red ;"> Droppa </td>
     <td style="background: grey ;"> </td>
</tr>
<tr> <td> Felles</td>
     <td style="background: yellow ;"> </td>
     <td style="background: yellow ;"> </td>
</tr>
<tr> <td> Høgre</td>
     <td style="background: green ;"> NaN </td>
     <td style="background: yellow ;"> </td>
</tr>
</table>

:::
::: rightcredit
:::

note:
Der er fire vanlige valg.  Terminologien er den samme som brukes i 
databasebehandling, der vi skiller mellom indre,  ytre, venstre og
høyre *join*.

Indre *join* dropper alle rader som ikke finnes i begge tabellene, 
mens ytre join tar med alle radene og fyller inn såkalte NaN-verdier
der data mangler.

NaN står for *Not a Number* og er et standardbegrep som dere kan
støte på ofte i datasett.  Det kan godt være at dere laster nede
datasett med NaN-verdier fordi måledata av en eller anden grunn
mangler.

Venstre og høyre *join* bruker radene fra henholdsvis venstre og
høyre tabell, og dropper eller fyller inn verdier i søylene fra 
den andre tabellen.


---

<!-- slide template="[[tpl-smalltext]]" -->

# *View* eller *Copy*

```python
df2 = df[ df["varegruppe"] == "Fersk oppalen laks" ]
```


```python
df2 = df2.copy()
```
<!-- element class="fragment" -->


::: credit
:::

note:
Det siste begrepet jeg vil prøve å forklare i dag er *views*.
Da vi filtrerte filtrerte datasettet tidligere, og lavet `df2`
med data om frossenlaks, fikk vi *ikke* et nytt datasett.

Den nye variabelen `df2` gir oss et nytt *view* til det gamle
datasettet, hvilket betyr at om vi gjør endringer i `df2`, 
gjør vi også endringer i det opprinnelige datasettet `df`, og
vise versa.

Dette kan være både nyttig og problematisk, avhengig av hva vi
skal gjøre videre, og derfor er det viktig å være oppmerksom.

(fragment)
Vi kan godt lave en kopi av datasettet, slik at vi kan bruke dem
uavhengig av hverandre.  Det gjør vi med `copy()`-metoden.

---

# Slutt

Jeg beklager hvis jeg har overveldet dere med detaljer.

Det vi skal ta med oss videre i dag er dette perspektivet på
datasett som tabeller med rader og søyler som vi kan manipulere.

python og pandas gir oss meget kraftfulle verktøy for å manipulere
datasett, men slike verktøy må man lære ett ad gangen.

