---
tags:
  - exercise
  - simulering
  - loop
---


+ Problem.
	+ lån med årleg rente
	+ Sjå [[Sparekalkulator]]
+ Relativt enkelt problem.
	+ kan løysast analytisk, om du kan litt matematikk
	+ kan løysast i rekneark, om du har god orden
	+ me løyser det her for å demonstrera nokre grunnleggjande programeringskonsept og korleis me kan leika med ulike tankeeksperiment
	+ med litt røynsle og litt kreativitet er der inga grense for kva de kan gjera
		+ vert det komplekst nok, får de til meir med programmering enn med rekneark

## Disposisjon

Simulering vert ofte brukt for å modellera og analysera moglege framtidsscenario. I staden for å laga utvikla éin modell som skildrar kva som må skje eller sannsynligvis skjer, simulerer ein eitt mogleg scenario, basert på eitt sett føresetnader. So kan ein evt. simulera fleire gongar med ulike færesetnader. Dette er særleg nyttig i komplekse og probabilistiske modellar, som det ofte er uråd å løysa analytisk. Me høyrer ofte om utgreiingar som refererer til simulering, t.d. i epidemologi og smittevern og i traffikkprogrnosar og vegplanleggjing. 

Her skal me sjå på eit ganske enkelt problem, for å illustrera dei mest grunnleggjande programmeringsteknikkane. Me tek for oss eit lån, fyrst med rentekostnader og nedbetaling. Dette kan me løysa matematisk og analytisk, men mange vil kanskje finna simuleringa enklare å forstå. Deretter skal me sjå på tilfeldige rentesvingingar, noko som krev langt meir avansert matematikk å løysa analytisk.

Etter økta skal de kunna
1. sjå korleis simulering kan brukast til å forstå kva som kan skje i ulike samfunnsscenario.
2. bruka *løkker* (`for` eller `ẁhile`) i programmering
3. programmera med slumptal og tilfeldige hendingar

### Den fyrste løkka - rente kvart år

Eit lån, og mange andre kontantstraumar, er ein enkel prosess. Prosessen er diskret, i den tydinga at tida beveger seg i faste steg eller periodar, t.d. kvart år eller kvar månad.  Dette gjeld ikkje *spot*-marknader der transaksjonar skjer vilkårleg tett, og uansett kor ofte du observerer prisen eller saldoen, so kan nokon ha rukke å selja noko og påverka prisen imellom observasjonane. Det skal me ikkje tenkja på her.  Lat oss sjå på eit enkelt lån der rentene vert kapitaliserte 31. desember kvart år.

Koden vert enklast å lesa dersom me bruker ein variabel med namn til rentesats.
Lat oss starta med 5%.
```
rentesats = 5  # Rentesats i prosent
rente = 5/100  # Rentesats til utrekning
```

No treng me kode som gjentek den same operasjonen kvart år. Den mest grunnleggjande måten å gjera det på, er med ei løkke (*loop*). Der finst ulike formar.  Lat oss sjå på `for`-løkka fyrst. 

**Oppgåve** Prøv fyrst å lesa koden under. Går det an å forstå kva som skjer utan å køyra koden? Køyr so koden og sjå på resultatet.
```
saldo = 10.000
for year in range(2025,2045):
   print( f"Lånesaldo 1. januar {year}: {saldo}" )
   saldo = saldo + saldo*rente
   print( f"Lånesaldo 31. desember {year}: {saldo}" )
```

Løkka definerer ein variabel (her `year`) som tek kvar verdi i ei liste eller eit listeliknande objekt (her `range`). Koden inni løkka vert køyrd éin gong med kvar verdi. Lånet vert utbetalt berre ein gong, før løkka starta, her med eit lånebeløp på 10.000.

**Merk** `range` er ikkje ei liste, men ein sokalla iterator. Det speler inga rolle, bortsett frå når me ynskjer å inspisera objektet. Det går derimot an å konvertera til ei liste.

```
print( list( range(2024,2045) ) )
```
Me kan samanlikna det med sjølve iteratoren:

```
print( range(2024,2045) )
```

**Oppåve**  `for`-løkka går like godt med ei liste.  Prøv å byta ut `range(2025,2045)` med ei liste, t.d. `[ 2025, 2026, 2027, 2028 ]`.

### Nedbetaling

```
saldo = 10.000
terminbetaling = 1000
for year in range(2025,2045):
   print( f"Lånesaldo 1. januar {year}: {saldo}" )
   saldo = saldo + saldo*rente
   saldo = saldo - terminbetaling
   print( f"Lånesaldo 31. desember {year}: {saldo}" )
```

*Oppgåve*  Kva skjer om du trekk frå terminbetalinga før du legg til renta? Gjer det nokon forskjell?

```
saldo = 10.000
terminbetaling = 1000
year = 2025
while saldo > 0:
   print( f"Lånesaldo 1. januar {year}: {saldo}" )
   saldo = saldo + saldo*rente
   saldo = saldo - terminbetaling
   print( f"Lånesaldo 31. desember {year}: {saldo}" )
   year = year + 1
```

**Oppgåve** Kva skjer om du set terminbetalinga lågt, t.d. til 200?

**Oppgåve** Ofte vert lånet belasta med eit fast gebyr i tillegg til rentene.  Legg til eit gebyr på 50kr/år i simuleringa. Korleis påverker det lånet?
### Plotting og annan bruk av utrekningane

1. Plott
2. Rekn ut total

### Den matematiske løysinga

1. Geometrisk rekkje - lukka form
	1. plott og samanlikna

### Plott og samanlikning

### Tilfeldige renteendringar i framtida

1. Legg til tilfeldige rentehopp


### Oppgåver

+ Serielån - plott terminbeløp
+ Månadleg betaling