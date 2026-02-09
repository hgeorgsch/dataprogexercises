---
tags: [intro, jupyter, function, plot]
title: Introduksjon til Jupyter Notebook
author: Hans Georg Schaathun
date: 20. mars 2025
jupytext:
  cell_metadata_filter: -all
  root_level_metadata_filter: -tags,-title,-author,-date
  formats: md:myst,ipynb
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

# Programmering og Jupyter Notebook

## Dei fyrste stega

Programmering er mykje rart. Folk som bruker programvareutvikling bruker gjerne andre verkty enn dei som programmerer matematiske modellar eller statistiske analysar. Målet med *dette* kurset er å bruka store datasett til å forstå verda, gjennom statistiske analysar, visualisering eller simulering. Mange bruker allereie rekneark til denne jobben, men mange nyttige datasett er for store til å lasta dei i rekneark, og då treng ein andre verkty.

I denne samanhengen er *Jupyter Lab*, som dette dokumentet er skrive i, eit nyttig verkty. Her kan me kombinera tekst, programkode og utdata frå programmet i eitt og same dokument, slik at det er lett å sjå kva som foregår.

::: {admonition} Oppgåve
Når du les dette, bør du lasta ned heile dokumentet i Jupyter-format og 
opna det Jupyter Lab.

1. I nedlastingsmenyen øvst på sida, vel du `.ipynb`, som er
   filendinga Jupyter bruker.
2. Opna jupyter lab, anten frå Anaconda Navigator, eller ved å skriva
   `jupyter lab` i eit terminalvindauga.
3. Opna filnavigatøren med mappesymbolet til venstre i Jupyter Lab.
4. Finn dokumentet som du nett lasta ned.  Sannsynlegvis ligg det
   i *Downloads*-katalogen.
   Dokumentet skal ha filnavn som ender på `.ipynb`.  Om det ikkje
   har det vel du *Rename* i kontekstmenyen (høgreklikk) og legg
   til `.ipynb` i filnamnet.
5. Opna dokumentet ved å dobbelklikka.
:::

::: {hint}
Det er ikkje alltid heilt trivielt å opna eit Jupyter-dokument på Windows
og MacOS.
Det hender at vevlesaren endrar namnet slik at det sluttar på `.txt`, og då
kjenner ikkje Jupyter Lab det att.

Det enklaste plar vera å bruka filnavigatøren på venstre hand i Jupyter Lab.
Kontekstmenyen (høgreklikk på filnamnet) gjev et val for *rename*, der du 
kan endra filnament slik at det sluttar på `.ipynb`.
Når det er gjort, kan du dobbelklikka for å opna det i Jupyter Lab.
:::

Eit dokument er delt opp i to typar celler som du skriv, samt utdata-celler.
Du kan dobbelklikka på ei celle for å redigera innhaldet, og du kan køyra
ho med *play*-knappen øvst på sida.
Der finst hurtigtastar som ein kan slå opp.

Denne teksta er ei *markdown*-cellae, som me bruker til tekst.
I tillegg kan me skriva kode-celler, som den fylgjande.

```{code-cell} ipython3
print( "Hello World!" )
```

Kodecella innheld programkode som vert køyrd av maskina når du trykkjer Skift-Lineskift.
Koden er skrive i eit språk som heiter *python* og som er vorte mektig populært dei siste tjue åra. Jupyter er ikkje dei einast programmet som tolkar og køyrer *python*-kode.  Det kan me koma tilbake til.

Målet i oppgåvene under er å testa at de har installert Jupyter,
at det verkar, og at de kan redigera Jupyter-dokument.

:::{admonition} Definisjon
Instruksjonen `print` er eit døme på ein **funksjon** i python.
Det er ein førehandsdefinert instruksjon som vert utførd når funksjonsnamnet
er etterfulgt av eit parentesuttrykk.  Det som står inni parentesen
(`"Hello World!"`) kaller me **argumentet** til funksjonen.
:::

## Kode og program

Eg vil ikkje kalla innhaldet i kodecella over for eit program.
Det er berre éin einskild instruksjon. Eit program er ein serie instruksjonar, som skal utførast i rekkjefylgje.  Dette kurset har eit program, av økter og aktivitetar som eg har instruert at me skal utføra. Rett nok er me menneske og kan improvisera.  Den fridommen har maskina ikkje. Ho gjennomfører programmet strengt som det er skrive.  T.d.

```{code-cell} ipython3
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

:::{admonition} Definisjon
Ein **variabel** er eit namn som har ein verdi som kan variera ettersom
programmet køyrer.  I dømet over er `h`, `m` og `bmi` variablar.
Me kan **tilordna** (*assign*) ein ny verdi til ein variabel med eit
**tilordingsuttrykk**.  Python bruker likskapsteiknet `=` som tilordningssymbol.
:::

:::{caution} 
Merk at tilordningsuttrykket ikkje skal lesast som matematisk likskap.
T.d. kan me skriva `variabel = variabel + 1`, der venstre- og høgresida
openbert er ulike.  
Høgresida vert rekna ut fyrst, med den gamle verdien av `variabel`,
før verdien vert tilordna namnet `variabel` på venstre side.
Matematikarar vil gjerne skrive $:=$ eller $\leftarrow$ som tilordningssymbol,
medan $=$ tyder ein påstand om at dei to sidene *er* like.
:::

Det er litt voldsomt med desimalar, so me kan instruera python til å bruka t.d. 2 desimalar.

```{code-cell} ipython3
print( f"BMI er {bmi:.2f}" )
```

Legg merke til at python hugsar alle variablane frå forrige kodecelle.  

:::{admonition} Oppgåver
1.  Sjekk at du kan redigera ei kodecelle.
    1. Dobbelklikk på kodecella med utrekninga.
    2. Endra tala.
    3. Rekna ut BMI på nytt.  Trykk Skift-lineskift for å køyra koden.
    4. Ser det rett ut?
2.  Kan du endra utskrifta slik at programmet skriv BMI med éin desimal?
3. Kan du redigera ei *markdown*-celle òg?  Prinsippet er det same.  Dobbelklikk på cella, skriv kva du vil, og trykk Skift-lineskift for å *rendra* cella.
:::

::: {tip}
Du må gjerne redigera dokumentet og fjerna det som 
er overflødig for deg.
:::

## Parenteser og presedens

Parenteser går ofte i kluss, så det er verd å seia nokre ord om det med ein gong.
Me bruker dei på same måte som i matematikken.
$$
( 5 + 3 ) \cdot 2
$$
er ikkje det same som 
$$
5 + 3 ( \cdot 2 )
$$

::: {admonition} Refleksjon
Korleis les du
$$
5 + 3 \cdot 2\;\text{?}
$$
Som
$( 5 + 3 ) \cdot 2$ eller $5 + 3 ( \cdot 2 )$?
:::

I python skriv me

```{code-cell} ipython3
print( (5+3)*2 )
print( 5+(3*2) )
```

::: {admonition} Oppgåve
Korleis reknar python $5 + 3 \cdot 2$?
Prøv.
:::

Somme ting må skrivast om med ekstra parenteser i python, slik som kompliserte brøkar:
$$
\frac{ 2\cdot(5+3) }{ 40-(7*5) } 
$$
Det vert

```{code-cell} ipython3
print( (2*(5+3))/(40-(7*5)) )
```

::: {admonition} Oppgåve
Kva skjer om du sløyfer parentesar?
+ `2*(5+3)/(40-(7*5))`
+ `(2*(5+3))/40-(7*5)`
+ `2*(5+3)/40-(7*5)`

Kvifor?
:::

::: {admonition} Oppgåve
Korleis vil du skriva dette i python?
$$
\frac{ (5+3)^2 }{ 5+3^2 } 
$$
:::

Enkelt sagt vert parenteser rekna innanfrå og ut.  
Det inste parentesuttrykket vert rekna ut fyrst, og erstatta med resultatet, før neste vert rekna ut.

Presedens tyder at nokre operatorar vert rekna ut før andre, dersom der ikkje er parenteser som
styrer.  Det er relativt lett å hugsa dei grunnleggjande aritmetiske operatorane som me kjenner
frå matematikken, der potens (`**`) kjem før multiplikasjon og divisjon (`*` og `/`) som kjem før 
addisjon og subtraksjon (`+` og `-`).  Difor trong me ikkje parentes i uttrykket `m / h**2` for `bmi`.
Når de lærer fleire operatorar, kan presedensreglane vera vanskelege å hugsa, og det er ofte
enklare å setja nokre ekstra parentesar for å slippa å tenkja på presedens.

## Markdown

Formatteringa av teksta er sikkert uvand for mange. Når me redigerer, ser me ikkje korleis teksta ser ut, men kodar som er ein del av teksta. Det er fyrst når me «køyrer» cella, med Skift-lineskift, at teksta vert vist pent formattert.

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

Markdown støtter også matematikk med $\LaTeX$ syntax
$$
f(x) = 3x^2 + x - 10. 
$$

:::{admonition} Oppgåver
Bruk teksta mi over som døme, og svar på fylgjande.
Dobbelklikk for å sjå eller redigera koden og Skift-lineskift for å køyra (*rendra*).

1. Kva kode vert brukt til utheva skrift og kursiv?
2. Kva er skilnaden på ein og fleire skigardard (`#`)?
:::

## Funksjonar 

Funksjonar er litt tvetydig når me programmerer.
Ovanfor har me sett to ulike formar for funksjon.
I python er `print` ein funksjon som *gjer* noko, dvs. skriv ut noko
på skjermen.
I matematikken er $f(x)$ ein funksjon, som returnerer ein verdi.

Me kan programmera våre eigne funksjonar i python, og dei kan òg representera
matematiske funksjonar.  T.d.

```{code-cell} ipython3
def f(x):
    return 3*x**2 + x - 10
```

Kodeordet `def` seier at me definerer ein funksjon, som heiter `f` og har
eitt argument `x`.  Kodeordet `return` seier at funksjonen returnerer ein verdi.
Merk indenteringa.  Alt som er indentert er ein del av `def`-utsegna.  Neste
linje som ikkje er indentert vert ein ny instruksjon.

Me kan kalla funksjonen, t.d. som

```{code-cell} ipython3
print( "Funksjonsverdi", f(5) )
```

eller som del av eit uttrykk

```{code-cell} ipython3
print( f"Eit uttrykk f(10)*2-1 = {f(10)*2-1}." )
```

::: {admonition} Oppgåve
Kva er verdien av $f(8)$.
Lag ein kodeblokk og bruk funksjonen.
:::

Det er mogleg
for funksjonar i *python* både å returnera verdi og å gjera noko.

```{code-cell} ipython3
def f(x):
    print( f"x={x}" )
    return 3*x**2 + x - 10
```

:::{note}
Sjølv om `print` er ein funksjon som «gjer noko»,
så gjer han ingenting her, når `f` vert definert.
Han gjer noko når `f` seinare vert *brukt*.
:::

::: {admonition} Oppgåve
Kva skjer når du reknar ut $f(8)$ med den nye funksjonen `f`?
Lag ein kodeblokk og prøv.
:::

## Folketalsmodell

Lat oss ta eitt litt meir avansert døme.

Ofte har me matematiske modellar som skildrar forventa samfunns-
og foretningsutvikling.  T.d. meiner ein at folkeveksten i eit land
ofte kan skidrast som
$$
P(t) = \frac{K}{1+A\exp(-rt)} 
$$
der
+ $P(t)$: folketal ved tiden $t$
+ $r$ er relativ vekstrate, feks 2% (0,02)
+ $K$ er makskapasiteten til populasjonen
+ $\exp$ er den naturlege ekponentialfunksjonen $e^x$ der $e$ er 
  Eulers tall: $e\approx 2,71828$
+ $A$ er en koeffisient definert ved:
  $A = \frac{K-P_0}{P_0}$
  der $P_0$ er folketalet ved $t=0$.

For å implementera denne funksjonen i *python* er det enklast å bruka
ein modul som gjev tilgang til $\exp$-funksjonen.  Då bruker me ein
`import`-instruksjon.

```{code-cell} ipython3
import math

print( "exp 1 = ", math.exp(1) )
print( "exp 10 = ", math.exp(10) )
```

:::{admonition} Definisjon
Ein **modul** i python er ein samling definisjoner som er meint for
gjenbruk i ulike program. 
I dømet over er `math` ein slik modul, og `import`-instruksjonen
lastar denne modulen slik at me kan bruka funksjonar som er definerte
der.
Punktumnotasjonen i `math.exp(1)` seier at me bruker funksjonen
`exp` som er definert i `math`.
:::

Då kan me t.d. skriva

```{code-cell} ipython3
def folketal(tid):
    K = 3500000
    P0 = 45000
    A = (K-P0)/P0
    r = 0.04
    return K / ( 1 + A*math.exp(-r*tid) )

print( f"folketal etter 50 år er {folketal(50)}")
```

:::{admonition} Oppgåve

På Island er der 372 520 innbyggjarar (2021). 
Me reknar med at Island maksimalt kan oppretthalda eit folketal
på 4 millionar og at relativ vekstrate er 2% (=0,02).

*Skriv ein python-funksjon som reknar ut folketalet på Island i 2040 
og skriv ut resultatet saman med relevant informasjon om føresetnadene.*

(Du kan sjølvsagt ta utgangspunkt i dømet og endra tala.)
:::

## Plott

For å forstå ein matematisk modell ynskjer me som regel å plotta han.
Dette kan me gjera med fylgjande kode.

```{code-cell} ipython3
import matplotlib.pyplot as plt

xs = [ x for x in range(-5,+5) ]
ys = [ f(x) for x in xs ]

plt.plot( xs, ys )
plt.show()
```

Her dukkar der opp eit par nye konsept.
Dei to variablane, `xs` og `ys` vert definert som lister.

:::{admonition} Oppgåve
Kva er `xs` lik?  Lag ei ny kodecelle med ein `print`-instruksjon for å sjå.
:::

::: {hint}
Ofte har me lyst til å leggja inn kode midt i ein 
*markdown*-blokk.  Kontekstmenyen (høgreklikk) har eit val
for «split cell» som ein kan bruka, før ein legg inn den nye
cella.
:::

Den andre lista, `ys` er definert ved det som vert kalla listekomprehensjon,
elementa i lista er alle verdiane `f(x)` der `x` tek kvar verdi i `xs`.
Dette tilsvarer mengekomprehensjon som de kanskje har sett i matematikken,
$\{ f(x) | x\in X\}$.

:::{admonition} Oppgåve
Lag ei ny kodecelle med ein `print`-instruksjon for å sjå
kva `ys` er lik.  Verker tala rimelege?
:::


:::{admonition} Oppgåve
Plottet over er kanskje litt grovkorna.
Kan du auka talet på punkt ved å endra definisjonen på `xs`?

Kor mange $x$-verdiar treng du for å få eit pent plott?
:::

:::{admonition} Oppgåve
Slå opp [dokumentasjonen på plot-funksjonen](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html) 
og sjå om du kan endra farge på kurva og setja namn på aksane.
Kva synest du trengst for å gjera grafen presentabel?
::: 

:::{admonition} Oppgåve
Bruk døma over og lag eit plott over estimert folketal på Island over dei neste åtte åra.
:::

## Opprydding

::: {admonition} Oppgåve
Når me arbeider med fleire program, er det lett å rota bort filene sine. 
Ta deg difor litt tid etter øvinga til å laga eit system for arbeidsfilene
dine frå kurset, og samla alle filene som du har brukt på ein plass.
:::

Eit par råd frå korleis eg gjer det,

1.  Når du lagar nye filer, heiter dei *Untitled*, og ein har raskt mange slike
    filer.  Gjer det til ei vane å byta namn på filene so snart som råd.-
    Du kan m.a. gjera det med høgreklikk på fanehodet i *Jupyter Lab*
2.  Lag deg ein prosjektkatalog (mappe) for kurset, med ein underkatalog for
    opningssamlinga.  Samla materialet der.
3.  Filnavigatøren i *Jupyter lab* fungerer høveleg godt både til å laga katalogar,
    flytta filer og namna om filer.  Bruk høgreklikk.
4.  Dersom du allereie har gode vaner for å halda orden på filene dine, so er der
    ingen grunn for å endra dei for dette kurset.

## Nyttig?

Døma over er sjølvsagt enkle, men me må kunna krabba før me lærer å gå.

Me vert heller ikkje særleg flinke til å gå ved å få det forklart.
Den einast måten ein vert god på, er å prøva seg fram
og gå der ein har lyst til.

Over har me vist eit ganske breidt utval av ganske enkle operasjonar.
Etter kvart skal me koma tilbake til fleire detaljar, 
men de må for all del spørja kva gong de snublar.

## Meir stoff 

+ [Kjapt cheat sheet til hvordan skrive markdown](https://www.markdownguide.org/cheat-sheet),
+ [en litt større tutorial med mattetriksene til Latex](https://ashki23.github.io/markdown-latex.html)

```{video} https://www.youtube.com/watch?v=uVLzL5E-YBM
```
