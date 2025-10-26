---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  name: dataprog
  language: python
  display_name: dataprog
---

# Lineær Regresjon i scikit-learn

*Scikit-learn* (`sklearn`) er eit populært bibliotek både for maskinlæring og
konvensjonell statistikk.  Mange populære datasett er inkludert
i biblioteket, til testing og utprøving, og her skal me bruka eitt 
av dei, nemleg eit for prediksjon av utvikling av diabetes.
Detaljane står i 
[dokumentasjonen på datasettet](https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset).


::: {hint}
Når me finn datasett skal me vera merksame på kvar dei kjem frå og
med kva hensikt dei er gjort tilgjengeleg.  Data i dette kurset kan
me grovt dela i vitskaplege og teknologiske data.

Vitskaplege data er empiriske data som er samla og røkta for å la
oss seia noko om røynda.
[Statistisk Sentralbyrå](https://www.ssb.no/) og
[EuroStat](https://ec.europa.eu/eurostat) publiserer slike data.
Ein kan òg få børsdata, men dei er ikkje alltid gratis.

Teknologiske data er røkta for å testa maskinlæringsmodellar,
statistiske metodar og programvare. Slike data kan vera empiriske,
men dei kan òg vera syntetisk generert for å likna empiriske datasett.
Det kan vera viktig når empiriske data er sensitive.
Empiriske datasett kan òg vera forenkla for å vera enklare å bruka og
for å testa spesifikke teknikkar.

I denne øvinga bruker me eit slikt teknologisk datasett.
Andre populære kjelder til slike datasett er
[Kaggle](https://www.kaggle.com/) og [UC Irvine](https://archive.ics.uci.edu/).
:::

+++

## Rettleidd læring

Den teknikken som me skal bruka her er kjend i maskinlæring som
rettleidd læring eller *supevised learning*.
Me har eit datasett der kvart individ eller objekt har nokre eigenskapar $x$
som er enkle å observera og nokre eigenskapar $y$ som er vanskelegare.
Me ynskjer å laga ein *prediksjonsmodell* som let oss predikera $y$ ved
hjelp av $x$.

I rettleidd læring føreset me eit datasett der både $x$ og $y$ er kjende
for ei rekkje individ. 
Merk at både $x$ og $y$ kan innehalda éin eller fleire variablar.

::: {admonition} Definisjon
Ein **modell** i maskinlæring og statistikk er ein matematisk funksjon
$M(x) = y$.  Når me reknar ut $M(x)$ seier me gjerne at me predikerer $y$.

Når me **trener** ein modell bruker me eit datasett med mange par $(x,y)$
til å tilpassa koeffisientane (ofte kalt *vektene*) i modellen, slik
at prediksjonane vert best mogleg.

Når me **testar** modellen bruker me òg eit datasett med par$(x,y)$.
For kvar $x$ finn me $\hat y=M(x)$ og samanliknar prediksjonen $\hat y$
med den sanne verdien $y$ for å sjå kor god prediksjonen er.
:::

I *praktisk bruk* observerer me berre $x$, og den einaste måten me kan
finna $y$ på, er å bruka prediksjonen $\hat y=M(x)$ frå modellen i
staden.

For å få ein påliteleg test av modellen, er det viktig at testdatasettet
er uavhengig av treningsdatasettet.  Ein modell som gjer det godt på
treningssettet treng ikkje generalisera til andre data.

Desse prinsippa er dei same for klassiske teknikkar som lineær regresjon
og for nevrale nettverk og andre moderne maskinlæringsalgoritmar.
Biblioteket `sklearn` er generisk og støtter heile spekteret av modellar.
I denne øvinga bruker me lineær regresjon.


+++

## Datasettet

For å lasta datasettet importerer me `sklearn` og bruker biblioteket.
Datasettet som me vil bruka er publisert som ein del av `sklearn` for
testformål.

```{code-cell} ipython3
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
display(diabetes)
```

::: {admonition} Oppgåve
Kva datatype er `diabetes`?
:::

::: {admonition} Refleksjon
Kva delar av `diabetes`-objektet er interessante for analyse?
:::

Dette datasettet er førebudd spesielt for testing av regresjonsmodellar.
Difor skil det mellom *input* eller `data`, og den variabelen som ein
skal freista å predikera, *target*.

```{code-cell} ipython3
print(diabetes.data.shape)
print(diabetes.target.shape)
```

Det er alltid nyttig å sjå på dimensjonane på datasett.
Her har med 442 rader, same for `data` og `target`.
Der er ti inn-variablar i `data` og éin ut-variabel i `target`.
Om me ser på eit par liner i toppen av kvar matrise, ser me at alt
er tal.

```{code-cell} ipython3
print(diabetes.target[:3])
print(diabetes.data[:3,:])
```

::: {hint}
Datatypen åt `diabetes.data` og `diabetes.target` er `numpy` *array*.
Sjå [numpy](./numpy.ipynb)-øvinga for meir informasjon.
:::

::: {admonition} Merknad
Datasettet er skalert og normalisert.  Det har ein del føremonar for
algoritmane, men for å kunne tolka data må me då finna ut korleis
dei er skalert for å konvertera dei til kjende einingar.  
Det kan vera at ein kan finna denne informasjonen i dokumentasjonen
og andre kjelder som har utvikla datasettet, men det tek me oss ikkje
tid til.
:::

## Visualisering med spreidingsplott

::: {admonition} Oppgåve
Datastrukturen `diabetes` inneheld og ei beskriving, som `diabetes.DESCR`.
For å sjå beskrivinga, er det best å bruka `print` eller `display`.

Kva tyder dei ulike søylene?
:::


Normalt bruker ein fleire *input*-variablar i modellen, men for å
kunna visualisera han pent i 2D, skal me berre bruke éin.
T.d. kan me ta ut den tredje søyla.

```{code-cell} ipython3
import numpy as np
x = diabetes.data[:,2:3]
print(x.shape)
y = diabetes.target
print(y.shape)
```

::: {admonition} Oppgåve
Kva er skilnaden på `diabetes.data[:,2:3]` og `diabetes.data[:,2]`?  
Du kan sjekka ved å endra på koden?
:::

Merk at `x` må vera ei to-dimensjonal matrise når me går vidare,
sjølv om ho berre har éi søyle.

Før me går vidare, er det greitt å visualisera, so me ser kva
me arbeider med.

```{code-cell} ipython3
import matplotlib.pyplot as plt

ax = plt.subplot()
scatter = ax.scatter( x, y )
ax.set(xlabel="$x$", ylabel="$y$")
```

::: {admonition} Refleksjon
Kva fortel plottet deg?

Variablane her er hhv. BMI ($x$) og sjukdomsutvikling ($y$).
Er der samanheng mellom dei to?  Trur du BMI er ein god predikator
aleine?
:::

::: {admonition} Merknad
I aksenamna brukte me notasjonen `$x$` og `$y$`.  
Det er $\LaTeX$-notasjon som gjerne kan brukast til
matematiske symbol både i matplotlib og markdown.
:::

+++

## Prediksjonsmodell

Det fyrste me må gjera i `sklearn` er å instantiera ein modell.

```{code-cell} ipython3
from sklearn import linear_model
reg = linear_model.LinearRegression()
```

Desse kodelinene lagar ein lineær regresjonsmodell, men me har ikkje
tilpassa vektene, so modellen representerer ingenting og evt. 
prediksjonar vil vera vilårlege.
For å tilpassa vektene til datasettet vårt, bruker me `fit()`-metoden.

```{code-cell} ipython3
reg.fit(x,y)
```

No har me ein modell av datasettet, og alt er klart for å gjera
prediksjonar.
Lat oss sjå for oss at me observerer ein person med $x=0{,}1$. 
Me kan predikera $y$ slik.

```{code-cell} ipython3
print( reg.predict([[0.1]]) )
```

::: {admonition} Refleksjon
Samanlikna denne prediksjonen med spreidingsplottet over.
Verker prediksjonen sannsynleg?
:::

::: {admonition} Merknad
Innparametern til `predict` er ein 2D-struktur, anten ein numpy-*array* eller her 
ei liste av lister.  Grunnen er at `predict` kan predikare for mange $x$-verdiar
(rader) samstundes, i tillegg til at der vanligvis er fleire inn-variablar
(søyler).
:::

Me kan plotta prediksjonsmodellen ved å predikera nokre verdier, slik:

```{code-cell} ipython3
ax = plt.subplot()
scatter = ax.scatter( x, y )
ax.set(xlabel="$x$", ylabel="$y$")

xv = [ -0.1, 0, 0.1, 0.15 ]
yv = [ f(x) for x in xv ]
ax.plot( xv, yv, "r:" )
```

::: {admonition} Refleksjon
Er prediksjonsmodellen ein rimeleg modell av datasettet?
:::

## Under panseret

For dei som kjenner matematikken i lineær regresjon er det nyttig å ta
ein titt under panseret.
Den lineære regresjonsmodellen er likninga
$$\hat y = ax + b.$$
Det er altso dei to koeffisientane $a$ og $b$ som vert bestemte
av `fit()`-metoden.
Me kan lesa desse koeffisientane ut av modellen.

```{code-cell} ipython3
print(reg.coef_)
print(reg.intercept_)
```

Konstantleddet $b$ vert kalt *intercept*, medan stigningstalet $a$ er
den eigentlege koeffisienten.
Koeffisienten er ei matrise fordi ein lineær modell treng éi vekt per *input*-variabel.
Vanligvis vil matrisa ha meir enn eitt element.
Me kan definera regresjonslikninga $f(x) = ax+b$ som ein python-funksjon, slik:

```{code-cell} ipython3
a = reg.coef_.flatten()[0]
b = reg.intercept_
def f(x): return a*x + b
```

Me har brukt `flatten()` for å flata ut matrisa og henta det eine elementet ho
inneheldt.

I teoren skal denne funksjonen `f()` gjera akkurat det same som `reg.predict()`.

::: {admonition} Oppgåve
Lag eit plott som samanliknar prediksjonane frå `f` og `reg.predict`.
Er dei alltid like?
:::


## Oppsummering

Læringsmålet i denne øvinga har vore å sjå ein mogleg syntaks
for lineær regresjon i python.

Me har vald scikit-learn her fordi det er eit utbreidd val for
trening og testing av maskinlæringsmodellar, og ein kan bruka
mange ulike algoritmar i det same rammeverket og med den same
syntaksen.

Det er ikkje det beste valet for statistikk, der ein gjerne
vil analysera dei einskilde parametrane i modellen.
Då kan ein anten sjå etter andre bibliotek, eller implementera
dei matematiske formlane sjølv.

Dømet er basert på ein post frå
[Medium](https://medium.com/@heyamit10/how-to-perform-linear-regression-using-pandas-scikit-learn-9fcfa6085fb0)

