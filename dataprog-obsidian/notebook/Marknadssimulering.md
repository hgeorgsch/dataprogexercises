---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Marknadssimulering

Eit nyttig område for simulering er marknadsanalyse.
Det er ikkje trivielt, for simuleringa krev at me har ein
modell for korleis kundane oppfører seg, men dersom me har
det, kan me testa konsekvensane av ulike foretningsmessige
grep, som rabattar og tilbodskampanjar.

Me skal ikkje gå inn på korleis ein modellerer kundane.
Det veit psykologar og marknadsanalytikarar meir om.
Her får me nøya oss med enkle og naïve modellar og heller
fokusera på korleis me kan setja saman simuleringa i python.

Me vil trengja to bibliotek, både `random` som me studerte
under [](Tilfeldigheit), og `pyplot` som me har brukt mange
gongar til plotting.

```{code-cell} ipython3
import random
import matplotlib.pyplot as plt
```

::: {hint}
Hugs at oppgåver er vegleiiande.  Målet ditt er å utforska 
korleis du kan modellera omsettinga i ein butikk og kva
som skjer med ulike føresetnader.
Oppgåvene er berre forslag til retningar.
Det er bra å vera kreative.
:::

## Steg 1: Handlande kundar

Lat oss sjå for oss kolonialen på hjørnet.
Før me ser på den handlande kunden, lat oss skipa ein
modell for varene i butikken.
Ein vare har mange eigenskapar, men me treng i utgangspunktet
berre to; namnet og prisen.  
Dette kan me modellera som ein *dictionary* eller `dict` i python.

```{code-cell} ipython3
varer = { "Epler": 10.0,
          "Pærer": 15.0,
          "Bleier": 35.0,
          "Sjokolade": 6.0,
          "Melk": 20.0,
          "Rundstykker": 13.0
        }
```

Ein *dictionary* er ein samling av par, nykel:verdi, som stort
sett vert brukt når me treng å kunna slå opp verdien for ein
gjeven nykel raskt og enkelt.
Her let me nykelen vera namnet og verdien vera prisen.
Ein kan sjølvsagt stussa på at butikken berre har seks varer, og
om epleprisen er per stykk eller per kilo, men det lèt me liggja
til me har kontroll på det grunnleggjande.

Me skal simulera ein ganske dum kunde, som handlar på måfå.
Før me kodar kunden, lat oss uttvetydig definera kva han gjer.

::: {admonition} Definisjon
Ein *måfåkunde* plukkar varer tilfeldig, heilt til han
anten er lei eller er tom for pengar.
Der er eit konstant sannsyn (t.d. 10%) for at han er lei etter
kvar vare.

Resultatet når måfåkunden handlar er ei liste med varer
og ein totalpris for alle varene.
:::

Dette kan me omsetja til python, som ein funksjon som 
simulerer handlinga åt kunden.

```{code-cell} ipython3
def måfåhandling(budsjett=200,sluttsjanse=0.1):

    handlekurv = []
    total_pris = 0.0

    varenavn = list(varer.keys())

    fortsett = True
    while fortsett:
        vare = random.choice(varenavn)
        varepris = varer[vare]

        if budsjett > varepris:
            handlekurv.append( (vare,varepris) )
            print( f"Handlar {vare} til {varepris} kr." )
            total_pris += varepris
            budsjett -= varepris
        else:
            print( f"Tom for pengar.  Vurderte {vare} til {varepris} kr." )
            fortsett = False
    
        if random.random() < sluttsjanse:
            print( f"Lei!" )
            fortsett = False
    return total_pris, handlekurv
```

::: {admonition} Oppgåve 
Gå gjennom koden steg for steg.
Ser det ut som om koden oppfører seg i tråd med definisjon?
Bruk hinta under, som skildrar vanlege triks som me har brukt.
:::

::: {hint}
Funksjonen `random.choice()` plukkar eit tilfeldig element frå ei liste.
Han kan ikkje brukast på andre datastrukturar, so når me har ein `dict` 
må me henta ut nyklane i ei liste.
:::

::: {hint}
Ofte ynskjer me ei løkke med fleire ulike sluttvilkår.
T.d. avbryt måfåkunden både når han er tom for pengar og når han er lei.
Då er det vanleg å bruka ein bolsk variabel `fortsett` som me set til 
`True` før løkka startar.
Inni løkka testar me kvart vilkår, og set til `False` om testen seiar
at løkka bør slutta.
:::

::: {hint}
Eit vanleg problem er å simulera ei hending som opptrer med
$x$% sannsyn.
Standardløysinga er å dra eit tilfeldig tal $X$ i intervalet
0 til 1.  
Om $X$ er uniformt fordelt, er det $x$% sjanse for at $X<\frac{x}{100}$,
og dette vert kriteriet for at hendinga skjer.
:::

::: {admonition} Oppgåve 
Køyr funksjonen og skriv ut resultatet.
Kva er returverdien?
:::

::: {admonition} Refleksjon 
Funksjonen skriv ut informasjon for kvar iterasjon i løkka.
Verker utskrifta rimeleg for ein måfåkunde?
:::


## Steg 2:  Mange kundar i butikken 

::: {admonition} Oppgåve

Simuler valdsamt mange kundar som handlar og plott
eit histogram over pengebruken per kunde.
Du finn grunnteknikkane du treng i øvinga om
[](Tilfeldigheit).

:::

::: {hint}

Me er berre interessert i kor mykje kundane handlar for, men
funksjonen som me skreiv over, returnerer både totalprisen og
handlekurven.  For å skilja desse to variablane kan me skriva
```ipython
kr, kurv = måfåhandling()
```
:::

```{code-cell} ipython3
pengebruk = []
n = 10000
for _ in range(n):
    kundens_pengebruk = måfåhandling()
    pengebruk.append(kundens_pengebruk)

snitt = sum(pengebruk)/n
print(f"Kunder legger i snitt igjen {snitt:.2f} kroner per handletur")

plt.hist(pengebruk, 20)
plt.show()
```


## Steg 3: Varer på salg

Me ynskjer å undersøkja korleis sal og omsetting vert påverka
om me set varer på tilbod. 
Me tek utgangspunkt i ein butikk med eit lite knippe varer til
fast pris, som skildra og simulert over.
Vidare går me ut frå
+ at når ein kunde kjem inn i butikken, har kvar vare ei viss sjanse
  for at kunden kjøper det.
* at når ei vare kjem på sal aukar denne sjansen.

Lat oss starta med å utvida varemodellen.
I staden for berre pris, treng me ein vegleidande pris og
ein salspris.  I utgangspunktet er dei to prisane like.

```{code-cell} ipython3
varer = [ { "vare" : "Epler", "veilpris": 10.0, "salspris": 10.0 },
          { "vare" : "Pærer", "veilpris": 15.0, "salspris": 15.0 },
          { "vare" : "Bleier", "veilpris": 35.0, "salspris": 35.0 },
          { "vare" : "Sjokolade", "veilpris": 6.0, "salspris": 6.0 },
          { "vare" : "Melk", "veilpris": 20.0, "salspris": 20.0 },
          { "vare" : "Rundstykker", "veilpris": 13.0, "salspris": 13.0 },
        ]
```

Her har me vald å representera vareutvalet som ei liste, der kvar
vare er ein `dict`.  Me bruker ein `dict` til varene for å gjera
det lettare å sjå kva pris som er kva.  Me kunne ha late
vareutvalet forbli ein `dict` sjølv om han inneheld andre `dict`*s*,
men det ville ha gjeve oss litt fleire nye syntakselement å læra,
og me har nok som det er.

Me treng ein funksjon som reknar ut sannsynet for at kunden
kjøper ei vare.  Me skal ikkje seia mykje om denne modellen,
berre definera han som ein funksjon, slik:

```{code-cell} ipython3
import numpy as np

def kjopssannsyn(vare,P0=0.2):
    """
    Logistisk modell for salgssannsynlighet gitt %vis avlsag.
    Parameteren `P0` er en basissannsynlighet uten avslag.
    """
    K = 1
    A = (K-P0)/P0
    # disc er rabatten
    disc = ( vare["veilpris"] - vare["salspris"] ) / vare["veilpris"]
    return K/(1+A*np.exp(-(r*disc)))
```

::: {admonition} Oppgåve

Test funksjonen `kjopssannsyn()`.
Parameteren `vare` skal ha same form som i `varer`-katalogen over,
dvs. t.d. `{ "veilpris" : 10, "salspris" : 6 }`.
Test nokre varer me ulike prisar for å sjå kva kjøpssannsyn du
får.

1. Aukar eller avtar sannsynet med aukande rabatt?
2. Samanlikna to varer med same salspris og ulike vegleidande pris.
   Korleis varierer sannsynet med veil. pris?
3. Samanlikna to varer som er sett ned med 20%.  Avheng sannsynet
   av salsprisen eller berre av rabatten (i prosent)?

:::

No må me laga ein ny kundemodell, som tek omsyn til tilbodsprisar.
Den nedanståande funksjonen fylgjer malen frå den forrige kundemodellen
i stor grad, men kunden vurdererer no kvar vare éin gong og kjøper
med eit vist sannsyn om han har råd.

```{code-cell} ipython3
def tilbodshandling(varer,budsjett=200):

    rest = budsjett
    handlekurv = []
    total_pris = 0.0

    for vare in varer:
        p = kjopssannsyn(vare)
        if random.random() < p and vare["salspris"] <= rest:
            rest -= vare["salspris"]
            total_pris += vare["salspris"]
            handlekurv.append( vare )

    return total_pris, handlekurv, rest
```

::: {admonition} Refleksjon

Korleis forstår du endringaene frå den fyrste kundemodellen?

:::

::: {admonition} Oppgåve

Prøvekøyr kundemodellen nokre gongar.
Ser handlekorgane fornuftige ut?

:::

::: {admonition} Oppgåve

Lag ein ny variabel som liknar `varer` men der salsprisane er endra.
Prøvekøyr kundemodellen med dei nye prisane.
Ser handlekorgane fornuftige ut?
Korleis er dei endra?

:::

Legg merke til at varelista (`dict`-objektet) er no ein parameter
til funksjonen, slik at me kan ha fleire varemodellar i spel, med
ulike tilbod og rabattar, og testa kunden på kvar varemodell.


##  Steg 4: Ein dag i butikken

Lat oss gå ut frå at butikken ikkje endrar prisane i laupet av
dagen, slik at det same vareutvalet og dei same prisane gjeld
heile dagsperioden.  Då kan me simulera ein dag i butikken
ved å setja opp eitt vareutval og ei rekkje kundar.

```{code-cell} ipython3
def simuler_dag(n, vareutvalg):
    kurvliste = []
    salgsliste = []
    
    for _ in range(n):
        pris, kurv, _ = tilbodshandling(vareutvalg)
        kurvliste.append(kurv)
        salgsliste.append(pris)

    return salgsliste, kurvliste
```

::: {admonition} Refleksjon
Kva gjer funksjonen over?
:::

::: {admonition} Oppgåve
Prøvekøyr `simuler_dag()` og skriv ut resultatet.
Verkar resultatet fornuftig?
:::

::: {admonition} Oppgåve

Prøvekøyr `simuler_dag()` og skriv ut resultatet.
Verkar resultatet fornuftig?

:::

::: {admonition} Oppgåve
Legg inn nokon tilbodsprisar, og sjå korleis det påverkar omsettinga.
Merk at det er enkelt å rekna ut omsettinga, frå lista over handlesummar.
```python
kr, kurvar = simuler_dag(100,varer)
omsetting = sum(kr)
```
:::

::: {admonition} Oppgåve
Plott omsettinga som ein funksjon av rabatten på eple.

Her må du laga ei liste med ulike epleprisar som vert $x$-verdiane dine,
ei liste med vareutval for kvar eplepris, og ei liste med $y$-verdiar
som du får ved å køyra simuleringa og notera omsettinga.
:::

::: {hint} 
Det går an å automatisera alle stega i oppgåva over i eit program,
men om du ikkje sjølv ser korleis, bør du gjera det for hand fyrst,
sjølv om det er tungvint.
:::


## Steg 5: Ulike kundar

So langt er alle kundane like i simuleringa.
Det er sikkert meir realistisk om dei har ulike budsjett.

Det kan òg vera problematisk at dei går gjennom varene i same rekkjefylgje,
fordi det gjer at det alltid er den same varen som ikkje vert vurdert, når
kunden går tom for pengar.

Me kan løysa båe problema ved å laga tilfeldig kundar. 
Kvar kunde må då ha si eiga vareliste, som er stokka i tilfeldig orden.
Dessutan må dei ha kvart sitt tilfeldige budsjett.

+ For å stokka ei liste, kan me bruka `random.shuffle()`.
+ For å få eit tilfeldig budsjett, må du velja fordeling. 
  - Me kan bruka t.d. `random.gauss()` eller `random.uniform()`

Då kan me få noko slikt:

```{code-cell} ipython3
def lag_kunde(varer):
    budsjett = random.gauss(mu=middelverdi_budjsett, sigma=standardavvik)
    kundevarer = varer
    random.shuffle(kundevarer)
    return budsjett, kundevarer
```

::: {admonition} Oppgåve
Skriv om `simuler_dag()` med tilfeldige kundar.
Dvs. inni løkka må du generera ein tilfeldig kunde, i staden for
å bruka dei faste verdiane.
:::

::: {admonition} Oppgåve
Køyr simuleringa med ulike tilbodskampanjar og visualiser resultatet.
:::

::: {admonition} Oppgåve
Kva kan me læra av simuleringa?
Skriv eit lite refleksjonsnotat (oppsummering/avslutning av øvinga)
der du drøftar kva du har lært, kva som er nyttig og korleis ein
kunne ha godt vidare for å få ein betre og meir realistisk simulering.
:::


## Variant: Simulere markedsdynamikk

Oppgåva under er kopiert frå i fjor og ikkje redigert.

::: {admonition} Oppgåve

1. Set opp en markedsmodell for et gode:
 
* Tilbud: $Q_s = a - bP+\epsilon_s$
* Etterspørsel $Q_d = c + dP +\epsilon_d$
Her er:
* $Q_d =$ Kvantum etterspurt
* $Q_s =$ Kvantum "tilbudt"
* $P = $ Pris
* $a,b,c,d =$ Konstanter dere bestemmer
* $\epsilon_d, \epsilon_s = $ "Sjokk" i markedet for tilbud og etterspørsel

Velg fornuftige verdier for $a,b,c$ og $d$

2. Implementer tilfeldig sjokk i markedet
   * Velg $\epsilon_d$ og $\epsilon_s$ tilfeldig fra en normalfordeling med middelverdi 0 og et passende standardavvik
   * Her kan du bruke `random.gauss(..)` eller numpy sin `np.random.normal(...)`

3. Simuler markedet over tid
   * Simuler et visst antall perioder (feks 50)
   * For hver periode skal du:
     - Regne ut nye markedssjokk $\epsilon_d$ og $\epsilon_s$
     - Bestemme likevektsprisen $P^*$
     - Bestemme likevektskvantumet $Q^*$
4. På et gitt tidspunkt simulerer vi **en** intervensjon (?) i markedet (Feks halveis i simuleringen):
   * Skatt: Øk etterspørselfunksjonens $a$ for å simulere økt beskatning på produksjon
   * Subsidier: Minsk etterspørselfunksjonens $a$ for å simulere subsidier til produksjon
   * Innfør en makspris eller minimumspris
   * Fortsett simuleringen med oppdatert modell for markedsdynamikken

5. Plot resultat med matplotlib
   * Plot likevektspris og likevektskvantum over tid

:::

