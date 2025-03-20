---
tags:
   - intro
   - jupyter
---

+ Jonas' utgåve:  `Intro-JH.ipynb`

# Programmering og Jupyter Notebook
## Dei fyrste stega

Programmering er mykje rart. Folk som bruker programvareutvikling bruker gjerne andre verkty enn dei som programmerer matematiske modellar eller statistiske analysar. Målet med *dette* kurset er å bruka store datasett til å forstå verda, gjennom statistiske analysar, visualisering eller simulering. Mange bruker allereie rekneark til denne jobben, men mange nyttige datasett er for store til å lasta dei i rekneark, og då treng ein andre verkty.

I denne samanhengen er *Jupyter Notebook*, som dette dokumentet er skrive i, eit nyttig verkty. Her kan me kombinera tekst, programkode og utdata frå programmet i eitt og same dokument, slik at det er lett å sjå kva som foregår.

Eit dokument er delt opp i to typar celler som du skriv, samt utdata-celler.  Denne teksta er ei *markdown*-cellae, som me bruker til tekst.  I tillegg kan me skriva kode-celler, som den fylgjande.

```
print( "Hello World!")
```

Kodecella innheld programkode som vert køyrd av maskina når du trykkjer Shift-Lineskift.
Koden er skrive i eit språk som heiter *python* og som er vorte mektig populært dei siste tjue åra. Jupyter er ikkje dei einast programmet som tolkar og køyrer *python*-kode.  Det kan me koma tilbake til.

Målet i oppgåvene under er å testa at det har installert Jupyter, at det verkar og at de kan redigera Jupyter-dokument.
## Kode og program

Eg vil ikkje kalla innhaldet i kodecella for eit program. Det er berre éin einskild instruksjon. Eit program er ein serie instruksjonar, som skal utførast i rekkjefylgje.  Dette kurset har eit program, av økter og aktivitetar som eg har instruert at me skal utføra. Rett nok er me menneske og kan improvisera.  Den fridommen har maskina ikkje. Ho gjennomfører programmet strengt som det er skrive.  T.d.

```
h = 1.83
m = 87
bmi = 87 / h**2
print( f"BMI er {bmi}" )
```

Dette er eit *program*.  Maskina er instruert til å gjera fleire ting i rekkjefylgje, og me får ikkje resultatat før til slutt.

Her har me brukt fleire viktige mekanismar i programmering.
+ Variablar, `h` og `m` vert *tilordna* verdiar med likheitsteikn
+ Aritmetikk, når me tilordnar `bmi` reknar me ut eit reknestykke med divisjon `/` og potens `**`
+ `print` skriv ut ei melding på skjermen
+ `f"` ... `"` markerer ein formattert tekststreng.  Her kan me bruka krøllparentesane til å inkludera variablar (`bmi`).

Det er litt voldsomt med desimalar, so me kan instruera python til å bruka t.d. 2 desimalar.
```
print( f"BMI er {bmi:.2f}" )
```
Legg merke til at python hugsar alle variablane frå forrige kodecelle.  

#### Oppgåver

1.  Sjekk at du kan redigera ei kodecelle.
	1. Dobbelklikk på kodecella med utrekninga.
	2. Endra tala.
	3. Rekna ut BMI på nytt.  Trykk Shift-lineskift for å køyra koden.
	4. Ser det rett ut?
2.  Kan du endra utskrifta slik at programmet skriv BMI med éin desimal?
3. Kan du redigera ei *markdown*-celle òg?  Prinsippet er det same.  Dobbelklikk på cella, skriv kva du vil, og trykk Shift-lineskift for å *rendra* cella.

## Markdown

Formatteringa av teksta er sikkert uvand for mange. Når me redigerer, ser me ikkje korleis teksta ser ut, men kodar som er ein del av teksta. Det er fyrst når me «køyrer» cella, med Shift-lineskift, at teksta vert vist pent formattert.

Som *python* er *markdown* eit maskinspråk. Det er ikkje eit programmeringsspråk, sidan det ikkje er program som vert uttrykte, men noko som me gjerne kallar *markup*-språk.  *Markdown* er eit ordspel, og uttrykkar at det skal vera enklare å skriva og å lesa enn andre kjende *markup*-språk som LaTeX og HTML.

I tillegg til formatteringane som eg har brukt over, kan me bruka **utheva** tekst, og
+ unummererte punktlister
+ i tillegg til nummererte lister som du såg over
+ samt tabellar

| Frukt   | Pris (NOK) |
| :------ | ---------: |
| Eple    |         30 |
| Pære    |         50 |
| Plommer |         45 |

Markdown støtter også matematikk med $\\LaTeX$ syntax
$$ f(x) = 3x^2 + x - 10 $$
#### Oppgåver


Til mappen kan dere selvfølgelig også levere kun koden i en jupyter-notebook eller python (\\*.py) fil og rapport og annen tekst som en pdf eller word-fil"

```
# Dette er en kodecelle i python
print("Hello World!")
# Alt som kommer etter # er en kommentar og blir fullstendig ignorert
```

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

Vi kan sjekke datatypen til en variabel med funksjonen `type(<variabel>)`"
   ]
  },
  {
cell_type": "code",
execution_count": 5,
id": "7ecbbfd8",
metadata": {},
outputs": [
    {
name": "stdout",
output_type": "stream",
text": [
hei
hallo
     ]
    }
   ],
source": [

#Heltall
antall_epler = 6
Antall_epler = 4

#Flyttall
temperatur = 39.9
celeritas = 3e8 # Vitenskapelig notatsjon 3 * 10^8
h = 6.63e-34 # Plancks konstant 6.63 * 10^(-34)


#Tekststreng

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


Datatypen til en variabel blir bestemt når vi gir variablen en verdi slik som over

Dersom vi trenger å skifte datatypen, eller vil spesifisere hvilken datatype vi vil ha bruker vi funksjonene:
* `int(x)`: Gjør om `x` til heltall
* `float(x)`: Gjør om `x` til flyttall
* `str(x)`: Gjør om `x` til en tekststreng

Skal vi gjøre om et flyttall `x` til et heltall med `int`-funksjonen blir tallene etter komma fjernet. Dersom vi vil avrunde, må vi gjør det med `round(flyttall, antall_siffer)` før vi bruker `int` funksjonen "
   ]
  },
  {
cell_type": "code",
execution_count": 14,
id": "e2d73e43",
metadata": {},
outputs": [
    {
name": "stdout",
output_type": "stream",
text": [
91
     ]
    },
    {
name": "stdin",
output_type": "stream",
text": [
Hvor gammel er du? 37

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
    "
   ]
  },

x =  8 
y =  3 


summen:  11
differanse 5
dele 2.6666666666666665
potens 9
mod 2
heltallsdivisjon:  2


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


# Eksempel: Populasjonsvekst

Populasjonsvekst over tid i feks et land kan beskrives av følgende formel:
$$
P(t) = \\frac{K}{1+Ae^{-rt}}
$$
Her er:
* $P(t)$: Populasjon ved tiden t
* $t$ er tiden
* $r$ er relativ vekstrate, feks 2%
* $K$ er makskapasiteten til populasjonen
* $e$ er eulers tall: $e\\approx 2,71828$

$A$ er en koeffisient definert ved:
$$
A = \\frac{K-P_0}{P_0}
$$
Hvor $P_0$ er populasjonen ved $t=0$

På Island er det 372 520 innbyggere (2021). <br> Vi antar at Island maksimalt kan opprettholde en populasjon på 4 millioner og at relativ vekstrate på Island er 2%.

**Skriv et python-program som regner ut antall innbyggere på Island i 2040 og printer ut resultatet sammen med relevant informasjon**"

```
#Folketall på Island

e = 2.71828 #Eulers tall (Vi skal se en bedre måte å hente slike konstanter)
```

### Nyttig?

Enkle programmet som det over kan allerede være nyttig.

Siden vi la inn data fra problemet vårt (vekstrate, sluttid, startpopulasjon osv) i egne variabler, og brukte disse variablene til alle videre utregninger, kan vi raskt sjekke hva populasjonen er blir 2050, eller hva populasjonen blir om vekstraten er 5% kun ved å forandre verdien til disse «startvariablene»

* Legg inn parametere, startverdier og konstanter som egne variablene
* Bruk disse i alle videre beregninger

Vi kan også la den som bruker programmet legge inn noen av tallene/parameterene
med `input(<melding til bruker>)` funksjonen. Den viser meldingen til brukerene
og lar de skrive inn tall eller tekst som blir gitt til python som en tekststreng

```
# Krisekalkulator: Bruker gir sin alder og programmet oppgir
# hvor lenge det er til han fyller 40
```

## Meir stoff 

+ [Kjapt cheat sheet til hvordan skrive markdown](https://www.markdownguide.org/cheat-sheet),
+ [en litt større tutorial med mattetriksene til Latex](https://ashki23.github.io/markdown-latex.html)

![YouTube](https://www.youtube.com/watch?v=uVLzL5E-YBM)
