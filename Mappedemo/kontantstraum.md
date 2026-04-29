---
jupytext:
  formats: ipynb,md:myst
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

# Simulering av kontantstrøm oppgave

Jeg legger opp egne eksempler på tall og område der det er behov for. 
Oppgaven som omhandler kontantstrøm er både interessant og relevant for meg fordi jeg studerer økonomi og administrasjon, der lån og renter er sentrale temaer i pensumet. Å forstå de grunnleggende mekanismer sånn som renters rente er viktig, både for videre studier og for å kunne bruke kunnskapen senere i arbeidslivet. 
I denne oppgaven så skal jeg bruke Python for å simulere ulike scenarioer, og se hva som skjer hvis terminbeløpet er for lavt, eller hvis renten endrer seg tilfeldig.

+++

## Del 1. Simulering av rente *uten* nedbetaling

Jeg starter med et lån på 15.000 kr og en årlig rente på 8%. 
Jeg har laget to variabler som heter **"rente"** og **"saldo"** for å kunne holde litt styr på verdiene. 

Jeg ønsker å se hvordan saldoen utvikler seg gjennom 10 år med startsåret 2025 til 2035. 
Jeg har skrevet inn en antagelse at koden skal starte fra og med 1. januar 2025. 

For å kunne simulere dette så bruker jeg en **"for-løkke"** som skal hjelpe oss å kunne gjenta koden flere ganger år for år. Jeg har dermed også satt inn en **"range"** funksjon. Range kommer til å avgrense tallene som vi skal se på i dette tilfellet så er det årene 2025-2036. Det vil si at koden kommer til å kjøre gjentatte ganger fra og med 2025 og stoppe etter 31.desember 2034. Det er viktig å få med seg at **"range"** funksjonen kommer ikke til å printe ut og inkludere 2035. Likevel så er dette i tråd med det faglige i studiet mitt. Verdien 31.desember 2034 skal være lik verdien 1.januar 2035.

```{code-cell} ipython3
import matplotlib.pyplot as plt

rente=0.08 #rentesats i desimal tall
saldo=15000 #startlån beløpet  

#Nå vil jeg se rentesatsen på lånet gjennom foreks 10 år. For dette så må jeg bruke en for-løkke. 
#Vi antar at startåret er 1. Januar 2025

for year in range(2025, 2035):    
    print(f"Lånsaldoen den 1. januar {year:} er: {saldo:.2f}")   
    #f"" tilater oss å printe ut setninger og legge inn koder og variabler i strengen
    saldo=saldo + saldo*rente
    print(f"Lånsaldoen den 31.desember {year:} er: {saldo:.2f}")
```


*Bytte ut **range** for **list***

Om jeg bytter ut **range(2025,2035)** med en liste som **[2025,2026,2027]** så ser jeg at koden fungerer på samme måte. Men forskjellen er at en **range** funskjon lager listen automatisk uten at jeg må skrive inn hvert tall. En **liste** funksjon gir meg muligheten til å velge fritt de årene jeg vil ha med. 

**Range** funskjonen er praktisk om jeg vil ha en jevn sekvens mens en **list** funskjon er nyttig om jeg ønsker noen utvalgte år.

```{code-cell} ipython3
rente=0.08 #rentesats i desimal tall
saldo=15000 #startlån beløpet  

#Nå vil jeg se rentesatsen på lånet gjennom foreks 10 år. For dette så må jeg bruke en for-løkke. 
#Vi antar at startåret er 1. Januar 2025

for year in [2025,2026,2027]:    
    print(f"Lånsaldoen den 1. januar {year:} er: {saldo:.2f}")   
    #f"" tilater oss å printe ut setninger og legge inn koder og variabler i strengen
    saldo=saldo + saldo*rente
    print(f"Lånsaldoen den 31.desember {year:} er: {saldo:.2f}")
```

*Liten refleksjon*

Etter å ha kjørt den orginale koden så ser vi at saldoen vokser hvert år, og dette er fordi renten legges til og det oppstår en renters rente. Jeg ønsket at koden skulle **"print"** datoen 1.januar med tilsvarende år og saldo. 

Jeg har brukt formatet **".2f"** for å begrense utskriften til 2 desimaler slik at tallene blir lettere å lese. 
For å kunne bruke variabler inne i en print streng så brukte jeg **f""**, som lar oss skrive inn variabler direkte i teksten.

+++

## Del 2. Simulering av rente *med* nedbetaling

I den første modellen så så vi at at saldoen vokste hvert år fordi rentene ble bare lagt til, uten noen nedbetaling. Dette i virkeligheten er urealistisk, med tanke på at lån skal vanligvis betales ned over tid. Dermed så utvikler vi oppgaven.

Her har vi samme grunn tall med rente på 8% og saldo, altså lånbeløpet på 15.000kr. Men denne gangen så har vi satt inn at vi kommer til å legge inn nedbetaling.
Et terminbeløp er det beløpet man avtaler, som oftes på forhand, å betale til långiver hvert år eller hver termin, kan være månedlig, kvartalvis men vi skal se på årlig terminbeløp. I denne oppgaven setter jeg det til 500kr per år. 

For å kunne simulere dette i Python så må jeg legge til renter, der vi bruker formelen **"saldo * rente"**, trekke fra et terminbetaling, **"saldo med rente - terminbetaling"**, og skrive ut saldoen både ved starten og slutten av året, igjen 1. januar og 31. desember. Siden dette gjelder fortsatt 10 år , 2025 til 2035, så benytter vi **"for-løkken"** igjen.

```{code-cell} ipython3
rente = 0.08 #rentesats i desimal
terminbeløp = 500  #ny variabel terminbeta
saldo = 15000

for year in range(2025, 2035):
    print(f"Lånesaldo 1. januar {year} er: {saldo:.2f}")
    saldo = saldo + saldo*rente   # vi legger til renta
    saldo = saldo - terminbeløp  # siden det er nedbetaling så trekker vi terminbeløp fra saldo med rente
    print(f"Lånesaldo 31. desember {year} er: {saldo:.2f}")
```

---------
*Rekkefølgen på renter og terminbeløp byttes*

Dersom vi trekker fra terminbeløpet **før** vi legger til renten vil saldoen ha blitt lavere enn i modellen vi har brukt til nå. 
Eksempel: 
- Lånesaldo 1.januar 2026 med *rente lagt til først* = 15.700kr
  Da legges renten på toppen av 15.700kr
- Lånesaldo 1.januar 2026 med *terminbeløp trukket fra først* = 15.660kr
  Da legges rente på et lavere grunnbeløp

Dette betyr at om vi bytter rekkefølgen så ender vi opp  med å skylde litt mindre penger hvert år. 

Denne scenarioen er urealistisk fordi man beregner renter av hele beløpet du skylder **før** de trekker avdraget.

```{code-cell} ipython3
rente = 0.08 #rentesats i desimal
terminbeløp = 500  #ny variabel terminbeta
saldo = 15000

for year in range(2025, 2035):
    print(f"Lånesaldo 1. januar {year} er: {saldo:.2f}")
    saldo = saldo - terminbeløp  # Her prøver vi å trekke fra terminbeløpet før vi legger til renten 
    saldo = saldo + saldo*rente   # vi legger til renta ETTER å ha trukket fra terminbeløpet
    
    print(f"Lånesaldo 31. desember {year} er: {saldo:.2f}")
```

*Liten refleksjon*

Etter koden har blitt kjørt ser jeg at saldoen har fortsatt å vokse selv om jeg betalte 500kr hvert år som nedbetaling. Denne årsaken er fordi renten er på 8% av saldoen og dette utgjør mer enn terminbeløpet, dermed så vil ikke nedbetalingen klare å med andre ord ta gjen renteveksten. 

Jeg kan se hvordan renters rente påvirker lån. Lånet blir dyrere og vokser fordi rentene også får renter. Hadde jeg økt terminbeløpet så ville til slutt saldoen begynt å synke i stedet for å vokse. 

Med denne simuleringen ser jeg at det er tydeligvis et alt for lavt terminebløp og konsekvensen er at gjelden blir større, selv med regelmessig nedbetaling. 

Igjen så brukes **".2f"** for å begrense antall desimaler i utskriften. Videre i oppgaven så skal jeg fortsette å bruke 2 desimaler.

+++

----------
*Bruk av **While løkke** i oppgaven*

I de tidligere simuleringene brukte jeg en **for løkke** som kjørte gjennom et fast antall år, 10 år. Dette fungerer fint, men i virkeligheten er det mer naturlig å simulere helt til lånet blir faktisk nedbetalt. 

For å kunne vise dette frem så kan jeg bruke en **while løkke** som fortsetter å kjøre koden så lenge en betingelse er sann. 
Jeg skriver derfor at betingelsen som koden skal følge er : "saldo > 0"
Det vil si at så lenge saldoen er større enn 0, så vil løkken fortsette å kjøre. 

Jeg setter startlånet til 15.000kr, renten til 8% og terminbeløpet til 2.000kr. 
Programmet skal skrive ut saldoen hvert år frem til lånet er ferdig nedbetalt.

```{code-cell} ipython3
rente = 0.08
saldo = 15000
terminbetaling = 2000
year = 2025  # Vi setter inn årstallet utenfor løkken. Dette er fordi "while" ikke holder styr på det selv

while saldo > 0:
    print(f"Lånesaldoen 1. januar {year}: {saldo:.2f} kr")
    saldo = saldo + saldo*rente
    saldo = saldo - terminbetaling
    print(f"Lånesaldoen 31. desember {year}: {saldo:.2f} kr")
    year = year + 1   # Siden "while" ikke holder styr på årstallene selv så må vi øke året med 1 for hver gjennomløp 
```

*Liten refleksjon*

Når jeg kjører denne koden så ser vi at løkken stopper automatisk når saldoen blir mindre eller lik 0, slik som betingelsen min ble satt til. 
Bruk av **while** funksjonen er mer fleksibelt enn **for løkken** og dette er fordi da trenger jeg ikke å vite på forhånd hvor mange år nedbetalingen vil ta. 

En forksjell er at jeg måtte definere variabelen "year" før løkken startet, og selv sette inn at "year" skal øke med 1. Så selv om **while** funksjonen gir mer kontroll og fleksibilitet, så kreves det litt mer koding enn for en **for løkke**

+++

### *Simulering med gebyr*

I praksis kan et lån ha både renter og gebyrer. Dette betyr at saldoen vil øke med både renten som blir lagt til og det fast gebyret hvert år, før nedbetalingen trekkes fra. 

For å simulere dette så bruker vi samme tall fra forrige koding. 
Jeg legger til et gebyr på 100kr per år.

```{code-cell} ipython3
rente = 0.08
saldo = 15000
terminbetaling = 2000
gebyr=100
year = 2025  

while saldo > 0:
    print(f"Lånesaldoen 1. januar {year}: {saldo:.2f} kr")
    saldo = saldo + saldo*rente
    saldo = saldo + gebyr  #her legges til gebyr på saldo beløpet med renter
    saldo = saldo - terminbetaling
    print(f"Lånesaldoen 31. desember {year}: {saldo:.2f} kr")
    year = year + 1   
```

*Liten refleksjon*

Når jeg legger til et gebyr på 100 kr hvert år, ser jeg at saldoen reduseres saktere enn i modellen uten gebyr.  
Det tar derfor lenger tid å betale ned hele lånet. Dette ser vi med at uten gebyr så vil jeg ha nedbetalt hele lånet i 2036 mens når gebyret på 100kr er lagt til så er lånet ikke nedbetalt før i 2037

Selv om 100 kr virker lite sammenlignet med terminbeløpet på 2000 kr, får det en tydelig effekt over tid.  
Dette viser hvordan små faste kostnader kan forlenge nedbetalingstiden og gjøre lånet dyrere totalt sett.

+++

---------
**Tredje del av oppgaven** *Plotting av utregning*

Opptil nå har jeg bare skrevet ut saldoen med koden **print**. Dette gir en oversikt men det kan være vanskelig å se helheten over flere år. En bedre og kanskje litt mer ryddig måte å holde styr over alle tallene er å langre saldoen for hvert år i en liste, og deretter bruke **matplotlib** til å lage en graf. Helt på toppen av første kode celle så ser du at jeg har satt inn "import matplotlib.pyplot as plt". Der har jeg importert et bibliotek for å lage grafer, og **as plt** betyr at vi kan skrive **plt** i stedet for hele navnet. Dette er gjort med tanke på oppgavene fremover. 

For å kunne lage en graf så lager jeg 2 lister: 
1. **x**: årstallene
   som skal representere tids-asken
2. **y**: saldoen
       som skal representere beløpet

I starten så setter jeg inn saldo på 15.000kr og startsåret til 2025. Jeg skal simulere 10 år med data. 

Deretter så må jeg bruke en **for løkke** for å legge til renter hvert år og lagre saldoen i listen. 

Til slutt så plotter jeg resultatene i en linjegraf

```{code-cell} ipython3
rente=0.08  #rente på 8%
saldo=15000

x=[2024]    # liste for årstall som settes på x-aksen
y=[saldo]   # liste for saldo som settes på y-aksen 

for year in range(2025, 2035):
    saldo = saldo + saldo*rente
    y.append(saldo)   # Vi legger til den nye saldoen etter at renter er lagt til
    x.append(year)    # Vi legger til det nye årstallet som kommer bakkerst

plt.plot(x, y)
plt.title("Lån uten nedbetaling")
plt.xlabel("År")
plt.ylabel("Saldo (kr)")
plt.show()
```

*Liten refleksjon*

Her så ser vi at jeg har laget to lister for årstallene og for saldoen. Ved bruk av **append** legger jeg til ett nytt element bakert i listen for hvert år som går. Dette gjør at jeg til slutt sitter igjen med 2 lister og de har da like mange elemeter, der hvert år har en tilhørende saldo. 

Når jeg skal tenge inn grafen og plotte inn dataen bruker jeg funskjoner fra **matplotlib**. 

- **plt.plot(x, y)** lager selve linjegrafen, med år på x-aksen og saldo på y-aksen.  
- **plt.title("Lån uten nedbetaling")** setter en tittel øverst i figuren.  
- **plt.xlabel("År")** setter en tekst under den horisontale aksen (årstallene).  
- **plt.ylabel("Saldo (kr)")** setter en tekst langs den vertikale aksen (lånebeløpet).  
- **plt.show()** viser selve figuren på skjermen.  

Grafen gjør det mye lettere å forstå helheten enn om jeg bare hadde printet ut saldoen år for år som vi gjorde i oppgavene ovenfor.   
Vi ser at kurven vokser stadig brattere og dette viser effekten av renters rente, der rentene også begynner å vokse på de tidligere rentene.

+++

----------
*Plotting av utregning **med** nedbetalinger*

Så i forrige del lagret jeg saldoen for hvert år i en liste og lagde grafen uten noe nedbetaling. Nå bygger vi videre på modellen slik at den også inkluderer en fast terminbetaling hvert år. 

Samme parameter gjelder: 
- Start saldo: 15.000kr
- Rente: 8%
- Terminbeløp: 500kr

Jeg forventer ikke at lånet blir nedbetalt, og faktisk kommer til å vokse enda raskere, siden rentene som legges til hvert år er langt større enn terminbeløpet jeg betaler. 

Igjen så bruker jeg 2 lister, **x** for årstall og **y** for saldo. 
Hvert år så regner koden ut saldoen ved å legge til renter og trekke fra terminbeløpet, og deretter lagrer jeg resultatet med **append**.

Som i forrige oppgave så lager jeg en plott som viser hvordan saldoen endrer seg over tid.

```{code-cell} ipython3
rente=0.08  #rente på 8%
saldo=15000
terminbetaling=500

x=[2024]  # liste med startåret
y=[saldo] # liste med startsaldoen

for year in range(2025, 2035):
    saldo = saldo + saldo*rente   # legg til renter på saldoen 
    saldo = saldo - terminbetaling  # trekk fra terminbetalingen
    y.append(saldo)   # lagre saldoen
    x.append(year)    # lagre årstallet

plt.plot(x, y)
plt.title("Lån med årlig nedbetaling")
plt.xlabel("År")
plt.ylabel("Saldo (kr)")
plt.show()
```

*Liten refleksjon*

Her bruker jeg nesten samme metode som i forrige del, men nå trekker jeg fra et terminbeløp etter at rentene er lagt til.  
Dette gir en litt annen utvikling enn når saldoen vokser med renter.  
  
Jeg legger også inn formelen: "saldo = saldo - terminbetaling" som skal trekke fra det faste terminbeløpet.  

Når jeg skal tegne grafen så setter jeg inn det samme som i forrige oppgave. 
- **plt.plot(x, y)** lager en linjegraf der år (x) plottes mot saldo (y).  
- **plt.title("Lån med årlig nedbetaling")** gir grafen en forklarende overskrift.  
- **plt.xlabel("År")** og **plt.ylabel("Saldo (kr)")** setter navn på aksene.  
- **plt.show()** viser selve figuren.  

Med en rente på 8% og bare 500kr i nedbetaling per år, ser vi at saldoen vokser veldig fort. Grafen viser en bratt stigende kurve som forteller at lånet kommer **ikke** til å bli nedbetalt innen for tidsrammen som jeg har satt, 10 år. 

Grafen illustrerer det jeg fant i "**Andre del av oppgaven**: *Simulering av rente med nedbetaling*". 
Når rentekostnaden alene er større enn terminbeløpet, vokser lånet selv om jeg betaler hvert år. 
Vi ser hvordan y-aksen på grafen slutter på beløpet litt over 24.000kr mens y-aksen på grafen til *Lån uten nedbetaling* slutter på 32.500kr 

Vi ser også at sluttverdien på grafen sin y-akse ender litt over 24.00kr mens i grafen for *Lån uten nedbetaling* endte saldoen på ca. 32.500kr. Dette viser oss at nedbetaling på 500kr hjelper litt, men ikke nok til å stoppe veksten.

+++

---------
**Fjerde del av oppgaven** *Gjenbruk av simuleringer med funksjoner*

Så langt har jeg sett på utviklingen av lånet med ett bestemt terminbeløp. I stedet kan jeg løse oppgaven ved bruk av **funksjoner**. En funksjon lages med **def** som definer selve funksjonen jeg skal bruke. 
Funskjonen fungerer som en slags oppskrift. Jeg gir funksjonen noen tall og den gjør utregningene for oss. 
Til slutt bruker jeg **return** funksjonen for å sende resultatene tilbake slik at jeg kan bruke dem videre sånn som når jeg skal lage en graf.

```{code-cell} ipython3
def loan(saldo=15000, rente=0.08, terminbeløp=0, year=2025, gebyr=0, maks_år=20):
    x = [year]      # liste med år
    y = [saldo]     # liste med saldoer
    
    while saldo > 0 and len(x) <= maks_år:
        saldo = saldo + saldo*rente   # legge til rente
        saldo = saldo + gebyr         # legge til gebyr
        saldo = saldo - terminbeløp  # trekker fra terminbeløp
        year = year + 1               # gå videre til neste år
        x.append(year)                # legg år til i listen
        y.append(saldo)               # legg saldo til i listen
    return x, y                       # returnerer to lister: x = år, y = saldo

```

Jeg kaller funkjsonen **loan**. Deretter så setter vi inn verdiene i parantesen. Disse verdiene kalles **parametere**. Vi kan endre på disse tallene hver gang vi kjører en funksjon. 
Som jeg har nevnt tidligere i oppgaven så har vi 2 lister, **x** som lagrer årstall og **y** som lagrer saldo. 

I denne koden så bruker jeg **while** funksjonen som gjør at programmet kjører helt til lånet er betalt tilbake, eller når vi har nådd maks antall år. 

**return** sender listene tilbake slik at jeg kan bruke dem videre når jeg skal illustrere en graf.

```{code-cell} ipython3
startsaldo = 15000
rente = 0.08
startår = 2025
 

# Første simulering: terminbeløp 500 kr
x, y = loan(saldo=startsaldo, rente=rente, terminbeløp=500, year=startår)



plt.plot(x, y, "r--", label="Terminbeløp 500 kr")
plt.title("Lån 15 000 kr, rente 8 % (fra 2025)")
plt.xlabel("År")
plt.ylabel("Saldo (kr)")
plt.legend()
plt.show()
```

*Liten refleksjon*

I denne simuleringen starter lånet på 15 000 kr med 8 % årlig rente, og vi betaler 500 kr per år.  
Som grafen viser så går saldoen aldri ned, men vokser kraftig fra år til år.  
Årsaken er at terminbeløpet på 500kr er mye lavere enn rentekostnaden på 8%. Dermed dekker jeg ikke rentene, og gjelden øker hele tiden.  

I grafen ser vi at jeg har satt inn en liten forklaringsboks av hva linjen betyr. Dette ble gjort ved **plt.legend()**. 

Vi ser at grafen stiger raskt og igjen dette illustrerer effekten av renters rente. Fordi terminbeløpet er så lavt i praksis betyr dette at man alltid må betale mer enn rentene, ellers vil lånet vokse uendelig.

+++

-------
*Sammenligner grafen med forksjellige renter*

```{code-cell} ipython3
x8,y8 = loan(15000,rente=0.08,terminbeløp=500)
x5,y5 = loan(15000,rente=0.05,terminbeløp=500)
x2,y2 = loan(15000,rente=0.02,terminbeløp=500)
plt.plot( x8, y8, 'r--', x5, y5, 'b:', x2, y2, 'g' )
plt.title("Lån med 3 forksjellige renter")
plt.legend( [ "8%", "5%", "2%" ] )
plt.show()
```

*Liten refleksjon*

Her sammenligner jeg tre simuleringer med samme startbeløp på 15.000kr og samme terminbeløp på 500kr per år, men med ulike renter: 8%, 5% og 2%.  

Grafen viser tydelig hvordan rentenivået påvirker utviklingen:  
- Med **8 % rente** vokser gjelden raskt, siden terminbeløpet er altfor lavt til å dekke rentene.  
- Med **5 % rente** flater kurven mer ut, men saldoen fortsetter likevel å stige.  
- Med **2 % rente** blir gjelden faktisk nedbetalt over tid, fordi terminbeløpet er større enn rentekostnadene.  

For å skille de tre scenarioene har jeg gitt kurvene ulike farger: **r** for rød, **b** for blå og **g** for grønn.  
I tillegg har jeg valgt forskjellige linjestiler: **--** for stiplet, **:** for prikket og uten symbol for et heltrukket linje.  

Jeg lager en forklaringsboks som viser hvilken kurve som hører til hvilken rente.

Denne simuleringen gjør det veldig tydelig hvor avgjørende rentenivået er for om et lån blir nedbetalt eller fortsetter å vokse.

+++

## Del 5. Tilfeldig renteendringer i fremtiden

Til nå har jeg brukt en fast årlig rente på enten 8% eller 5% og 2%. For å gjøre modellen mer realistisk, skal jeg simulere en tilfeldig endret rente.

Før dette så avklarer jeg noen antakelser først: 
- Hvert år er det **10 % sjanse** for at renten går **opp** med 0,5 prosent
- Hvert år er det **10 % sjanse** for at renten går **ned** med 0,5 prosent
- Ellers forblir renten uendret det året.

For å kunne simulere tilfeldige tall så "import" jeg en **random bibliotek**. 
Jeg begynner med å teste slumptall med ved bruk av **random.randint(1, 10)** som gir et heltall fra 1 til 10, og deretter bygger jeg en lån funksjon som bruker disse tilfeldige endringene.

```{code-cell} ipython3
import random
import matplotlib.pyplot as plt

# Dette blir en liten test av random.randint.
# Trekk 20 tilfeldige tall 1..10 for å se variasjon
[ random.randint(1,10) for _ in range(20) ]
```

*Liten refleksjon*
Koden **random.randint(1,10)** gir et heltall fra 1 til 10, og random vil si at jeg får tilfeldige tall hver gang.  

Dette bruker jeg til å "kode" hendelser:
- **1**: rente opp
- **10**: rente ned
- **2-9**: renten er uendret
Slik kan jeg simulere at renteendringer skjer med bestemte sannsynligheter.


------
*En lån funskjon med tilfeldige renteendringer*


Nedenfor så lager jeg **loan_random**, som er som den vanlige lånefunksjonen, men med en ekstra del:
- Jeg trekker et tilfeldig tall mellom 1...10 hvert år.
- Hvis tallet er 1 så øker jeg renten med 0,5 prosentpoeng.
- Hvis tallet er 10 så senker jeg renten med 0,5 prosentpoeng.
- Så beregnes årets renter, og eventuelle gebyr legges til, terminbeløp trekkes fra, og året inkrementeres.

Jeg lagrer år i listen **x** og saldo i **y**, for å kunne plotte senere.

Jeg bruker samme tall som før: 
- startsaldo: **15.000kr**
- startår: **2025**
- start-rente: **8%**
- terminbeløp: **jeg kan variere dette**

```{code-cell} ipython3
import random
import matplotlib.pyplot as plt

def loan_random(saldo=15000, rente=0.08, terminbelop=2000, year=2025, gebyr=0, maks_år=100):
    """
     10 % sjanse: rente opp +0.005
     10 % sjanse: rente ned -0.005
     Ellers uendret det året.
    """
    x = [year - 1]
    y = [saldo]
    r = rente

    while saldo > 0 and len(x) <= maks_år:
        slump = random.randint(1,10)
        if slump == 1:
            r += 0.005
        elif slump == 10:
            r -= 0.005

        saldo = saldo + saldo*r
        saldo = saldo + gebyr
        saldo = saldo - terminbelop

        x.append(year)
        y.append(saldo)
        year += 1

    return x, y
```

Først definerer jeg funksjonen med **def**. Inne i parentesen ligger parametere som kan endres når jeg kaller funksjonen:  
- **saldo** (lånebeløp)  
- **rente** (start-rente)  
- **terminbeløp** (hvor mye vi betaler ned hvert år)  
- **year** (startår)  
- **gebyr** (fast gebyr per år)  

Jeg benytter en **docstring** som betegnes med """...""". Dette er en tekstforklaring som står inne i en funskjon. 
Fordi teksten er satt i en **docstring** så bryr Python ikke seg om denne når jeg skal kjøre programmet.     

Videre oppretter jeg to lister som vanlig, **x** som lagrer årstall, og **y** som lagrer saldo for hvert år  

Jeg satt også **r = rente**, som er en type lokal kopi av renten. Dette vil føre til at jeg kan justere renten underveis. 

Selve simuleringen skjer i en **while-løkke**, som kjører så lenge saldoen er over 0 og antall år ikke overstiger 100.  
Hvert år trekker jeg et tilfeldig tall med **random.randint(1,10)**. Hvis tallet er **1**, øker renta med 0.5 prosentpoeng, og hvis tallet er **10**, synker renta med 0.5 prosentpoeng. Alle andre tall enn 1 og 10 vil resultere at renten er uendret. 

Deretter regnes ny saldo ut ved å først legge til renter ved formellen: **saldo + saldo*r**, så legger jeg til eventuelle gebyrer, og tilslutt så trekker jeg fra terminbeløpet. 

Året økes med **year += 1**, og både år og saldo legges inn i listene med **append**.  

Til slutt returnerer funksjonen **x, y**, som er listene med utviklingen av lån over tid slik at jeg kan **plotte** utviklingen.

Denne koden har da vist hvordan man kan bruke funskjoner og betingelser med tilfeldige tall til å simulere et økonomisk situasjon.  


Jeg kjører funksjonen flere ganger med de samme parameterne for å se hvordan tilfeldige renteendringer gir ulike forløp.  
Jeg viser to tilfeller: **terminbeløp 2000 kr**, som ofte klarer å fullføre nedbetalingen og **terminbeløp 500 kr**, som ofte ikke klarer det.

```{code-cell} ipython3
plt.figure()
for _ in range(12):
    x, y = loan_random(saldo=15000, rente=0.08, terminbelop=2000, year=2025, gebyr=0, maks_år=100)
    plt.plot(x, y)

plt.title("Tilfeldige renteendringer med terminbeløp på 2.000kr")
plt.xlabel("År")
plt.ylabel("Saldo (kr)")

plt.show()


plt.figure()
for _ in range(12):
    x, y = loan_random(saldo=15000, rente=0.08, terminbelop=500, year=2025, gebyr=0, maks_år=100)
    plt.plot(x, y)

plt.title("Tilfeldige renteendringer med terminbeløp på 500kr")
plt.xlabel("År")
plt.ylabel("Saldo (kr)")

plt.show()
```

*Liten refleksjon*
Her så har jeg kjørt de forskjellige simuleringene med 12 runder i hver, den første grafen viser en terminbeløp på 2.000kr og den andre grafen som viser en terminbeløp på 500kr. 

**Terminbeløp 2.000kr** så ser man at de fleste simuleringene viser at lånet blir nedbetalt innenfor en rimelig tidsperiode, selv om varigheten vil variere og dette er på grunn av de tilfeldige renteendringene. 

**Terminbeløp 500kr** så ser man at saldoen i alle simuleringene fortsetter å stige. Dette skjer fordi terminbeløpet er for lavt i forhold til rentene, særlig når renten stiger.  

Denne modellen er veldig enkel. Jeg tok for meg 3 antagelser: 10% sjanse for at renten går opp med 0,5% og 10% sjanse for at den går ned med 0,5%, og ellers er renten uendret. Man kan si at modellen er nyttig for å illustrere hvordan tilfeldigheter kan påvirke et lån, men ellers ville jeg ikke sagt at dette er en god modell for virkelige renteendringer. I praksis så er renteutvikling utrolig mer kompleks og påvirkes av faktorer som inflasjon, økonomisk vekst innad et land og internasjonale forhold. Med det så kan jeg bekrefte at modellen har mye rom for forbedringer.

+++

## Siste del. Sammenligning av serie- og annuitetslån

Opptill nå så har jeg kjørt simuleringer som tar for seg **annuitetslån**. Det som kjennetegner et annuitetslån er at de har *fast terminbeløp* hvert år. Det er veldig typisk at renteandelen er høy på starten og synker etter hvert, i og med at avdragsandelen øker. Nå skal jeg også inkludere simuleringer med et **serielån**. Serielån kjennetegnes ved at det er et *fast **avdrag***, mens rentene beregnes på det gjenstående saldoen. Det vil lede til at totalbetalingen blir høy på starten og synker over tid. 

Her simulerer jeg begge typer år for år for å sammenligne **saldo-utviklingen*

```{code-cell} ipython3
import matplotlib.pyplot as plt

def annuitet_saldo(saldo=15000, rente=0.08, start=2025, slutt=2035, terminbeløp=1000):
    """Annuitetslån: fast terminbeløp 'terminbeløp' hvert år, renter beregnes på saldo."""
    x = [start - 1]
    y = [saldo]
    
    for year in range(start, slutt + 1):
        saldo = saldo + saldo*rente         # legg til rente
        saldo = saldo - terminbeløp     # trekk fra fast terminbeløp
        x.append(year); y.append(saldo)
    return x, y

def serie_saldo(saldo=15000, rente=0.08, start=2025, slutt=2035):
    """Serielån: fast avdrag = saldo / antall år, rente beregnes på gjenstående saldo."""
    n = (slutt - start+ 1)
    fast_avdrag = saldo / n
    x = [start - 1]
    y = [saldo]
    
    for year in range(start, slutt + 1):
        rente_bet = saldo * rente
        betaling = rente_bet + fast_avdrag   # total betaling det året
        saldo = saldo + rente_bet - betaling # = saldo - fast_avdrag
        x.append(year); y.append(saldo)
    return x, y

xA, yA = annuitet_saldo(saldo=15000, rente=0.08, start=2025, slutt=2035, terminbeløp=2000)
xS, yS = serie_saldo(saldo=15000, rente=0.08, start=2025, slutt=2035)

plt.plot(xA, yA, "r-", label="Annuitetslån (fast terminbeløp)")
plt.plot(xS, yS, "b--", label="Serielån (fast avdrag)")
plt.title("Saldo-utvikling: Annuitet vs. Serie (årlig)")
plt.xlabel("År"); plt.ylabel("Saldo (kr)"); plt.legend(); plt.show()
```

*Liten refleksjon*
Grafen viser at **serielånet* reduserer saldoen *linjært*, altså ved faste avdrag hvert år, mens **annuiteten** gir ogte en mer *gradvis* reduksjon, spesulet om terminbeløpet er lavt i forhold til rentene som er skylt. 

Siden **serielån** har samme rente så vil det gi et *lavere* totale rentekostnader og dette er fordi saldoen vil falle raksere på starten. 

Med **annuitet** så er det en jevnere likviditet, altså samme beløp hvert år, som ofte er grunnent til at privatkunder velger denne type lån. 

------
*Månedlig rente og betalinger*

Årlige terminer er uvanlig i praksis. Her simulerer jeg en **månedlig kapitalisering** og en **månedlig betaling**.
Jeg brukte **nominal årlig rente** delt på 12 måned: rente_m=rente_å/12. 
For annuitet så beregner jeg et fast **månedsbeløp** med vanlig formel
For serielån så beregner jeg fast **månedsavdrag** med = saldo / antall måned

Etter det så vil jeg plotte saldo hver måned over hele perioden.

```{code-cell} ipython3
import math
import matplotlib.pyplot as plt

def annuitet_manedlig(saldo=15000, rente_å=0.08, start=2025, slutt=2035):
    """Annuitet måned: fast termin per måned som jeg beregner med formel."""
    rente_m = rente_å / 12
    antall_mnd = (slutt - start + 1) * 12
    # Annuitetsformellen for terminbeløp:
    if rente_m == 0:
        terminbeløp = saldo / antall_mnd
    else:
        terminbeløp = saldo * (rente_m) / (1 - (1 + rente_m) ** (-antall_mnd))

    
    # x som YYYY.MM for enkelhet (kan også bruke heltall 0..n_mnd)
    x = [f"{start-1}.12"]
    y = [saldo]

    year = start; month = 1
    for _ in range(antall_mnd):
        # legg til månedlige renter og trekk termin
        saldo = saldo + saldo*rente_m - terminbeløp
        # oppdater "kalender"
        x.append(f"{year}.{str(month).zfill(2)}"); y.append(saldo)
        month += 1
        if month == 13:
            month = 1; year += 1
    return x, y, terminbeløp

def serie_manedlig(saldo=15000, rente_å=0.08, start=2025, slutt=2035):
    """Serielån månedlig: fast avdrag per måned, rente beregnes på restsaldo."""
    rente_m = rente_å / 12
    antall_mnd = (slutt - start + 1) * 12
    fast_avdrag = saldo / antall_mnd

 
    x = [f"{start-1}.12"]
    y = [saldo]
    year = start; month = 1
    for _ in range(antall_mnd):
        rente_bet = saldo * rente_m
        betaling = rente_bet + fast_avdrag
        saldo = saldo + rente_bet - betaling  # = saldo - fast_avdrag
        x.append(f"{year}.{str(month).zfill(2)}"); y.append(saldo)
        month += 1
        if month == 13:
            month = 1; year += 1
    return x, y, fast_avdrag

# Kjør og plott
xAm, yAm, termin_mnd = annuitet_manedlig(saldo=15000, rente_å=0.08, start=2025, slutt=2035)
xSm, ySm, avdrag_mnd = serie_manedlig(saldo=15000, rente_å=0.08, start=2025, slutt=2035)

plt.plot(yAm, "r-",  label=f"Annuitet mnd (termin ≈ {termin_mnd:.2f} kr)")
plt.plot(ySm, "b--", label=f"Serie mnd (fast avdrag ≈ {avdrag_mnd:.2f} kr)")
plt.title("Saldo-utvikling: månedlig kapitalisering og betalinger")
plt.xlabel("Måned (0=start)"); plt.ylabel("Saldo (kr)"); plt.legend(); plt.show()
```

*Liten refleksjon*

Jeg har brukt koden **.zfill(2)**. Den brukes for å fylle på nuller foran et tall slik at det får en bestemt lengde. Jeg skrev inn **.zfill(2)** for at mars måneden (den tredje måned) skrives 03 og ikke bare 3. Dette ble nyttig når jeg skulle vise datoer eller måneder på en pen og litt mer oversiktlig måte. 

En månedlig kapitalisering gjør at renteeffekten forløper **jevnere** gjennom året. Med en **annuitet** så gis et konstant termin, mens med **serie** så gis en synkende totalbeløp. 
Over smame total horisont vil serie vanligvis gi **lavere rentekostnader**, men høyere betaling i starten.

+++

## Oppgave 3: Sannsynlighet justeres etter forrige endring (momentum)

I virkeligheten ser vi ofte "trender": etter en renteøkning er det **litt høyere** sannsynlighet for enda en økning, helt til en nedgang faktisk inntreffer (og motsatt).

Jeg implementerer dette slik:
- Jeg trekker tall fra 1..100 (mer finmasket enn 1..10).
- Jeg har to terskler: `terskel_opp` og `terskel_ned`.
  - Hvis `rand <= terskel_opp` → rente **opp** (+0.5 pp)
  - Hvis `rand >= 101 - terskel_ned` → rente **ned** (−0.5 pp)
  - Ellers uendret
- Etter en **oppgang**: øker jeg `terskel_opp` litt og reduserer `terskel_ned` litt (momentum opp).
- Etter en **nedgang**: øker jeg `terskel_ned` litt og reduserer `terskel_opp` litt (momentum ned).
- Tersklene holdes innenfor rimelige grenser (f.eks. 5–35 %).

```{code-cell} ipython3
import random
import matplotlib.pyplot as plt

def loan_random_momentum(saldo=15000, rente=0.08, terminbeløp=2000,
                         start=2025, slutt=2035, gebyr=0,
                         steg=0.005,
                         terskel_opp_init=10, terskel_ned_init=10,
                         min_terskel=5, max_terskel=35):
    """
    Momentum-modell for renteendringer:
    - Start-sannsynligheter: terskel_opp_init% for opp, terskel_ned_init% for ned
    - Etter en oppgang: terskel_opp økes litt, terskel_ned reduseres
    - Etter en nedgang: terskel_ned økes litt, terskel_opp reduseres
    - Trekker rand i [1..100] for hvert år
    """
    x = [start - 1]; y = [saldo]
    r = rente
    t_opp = terskel_opp_init
    t_ned = terskel_ned_init

    for year in range(start, slutt + 1):
        rand = random.randint(1, 100)
        changed = False

        if rand <= t_opp:
            r += steg
            t_opp = min(max_terskel, t_opp + 3)   # litt mer sannsynlighet for ny oppgang
            t_ned = max(min_terskel, t_ned - 2)   # litt mindre sannsynlighet for nedgang
            changed = True
        elif rand >= 101 - t_ned:
            r -= steg
            t_ned = min(max_terskel, t_ned + 3)
            t_opp = max(min_terskel, t_opp - 2)
            changed = True
        # ellers: r uendret, terskler uendret

        # oppdater saldo for året
        saldo = saldo + saldo*r
        saldo = saldo + gebyr
        saldo = saldo - terminbeløp

        x.append(year); y.append(saldo)

    return x, y


# Vis noen løp med momentum, termin 2000
plt.figure()
for _ in range(8):
    x, y = loan_random_momentum(saldo=15000, rente=0.08, terminbeløp=2000, start=2025, slutt=2035)
    plt.plot(x, y)
plt.title("Momentum i renteendringer – flere simuleringer (termin 2000)")
plt.xlabel("År"); plt.ylabel("Saldo (kr)"); plt.show()

# Sammenlign termin 500 vs 2000 med momentum (ett løp hver)
x500, y500 = loan_random_momentum(saldo=15000, rente=0.08, terminbeløp=500, start=2025, slutt=2035)
x2k,  y2k  = loan_random_momentum(saldo=15000, rente=0.08, terminbeløp=2000, start=2025, slutt=2035)

plt.plot(x500, y500, "r--", label="Termin 500 (momentum)")
plt.plot(x2k,  y2k,  "b-",  label="Termin 2000 (momentum)")
plt.title("Momentum-modell – sammenligning terminbeløp")
plt.xlabel("År"); plt.ylabel("Saldo (kr)"); plt.legend(); plt.show()
```

*Liten refleksjon*

I oppgaven med tilfeldige renteendringer bruker vi en terskel som en slags grenseverdi for å avgjøre når renta skal gå opp eller ned.
I den enkle modellen hadde vi alltid 10 % sjanse for oppgang og 10 % sjanse for nedgang, uavhengig av hva som hadde skjedd tidligere. Dette er ganske statisk og lite realistisk.
Når vi innfører en *t kan vi endre sannsynligheten avhengig av situasjonen:
Dersom renta nettopp gikk opp, kan vi øke terskelen slik at sannsynligheten for en ny renteoppgang blir større.
Dersom renta nettopp gikk ned, kan vi gjøre det samme med terskelen for nedgang.

På denne måten blir modellen mer dynamisk og minner mer om virkeligheten, der renteendringer ofte kommer i serier og ikke helt tilfeldig hvert år.

En terskel kan for eksempel være satt til 20 %, som betyr at det er 20 % sjanse for renteoppgang. Når et tilfeldig tall (slump) blir trukket, sjekker vi om det er innenfor terskelen. Er det lavere eller lik terskelverdien, får vi renteoppgang.

Kort sagt: Terskelen fungerer som en sannsynlighetsgrense, og gir oss mulighet til å justere hvor sannsynlig renteendringer er, basert på tidligere hendelser.

- Momentum gjør at renta ofte **holder seg i samme retning** noen år før den snur. Det gir mer «klumper» av opp- eller nedgangsår.
- Konsekvens: saldo-baner spriker mer i perioder med **opp-trend**, og bedrer seg i **ned-trend**.
- Ser du at terminbeløpet 500 kr gir økende saldo i mange løp? Selv med noen ned-trend-år er det ofte ikke nok.

+++

## Avsluttende refleksjon

Denne oppgaven har gitt meg en praktisk forståelse av hvordan simulering kan brukes til å undersøke økonomiske spørsmål. Jeg har brukt tekniske ferdigheter som løkker, betingelser, funksjoner, lister og plotting for at jeg skal kunne bygge små modeller som svarer på oppgavene. Å kunne simulere hendelser som ser på hva som kan skje hvis renten øker, eller hvor lavt  terminbetalingen kan være før gjelden begynner å vokse? Ved å utvide til månedlig kapitalisering og legge inn tilfeldige renteendringer så ser jeg hvordan samme lån kan få svært ulik utvikling avhengig av forksjellige forutsetninger. Når det gjelder det faglige har jeg fått en tydeligere forståelse av renters rente, forskjellen mellom annuitetslån og serielån, samt risikoen ved lave terminbeløp som ikke dekker rentene.

Dette betyr noe for meg som studerer økonomi fordi slike modeller er nyttige i budsjettering, investeringsvurderinger og risikoanalyse. I arbeidslivet kan jeg bruke samme tilnærming for å teste robustheten i planer, kommunisere usikkerhet med enkle grafer, og begrunne anbefalinger med data. Samtidig så inser jeg at modellene og simuleringene er meget forenklet og for å kunne simulere gode beslutninger og virkelige sammenhenger så må kodene og modellene utvikles og bygges på.

```{code-cell} ipython3

```
