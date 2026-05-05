---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  name: python3
  display_name: Python 3 (ipykernel)
  language: python
---

# Kundesegmentering med Klyngeanalyse

Tenk deg at du jobber som dataanalytiker i en bank.
Markedsavdelingen ønsker å kjøre målrettede kampanjer,
men de vet ikke *a priori* hvilke «typer» kunder de har. 
De maskinlæringsmetodene som vi har sett på hittil forutsetter at vi allerede har bestemt hvilke kategorier vi vil dele datasettet i, f.eks. overklasse, middelklasse og arbeiderklasse, og at vi har en metode, om enn kostbar, for å identifisere kategoriene i et datasett som vi kan bruke til trening.
Dette kalles veiledet trening eller *supervised learning*.

Dersom vi ikke har bestemt en kategorisering som vi mener er relevant, kan vi bruke *unsupervised learning* eller trening uten veiledning.
Det vanligste eksempelet på trening uten veiledning er klyngeanalyse (*clustering*).

Vi kan bruke klyngeanalyse for å dele kundemassen inn i klynger (segmenter) som har meget til felles uten å ha nogen formening om *hva* de har til felles.

I dette eksempelet skal vi ta for oss kredittkortkunder, og se hvordan vi kan segmentere kundemassen ved hjelp av klyngeanalyse, for derefter å analysere hva som kjennetegner de ulike segmentene.
Kjøper de mye på avbetaling?
Tar de ut mye kontanter? Betaler de hele regningen hver måned?

::: {admonition} Mål
Identifisere grupper av kunder som ligner på hverandre.
:::

For en bank eller en markedsavdeling kan dette være verdifullt.
Hvis vi vet hvilke klynger kundene våre tilhører, kan vi feks:
* Sende målrettede reklamekampanjer.
* Utvikle skreddersydde finansprodukter (f.eks. et kredittkort for de som reiser mye).
* Identifisere risiko (kunder som tar opp mye gjeld og betaler lite).

::: {admonition} Datasett
I denne leksjonen skal vi bruke et kjent datasett fra Kaggle
som inneholder bruksmønsteret til ca. 9000 kredittkortkunder.
:::


## Bakgrunn

::: {admonition} Hvordan fungerer K-Means-algoritmen?
:class: note dropdown

En av de mest populære algoritmen for klyngeanalyse heter **K-Means**. Navnet avslører egentlig hvordan den fungerer: "K" står for antall klynger vi ønsker å finne, og "Means" (gjennomsnitt) refererer til hvordan algoritmen finner midtpunktet i disse klyngene.

Slik jobber $K$-Means, steg for steg:
1. **Velg K:** Vi bestemmer oss for hvor mange klynger vi vil dele kundene inn i (f.eks. $K = 4$).
2. **Plasser ut midtpunkter:** Algoritmen slipper ned $K$ tilfeldige midtpunkter (kalt *centroider*) i datasettet vårt.
3. **Fordel kundene:** Hver eneste kunde blir tildelt det midtpunktet de ligger nærmest. Nå har vi 4 midlertidige klynger.
4. **Flytt midtpunktet:** Algoritmen regner ut gjennomsnittet av alle kundene i en klynge, og flytter selve midtpunktet til dette nye gjennomsnittet.
5. **Gjenta:** Siden midtpunktene nå har flyttet på seg, må vi fordele kundene på nytt (Steg 3). Dette gjentar seg helt til midtpunktene slutter å flytte på seg. Da er algoritmen i mål!
:::

::: {admonition} Hva betyr "nærmest" i data science?
:class: tip dropdown

Når vi sier at algoritmen finner det midtpunktet som er "nærmest", mener vi matematisk avstand. For å kunne måle denne avstanden riktig, er det helt kritisk at alle variablene våre har samme skala. Hvis vi har én variabel som måles i titusener (f.eks. kredittgrense) og en annen som måles fra 1 til 12 (f.eks. måneder som kunde), vil algoritmen ignorere den lille variabelen helt. Derfor må vi alltid **skalere (standardisere)** dataene våre før vi kjører K-Means!
:::

+++

## Oppsett

Vi importerer de vanlige bibliotekene en gang, i tillegg til `seaborn`
som vi skal bruke til visualisering.
Bibliotekene for klyngeanalyse skal vi importere etter hvert som vi
trenger dem.

```{code-cell} ipython3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
```

## Steg 1. Datasett

::: {admonition} Oppgåve
Last ned datasettet
fra [Kaggle](https://www.kaggle.com/datasets/arjunbhasin2013/ccdata)
eller fra kurssiden.  Filen skal hete `CC GENERAL.csv`.
:::

Vi begynner med å laste inn data og biblioteker:

```{code-cell} ipython3
df = pd.read_csv("CC GENERAL.csv")
df.head()
```

### Variabler

Når vi skriver ut de første radene, ser vi at datasettet inneholder en rekke kolonner med tall. Hver rad representerer én unik bankkunde og deres adferd over «de siste 6 månedene». 

Selv om vi skal la K-Means-algoritmen se på alle variablene for å finne skjulte mønstre, skal vi spesielt se på 5 av de 17 variablene:

1. **`BALANCE`**: Saldoen på kortet. Dette viser hvor mye penger kunden skylder banken akkurat nå.
2. **`PURCHASES`**: Hvor mye kunden har handlet for totalt (i butikk/på nett).
3. **`CASH_ADVANCE`**: Hvor mye kontanter kunden har tatt ut med kredittkortet.
4. **`PAYMENTS`**: Hvor mye kunden totalt har betalt ned på kredittkortregningen sin.
5. **`CREDIT_LIMIT`**: Kundens kredittgrense.

::: {admonition} Andre variabler
:class: note
Du kan lese mer om de andre variablene på kaggle, [ https://www.kaggle.com/datasets/arjunbhasin2013/ccdata,]( https://www.kaggle.com/datasets/arjunbhasin2013/ccdata)
:::

+++

## Steg 2: Datavask og manglende verdier

Før vi kan begynne å lete etter spennende kundesegmenter, må vi sikre at dataene våre er av god kvalitet. Maskinlæringsalgoritmer (som K-Means i Python) takler nemlig ikke tomme celler, også kalt manglende verdier eller `NaN` (Not a Number). Hvis vi mater algoritmen med et datasett som har hull i seg, vil koden vår rett og slett krasje.

Vi starter derfor med å bruke `.isna().sum()` for å telle nøyaktig hvor mange tomme celler vi har i hver eneste kolonne:

```{code-cell} ipython3
# Undersøker om vi mangler data
df.isna().sum()
```

::: {admonition} Refleksjonsspørsmål
Er manglende data et problem i dette tilfellet?
Kan vi tillate oss å droppe alle radene med manglende data?
Du må gjerne legge til kode for å sjekke hvor stort datasettet
:::

+++

### Vurdering: Hva gjør vi med hullene?

Resultatet over viser at vi mangler 313 verdier i kolonnen `MINIMUM_PAYMENTS` og 1 verdi i `CREDIT_LIMIT`. Datasettet vårt har totalt ca. 8950 rader. De manglende verdiene utgjør altså bare rundt 3,5 % av det totale datagrunnlaget vårt.

Når vi som dataanalytikere møter manglende data, har vi grovt sett to valg:
1. **Imputering:** Vi kan fylle inn de tomme cellene med "kvalifiserte gjetninger", for eksempel gjennomsnittet eller medianen til resten av kundene.
2. **Sletting:** Vi kaster de radene som mangler data helt ut av datasettet.

I vårt tilfelle velger vi **sletting** (gjennom Pandas-funksjonen `.dropna()`). Vi har fortsatt over 8600 komplette kunder igjen å bygge segmenter på, sannynsligvis nok data for K-Means. Hvis vi i stedet fyller inn fiktive gjennomsnittstall for hva folk betaler i minimumsavdrag, risikerer vi å vanne ut dataene og i verste fall skape kunstige mønstre som ødelegger for klyngene våre.

```{code-cell} ipython3
# 1. Vi fjerner alle rader som mangler data
df = df.dropna()
```

Samtidig benytter vi anledningen til å fjerne kolonnen `CUST_ID`. Dette er bare et unikt kundenummer (f.eks. "C10001"). K-Means regner ut *matematisk avstand*, og denne ID-variabelen med bokstaver skal ikke være med i selve analysen.

```{code-cell} ipython3
# 2. Vi kaster kunde-ID-kolonnen
df = df.drop("CUST_ID", axis=1)

# Sjekker at vi fortsatt har nok kunder igjen til analysen vår
print(f"Antall kunder igjen i datasett: {len(df)}")
```

## Steg 3: Utforskende dataanalyse (EDA)

Før vi slipper løs maskinlæringen, er det god praksis å bli visuelt kjent med dataene våre. Vi kaller dette Utforskende Dataanalyse (EDA - Exploratory Data Analysis). Målet er å se etter sammenhenger (korrelasjoner) og se hvordan dataene er fordelt. Er de fleste kundene ganske like, eller har vi noen ekstreme avvikere?

::: {admonition} Et nytt verktøy: Seaborn
:class: tip dropdown

Til nå har vi kanskje brukt standardverktøyet `matplotlib` for å lage grafer.
Nå skal vi bruke et bibliotek som heter **Seaborn** (`import seaborn as sns`). 

Seaborn er bygget "på toppen av" matplotlib, men er spesialdesignet for statistisk analyse og har **innebygd støtte for Pandas DataFrames**.
Dette gjør det ganske behagelig å jobbe med som dataanalytiker.

På overflaten har nesten alle Seaborn-funksjoner den samme logiske og enkle strukturen. Du gir funksjonen selve tabellen din, og forteller deretter hvilke kolonner som skal tegnes opp:
`sns.plottetype(data=df, x="kolonnenavn", y="kolonnenavn", hue="grupperingskolonne", ...)`

Der matplotlib ofte krever mange linjer med kode, gjør Seaborn det samme med én linje, og grafene ser mye mer moderne ut rett ut av boksen. Vil du se mulighetene, anbefales [Seaborns offisielle oversikt over funksjoner (Tutorial)](https://seaborn.pydata.org/tutorial/function_overview.html) på det sterkeste!
:::

### Det store overblikket: Pairplot

Vi starter med et fugleperspektiv. En `pairplot` tar en liste med variabler og plotter *alle mot alle* i en stor matrise. Langs diagonalen får vi se selve fordelingen av hver enkelt variabel. 

Siden det er tungt for maskinen å plotte alle 17 variablene samtidig, plukker vi ut de 5 forretningskritiske variablene vi definerte tidligere:

```{code-cell} ipython3
# Vi definerer listen med favorittvariablene våre
sel_features = ["PURCHASES", "CASH_ADVANCE", "BALANCE", "PAYMENTS", "CREDIT_LIMIT"]

# Lager et pairplot. corner=True fjerner speilbildene slik at det blir lettere å lese!
# diag_kind angir fordelingsfunksjonen langs diagonalen, vi kunne også bruk "hist" for histogram
g = sns.pairplot(df[sel_features], corner=True, diag_kind="kde")

# Justerer størrelsen litt så den blir god å lese
g.figure.set_size_inches(12, 12)

# Viser grafen
plt.show()
```

Hvis du ser på fordelingene (grafene som går på skrått nedover), vil du legge merke til at nesten alle sammen har en lang "hale" mot høyre. Dette er typisk i feks. finansdata; de aller fleste kundene har lave saldoer og få kjøp, men det finnes en liten gruppe kunder som drar kortet for ekstreme summer.

For å se nærmere på disse ekstreme kundene, kan vi dykke ned i to spesifikke variabler med en `JointGrid`.

+++

### Saldo vs. Kjøp

La oss se på sammenhengen mellom hvor mye kunden skylder (`BALANCE`) og hvor mye kunden handler for (`PURCHASES`). Vi bruker et spredningsplot (scatterplot) for å se hver enkelt kunde som en prikk. I tillegg legger vi inn et "boxplot" på kantene. Et boxplot er fantastisk til å vise hvor "normalen" befinner seg (inni boksen), og hvor avvikerne (prikkene på utsiden) er.

```{code-cell} ipython3
# Setter opp et tomt rutenett for to variabler
g = sns.JointGrid(data=df, x="BALANCE", y="PURCHASES", height=8)

# Legger inn spredningsplottet i midten (alpha gjør prikkene litt gjennomsiktige)
g.plot_joint(sns.scatterplot, alpha=0.4)

# Legger inn boxplots på margene for å tydeliggjøre "outlierne"
g.plot_marginals(sns.boxplot)

plt.show()
```

Når vi ser på spredningsplottet i midten, ser vi at nesten alle prikkene (kundene) ligger moset sammen i en massiv klump nede i venstre hjørne. Samtidig strekker aksene seg helt opp til over 40 000. Dette skjer fordi et relativt lite antall kunder har ekstrem adferd sammenlignet med «hvermansen». 

For å virkelig forstå hvor skjevt dette er, kan vi se på **boksplottene** som ligger på topp- og høyremargen. 


Slik leser vi de:

1. **Selve boksen:** Boksen representerer de midterste 50 % av kundene våre (fra 25. til 75. persentil). Som vi ser, er denne boksen knøttliten og trykket helt ned mot null. Det betyr at den "vanlige" kunden har veldig lav saldo og få kjøp.
2. **Streken inni boksen:** Dette er medianen (den kunden som er nøyaktig i midten hvis vi stiller alle opp på rekke).
3. **Værhårene (linjene som stikker ut):** Disse viser det "normale" variasjonsområdet for vanlige kunder.
4. **Alle de svarte prikkene på utsiden:** Dette er matematisk definerte **uteliggere (outliers)**. Man kaller dem gjerne for «hvaler» – de få kundene som står for et stort volum av feks gjeld eller forbruk.

Siden den store massen av kunder er så sammentrykt, er det vanskelig å se noen mønstre i selve klumpen. Heldigvis finnes det triks for å spre dem ut

### Se tydeligere med logaritmisk skala

For å faktisk kunne se mønsteret inni den store klumpen med "vanlige" kunder, kan vi endre aksene til en **logaritmisk skala**. Dette fungerer som et forstørrelsesglass som strekker ut de lave verdiene, og komprimerer de ekstremt høye verdiene.

```{code-cell} ipython3
# Setter opp et tomt rutenett for to variabler
g = sns.JointGrid(data=df, x="BALANCE", y="PURCHASES", height=8)

# Legger inn spredningsplottet i midten (alpha gjør prikkene litt gjennomsiktige)
g.plot_joint(sns.scatterplot, alpha=0.4)

# Legger inn boxplots på margene for å tydeliggjøre "outlierne"
g.plot_marginals(sns.boxplot)

g.ax_joint.set_xscale('symlog')
g.ax_joint.set_yscale('symlog')
g.ax_joint.grid(True, linestyle="--", alpha=0.5)

plt.show()
```

```{code-cell} ipython3

```

::: {admonition} 'symlog' og 'log'?
:class: note dropdown

Vanligvis, når vi ønsker en logaritmisk skala i Python (for eksempel i et standard Matplotlib-plot), bruker vi kommandoen `plt.xscale("log")`. 

Problemet i vårt spesifikke datasett er at mange kunder har *nøyaktig 0 kr* i kjøp eller saldo. Som du kanskje husker fra matten, er logaritmen av 0 ikke definert (den går mot minus uendelig). Hvis vi hadde brukt en vanlig `"log"`-skala her, ville Python enten gitt oss en feilmelding, eller enda verre: den ville bare slettet alle punktene med 0 kr fra grafen uten å si ifra!

Løsningen er å bruke `"symlog"` (symmetrical log). Dette er en genial funksjon som fungerer akkurat som en vanlig logaritmisk skala for store tall, men som glir over til å bli en vanlig lineær skala akkurat rundt nullpunktet. På denne måten får vi i pose og sekk: Vi strekker ut de store tallene for å se mønstre, *og* vi beholder kundene med 0 kr i forbruk trygt i grafen vår!
:::


::: {admonition} Hva betyr dette for maskinlæringen vår?
:class: warning

Boksplottet på toppen og siden bekrefter mistanken vår: Vi har mange "outliere"! De svarte prikkene som strekker seg langt ut til høyre og oppover, er kunder med helt ekstrem adferd sammenlignet med normalen (inni selve boksen). 

Dette skaper et lite problem for oss. Siden K-Means-algoritmen baserer seg på å måle avstander mellom punkter, kan disse ekstreme "hvalene" trekke klyngenes midtpunkter helt ut av kurs. K-Means lar seg nemlig veldig lett påvirke av slike uteliggere. 

Derfor må vi **skalere** dataene våre og vurdere om vi skal **fjerne** "outliere" eller gjøre en log-transformasjon på disse kolonnene ($x^{\prime} = \log{(x+1)}$)
:::

+++

### Risiko og Kredittutnyttelse

For en bank er det ett forhold som er kanskje enda viktigere enn hvor mye kunden handler for: Hvor stor **risiko** utgjør kunden? 

For å analysere dette, skal vi se på forholdet mellom hvor mye kunden skylder akkurat nå (`BALANCE`), og hva kredittgrensen deres er (`CREDIT_LIMIT`). Nærmer de seg taket for hva de har lov til å låne? Vi lager et nytt scatterplot for å se om vi finner et mønster.

```{code-cell} ipython3
# Nytt JointGrid for Balance vs Credit Limit
g2 = sns.JointGrid(data=df, x="BALANCE", y="CREDIT_LIMIT", height=8)

# Vi bruker scatterplot med rød farge for å illustrere risiko
g2.plot_joint(sns.scatterplot, alpha=0.4, color="darkred")

# Boksplott på margene for å se fordelingen
g2.plot_marginals(sns.boxplot, color="darkred")
# Vi kan også ha histogram langs margene:
#g2.plot_marginals(sns.histplot, color="darkred")

plt.show()
```

Dette plottet ser ganske annerledes ut! Legg merke til at prikkene danner en slags usynlig, skrå vegg. Denne "veggen" representerer grensen der saldoen er nøyaktig lik kredittgrensen. 

Kunder som ligger presset helt opp mot denne skrå streken, har "maket ut" kredittkortet sitt. For en bank er dette et klassisk faresignal, fordi det betyr at kunden ikke har mer å gå på og potensielt sliter med å betale ned gjelden sin. 

Ved å fôre K-Means-algoritmen med disse variablene etterpå, håper vi at den klarer å skille de "trygge" kundene fra de som utgjør en høy risiko, helt av seg selv!

+++

## Steg 4: Korrelasjon — Henger variablene sammen?

Før vi mater dataene våre inn i en maskinlæringsalgortime, er det viktig å vite om noen av variablene våre dypest sett måler "det samme". K-Means-algoritmen teller nemlig avstand. Hvis vi fôrer den med to variabler som er ekstremt sterkt korrelert (de beveger seg helt i takt), vil algoritmen i praksis gi denne egenskapen dobbel vekt!

For å undersøke dette, skal vi lage en korrelasjonsmatrise for *hele* datasettet vårt (alle 17 variablene). Vi regner ut *Pearsons korrelasjonskoeffisient*, som går fra -1 (perfekt negativ sammenheng) til 1 (perfekt positiv sammenheng). 0 betyr at det ikke er noen sammenheng.

For å gjøre en så enorm tabell leselig for menneskeøyne, bruker vi Seaborn til å lage et stort "varmekart" (heatmap).

```{code-cell} ipython3
# Regner ut korrelasjonen for hele datasettet
korrelasjon_alle = df.corr()

# Setter opp en stor figur slik at vi får plass til alle de 17 variablene
plt.figure(figsize=(16, 12))

# Lager varmekartet. 
# annot=True skriver inn tallene, og fmt=".1f" tvinger frem kun 1 desimal for å unngå kaos!
sns.heatmap(korrelasjon_alle, annot=True, fmt=".1f", cmap="coolwarm", vmin=-1, vmax=1)

plt.title("Korrelasjonsmatrise for alle kredittkortvariablene")
plt.show()

#Viser tabelenn for de 5 utvalgte
display(korrelasjon_alle.loc[sel_features, sel_features])
```

Vi undersøker varmekartet med korrelasjonsverdier: Den røde streken på skrå er bare variablene som krysser med seg selv (som alltid er 1). Vi ser etter andre mørkerøde eller blå bokser.

1. **De åpenbare tvillingene:** Se på `PURCHASES` og `ONEOFF_PURCHASES` (engangskjøp). De har en korrelasjon på over 0.9! Det samme gjelder `PURCHASES` og `PURCHASES_TRX` (antall transaksjoner). Dette gir totalt mening: Kunder som kjøper mye, har også mange transaksjoner.
2. **Kjøp og betaling:** Vi ser en tydelig positiv sammenheng mellom `PURCHASES` og `PAYMENTS`. Kunder som drar kortet for store summer, pleier også å overføre større summer for å betale ned på regningen.

I en streng statistisk analyse ville vi kanskje ha kastet noen av "tvillingvariablene" for å unngå at kjøpsadferd får uforholdsmessig mye makt over klyngene våre (dette kalles multikollinearitet). Men for denne øvelsen beholder vi alle variablene, slik at K-Means får et så rikt bilde av kunden som mulig. Vi ser ellers at det er lav korrelasjon mellom variablene.

::: {admonition} Fargekart(`cmap`) i Seaborn
:class: tip dropdown

I koden over brukte vi `cmap="coolwarm"`. Dette fargekartet er bra for korrelasjoner. Det gjør at negative tall (motsatt sammenheng) blir kalde og blå, mens positive tall (sterk sammenheng) blir varme og røde. Verdier rundt 0 (ingen sammenheng) glir inn i den nøytrale, grå bakgrunnen. Dette gjør at øynene dine automatisk trekkes mot faresignalene
:::

+++

## Steg 5: Standardisering og optimalt antall klynger

Nå har vi rene data, og vi kjenner til svakhetene i dem (som at vi har noen "hvaler" av noen kunder). Nå skal vi gjøre dataene spiselige for K-Means-algoritmen.

### 4.1 Skalering av dataene

Som vi var inne på tidligere, regner K-Means ut matematisk avstand for å finne ut hvilke kunder som er like. 
Tenk deg at vi ser på variablene `BALANCE` (som kan gå opp til 20 000 kr) og `TENURE` (hvor mange måneder kunden har hatt kortet, som går fra 1 til 12). Siden avstanden mellom 0 og 20 000 er gigantisk i forhold til avstanden mellom 1 og 12, vil algoritmen utelukkende bry seg om saldoen, og totalt ignorere hvor lenge de har vært kunder.

For å fikse dette bruker vi en teknikk som kalles **Standardisering** (`StandardScaler`). Den klemmer og strekker på alle variablene våre slik at alle sammen får et gjennomsnitt på 0, og et standardavvik på 1. Da stiller alle variablene likt i "kåringen" av klyngene.

```{code-cell} ipython3
# Importerer verktøyet for standardisering fra scikit-learn
from sklearn.preprocessing import StandardScaler

# Lager en "skalerings-maskin"
scaler = StandardScaler().set_output(transform="pandas")

# Kjører dataene våre gjennom maskinen. 
# (Fit regner ut gjennomsnittet, transform utfører selve endringen)
df_scaled = scaler.fit_transform(df)

# Tar en titt på de skalerte dataene. Legg merke til at tallene nå er små (både positive og negative)!
df_scaled.head()
```

::: {admonition} Et lite scikit-learn-triks: Hvorfor bruke "set_output"?
:class: tip dropdown

Tradisjonelt sett har maskinlæringsbiblioteket `scikit-learn` vært litt kronglete å jobbe med sammen med Pandas. Når man sendte en pen Pandas-tabell inn i en skaleringsmaskin, spyttet den nesten alltid ut en "ren" tallmatrise i retur – der alle kolonnenavnene og rad-ID-ene var slettet! 

Tidligere måtte vi derfor bygge tabellen vår opp på nytt manuelt rett etter skaleringen, slik som dette:
`df_scaled = pd.DataFrame(skalert_data, columns=df.columns)`

Dette er jo litt tungvint. For å slippe dette manuelle steget, bruker vi det moderne trikset `.set_output(transform="pandas")` når vi oppretter maskinen. Da gjør scikit-learn ryddejobben for oss, og vi får en fiks ferdig tabell tilbake!
:::

+++

### 4.2 Hvor mange klynger skal vi ha? (Elbow og Silhouette)

K-Means krever at vi forteller den på forhånd hvor mange klynger ($K$) den skal lete etter. Hvordan man finner dette er ikke nødvendigvis så lett å si. Det finnes heller ikke noe klar fasit - vi må bruke skjønn og praktisk tolkning fra det dataene beskriver og leve med litt usikkerhet. Vi har heldigvis 2 håndfaste teknikker som kan hjelpe oss.

Vi kan teste flere forskjellige verdier for $K$ (for eksempel fra 2 til 10) og la to matematiske mål hjelpe oss med å velge den beste:

1. **Inertia (Elbow-metoden):** Måler hvor kompakte klyngene er (hvor kort avstand det er fra kundene inn til midtpunktet i klyngen sin). Vi vil at dette tallet skal være så lavt som mulig. Hvis vi plotter dette, ser grafen ofte ut som en arm, og vi leter etter "albuen" der grafen slutter å stupe og begynner å flate ut. 
2. **Silhouette-score:** Måler både hvor tette klyngene er internt, og hvor tydelig de er skilt fra andre klynger. Verdien går fra −1 til 1, og høyere verdi betyr vanligvis bedre klyngedannelse

+++

Nå skal vi la datamaskinen trene en hel haug med K-Means-modeller (fra $K=2$ til $K=20$), og lagre poengsummene (`inertia`og `silhouette`) for hver runde slik at vi kan plotte dem. 

> *(Merk: Vi velger å stoppe på 20 klynger. Å regne ut Silhouette-score er en veldig tung matematisk operasjon for datamaskinen, og vi ønsker ikke at koden skal bruke evigheter på å kjøre!)*

```{code-cell} ipython3
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Vi tester antall klynger (k) fra 2 til og med 10
k_list = range(2, 21)

inertia_list = []
sil_score = []

for k in k_list:
    # random_state=11 sørger for at K-Means gir nøyaktig samme svar hver gang
    model = KMeans(n_clusters=k, n_init=50).set_output(transform="pandas")
    
    # Vi trener modellen på de skalerte variablene våre
    result = model.fit_predict(df_scaled)
    
    # Lagrer poengsummene
    inertia_list.append(model.inertia_)
    sil_score.append(silhouette_score(df_scaled, result))

# --- Plotter Inertia (Elbow-metoden) ---
plt.figure(figsize=(8, 4))
plt.plot(k_list, inertia_list, 'o-', color="blue")
plt.xticks(k_list)
plt.title("Elbow-metoden (Inertia)")
plt.xlabel("Antall klynger (K)")
plt.ylabel("Inertia (lavere er bedre)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# --- Plotter Silhouette-score ---
plt.figure(figsize=(8, 4))
plt.plot(k_list, sil_score, 'o-', color="orange")
plt.xticks(k_list)
plt.title("Silhouette-score")
plt.xlabel("Antall klynger (K)")
plt.ylabel("Score (høyere er bedre)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
```

## Steg 6: Trene den endelige modellen

Å tolke disse grafene er like mye kunst som vitenskap:

1. I **Elbow-plottet** ser vi at kurven faller raskest i starten 2-4, og begynner å flate ut og danne en svak "albue" et sted mellom 4 og 5 klynger. Videre økning av antall klynger gir fortsatt forbedring, men mye mindre per ekstra klynge.
2. I **Silhouette-plottet** har vi en soleklar topp på **K = 3**. Etter dette stuper faktisk poengsummen ned i en dal ved K=4 og 5, før den bygger seg opp til en ny, men litt lavere topp rundt K=9.

Matematikken sier at kundene våre klumper seg aller best sammen hvis vi deler dem i 3. Hvis markedsavdelingen insisterte på at de trengte mange, finkornede segmenter, ville det neste logiske valget vårt vært 9. Dette er forbi «albuen», men silhouette-scoren får en ny topp her. $K=3$ klynger ser ut til å være før albuen rundt 4-5, slik at vi også kan forsvare $k=4$. Selv om `silhouette_scoren` faller en del her er ikke forskjellen enorm. 

### Er ikke 0.25 egentlig en veldig lav score?

Som en tommelfingerregel er en score over 0.7 god, over 0.5 rimelig og mellom 0.25-0.5 svak. 

Hvis du ser på Y-aksen for Silhouette-scoren, vil du legge merke til at vinneren (K=3) bare får en score på rett under 0.25. 

Rent matematisk betyr en score under 0.25 at klyngene våre er svake, at de overlapper en del, og at grensene mellom dem er utydelige. Hvorfor får vi ikke høyere score? 

Vi kan peke på flere grunner:
1. **Menneskelig adferd:** I virkeligheten finnes det ingen skarp og magisk strek mellom en "gjennomsnittskunde" og en "storkunde". Adferd er et spekter, ikke pene bokser. Selv om matten klager over overlapp, kan disse segmentene likevel være gull verdt for banken.
2. **Hvaler og «outliere»:** KMeans er sensitiv for ekstreme verdier som trekker ut sentrumene i klyngene og «ødelegger». Vi kan fjerne disse, men vi vil jo prøve å fange opp «hvalene» da de er verdifulle kunder. Vi kan vurdere log-transformasjon, eller brukt en annen metode til å skalere dataene. Vi brukte `StandardScaler` men kan vurdere å bruke `RobustScaler` i stedet. Denne bruker blant annet "median" i stedet for gjennomsnittet til å skalere og er designer for å ignorere "outliere"
3. **Dimensjonalitetens forbannelse:** Vi ba algoritmen vurdere alle 17 variabler samtidig. Det betyr at maskinen leter etter klynger i et 17-dimensjonalt rom. I høye dimensjoner begynner matematisk avstand å miste litt av meningen sin, og alt ser ut til å flyte sammen. Dette fenomenet kalles *The Curse of Dimensionality*, og det presser Silhouette-scoren nedover. Vi kan vurdere å redusere dimensjon med feks PCA men 17-dimensjoner og 8600+ rader burde være OK

### Valg av $K$

For å gjøre vår aller første kundeprofilering oversiktlig og meningsfull, lytter vi til den absolutte toppen i dataene og velger **K = 3**.

Nå gjenstår det viktigste: Vi trener en endelig modell med 3 klynger, finner ut hvilken klynge hver kunde tilhører (0, 1 eller 2), og **limer disse merkelappene tilbake i den originale datatabellen vår (`df`)**. Det er jo de faktiske krone-beløpene vi vil analysere etterpå, ikke de skalerte dataene.

```{code-cell} ipython3
# Vi bestemmer oss for 3 klynger basert på innsikten fra Silhouette- og Elbow-plottene
cluster_n = 3

# Setter opp K-Means-maskinen. 
# n_init=50 tvinger algoritmen til å prøve 50 forskjellige startposisjoner. 
kmeans = KMeans(n_clusters=cluster_n, n_init=50)

# Vi trener modellen på de SKALERTE dataene. 
# Algoritmen regner, og spytter ut en merkelapp (0, 1 eller 2) for hver kunde.
clusters = kmeans.fit_predict(df_scaled)

# Nå som matten er ferdig, vil vi analysere kundene i ekte kroner og øre.
# Derfor lager vi en kopi av den ORIGINALE (uskalerte) tabellen vår.
df_clusters = df.copy()

# Til slutt limer vi klynge-merkelappene (0, 1, 2) inn som en helt ny kolonne i denne kopien
df_clusters["cluster"] = clusters
```

## Steg 7: Bli kjent med klyngene (Profilering)

Datamaskinen har nå delt kundene våre inn i tre grupper (0, 1 og 2). Men K-Means gir ikke gruppene navn – det er vår jobb som analytikere! 

Før vi ser på *hva* som kjennetegner kundene, burde vi sjekke *hvor mange* som havnet i hver gruppe. Hvis en klynge bare består av noen få personer, er det ikke et reelt kundesegment vi kan bygge markedsføring rundt, og vi har ikke kjørt en god KMeans

```{code-cell} ipython3
# Teller opp antall kunder i hver klynge, og sorterer listen fra 0 til 2
klynge_storrelser = df_clusters["cluster"].value_counts().sort_index()

# Viser resultatet pent som en tabell
display(klynge_storrelser.to_frame(name="Antall kunder"))
```

### Er klyngene våre fornuftige?

Når vi ser på fordelingen over, ser vi noe typisk for kundedata: Vi har én gigantisk "hovedgruppe" (Klynge 0 med nesten 6000 kunder), og to mindre, men tydelige nisjegrupper (Klynge 1 og 2 med over 1000 kunder hver). Alle tre er mer enn store nok til å være reelle markedssegmenter.

At Klynge 0 er så massiv, betyr rett og slett at flertallet av kundene våre har en ganske "normal" og udramatisk kortbruk. K-Means-algoritmen har identifisert de mest ekstreme ytterpunktene i datasettet og skilt dem ut i egne grupper, mens resten har havnet i den store gryta. 

::: {admonition} Kan vi dele opp hovedgruppen enda mer?
:class: tip dropdown

For en markedsavdeling kan et segment på nesten 6000 kunder fort bli litt for bredt til at man kan lage skreddersydde kampanjer. Det er høyst sannsynlig at denne gigantiske Klynge 0 inneholder flere ulike undergrupper (f.eks. "De som bare handler på nett", "De som handler matvarer", osv.). 

Hvordan kunne vi funnet disse?
- Vi kunne valgt en mye høyere $K$ helt i starten (husker du den andre toppen i Silhouette-plottet rundt $K=9$?).
- Vi kan filtrere ut bare disse 6000 kundene til en egen tabell, og kjøre en helt ny og dedikert klyngeanalyse *kun* på dem for å finne sub-segmenter! 
:::

+++

### Bygge kundeprofiler

Resultatet over bekrefter at alle klyngene har en meningsfull størrelse. Klynge 0 er desidert størst (mesteparten av kundebasen), mens de to andre utgjør mindre, men fortsatt betydelige segmenter.

For å gi gruppene meningsfulle navn (som "De forsiktige" eller "Storkonsumentene"), må vi se på gjennomsnittsverdiene for hver gruppe. Vi bruker Pandas-funksjonen `.groupby()` for å samle kundene per klynge, og regner ut gjennomsnittet for de viktigste forretningsvariablene våre.

```{code-cell} ipython3
# Vi velger ut de viktigste kolonnene for å forstå økonomien deres
viktige_kolonner = ["BALANCE", "PURCHASES", "CASH_ADVANCE", "CREDIT_LIMIT", "PAYMENTS"]

# Grupperer på klynge og regner ut gjennomsnittet (runder av til hele kroner for ryddighet)
profiler = df_clusters.groupby("cluster")[viktige_kolonner].mean().round(0)

profiler
```

### Tolkning av kundeprofilene

Når vi ser på tabellen over, begynner klyngene plutselig å gi praktisk forretningsmessig mening. La oss koble tallene til ekte kundetyper
- **Klynge 0 – "Gjennomsnittskunden / De forsiktige":** Den store hovedgruppen vår har relativt lave saldoer (830 i snitt), moderate kjøp (519), og tar nesten aldri ut kontanter (334). Kredittgrensen deres er også den laveste. Dette er "hvermansen" som bruker kortet forsiktig og fornuftig.
- **Klynge 1 – "Kontant-uttakerne / Høy risiko":** Denne gruppen utmerker seg med høy tall i `CASH_ADVANCE` (hele 3907 i snitt!) og har den høyeste gjelden (`BALANCE` på 4027). De handler nesten ingenting i butikk (`PURCHASES` er på bunn med 387), men bruker kortet som en ren kredittkilde for å ta ut kontanter. Dette er kanskje en risikogruppe banken må følge nøye med på.
- **Klynge 2 – "VIP / Storkonsumentene":** Den siste gruppen har et stort forbruk (`PURCHASES` på 4301) og har fått den høyeste kredittgrensen av banken (7775). Dette er kundene som drar kortet for alt mulig, og betaler ned store summer (`PAYMENTS`) underveis. De er lønnsomme brukere for banken.




### Gi klyngene forretningsmessige navn (Labels)

Før vi går videre til å visualisere disse kundene, gir vi klyngene navn.
Ingen markedsavdeling ønsker å forholde seg til "Klynge 0" og "Klynge 1". De vil ha ekte navn!

Vi vet nå hvilken klynge som er hva. La oss bruke Pandas-funksjonen `.map()` for å bytte ut de kjedelige tallene (0, 1, 2) med de nye, beskrivende navnene våre i en ny kolonne:

```{code-cell} ipython3
# Vi lager en ordbok (dictionary) som kobler tallet til riktig navn
# (Basert på tallene vi så i profiltabellen vår)
klynge_navn = {
    0: "lavfrekvens-brukere",
    1: "likviditets-fokuserte",
    2: "høyvolumsbrukere"
}

# Vi lager en ny kolonne hvor vi oversetter tallene til tekst
df_clusters["Segment"] = df_clusters["cluster"].map(klynge_navn)

# Tar en rask titt for å se at det fungerte:
df_clusters[["BALANCE", "PURCHASES", "cluster", "Segment"]].head()
```

### Hva skiller segmentene fra gjennomsnittet? (Heatmap)

Nå har vi gitt gruppene våre logiske forretningsnavn basert på snittforbruket deres i kroner og øre (eller hva nå enn valuta/enhet det er i dataene). For å virkelig forstå hvordan K-Means-algoritmen "tenkte" da den lagde disse gruppene, må vi se på de *standardiserte* dataene vi faktisk matet den med.

Husk at i de skalerte dataene er **0 nøyaktig gjennomsnittet for hele banken**. 
* Positive tall (røde) betyr at segmentet ligger *over* snittet.
* Negative tall (blå) betyr at segmentet ligger *under* snittet.

Vi grupperer de skalerte dataene våre på de nye segmentnavnene våre, og tegner et varmekart (heatmap). Da kan vi lese av kundeprofilene som en åpen bok.

Dette kunne vi også gjort med en gang og brukt heatmap-et til å bestemme hvilke segmenter KMeans har skilt ut.

::: {admonition} Hva var egentlig en Z-score igjen?
:class: tip dropdown

Husker du at vi brukte `StandardScaler` tidligere i oppgaven? Den funksjonen tok alle kronebeløpene våre og regnet dem om til **Z-scores**. 

En Z-score forteller oss rett og slett hvor mange standardavvik en verdi ligger over eller under gjennomsnittet:
* **0** betyr at verdien er *nøyaktig* på snittet for hele banken.
* **+1** betyr at kunden ligger ett standardavvik *over* snittet (høyt forbruk).
* **-1** betyr at kunden ligger ett standardavvik *under* snittet (lavt forbruk).

I tillegg til at KMeans må ha det slik, kan vi også nå se på "antall kjøp" og "kredittgrense i kroner" på nøyaktig samme skala.
:::

```{code-cell} ipython3
# Vi lager en kopi av de skalerte dataene for ikke å rote til originalen
df_scaled_profiling = df_scaled.copy()

# Vi henter inn Segment-navnene fra den andre tabellen vår
df_scaled_profiling["Segment"] = df_clusters["Segment"]

# Grupperer på segment og regner ut snittet for de standardiserte variablene
cluster_centroids = df_scaled_profiling.groupby("Segment").mean()
display(cluster_centroids)


# Plotter heatmap
plt.figure(figsize=(14, 6))

# Vi transponerer tabellen (.T) slik at variablene kommer på Y-aksen og segmentene på X-aksen.
# center=0 sørger for at fargeskalaen er helt hvit på akkurat gjennomsnittet!
sns.heatmap(cluster_centroids.T, cmap="coolwarm", annot=True, fmt=".2f", center=0)

plt.title("Kundeprofiler: Avvik fra bankens gjennomsnitt (Z-scores)")
plt.show()
```

+++ {"jp-MarkdownHeadingCollapsed": true}

Siden tallene er Z-scores (antall standardavvik fra snittet), kan vi se nøyaktig hva som definerer hver gruppe:

1. **Lavfrekvens-brukere:** Denne raden er farget i kalde, blåtoner (negative tall) over hele linja. De ligger konsekvent *under* bankens gjennomsnitt på både saldo, kjøp og kontantuttak. De er de rolige A4-kundene.
2. **Likviditets-fokuserte:** Her ser du en knallrød boks (høyt positivt tall) på `CASH_ADVANCE` og `BALANCE`, mens `PURCHASES` er blå. Dette viser «ekstrem-adferden» deres: De bruker ikke kortet i butikken, men makser det ut i minibanken
3. **Høyvolumsbrukere:** Denne gruppen lyser rødt på `PURCHASES`, `PAYMENTS` og `CREDIT_LIMIT`. De drar kortet ofte, og betaler store regninger.

+++

## Steg 8: Visualisering med PCA (Prinsipalkomponentanalyse)

Nå har vi tre velfungerende kundeprofiler. Men det gjenstår ett problem: Vi har 17 variabler. Det betyr at klyngene våre eksisterer i et 17-dimensjonalt rom. Hvordan i all verden skal vi kunne plotte det på en flat 2D-skjerm for å "se" kundene våre?

Løsningen er en genial matematisk teknikk kalt **PCA (Principal Component Analysis)**.  
Tenk på PCA som å lyse med en lommelykt på en kompleks 3D-figur for å se skyggen dens på en flat vegg. PCA tar våre 17 dimensjoner og komprimerer dem ned til de 2 dimensjonene (x og y) som fanger opp absolutt mest mulig av variasjonen i datasettet. 

Når vi har gjort det, kan vi endelig lage et scatterplot hvor hver prikk er en kunde, fargelagt etter hvilken klynge de tilhører!

```{code-cell} ipython3
from sklearn.decomposition import PCA

# Klemmer dataene ned til 2 dimensjoner for plotting
pca = PCA(n_components=2).set_output(transform="pandas")

# Kjører PCA på de SKALERTE dataene
pca_resultater = pca.fit_transform(df_scaled)

# Legger til koordinatene i hovedtabellen
df_clusters["PCA1"] = pca_resultater["pca0"]
df_clusters["PCA2"] = pca_resultater["pca1"]

# Plotter klyngene med navnene
plt.figure(figsize=(10, 8))
sns.scatterplot(
    data=df_clusters, 
    x="PCA1", 
    y="PCA2", 
    hue="Segment", 
    palette="viridis", 
    alpha=0.5          
)

plt.title("Kundesegmentene visualisert i 2D (PCA)")
plt.xlabel("Hovedkomponent 1 (Største variasjon i dataene)")
plt.ylabel("Hovedkomponent 2 (Nest største variasjon)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# Hvor mye av den totale variasjonen (100 %) fanger de to PCA-aksene våre opp?
print(f"Varians forklart av 2D-plottet: {pca.explained_variance_ratio_.sum() * 100:.1f} %")
```

PCA-plottet over er fantastisk for å se at vi faktisk *har* tre adskilte grupper, men X- og Y-aksen ("Hovedkomponent 1 og 2") er ren matematikk.

La oss plotte de to kritiske variablene mot hverandre: **(`PURCHASES`)** mot **(`CASH_ADVANCE`)**. Her bruker vi igjen `symlog`-trikset fra starten for å takle at veldig mange kunder har nøyaktig 0 i en av kategoriene.

+++

## Visualisering og avslutning

```{code-cell} ipython3
plt.figure(figsize=(10, 8))
sns.scatterplot(
    data=df_clusters, 
    x="PURCHASES",         # Hvor mye de handler for
    y="CASH_ADVANCE",      # Hvor mye kontanter de tar ut
    hue="Segment", 
    palette="viridis",
    alpha=0.6
)

# Vi bruker symlog (som vi lærte i starten!) for å se mønsteret bedre blant null-verdiene
plt.xscale('symlog')
plt.yscale('symlog')

plt.title("Våre tre kundesegmenter - Kjøp og uttak")
plt.xlabel("Kjøp i butikk / på nett (PURCHASES)")
plt.ylabel("Kontantuttak (CASH_ADVANCE)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
```

Vi undersøker hvordan klyngene oppfører seg. De lavfrekvente (lilla) klumper seg nede i hjørnet nær null (lite kjøp og uttak). Høyvolumsbrukerne (glyserønne) legger seg langt til høyre på X-aksen (høye kjøp), mens de likviditetsfokuserte (turkis) skyter rett opp langs Y-aksen klumper seg i toppen (høye kontantuttak). Modellen treffer bra.

+++

### Grupperte stolpediagram

For å se alle de fem viktigste variablene samtidig, er et klassisk stolpediagram ofte det mest effektive. 

Her bytter vi tilbake til de **standardiserte verdiene (Z-scores)**. Den svarte streken på 0 representerer den "gjennomsnittlige bankkunden". Alt som går over streken er forbruk over snittet, og alt under streken er under snittet.

```{code-cell} ipython3
# Et klassisk gruppert stolpediagram for å sammenligne segmentene
# Vi transponerer (.T) for å få variablene på X-aksen og segmentene som stolper
ax = cluster_centroids[sel_features].T.plot(
    kind="bar", 
    figsize=(12, 6), 
    colormap="viridis", # Beholder det samme fargetemaet som før!
    edgecolor="black",
)

plt.title("Sammenligning av kundesegmenter (Standardiserte verdier)", fontsize=14)
plt.xlabel("Variabel")
plt.ylabel("Z-score (Avvik fra snittet)")
plt.axhline(0, color='black', linewidth=1) # Tegner en tydelig strek på gjennomsnittet
plt.xticks(rotation=0) # Sørger for at teksten på X-aksen står vannrett
plt.legend(title="Segment")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
```

### Visuelle Kundepersonas (Interaktivt Radar-kart)

Stolpediagram er ryddig, men i presentasjoner for ledelsen er **radar-kart (spiderplots)** hyppeste måte å vise kundepersonas på.

Standardbibliotekene vi har brukt til nå (`matplotlib`, `seaborn`, `pandas`) har faktisk utrolig dårlig støtte for å lage pene radar-kart. Derfor bytter vi her verktøy til **Plotly**, som er et moderne bibliotek for interaktive grafer. Siden Plotly-kode ser litt annerledes ut, er kodesnutten under faktisk generert med hjelp av KI (Kunstig Intelligens)
::: {admonition} La KI hjelpe deg å plotte!
:class: tip

Det er utrolig mange detaljer å ha kontroll på og dille med når man visualiserer og lager figurer. Her er KI et utrolig nyttig verktøy å bruke. Forrige stolpediagram har også fått god hjelp fra KI; lærer som har tilvirket dette materialet har ikke i minnet detaljer om fargekart, `plt.axhline` og de hundrevis av andre små "options" vi har når vi plotter. En KI spytter disse ut raskt, og vi kan lette verifisere og gjøre småendringen ved å se på output (figur)

:::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
import plotly.express as px

# Smelter tabellen fra bred til lang for Plotly
df_radar = cluster_centroids[sel_features].reset_index().melt(
    id_vars="Segment", 
    var_name="Variabel", 
    value_name="Z-score"
)

# Vi tegner det interaktive radar-kartet
fig = px.line_polar(
    df_radar, 
    r="Z-score",           
    theta="Variabel",      
    color="Segment",       
    line_close=True,       
    markers=True
)

# Fyller inn farge inni formene
fig.update_traces(fill='toself', opacity=0.5)

#  Her setter vi width og height, og fikser skriftstørrelsen!
fig.update_layout(
    title=dict(text="Kundepersonas i spindelvev (Interaktivt)", font=dict(size=20)),
    polar=dict(
        radialaxis=dict(visible=True),
        angularaxis=dict(tickfont=dict(size=14)) # Gjør variabel-navnene litt større
    ),
    width=900,   # Gjør figuren 900 piksler bred (standard er ofte rundt 600)
    height=700,  # Gjør figuren 700 piksler høy
    legend=dict(font=dict(size=14)) # Gjør tegnforklaringen lettere å lese
)
#fig.show() # For deg
fig.show() # For å vise på nettsiden
```

```{code-cell} ipython3

```
