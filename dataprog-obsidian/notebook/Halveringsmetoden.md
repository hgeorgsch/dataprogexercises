---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  name: dataprog
  display_name: dataprog
  language: python
---

# Halveringsmetoden

I mange praktiske problem har me matematiske modellar som er for komplekse til at me kan løysa dei analytisk. Då bruker ein ofte numerisk analyse, der ein reknar ut omtrentlege løysingar for konkrete tal. Grunnlaget for numerisk analyse er programmering. Numeriske metodar er, i alle fall som hovudregel, iterative. Dei startar med ei dårleg gissing, reknar ut kor dårleg ho er, forbetrar gissinga, og gjentek frå start. Mange store matematikarar og tolmodige vitskapsmenn har sjølvsagt gjort dette for hand, men det er repetivt og krev nitidig presisjon. Maskiner gjer det betre. 
Og utan å gå lei.

Her skal me demonstrera ein av dei enklaste numeriske metodane, nemleg halveringsmetoden for likningsløysing. Hensikta med demonstrasjonen er ikkje fyrst og framst å læra denne bestemte teknikken, men å sjå eit praktisk døme på løkker og funksjonar i python, og å sjå prinsippane for iterative metodar.

# Kontrollflyt

Før me går i gang med metoden, lat oss sjå kjapt igjennom dei
grunnleggjande programmeringsteknikkane som me bruker.

Når ei kodeline vert køyrd i programmet, seier me at lina har *kontrollen*. 
Det er ikkje alltid at me ynskjer at kontrollen skal flyta vidare til neste kodeline.
Av og til vil me hoppa over kode avhengig av verdien på ein eller annan variable.

Lat oss definera ein variabel til testen.

```{code-cell} ipython3
testvar = 10
```

## Vilkårssatsen

Alle imperative programmeringsspråk har syntaks for 
*vilkårssatsar*.
I python ser han slik ut.

```{code-cell} ipython3
if testvar <= 0: print( "Ikkje-positivt tal")
else: print ("Positivt tal") 
```

Evt. kan ein ha meir enn to alternativ.

```{code-cell} ipython3
if testvar < 0: print( "Negativt tal")
elif testvar > 0: print ("Positivt tal") 
else: print( "Null" )
```

Me kan bruka vilkårssatsen inni ein funksjon:

```{code-cell} ipython3
def testfun(testvar):
    if testvar < 0: print( testvar, "Negativt tal")
    elif testvar > 0: print (testvar, "Positivt tal") 
    else: print( testvar )
```

```{code-cell} ipython3
testfun(-17)
testfun(3.4)
testfun(0)
```

## Løkke (repetisjon)

Alle imperative språk har òg løkker.  Der finst gjerne fleire variantar.
Den mest kompakte er for-løkka, som ser slik ut.

```{code-cell} ipython3
for i in range(7):
    print( "Repetisjon nr. ", i)
```

I for-løkka er der alltid ein indeksvariabel (`i` i dette tilfellet) som vert definert som ein del av sjølve løkkesyntaksen.
I `while`-løkka er det ikkje tilfellet:

```{code-cell} ipython3
while testvar > 0:
        print( "Repetisjon nr. ", testvar)
        testvar = testvar - 2
```

::: {admonition} Oppgåve
Merk at ``testvar`` har endra verdi.  Kva skjer om du køyrer dei blokkane over
(``if``- og ``while``-satsane) over ein gong til?
:::

+++

# Numerisk likningsløysings

Når me går i gang med likningsløysinga, vil me alltid skriva
likninga på formen $f(x) = 0$ for ein eller annan funksjon $f$.

## Eit enkelt døme

Lat oss sjå på tredjegradsfunksjonen $f(x) = 3x^3 + 10x^2 - 50x - 3$

```{code-cell} ipython3
def f(x): return 3*x**3 + 10*x**2 - 50*x - 3
```

Me kan testa funksjonen ved å plotta:

```{code-cell} ipython3
from matplotlib import pyplot as plt

plt.plot()
x = [ i/20 for i in range(-140,90) ]
y = [f(i) for i in x]
plt.plot(x,y,"-")
```

::: {admonition} Merknad
Notasjonen `[ i/20 for i in range(-140,90) ]` kaller me for 
listekomprehensjon.
Det er ein kjapp metode for å laga lange lister med kort kode.
Me genererer mange element på formen `i/20`, for kvar verdi
av `i` i `range(-140,90)`.
:::

## Halveringsmetoden

Me ser at funksjonen byter forteikn mellom 0 og 1, og sidan 
han er kontinuerleg, må der vera eit nullpunkt der.
Dette er nok til at me kan bruka halveringsmetoden.

Når me har eit intervall, $(0,1)$ i dette tilfellet, der
funksjonen må kryssa $x$-aksen, kan me rett og slett 
halvera intervallet, og finna ut om funksjonen på midtpunktet
(½) ligg over eller under null.  Då set me òg om funksjonen
kryssar $x$-aksen i den høgre eller venstre halvdelen av
intervallet.  Dermed står me att med eit nytt interval som
er halvparten so stort, og me kan gjena same prosess.
Når me har halvert intervallet mange nok gongar har me ei 
god tilnærming for $x$.  Feilen er i alle fall ikkje større
enn breidda på intervallet som står att.

Her er eit grafisk døme på ein anna funksjon.
Du kan klikka deg gjennom steg for steg.

[Lenke til halveringsmetoden grafisk](https://jonajh.folk.ntnu.no/forkurs/halveringsmetoden.html)
<iframe src=https://jonajh.folk.ntnu.no/forkurs/halveringsmetoden.html width=700 height=500>
</iframe>

Der er mange måtar å implementera dette i python.
Her er ein som finn ei løysing på $f(x)=0$ i intervallet $(-2,+2)$..

```{code-cell} ipython3
lower = -2
upper = +2
while abs(lower-upper) > 0.01: 
    midpoint = (lower+upper)/2
    if f(lower)*f(midpoint) < 0:
            upper = midpoint
    elif f(midpoint)*f(upper) < 0:
            lower = midpoint
sol = (lower+upper)/2
print( sol )
```

::: {admonition} Refleksjon
Forklar kva koden gjer steg for steg.
Er dette det same som i den grafiske demoen?
:::

Det er greit å ha ein funksjon som gjer halveringsmetoden på
ein vilkårleg funksjon `f`.
I python er dette uproblematisk.
Funksjonar kan ta andre funksjonar som argument, so me kan setja
heile løkka over inn i ein funksjon med `f`, `upper` og `lower`
som parametrar.

```{code-cell} ipython3
def bisect( f, lower, upper):
    while abs(lower-upper) > 0.01: 
        midpoint = (lower+upper)/2
        if f(lower)*f(midpoint) < 0:
            upper = midpoint
        elif f(midpoint)*f(upper) < 0:
            lower = midpoint
    return (lower+upper)/2
print( bisect(f,-2,2) )
```

::: {admonition} Refleksjon
Samanlikna `bisect()`-funksjonen med den frittstande løkka.
Er der nokon skilnad?
:::


::: {admonition} Refleksjon
Kva er den største moglege feilen i løysinga som `bisect()` returnerer?

Dvs;
sett `bisect()` returneret $\hat x$ medan den sanne verdien er $\bar x$.
Kva er den største moglege verdien på feilen $|\hat x-\bar x|$?
:::


::: {admonition} Oppgåve
Tredjegradsfunksjonen vår kryssar $x$-aksen fleire gongar.
Finn dei to andre nullpunkta på same måte.
:::

+++

## Forenkling av implementasjonen

Legg merke til at ``bisect`` reknar ut ``f(midpoint)`` to gongar.
Her er det ikkje noko problem, men dersom det tek tid å rekna ut $f$ er det bortkasta arbeid.
Det kan difor løna seg å endra funksjonen slik:

```{code-cell} ipython3
def bisect2(f,lower,upper):
    while abs(lower-upper) > 0.01: 
        midpoint = (lower+upper)/2
        fm = f(midpoint)
        if f(lower)*fm < 0: upper = midpoint
        elif fm*f(upper) < 0: lower = midpoint
    return (lower+upper)/2
print(bisect2(f,-2,2))
```

## Utviklinga gjennom algoritmen

Det er nyttig å sjå korleis estimatet utviklar seg steg for steg i algoritmen.
I dømet under samlar me opp alle estimata i ei liste `r`.

```{code-cell} ipython3
def bisect2log(function,lower,upper):
    r = []
    while abs(lower-upper) > 0.001: 
        midpoint = (lower+upper)/2
        fm = f(midpoint)
        if f(lower)*fm < 0: upper = midpoint
        elif fm*f(upper) < 0: lower = midpoint
        r += [midpoint]
    midpoint = (lower+upper)/2
    return r
xs = bisect2log(f,-2,2)
print(xs)
```

Merk at det siste talet i lista er det same estimatet som me har fått tidlegare.
Skilnaden er at me no veit alle estimata på vegen.
Dette kan me plotta:

```{code-cell} ipython3
n = len(xs)
x = range(n)
plt.plot(x,xs,"+-")
```

::: {admonition} Oppgåve
1. Korleis kan du auka presisjonen i halveringsmetoden, og få fleire riktige desimalar i svaret?
1. Gå vidare til dokumentet om Sekantmetoden.  Det er ein raskara algoritme i dei fleste tilfelle. Dokumentet gjev hovudstega, men du må fullføra algoritmen vha. idéane som me har presentert her.
:::

+++

## Oppsummering

Det viktigaste i dette dømet er 
1. Vilkårssatsen
1. Løkker
1. Algoritmen for halveringsmetoden.
