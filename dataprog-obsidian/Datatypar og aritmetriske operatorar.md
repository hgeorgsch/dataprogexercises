
## Datatyper og variabler

De 4 mest grunnleggende datatypene er:
1. Heltall `int`
2. Flyttall `float`
3. Tekststrenger / strenger `str`
4. Boolske verdier (sann/usann) `bool`

Heltall er heltall som vi kjenner de fra matematikken, kan være positiv eller negativ eller 0.

Flyttall er desimaltall som 1.2, $\\pi$ eller $\\frac{11}{7}$. Det kan virke rart å skille mellom heltall og desimaltall, er ikke de begge bare numeriske verdier? Grunnen til skillet er at heltall og flyttall representeres forskjellig når de lagres i datamaskinen.

Datatypen `bool` har bare to verdier: `True` og `False`

### Tekststrenger

Vi kan lage tekststrenger i python ved å bruke doble anførselstegn " "):
```
print("Hello world igjen...?")
```
Eller enkle anførselstegn ' ':
```
print('To tomater gikk over en vei')
```

Dersom vi har tekst som går over flere linjer, kan vi bruke tripel """ eller trippel ''':
```
print("""Der bode en underlig gråsprængt en 
på den yderste nøgne ø; –
han gjorde visst intet menneske mén 
hverken på land eller sjø; 
dog stundom gnistred hans øjne stygt, –
helst mod uroligt vejr, –
og da mente folk, at han var forrykt, 
og da var der få, som uden frykt 
kom Terje Vigen nær.""")
```

### Variabler

I programmering bruker vi *variabler* til å lagre data og informasjon slik at vi senere kan refere til og manipulere de. 

Det er viktig å gi variablene meningsfulle og deskriptive navn, og vi tilordner variablene en verdi ved bruk av `=`

Variabelnavnene må begynne med en bokstav eller understrek (_) og kan ellers inneholde tall men ikke spesialtegn

Vi kan sjekke datatypen til en variabel med funksjonen `type(<variabel>)`



```

#Heltall
antall_epler = 6
Antall_epler = 4

#Flyttall
temperatur = 39.9
celeritas = 3e8 # Vitenskapelig notatsjon 3 * 10^8
h = 6.63e-34 # Plancks konstant 6.63 * 10^(-34)

# Tekststreng
terje_vigen = """
Der bode en underlig gråsprængt en 
på den yderste nøgne ø; –
han gjorde visst intet menneske mén 
hverken på land eller sjø; 
dog stundom gnistred hans øjne stygt, –
helst mod uroligt vejr, –
og da mente folk, at han var forrykt, 
og da var der få, som uden frykt 
kom Terje Vigen nær.
"""



#Boolean
sant = True
usant = False



#Man kan tilordne funksjoner til en variabel også. Da dropper man ()
printe_funksjon = print
printe_funksjon("hei")

#NB - man kan overskrive innebygde funksjoner som print:
#print = "hp 1230"
print("hallo")
#Når det skjer restarter vi kernel


#Man kan sjekke hvilke datatype en variabel er med funksjonen type()

#Man kan lage flere variabler på en linje slik:
sats, ny_sats, type_sats = 0.2, True, "Grunnrenteskatt"
```


Datatypen til en variabel blir bestemt når vi gir variablen en verdi slik som over

Dersom vi trenger å skifte datatypen, eller vil spesifisere hvilken datatype vi vil ha bruker vi funksjonene:
* `int(x)`: Gjør om `x` til heltall
* `float(x)`: Gjør om `x` til flyttall
* `str(x)`: Gjør om `x` til en tekststreng

Skal vi gjøre om et flyttall `x` til et heltall med `int`-funksjonen blir tallene etter komma fjernet. Dersom vi vil avrunde, må vi gjør det med `round(flyttall, antall_siffer)` før vi bruker `int` funksjonen "



```
vekt = 90.8
vekt_int = int(vekt)
vekt_avrundet = int(round(vekt, 0))
print(vekt_avrundet)

#Dersom man vil ha heltallet 4 som flyttall bruker man funksjonen float()
#print(help(float))
epler = 4.0
epler2 = float(4)

#Vil man ha flyttallet 3e8 som heltall bruker man int()
#print(help(int))
lysets_hastighet = int(3e8)

#Ofte må man gjøre tekststrenger om til heltall eller flyttall
alder = input("Hvor gammel er du?")
alder_heltall = int(alder)
print("Typen til variabel alder:", type(alder))
tid_til_100 = 100-alder_heltall
print("Du er hundre om", tid_til_100, "år")"
```

## Aritmetiske operatorer

Når vi har laget variablene våres, vil vi kanskje manipulere de og gjøre noen utregninger.
Python har følgende aritmetiske operatorer:
| operator | navn | eksempel |
| -------- | ---- |  ------  |
| `+` |  Addisjon | `x+y` |
| `-` | Subtraksjon | `x-y`|
| `*` | Multiplikasjon | `x*y` |
| `/` | Divisjon | `x/y` |
| `%` | Modulus | `x%y` |
| `**` | eksponentiering | `x**2` |
| `//` | Heltallsdivisjon | `x//y`|

```
# Vi lager 2 variabler, x og y:
x = 8
y = 3

summen = x+y
differanse = x-y
gange = x*y
dele = x/y
potens = y**2
mod = 8%3
heltallsdiv = x//y

#Dersom vi vil ha linjeskift i en streng kan vi skrive det som "\\n"
print("x = ", x, "\\ny = ", y, "\\n\\n")
print("summen: ", summen)
print("differanse", differanse)
print("dele", dele)
print("potens", potens)
print("mod", mod)
print("heltallsdivisjon: ", heltallsdiv)
```


### Operator presedens

Hva mener vi når vi skriver `4/3*7` i python?
$$
\\frac{4}{3\\cdot 7}
$$
eller:
$$
\\frac{4}{3}\\cdot 7
$$
*Operatorpresedens/rekkefølge* bestemmer hvordan uttrykket tolkes. 
Python prioriterer operatorer i følge rekkefølge:
1. () - Paranteser løses opp før noe annet
2. ** - Deretter kommer eksponentiering
3. \\*, /, //, % - etterfulgt av gange, dele og modulo
4. -, + - Addisjon og subtraksjon kommer til slutt

Dersom to operatorer har samme presedens, evalueres det fra venstre mot høyre
slik at `4/3*7` blir $\\frac{4}{3}\\cdot 7$. 

`4/3**7` derimot, blir $\\frac{4}{3^7}$ og ikke $\\left(\\frac{4}{3}\\right)^7$ fordi `**` har høyere presedens enn `/`

Moralen i historien er altså at vi må passe på at uttrykkene blir regnet ut riktig, ved høvelig bruk a paranteser"


