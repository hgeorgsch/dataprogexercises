---
tags:
   - legacy/iif
---

+ kundedata1.json
+ `Oppgave4-JH.ipynb`
	+ mange variantar med og utan løysingsforslag

# 4.1

* Lag et program som går gjennom listen og regner ut hvordan saldo på sparekonto vokser over tid.
* Ta i første omgang utgangspunkt i at alle kunder sparer et fast terminbeløp $n$ ganger i året, til en fornuftig rente $r$

* Hvordan er fordelingen av sparepenger blant kundene? -- lag et histogram med pyplot (plt.hist(.....)) som viser dette
* Utifra fordelingen av sparepenger -- sett noen fornuftige grenser for foreksempel "lite bemidlet", "middels bemidlet" og "rike" kunder
* Oppdater dataene med disse klassifiseringene, og eventuelt annen nyttig info (gjennonsnittssaldo før/etter, max/min saldo..)
  - Her kan du gjerne gjøre "kundedata" listen til et felt i en annen datastruktur
* Vis fordeling med et kake-diagram og histogram
* Hvordan endrer denne fordelingen seg over tid?


# 4.2: Endring i fordeling over tid

* I dataen vi jobber med er startsaldo normalfordelt rundt 100,000 kr
* Vis denne fordelingen med et histogram
* Bruk feks `random.gauss()`eller `np.random.normal()` til å gi kundene ulike betingelser på terminbeløp og rente
* Hvilken effekt har dette på fordelingen av sparepengene når lang tid har gått?
* Kanskje kan du se på effekt på fordelingen om vi klassifiserer kundene inn i set på rike, middels- og lavt bemidlede kunder og gir de ulike sparebetingelser?

# 4.3: Gini-indeks

* Vi bygger videre i på programmet i 4.2
* Les deg opp på Gini-indeks og Lorenzkurven [her](https://en.wikipedia.org/wiki/Gini_coefficient)
* Plott fordelingen av sparepenger etter lengre tid når ikke alle har samme sparebetingelser:
  - Vis dette med Lorenzkurven
  - Regn ut Gini-indeks for fordelingen av sparepenger

# 4.4 Skjevfordelt startsaldo og terminbeløp

* La oss anta at startsaldoen eller terminbeløpet ikke er normalfordelt blant kundene
* Startfordelingene er heller gitt ved Lorenzkurven:  $L(x) = x^3$
* Gi kundene en startsaldo definert ved denne Lorenzkurven og finn ut hva som skjer med fordelingen over tid
* Fordel terminbeløp til kunder som tilsvarer denne Lorenzkurven og finn ut hva som skjer med fordelingen over tid
* Hilke faktorer er avgjørende for ulikhet og skjevfordeling når det kommer til sparing?
