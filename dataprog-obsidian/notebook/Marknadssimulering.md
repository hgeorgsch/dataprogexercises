---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
  formats: md:myst,ipynb
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

Me skal simulera ein ganske dum kunde, som handlar på måfå, og
som plukkar tilfeldige varer til han anten er lei eller tom for
pengar.
Dette kan gje ein funksjon som ser slik ut.

```{code-cell} ipython3
def simuler_handling(budsjett=200,sluttsjanse=0.1):

    handlekurv = []
    total_pris = 0.0

    varenavn = list(varer.keys())

    fortsett = True
    while fortsett:
        vare = random.choice(varenavn)
        varepris = varer[vare]

        if budsjett > varepris:
            handlekurv.append( (vare,varepris) )
            total_pris += varepris
            budsjett -= varepris
        else:
            fortsett = False
    
        if random.random()<sluttsjanse:
            fortsett = False
    return total_pris, handlekurv
```

::: {admontion} Oppgåve 
Gå gjennom koden steg for steg.
1.  Funksjonen har parameter, kor mykje pengar har kunden å handla for
    og kor stor er sjansen for at han er lei etter ei vare.
2.  Kunden startar med ein tom handlekurv med ein totalpris på 0.
3.  Me lager ei liste med varer `dict`-objektet.
    Lista fungerer betre med `random`.
4.  Me må ha ei løkke for å plukka fleire varer, og fordi der er fleire
    sluttkriterium, er det enklast å ha ein bolsk variabel `fortsett`
    saman med ei *while*-løkke.  Me skal setja `fortsett` til `False` 
    når me finn ein grunn til å avslutta.
5.  Kjenner du igen dei to neste linene, `vare =` og `varepris =`.
    Kva gjer dei?  Om det ikkje er openbert, lag ei ny celle med
    desse to linene, saman med `varenavn = list(varer.keys())` for
    å testa kva som skjer.
6.  No treng me ein test.  Kva tyder `budsjett > varepris` i praktiske
    termar?  Kvifor må me sjekka dette?
7.  I `if`-blokken ser me at me legg vara til handlekurven, aukar
    totalprisen og reduserer budsjettet.  Gjev dette meining?
8.  I `else`-blokken set me `fortsett` til usann.  Kvifor skal dette
    avslutta løkka?
9.  Den siste `if`-satsen avsluttar løkka dersom
    `random.random() < sluttsjanse`.  Kva testar me på her?
:::

::: {admontion} Oppgåve 
Køyr funksjonen og skriv ut resultatet.  Kva er returverdien?
:::

::: {hint}
Eit vanleg problem er å simulera ei hending som opptrer med
$x$% sannsyn.
Standardløysinga er å dra eit tilfeldig tal $X$ i intervalet
0 til 1.  
Om $X$ er uniformt fordelt, er det $x$% sjanse for at $X<\frac{x}{100}$,
og dette vert kriteriet for at hendinga skjer.
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
kr, kurv = simuler_handling()
```

:::

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
varer = { "Epler": { "veilpris": 10.0, "salspris": 10.0 },
          "Pærer": { "veilpris": 15.0, "salspris": 15.0 },
          "Bleier": { "veilpris": 35.0, "salspris": 35.0 },
          "Sjokolade": { "veilpris": 6.0, "salspris": 6.0 },
          "Melk": { "veilpris": 20.0, "salspris": 20.0 },
          "Rundstykker": { "veilpris": 13.0 "salspris": 13.0 },
        }
```

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

    for namn, vare in varer.items():
        p = kjopssannsyn(vare)
        if random.random() < p and vare["salspris"] <= rest:
            rest -= data["salspris"]
            total_pris += data["salspris"]
            handlekurv.append( (name,vare) )

    return total_pris, handlekurv, rest
```

::: {admonition} Refleksjon

Korleis forstår du endringaene frå den fyrste kundemodellen?

:::

::: {admonition} Oppgåve

Prøvekøyr kundemodellen nokre gongar.
Ser handlekorgane fornuftige ut?

:::

Legg merke til at varelista (`dict`-objektet) er no ein parameter
til funksjonen, slik at me kan ha fleire varemodellar i spel, med
ulike tilbod og rabattar, og testa kunden på kvar varemodell.


##  Steg 4: Simulera butikken

**TODO**

* Gjør noen antagelser om hvor mange kunder som kommer innom butikken hver dag
* Når en kunde kommer inn i butikken har de et visst budjsett som vi trekker tilfeldig fra en passende fordeling
  - Her kan dere bruke feks `random.gauss()`,`numpy.random.normal()`, `random.uniform()`
* Kunden ser så gjennom produktene og kjøper de basert på tilfeldighet (produktets parametre) og om de har penger igjen i budsjettet

* Sammenlign salg og omsetning for en måned med og uten produkter på tilbud
* Du velger selv hvordan sjansen for salg skal øke med tilbudsrate -- men den logistiske modellen er en god kandidat
* Fremstill resultatet av simulering grafisk med `matplotlib`

```{code-cell} ipython3


varersalg = {key: val.copy() for key, val in varer.items()} # Deepcopy av varer


middelverdi_budjsett = sum([data["pris"] for _,data in list(varer.items())])/3
standardavvik = 0.2*middelverdi_budjsett


def lag_kunde(varedata):
    """ Funksjon som "lager" en kunde
    Vi trekker et budsjett fra en normalfordeling
    Vi må også "shuffle" varene slik at kundene ikke ser på de i samme rekkefølge
    hele tiden

    funksjonen returnerer varene som liste av [("Vare_A", {"pris": ...,...}), ("Vare_B": data), ...]
    og budsjettet til kunden
    """
    budsjett = random.gauss(mu=middelverdi_budjsett, sigma=standardavvik)
    kundevarer = list(varedata.items())
    random.shuffle(kundevarer)
    return budsjett, kundevarer
    
def simuler_dag(n, vareutvalg):
    kjop = []
    forbruk = []
    
    for _ in range(n):
        budsjett, kundevarer = lag_kunde(vareutvalg)
        varekjop, totpris, _ = handle(kundevarer, budsjett)
        kjop.append(varekjop)
        forbruk.append(totpris)
    return forbruk, kjop


def lag_salg(discount= 0.2):
    for vare, data in varersalg.items():
        data["rabatt"] = discount
        data["sannsynlighet"] = Ps(discount, P0=data["sannsynlighet"])
    

daglig_salg = []
daglig_salg_rabatt = []
lag_salg(discount=0.2)

salg_kunde = []
salg_kunde_rabatt = []

for i in range(30):
    salg, _ = simuler_dag(1000,varer)
    daglig_salg.append(sum(salg))
    salg_rabatt, _ = simuler_dag(1000, varersalg)
    daglig_salg_rabatt.append(sum(salg_rabatt))


plt.plot(list(range(30)), daglig_salg, label="Fullpris")
plt.plot(list(range(30)), daglig_salg_rabatt, label="Kampanje")
plt.legend()
plt.show()
plt.hist(daglig_salg, alpha=0.5, label="Fullpris")
plt.hist(daglig_salg_rabatt, alpha=0.5, label="Kampanje")
plt.legend()
plt.show()
print(f"Under kampanjen øker omsetningen med {sum(daglig_salg_rabatt)/sum(daglig_salg)-1:.0%}")

    
rabs = np.linspace(0,1,1000)
prob = Ps(rabs)
plt.plot(rabs, prob)
plt.show()
```

## Oppgave 5.2: Simulere markedsdynamikk

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

```{code-cell} ipython3

```
