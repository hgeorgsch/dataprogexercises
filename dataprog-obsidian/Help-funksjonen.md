---
tags:
   - legacy/iif
---

## Første steg: `print()` og `help()`

Det første vi ser på er python *funksjonene* `print` og `help`.

### Funksjoner

Funksjoner i python er litt som «miniprogrammer». 
Disse miniprogrammene kjører og styrer vi i koden vår. Da sier vi at vi gjør *funksjonskall* eller *kaller* funksjonene.

Når vi gjør et funksjonskall bruker vi navnet til funksjonen pluss (...), feks slik:
```
print("Hello World!")
```
Inne i parantesene sender vi *funksjonsargumentene*. I eksempelet over gir vi `print`-funksjonen en tekststreng `"Hello world!"` som funksjonen printer til skjerm/standard output.

Funksjoner kan ta flere *argumenter*, da skiller vi de med et komma (arg1,arg2) inne i parantesen, eller den
kan ta ingen argumenter, da er parantesene tomme

Funksjoner kan også returnere, gi tilbake 1 eller flere verdier eller objekter, men kan også gi tilbake ingenting og gjøre noe i bakgrunnen heller (stille klokken, opprette en fil, sende en beskjed osv.)

```
from datetime import datetime

#Her tar vi 1 argument og returnerer ingenting
print("BØ!")

#Her tar print 2 argumenter og returnerer ingenting
print("UÆ!", "...ikke skrem meg", sep='\n', end='\n\n\n')

#Her tar funksjonen help 1 argument, printfunksjonen,
#og gir tilbake hjelpetekst som vi printer ut
print(help(print))

#Funksjonen now() fra datetime biblioteket tar ingen argumenter, og returnerer tid og dato
print(datetime.now())
```


### Innebygde, importerte og egendefinerte funksjoner

Funksjonene `help` og `print` er eksempler på *innebygde funksjoner*. 
De følger med python og er alltid tilgjengelige

Funksjonen `now()` har vi *importert* fra `datetime`-biblioteket.
Vi kan importere bibliotek, pakker, eller moduler som gir oss funksjoner som hjelper oss med feks dataanalyse (`pandas`), matematikk (`math`, `sympy`, `numpy`) eller grafikk/plotting (`matplotlib`)

Vi kan også lage egendefinerte funksjoner som hjelper oss å strukturere programmet vårt, og til at vi slepper å skrive samme kode flere ganger med forskjellige "inputs""


