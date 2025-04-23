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
+ Steg
	1.  *for*-løkka; per år, legg til rente 
		1. Plott
		2. Rekn ut total
	2. betal avdrag
		1. serielån
		2. annuitetslån
	3. Geometrisk rekkje - lukka form
		1. plott og samanlikna
	4. Legg til tilfeldige rentehopp

## Disposisjon

Simulering vert ofte brukt for å modellera og analysera moglege framtidsscenario. I staden for å laga utvikla éin modell som skildrar kva som må skje eller sannsynligvis skjer, simulerer ein eitt mogleg scenario, basert på eitt sett føresetnader. So kan ein evt. simulera fleire gongar med ulike færesetnader. Dette er særleg nyttig i komplekse og probabilistiske modellar, som det ofte er uråd å løysa analytisk. Me høyrer ofte om utgreiingar som refererer til simulering, t.d. i epidemologi og smittevern og i traffikkprogrnosar og vegplanleggjing. 

Her skal me sjå på eit ganske enkelt problem, for å illustrera dei mest grunnleggjande programmeringsteknikkane. Me tek for oss eit lån, fyrst med rentekostnader og nedbetaling. Dette kan me løysa matematisk og analytisk, men mange vil kanskje finna simuleringa enklare å forstå. Deretter skal me sjå på tilfeldige rentesvingingar, noko som krev langt meir avansert matematikk å løysa analytisk.

Etter økta skal de kunna
1. sjå korleis simulering kan brukast til å forstå kva som kan skje i ulike samfunnsscenario.
2. bruka *løkker* (`for` eller `ẁhile`) i programmering
3. programmera med slumptal og tilfeldige hendingar

### Lånet over tid

### Den matematiske løysinga

### Plott og samanlikning