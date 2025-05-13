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
# The Shrimp Game

Problemet er teke frå *AE201808 Næringsøkonomi*

+ *Topic* Competition and cooperation in oligopolies: 

## The game 

* Atari, BMI and Commodore own the only three shrimp boats on the island of New Ålesund.  

* Each shrimper incurs the same cost of $5.00 per pound of shrimp they catch (this includes the opportunity cost of time) and each can catch at most 75 pounds per day.  

* At the end of each day, they bring their catch to the only market on the island where price is determined by market demand and the supply of fish, and all shrimp is sold. All shrimp goes bad after one day, so a shrimper cannot keep shrimps off the market and sell them the next day.  

    The mayor of New Ålesund is also the supervisor of this market. He/she controls the pounds caught by each shrimper and announces the day’s price for shrimp. 

*    Let QA, QB, and QC denote Atari’s, BMI’s and Commodore’s catch, respectively. Once each has decided when to stop fishing and has brought his or her shrimp to market, the price is determined by the following equation:  

$$ P (Q_A, Q_B, Q_C)  =  45 – [ 0.2 \times (QA + QB + QC ) ] $$

* Each shrimper agrees that the above equation correctly predicts the market price of shrimp, and each tries to catch enough shrimp so as to maximize his or her dollar profits.  

* The profits $\pi$ for each shrimper equals the number of pounds caught multiplied by its profit margin, that is:   

$$ \pi_A (Q_A, Q_B, Q_C) = Q_A \left[ P (Q_A, Q_B, Q_C) – 5 \right]$$

* The three shrimpers have a history of family feuds and no personal contact. Each will have to set its shrimp production for the day without knowing what levels the other two shrimpers set. However, as described above, at the end of each day the production levels that were set by each shrimper will become public knowledge. 

## Objektorientert Modellering

Her er det enklast å tenkja på fleire parallelle program. Kvar fiskar har sitt program som avgjer kor mykje han vil fiska. Tilsvarande har marknaden, eller borgarmeistaren, sitt program som fastsett prisen basert på levert fangst. Når me deler opp problemet på denne måten, vert kvart program ganske enkelt. 

Fiskarane og borgarmeistaren er agentar, dvs. dei *gjer* ting i marknaden.  Ordet *agent* kjem frå latin og tyder ein som gjer noko eller som handlar. Agentbasert simulering er ein form for simulering der kvar agent i systemet vert modellert og implementert som ein autonom eining.  

Python er eit sokalla objektorientert språk. Me kan bruka eit objekt for å modellera ein agent.  I rekespelet treng me altso fire objekt, tre fiskarar og ein marknad.  Dei tre fiskarane har mange felles eigenskapar, og me seier at dei høyrer til same *klasse*.  Me kan t.d. definera ei klasse `Fisherman` slik:

```{code-cell} ipython3
import random
class Fisherman:
    def fangst(self):
		return  random.randint(0,75)
```

Denne klassa inneheld ein funksjon (definert med `def` som andre funksjonar).
Parameteren `self` er ein referanse til objektet sjølv.
Fiskaren fiskar eit tilfeldig volum som vert returnert.
Marknaden kan kalla denne funksjonen for å ha data til å rekna ut prisen.

Me kan *instantiera* og testa eit objekt av klassa slik:
```{code-cell} ipython3
ibm = Fisherman()
ibmfangst = ibm.fangst()
print( f"IBM leverer {ibmfangst} pund reker." )
```

Legg merke til syntaksen når me kaller funksjonen `fangst`. Me må bruka punktumnotasjonen fordi `fangst` er definert i objektet `ibm` (som har fått definisjonen frå klassa). Me har derimot ikkje noko argument som svarer til parameteren `self`.  Fordi `ibm`er eit objekt, tek python det automatisk med som parameteren `self`.

### Fiskarklassa

I tillegg til å avgjera fangsten, må fiskaren kunna rekna ut profitten sin.  Me må difor utvida definisjonen. Sidan profitten avheng av fangsten, må objektet hugsa fangstvolumet. Det kan t.d. gje denne definisjonen

```{code-cell} ipython3
import random
class Fisherman:
    def fangst(self):
        f = random.randint(0,75)
		self.sistefangst = f
		return f
    def profit(self,price):
        p = self.sistefangst*(price-5)
		self.sisteprofitt = p
		return p
```

Fangstvolument er tilfeldig som før, men vert no lagra i  ein variabel, `sistefangst` i objektet. Punktumnotasjonen i `self.sistefangst` seier at `sistefangst` er ein variabel *inni* (objektet) `self`. Til sist vert fangstvolument returnert. 

Profittfunksjonen tek prisen som parameter og bruker formelen frå modelldefinisjonen til å rekna ut profitten, som både vert lagra og returnert.

:::{admonition} Definisjon
Ein funksjon som er definert i ei klasse, vert normalt kalt ein *metode*.
:::

:::{admonition} Definisjon
Ein variabel som er definert i ei klasse, vert normalt kalt ein *attributt*.
:::

:::{admonition} Definisjon
Ei *klasse* er ein datatype som omfattar (evt. kan  omfatta) både data (`sistefangst`og `sisteprofitt`) *og* metodar (`fangst` og `profitt`) som verkar på typen. Ein variabel av ein klassetype kaller me for eit *objekt*, eller ein *instans* av klassa.
:::

Me kan sjølvsagt instantiera fleire objekt av same klasse.

```{code-cell} ipython3
atari = Fisherman()
atarifangst = atari.fangst()
print( f"Atari leverer {atarifangst} pund reker." )
commodore = Fisherman()
commodorefangst = commodore.fangst()
print( f"Commodore leverer {commodorefangst} pund reker." )
```

Me kan  òg sjekka at attributtane er forskjellige i dei to objekta.

```{code-cell} ipython3
print( f"Atari leverte {atari.sistefangst} pund reker." )
print( f"Commodore leverte {commodore.sistefangst} pund reker." )
```

Legg merke til at me har direkte tilgang til attributten i objektet, via punktumnotasjonen `atari.sistefangst`. Lat oss til slutt sjekka profittfunksjonen.

```{code-cell} ipython3
price = 15
print( f"Atari hadde profitt på ${atari.profitt(price)}." )
print( f"Commodore hadde profitt på ${commodore.profitt(price)}." )
```

:::{tip}
Normalt er det slik at metodane er definerte i klassa og aldri vert endra.  Alle instansar av klassa har same metodar. Attributtane høyrer derimot til objektet, og kvar instans har sine verdiar som kan endra seg ettersom programmet køyrer.

Dette er ikkje heilt sant.  Python tillet både klasseattributtar og redefinisjon av metodar
Python er eit svært fleksibelt språk, men me vil unngå å bruka denne fleksibiliteten, fordi koden elles lett vert vanskeleg å forstå. Mange andre språk, som Simula og Java, har strengare reglar som tvingar fram ein rigid struktur. 
:::

### Marknadsklassa

Lat oss no tenkja gjennom kva marknadsklassa treng.
+ Ho må kjenna alle fiskarane.
+ Ho må kunna rekna ut prisen.
+ Ho må styra tida, og be fiskarane om fangstresultat kvar dag.
Dette vil seia at me treng metodar for
1. Å registrera fiskarane
2. Rekna ut prisen
3. Køyra simuleringa, med ei løkke som held marknad kvar dag over tid.

Me kan koda dette på tusen ulike måtar, og kva måte som er best veit me eigentleg ikkje utan å prøva. Lat oss bruka høvet til å innføra eit nytt konsept.

:::{admonition} Definisjon
Ein *konstruktør* er ein metode som vert køyrd når objektet vert instantiert, for å initialisera verdiar i det nye objektet.
:::

I python heiter konstruktøren alltid `__init__`, og me kan definera og kalla han slik.

```{code-cell} ipython3
class Market:
   def __init__(self,fishermen,horizon=100):
       self.horizon = horizon
	   self.fishermen = fishermen

market = Market( [ atari, commodore ] )
print( market.horizon )
print( market.fishermen )
```

Når konstruktøren er definert, må alle dei obligatoriske argumenta vera med når objektet vert instantiert. Det andre argumentet `horizon` er tenkt som talet på dagar som vert simulert. Sidan det har ein initialverdi, er det valfritt å ta med. Fiskarane er lagra som ei liste med `Fisherman`-objekt. Denne kan vera vilkårleg lang, sjølv om oppgåva over føreset tre fiskarar.

:::{caution}
Python er fleksibelt og har ingen sjekk på om lista faktisk inneheld `Fishermen`-objekt. Det er lett å gjera feil, og feil kan vera vanskelege å finna. Det viktigaste for å unngå feil er å ha god orden, og testa kvar lille kodestubb for seg. Det går an å koda ulike testar for feilhandtering. Det er verd å koma tilbake til, men ekstra kode gjer det lett å mista oversikta, so inntil videra gjer me det enkelt. 
:::

No er det vanskelegast overstått.  Me kan gå vidare til sjølve simuleringa.

```{code-cell} ipython3
class Market:
   def __init__(self,fishermen):
	   self.fishermen = fishermen
   def price(self,totalquantity):
       return 45 - totalquantity/5
   def sim(self,horizon=100):
       for i in range(horizon):
           q = [ f.fangst() for f in self.fishermen ]
           qsum = sum(q)		   
		   price = self.price(qsum)
		   profit =  [ f.profit(price) for f in self.fishermen ]
		   print( f"Runde {i}: pris={price}; profit={profit}" )
   
```

Me tok bort `horizon` frå konstruktøren og la det i `sim`-funksjonen i staden.  Dette er ein smakssak.  Prisfunksjonen skulle vera likefram. Det er simulatorfunksjonen som er interessant.
+ Me bruker [[Listekomprehensjon]] for å rekna ut fangst og profitt for kvar fiskar i lista
+ Totalt kvantum er beint fram å rekna ut med `sum`-funksjonen.
+ Prisen reknar me ut med `price` frå objektet `self`.
+ Utskrifta er litt rudimentær, men det skal vera mogleg å sjå kor mykje fiskarane tener.

### Testing

Dokumentet over inneheld fleire delvise definisjonar av kvar klasse. Den *siste* definisjonen er derimot komplett.  For at simuleringa under skal verka, må me passa på at siste definisjon er køyrd sist.  Gå gjerne tilbake for å køyra cellene om att i rekkjefylgje.

Eg skriv simuleringa svært kompakt her. Fiskarane vert instantierte direkte i lista i argumentet til `Market`.

```{code-cell} ipython3
market = Market([ Fisherman() for i in range(3) ])
market.sim(7)
```

:::{admonition} Oppgåve
Korleis kan du køyra simuleringa med fire fiskarar?  Over 20 dagar?
:::

:::{admonition} Oppgåve
Legg til kode i `Fisherman` for å summera total profitt over tid, og skriv ut denne profitten. Tener alle fiskarane pengar over tid?
:::

:::{admonition} Refleksjon
Koden for å rekna total profitt over tid kan skrivast på ulike måtar. Korleis bør du skriva det for å få koden mest mogleg leseleg?
:::

:::{hint} 
Eit mantra i objektorientert programmering er *low coupling* og *high cohesion*. Det fyrste vil seia at me strebar etter minst mogleg avhengigheit mellom klassene. Når me endrar ei klasse, skal det krevja minimalt med endringar i andre klasser. Det siste tyder at kvar klasse skal konsis mål og meining. Det skal vera lett å forstå kva hensikt kvar klasse har, og ho bør ikkje gjera meir enn ho treng. Hensikta med dette mantraet er å gjera klassene mest mogleg gjenbrukbare.
:::


Simulering gjev oss ikkje noko direkte svar på kva som er rett rekepris eller kor mykje me lyt fiska. Nytteverdien i simulering er å testa ulike scenario.  Me kan variera både modellar og parameter. 
### Ulike fiskarstragiar: Arv og polymorfi


Metoden `fangst` implementerer *strategien* åt agenten. Denne strategien avgjer om fiskaren tener pengar eller ikkje, og meir vesentleg, strategien representerer alt fiskaren sjølv kan kontrollera.

:::{admonition} Definisjon
Ein *strategi* er ein handlingsplan som avgjer korleis agenten handlar i kvar mogleg situasjon. Dette omgrepet vert brukt, med små variasjonar, i kunstig intelligens (intelligente agentar), i simulering, spelteori og sosialøkonomi.
:::

Den `Fisherman`-agenten som me har implementert har ein triviell strategi, med tilfeldig val. Når me skal implementera fleire agentklasser med andre strategiar, løner det seg å bruka arv.  Me kan laga ein fiskar som alltid fiskar so mykje han kan slik.

```{code-cell} ipython3
class MaximalFisherman(Fisherman):
    def fangst(self):
        f = 75
		self.sistefangst = f
		return f
market = Market([ MaximalFisherman() for i in range(3) ])
market.sim(2)
```

Parentesuttrykket i `class`-lina seier at den nye klassa arver frå `Fisherman` og dermed har alle dei same metodane. Den eine metoden `fangst` vert omdefinert, medan `profit` vil vera identisk.

:::{admonition} Refleksjon
Er resultatet av simuleringa som venta?
:::

:::{admonition} Definisjon
Når klasse A *arver* klasse B, tyder det at A er eit særtilfelle av B og har alle dei same eigenskapane, sjølv om oppførselen kan variera.  Ein instans av A er òg ein instans av B. *Polymorfi* tyder at ein metode, t.d. `ob.fangst()` tek ulike formar (polymorfi $\sim$ fleire formar) avhengig av kva type (klasse) objektet har.
:::

I simulatoren kan marknadsobjektet bruka `fangst`-metoden utan å vita kva definisjon som gjeld. Det einast me veit er at ein kvan fiskartype har ein `fangst`-metode og kva hensikt metoden har. Berre fiskarobjektet kjenner sin eigen strategi.

:::{admonition} Oppgåve
Implementer ei adaptiv fiskarstrategi, dvs. ei klasse som arvar `Fisherman` med ein ny strategi, der han ser på profitten frå dagen før, og aukar fangsten om han tente pengar og reduserer han om han tapte. Korleis går simuleringa? Tener alle fiskarane pengar?

Du kan godt prøva deg fram med små og større endringar i fangstvolumet frå dag til dag. Er dette ein god strategi for fiskarane?
:::

:::{admonition} Oppgåve
Implementer ei underklasse av `Fisherman` som implementerer *Cournot-modelle*, dvs. fiskaren ser på kor mykje dei andre fiskarane fanga dagen før, og set sin fangst optimalt under føresetnad av at alle andre fiskar like mykje som dagen før.
:::

:::{admonition} Oppgåve
Køyr simulatoren med fleire fiskarar som implementerer ulike strategiar.  Kva strategi «vinn»?
:::

:::{admonition} Refleksjon
Kva simuleringar treng du for å finna ein fornuftig likevekt i marknaden?  Kva er fornuftig likevekt?
:::

:::{admonition} Oppgåve
*Shrimp Game* er eit særtilfelle av *Cobweb-modellen* (sjå t.d. [Dawid and Kopel 1998](https://link.springer.com/article/10.1007/s001910050066)). Korleis fungerer ulike strategiar dersom der er mange leverandørar i marknaden, kanskje 100 eller 1000? Du må heilt sikkert endra pris- og profittfunksjonen for at nokon skal tena pengar med so mange konkurranter, men det kan du gjera.
:::
