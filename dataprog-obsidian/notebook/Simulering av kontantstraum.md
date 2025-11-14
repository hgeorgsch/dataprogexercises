---
title: Simulering av kontantstraum
author: Hans Georg Schaathun
tags: [exercise, simulering, loop]
jupytext:
  cell_metadata_filter: -all
  formats: md:myst,ipynb
  root_level_metadata_filter: -title,-author,-tags
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Simulering av ein kontantstraum

Simulering vert ofte brukt for å modellera og analysera moglege framtidsscenario. I staden for å utvikla éin modell som skildrar kva som må skje eller sannsynligvis skjer, simulerer ein eitt mogleg scenario, basert på eitt sett føresetnader. So kan ein evt. simulera fleire gongar med ulike føresetnader. Dette er særleg nyttig i komplekse og probabilistiske modellar, som det ofte er uråd å løysa analytisk. Me høyrer ofte om utgreiingar som refererer til simulering, t.d. i epidemologi og smittevern og i traffikkprognosar og vegplanleggjing. 

Her skal me sjå på eit ganske enkelt problem, for å illustrera dei mest grunnleggjande programmeringsteknikkane. Me tek for oss eit lån, fyrst med rentekostnader og nedbetaling. Dette kan me løysa matematisk og analytisk, men mange vil kanskje finna simuleringa enklare å forstå. Deretter skal me sjå på tilfeldige rentesvingingar, noko som krev langt meir avansert matematikk å løysa analytisk.

::: {admonition} Læringsutbyte
Etter økta skal de kunna
1. sjå korleis simulering kan brukast til å forstå kva som kan skje i ulike samfunnsscenario.
2. bruka *løkker* (`for` eller `ẁhile`) i programmering
3. programmera med slumptal og tilfeldige hendingar
:::

## Den fyrste løkka - rente kvart år

Eit lån, og mange andre kontantstraumar, er ein enkel prosess. Prosessen er diskret, i den tydinga at tida beveger seg i faste steg eller periodar, t.d. kvart år eller kvar månad.  Dette gjeld ikkje *spot*-marknader der transaksjonar skjer vilkårleg tett, og uansett kor ofte du observerer prisen eller saldoen, so kan nokon ha rukke å selja noko og påverka prisen imellom observasjonane. Det skal me ikkje tenkja på her.  Lat oss sjå på eit enkelt lån der rentene vert kapitaliserte 31. desember kvart år.

Koden vert enklast å lesa dersom me bruker ein variabel med namn til rentesats.
Lat oss starta med 5%.

```{code-cell} ipython3
rentesats = 5  # Rentesats i prosent
rente = 5/100  # Rentesats til utrekning
```

No treng me kode som gjentek den same operasjonen kvart år. Den mest grunnleggjande måten å gjera det på, er med ei løkke (*loop*). Der finst ulike formar.  Lat oss sjå på `for`-løkka fyrst. 

:::{admonition} Oppgåve
Prøv fyrst å lesa koden under. Går det an å forstå kva som skjer utan å køyra koden? Køyr so koden og sjå på resultatet.
:::

```{code-cell} ipython3
saldo = 10000
for year in range(2025,2045):
   print( f"Lånesaldo 1. januar {year}: {saldo}" )
   saldo = saldo + saldo*rente
   print( f"Lånesaldo 31. desember {year}: {saldo}" )
```

Løkka definerer ein variabel (her `year`) som tek kvar verdi i ei liste eller eit listeliknande objekt (her `range`).
Python bruker innrykk (indentering) for å markera kva som høyrer til løkka.  
Kolon på slutten av `for`-lina markerer starten på ein *blokk*, som inkluderer alle liner som er innrykte i forhold
til `for`.
Denne blokken vert køyrd éin gong med kvar verdi av `year`.
Lånet vert utbetalt berre ein gong, før løkka starta, her med eit lånebeløp på 10.000.

::: {hint}
Blokknotasjonen går igjen.  Me såg han fyrst då me definerte
funksjonar med `def`.  Ogso `def`-lina slutta med kolon, og heile den indenterte blokken høyrde til funksjonen.
:::

**Merk** at `range` ikkje er ei liste, men ein sokalla iterator.
Det speler inga rolle, bortsett frå når me ynskjer å inspisera objektet. Det går derimot an å konvertera til ei liste.

```{code-cell} ipython3
print( list( range(2024,2045) ) )
```

Me kan samanlikna det med sjølve iteratoren:

```{code-cell} ipython3
print( range(2024,2045) )
```

:::{admonition} Oppgåve
`for`-løkka går like godt med ei liste.  Prøv å byta ut `range(2025,2045)` med ei liste, t.d. `[ 2025, 2026, 2027, 2028 ]`.
:::

## Nedbetaling

Den fyrste simuleringa viser korleis lånet veks med renter og rentesrente. I praksis betaler ein som regel lånet ned, gradvis år for år.  Sett at me startar med det same lånet som over, men betaler inn eit terminbeløp på 1000 kr same dagen som rentene vert kapitaliserte kvar år.

```{code-cell} ipython3
terminbetaling = 1000
```

:::{admonition} Oppgåve
Korleis vil du endra koden over slik at nedbetalinga òg vert simulert?
:::

Kan henda kjem du opp med noko slikt som dette:

```{code-cell} ipython3
saldo = 10000
for year in range(2025,2045):
   print( f"Lånesaldo 1. januar {year}: {saldo}" )
   saldo = saldo + saldo*rente
   saldo = saldo - terminbetaling
   print( f"Lånesaldo 31. desember {year}: {saldo}" )
```

:::{admonition} Oppgåve
Kva skjer om du trekk frå terminbetalinga før du legg til renta? Gjer det nokon forskjell?
:::

Her er det litt vilkårleg om me klarer å betala ned lånet innanfor simuleringsperioden fram til 2045 eller ikkje.  Det går an å skriva løkka slik at ho simulerer fram til lånet er nedbetalt.  Det enklaste er då å bruka `while` i staden for `for`.

:::{admonition} Refleksjon
Ser du kva koden under gjer før du køyrer han?
:::

```{code-cell} ipython3
saldo = 10000
year = 2025
while saldo > 0:
   print( f"Lånesaldo 1. januar {year}: {saldo}" )
   saldo = saldo + saldo*rente
   saldo = saldo - terminbetaling
   print( f"Lånesaldo 31. desember {year}: {saldo}" )
   year = year + 1
```

:::{admonition} Refleksjon
Kvifor må me setja `year` før løkka startar i dette tilfellet, og ikkje i tilfellet med `for`?
:::

Med `while`-løkka kan me gjenta koden heilt til eit eller anna vilkår er innfridd. Til samanlikning er `for`-løkka ganske rigid; ho handterer variabelen `year` sjølv og går gjennom førehandsbestemte verdiar. Med `while` tek programmøren heile ansvaret for variabelen og sluttkriteriet. Det gjev litt meir kode for å oppdatera `year`, men òg meir fleksibilitet.

:::{admonition} Oppgåve
Kva skjer om du set terminbetalinga lågt, t.d. til 200?
:::

:::{admonition} Oppgåve
Ofte vert lånet belasta med eit fast gebyr i tillegg til rentene.  Legg til eit gebyr på 50kr/år i simuleringa. Korleis påverkar det lånet?
:::

## Plotting og annan bruk av utrekningane

Som regel, når me simulerer, er me interesserte i data undervegs
i simuleringa, t.d. lånesaldo år for år.  I simuleringane over
har me ikkje lagra noko undervegs, berre skrive ut til skjerm.
Ein måte å endra dette på er å laga ein liste som samlar lagrar
resultatet i kvar iterasjon.

```{code-cell} ipython3
saldo = 10000
y = [ saldo ]
x = [ 2024 ]
for year in range(2025,2045):
   saldo = saldo + saldo*rente
   y.append( saldo )
   x.append( year )
print( x )
print( y )
```

Her lagar me to lister, kalt `x` og `y` som reflekterer at me skal plotta
resultatet straks.  Liste-typen har ein metode (eller funksjon) `append`
for å leggja til eit element på slutten av lista.  Dersom du er usikker
på korleis det verkar, so kan du flytta `print`-satsane inn i løkka og sjå
kva som skjer.

Me kan plotta som me har gjort før.

```{code-cell} ipython3
import matplotlib.pyplot as plt
plt.plot( x, y )
plt.show()
```

:::{admonition} Oppgåve
Plott utviklinga av lånesaldoen med årleg nedbetaling.
:::

## Gjenbruk av simuleringa med funksjonar

Slik me har gjort det til no, er det tungvint å variera parametrane
og gjenta simuleringa.
Me må kopiera fleire kodeliner og endra nokre få tal.
Dette kan me gjera enklare ved å definera funksjonar.

```{code-cell} ipython3
def loan(saldo=10000,rente=0.05,terminbetaling=0,year=2024,gebyr=0):
   y = [ saldo ]
   x = [ year ]
   while saldo > 0:
      saldo = saldo + saldo*rente
      saldo = saldo + gebyr
      saldo = saldo - terminbetaling
      year = year + 1
      y.append( saldo )
      x.append( year )
   return (x,y)
```

Her definerer me ein funksjon (med `def`) med mange parametrar:
`saldo`, `rente`, `year` og `gebyr`.
Dermed kan me velja ny parameterverdi kvar gong me køyrer funksjonen.
Kvar parameter har fått ein initialverdi, som gjer parameteren valfri.  
Dersom me ikkje spesifiserer ein paremeter, vert initialverdien brukt.
Returverdien frå funksjonen er ein tuppel med to verdiar.
Resten av koden burde vera gjenkjenneleg frå tidlegare døme, sjølv om
me har kombinert elementa på ein ny måte.

:::{admonition} Refleksjon
Den einaste parameteren som ikkje svarer til ein variabel i tidlegare
døme er `gebyr`.  Sjå på koden.  Kva representerer `gebyr`?
:::

Me kan t.d. bruka `loan`-funksjonen slik:

```{code-cell} ipython3
import matplotlib.pyplot as plt
x,y = loan(1000000,0.06,70000)
plt.plot( x,y )
```

:::{admonition} Definisjon
Du hugsar kanskje at verdiane i parentesen når me kaller (bruker)
funksjonen, vert kalt **argument**.
Namna som er lista i parentesen når me definerer funksjonen, vert
kalt **parametrar**.
Når funksjonen vert kalt, får parametrane verdi etter argumenta.
:::


Det går òg an å namngje ein eller fleire argument, og det gjer
ofte koden enklare å lesa.  T.d. kan me skriva

```{code-cell} ipython3
x,y = loan(1000000,terminbetaling=70000,gebyr=45)
plt.plot( x,y )
plt.show()
```

:::{caution}
Argument som ikkje er namngjevne, kaller me gjerne posisjonsargument.
Dei gjev verdi til parameteren i same posisjon.  
Namngjevne argument gjev verdi til parameter med same namn, og dei
kan kome i vilkårleg rekkjefylgje.
Bortsett frå éin ting.  Alle posisjonsargumenta må koma før dei
namngjevne argumenta.
:::

Lat oss no sjå på korleis me kan samanlikna simuleringar, t.d.
med ulike rentenivå

```{code-cell} ipython3
x5,y5 = loan(1000000,rente=0.05,terminbetaling=70000)
x4,y4 = loan(1000000,rente=0.04,terminbetaling=70000)
x3,y3 = loan(1000000,rente=0.03,terminbetaling=70000)
plt.plot( x5, y5, 'r--', x4, y4, 'b:', x3, y3, 'g' )
plt.legend( [ "5%", "4%", "3%" ] )
plt.show()
```

:::{admonition} Refleksjon
Kva tyder dei ulike argumenta til `plot`?
:::

:::{admonition} Refleksjon
Kva gjer `plt.legend()`?
Om du ikkje ser det med ein gong, so prøv å fjerna lina for å sjå 
kva som vert annleis.
:::

:::{admonition} Refleksjon
Kva skjer i simuleringa over om me set rentenivået til 6% eller 7%?
:::

Eit potensielt problem i simuleringa er at ho risikerer å køyra
uendeleg, dersom nedbetalinga ikkje dekkjer rentene.  
Det er god skikk å leggja inn ekstra stoppreglar for å unngå dette.
T.d. kan me stoppa simuleringa etter 100 år.

```{code-cell} ipython3
def loan2(saldo=10000,rente=0.05,nedbetaling=0,year=2024,gebyr=0):
   y = [ saldo ]
   x = [ year ]
   while saldo > 0 and len(x) < 100:
      saldo = saldo + saldo*rente
      saldo = saldo + gebyr
      saldo = saldo - terminbetaling
      year = year + 1
      y.append( saldo )
      x.append( year )
   return (x,y)
```

Her bruker me `len`-funksjonen som tel kor mange element som finst i lista.

:::{admonition} Oppgåve
Samanlikna lån med ulike terminbeløp (`nedbetaling`), ved å laga eit plott.
:::

:::{admonition} Oppgåve
Endra definisjonen av `loan2` slik at du har ein parameter til å setja
kor mange år som maksimalt skal simulerast.
:::

## Tilfeldige renteendringar i framtida

Alt som me har gjort til no, hadde du kanskje kunne gjort enklare
i rekneark.
Lat oss no auka komplekiteten eit hakk, og førestilla oss at rentenivået
vert endra tilfeldig i framtida.

Me kan t.d. tenkja oss at kvart år er det 10% sannsyn for at renta går
opp ½ prosentpoeng, og 10% sjanse for at ho går tilsvarande ned.
Då treng me ein mekanisme for slump.
Der finst fleire ulike modular og bibliotek som gjer dette i python.
Her kan me bruka eit av dei enklaste, som heiter
[random](https://docs.python.org/3/library/random.html).
Lat oss testa det fyrst.

```{code-cell} ipython3
import random
random.randint(1,10)
```

Dette er den einaste funksjonen me treng i dag;
`random.randint(1,10)` returnerer eit heiltal frå 1 til 10,
tilfeldig frå ei uniform fordeling.  Me kan kjapt testa at
me ikkje får same tal kvar gong, t.d.

```{code-cell} ipython3
[ random.randint(1,10) for x in range(20) ]
```

:::{admonition} Refleksjon
Ser resultatet rimeleg ut?
:::

:::{admonition} Refleksjon
Korleis kan me bruka eit slikt slumptal til å simulera
tilfeldige hendingar?
:::

Ein vanleg teknikk er å tolka ulike tal frå slumptalsgeneratoren
som ulike hendingar.  
T.d. kan me seia at 1 gjev renteoppgang og 10 gjev rentenedgang.
Då får me kanskje fylgjande som erstatning for `loan` og `loan2`.

```{code-cell} ipython3
def loan3(saldo=10000,rente=0.05,nedbetaling=0,year=2024,gebyr=0):
   y = [ saldo ]
   x = [ year ]
   while saldo > 0 and len(x) < 100:
      slump = random.randint(1,10)
      if slump == 1:
         rente = rente + 0.005
      elif slump == 10:
         rente = rente - 0.005
      saldo = saldo + saldo*rente
      saldo = saldo + gebyr
      saldo = saldo - terminbetaling
      year = year + 1
      y.append( saldo )
      x.append( year )
   return (x,y)
```

Her er der to nye element, som kan trengja forklaring.
Det fyrste er `if`, som liknar litt på `while`, bortsett
frå at `if` berre køyrer blokken éin gong dersom vilkåret
er sant, og ikkje fleire gongar so lenge som det er sant.
Vilkåret her er at `slump` må vera lik 1 for å få renteoppgang.
Fordi python bruker likskapsteiknet til tilordning, må me bruka
dobbelt likskapsteikn for likskap.  Dette er likskap i matematisk
forstand, som eit utsagn som kan vera sant eller usant.

Til slutt har me `elif`.  Dersom det fyrste `if`-vilkåret er sant,
vert `elif`-blokken ignorert.  Dersom det fyrste vilkåret er usant,
prøver maskina `elif` og sjekkar om `slump == 10` er sant.

I dette tilfellet vil me verkeleg simulera fleire gongar for å kunna
sjå tilfeldigheitene.

```{code-cell} ipython3
for i in range(12):
   (x,y) = loan3()
   plt.plot(x,y)
plt.show()
```

Legg merke til at me kan køyra `plt.plot()` mange gongar, og alt
kjem opp i den same figuren.

:::{admonition} Refleksjon
Er dette ein god sannsynsmodell for renteendringar i framtida?
Kan du forbetra han?
:::

:::{admonition} Oppgåve
Lag ein figur som simulerer lånet med andre parametrar.
:::

:::{caution}
Slumptal på ei datamaskin er ikkje strengt tatt tilfeldige.
Under panseret er der ein matematisk funksjon som genererer ein deterministisk
serie med tal, slik at det er relativt vanskeleg å forutsjå neste tal.
Dette er godt nok til dei fleste simuleringsformål, men i somme fagfelt
er det ei stor utfordring å laga slumptalsgeneratorar som er gode nok.

Der finst bibliotek som bruker data utanfrå, t.d. frå musa eller tastaturet,
til å finna ekte tilfeldige tal.  Problemet er at det går mykje treigare når
ein treng meir enn nokre få verdiar.
:::

## Oppgåver

:::{admonition} Oppgåve
So langt har me sett på annuitetslån, der terminbetalinga er eit fast beløp.
Tenk i staden på eit serielån, der du betaler rentene pluss eit fast 
nedbetalingsbeløp.
Lag eit plott som samanliknar utviklinga på serie- og annuitetslån.
:::

:::{admonition} Oppgåve
Me har simulert årlege terminar, noko som ikkje er særleg vanleg i røynda.
Lag simuleringar med månadleg rentekapitalisering og terminbetaling.
:::

:::{admonition} Oppgåve
I røynda kjem ei renteendring sjelden aleine.  
Kan henda vore burde sannsynlegheita for renteauke auka når den fyrste renteendringa
skjer, og ikkje gå ned før me ser ein rentenedgang.
Endra `loan3`-funksjonen for å simulera dette.

Det er litt plunder å få til, men du kan t.d.
1. Innføra ein variabel `terskel` og seia at me får renteoppgang når 
    `slump <= terskel`.
2. Kvar gong renta går opp eller ned, kan du justera `terskel`.
3. Slumptal frå 1 til 10 er kanskje for grovkorna, men du kan auka spennet til 100
    eller 1000.
4. Du kan laga ein tilsvarande terskel for rentenedgang.
:::

## Notat - materiale som vert utelate 

1. Geometrisk rekkje - lukka form
    1. plott og samanlikna

+ Problem.
    + lån med årleg rente
    + Sjå [[Sparekalkulator]]
+ Relativt enkelt problem.
    + kan løysast analytisk, om du kan litt matematikk
    + kan løysast i rekneark, om du har god orden
    + me løyser det her for å demonstrera nokre grunnleggjande programeringskonsept og korleis me kan leika med ulike tankeeksperiment
    + med litt røynsle og litt kreativitet er der inga grense for kva de kan gjera
        + vert det komplekst nok, får de til meir med programmering enn med rekneark

```{code-cell} ipython3

```
