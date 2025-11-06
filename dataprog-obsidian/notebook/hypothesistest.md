---
jupytext:
  cell_metadata_filter: -all
  formats: ipynb,md:myst,py:percent
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Plots for Evaluation and Hypothesis Testing

This script creates plot for the slides for one of the talks.
It is made available as examples and as a source of ideas, to
to showcase the constructions I use.

Sorry for the lanague mix; this is quick and dirty work.

```{code-cell}
import numpy as np
import matplotlib.pyplot as plt
```

We use `numpy` and `pyplot` as usual.
We also need the statistics package from `scipy`, but only
the binomial distribution, which is called `binom`.

```{code-cell}
from scipy.stats import binom
```

## One experiment 

Imagine that we make one experiment to test a classification model.
In the experiment, we make a number of trials, say $n=50$, and
for each trial we record either an error or a correct prediction.
The result of the experiment is the number $X$ of observed errors.

Since the experiment depends on random events, $X$ is a stochastic
(that is random) variable.
we want to understand how this variable is distributed under different
True error rates $p_e$.

We assume a particular error rate, say $p_e=0.1$, and try to model
probability distribution of $X$.

We define the constants $n$ and $p_e$ as suggested above.

```{code-cell}
n = 50
pe = 0.1
```

Feiltalet $X$ vil vera binomialfordelt.  Me treng ikkje gå inn på kva det
tyder, men om du har lese statistikk, kjenner du kanskje omgrepet.
Me definerer denne fordelinga, med parametra våre.

```{code-cell}
dist = binom(n,pe)
```

Denne variabelen er eit objekt med metodar som for å finna sannsynsfordelinga
og andre eigenskapar ved fordelinga.

Me vil fyrst plotta sannsynsfordelinga eller PMF (*Probability Mass Function*).
Lat oss plotta for $x$-verdiar opp til 20 feil.

```{code-cell}
x = range(20)
y = dist.pmf(x)
```

Her er $y$-verdiane rekna us som sannsynstettheiten frå `dist`-objektet vårt,
og me kan plotta `y`, slik.

```{code-cell}
plt.plot(x, y, color="blue", label=f'$n={n}$')
plt.xlabel('Feiltal')
plt.ylabel('Sannsyn')
plt.xticks(range(0,20,2))
plt.grid(True)
plt.savefig( "hyp0.svg" )
```

Ikkje overraskande ser me at det mest sannsynlege er rundt fem feil, som svarer
til 10% ($p_e$) av $50$ ($n$).
Det som er verd å merka seg er at det ikkje er usannsynleg å få to eller færre feil.
Me kan rekna ut dette kjapt med CDF-funksjonen (*Cummulative Density Function*)

```{code-cell}
dist.cdf(2)
```

Me har altso 11% sannsyn for to eller færre feil.  Det er altso ikkje usannsynleg at
om testen viser 4% feil, er likevel *sannsynlegheita* for feil meir enn 10%.

+++

## Hypothesis testing

Hypotesetesting er ein av dei sentrale teknikkane statistikken.  Når me har trent
ein modell, vil me gjerne testa hypotesen at *modellen er god nok*.
For å kunna bruka statistikk må me kvantifisera «god nok».
F.eks. kan me freista å testa om feilraten er mindre enn 10%.
Då definerer me den sokalla alternativhypotesen
$$H_1: p_e < 0.1$$

Hypotesetesting verkar derimot nesten alltid omvendt.
Me må definera ein hypotese som me ynskjer å avvisa, ikkje $H_1$ som
me ynskjer å stadfesta.  Her kan me bruka
$$H_0: p_e = 0.1$$
Dette er den sokalla nullhypotesen.
Det som er kritisk er at me har ei kjend sannsynsfordeling under $H_0$.
Det har me her, fordi $p_e$ har ein bestemt verdi.

Testen verkar slik at me føreset at $H_0$ er sann, og forkastar hypotesen dersom 
me observererer eit usannsynleg resultat i eksperimentet.  
Då kan me akseptera $H_1$ i staden.  Om me ikkje kan forkasta $H_0$, tyder ikkje
det at $H_0$ er sann og $H_1$ usann.  Dét tyder berre at me ikkje har nok prov
til å konkludera.

Før me gjer testen må me bestemma oss for kor usannsynleg resultatet må vera for
å forkasta nullhypotesen.  Dette kaller me for *signifikansnivået*.
T.d. kan me velja eit signifikansnivå på 5%, som vil seia at me forkastar $H_0$
dersom sannsynlegheita var høgst 5% for å få det observerte resultatet *eller*
noko mindre sannsynleg.

Me kan finna terskelverdien med `ppf()`-funksjonen, slik:

```{code-cell}
sig = 0.05
c0 = dist.ppf(sig)
print( c0, n, pe )
```

Dette fortel oss at sannsynet for å få $X<2$ feil er mindre enn 5%.
Dette er litt forvirrande fordi $X$ er diskret; der finst ikkje halve feil.
Me hugsar at sannsynet for $X\le2$ var 11%, men strengt mindre enn to vert
høgst éin, og sannsynet for anten null eller éin er under 5%.

Med dette signifikansnivået kan me altso berre forkasta nullhypotesen når
me observerer null eller éin feil.
Me kan visualisera dette i plottet vårt.

```{code-cell}
plt.figure()
c1 = int(c0)
plt.plot(x, y, color="blue", label=f'$n={n}$')
plt.fill_between(x[:c1], y[:c1], color="lightblue", alpha=0.5) 
plt.xlabel('Feiltal')
plt.ylabel('PDF')
plt.xticks(range(0,20,2))
plt.grid(True)
plt.savefig( "hyp1.svg" )
```

Det lyseblå området svarer til 5% (`sig`) sannsyn.  Me kan forkasta
nullhypotesen dersom me observerer eit feiltal i dette området.

::: {admonition} Merknad
Merk at feiltal $X\ge10$ òg er usannsynleg, men det ville tyda på
ein *dårlegare* modell.  Dersom me ynskte å visa $p_e\neq0{,}1$
kunne me ha delt det lyseblå området i to, og brukt litt på store
og litt på små feiltal.  Det ville ha vore ein tosidig test.
Testen vår er éinsidig; me forkastar berre $H_0$ på den eine sida
av forventingsverdien.
:::

Legg merke til at dersom faktisk feilsannsyn er nesten 5%, er det ganske
usannsynleg at me klarer å forkasta $H_0$.  Hypotesetesting er formulert
slil at me berre konkluderer når me har gode marginar.

Me kan bøta på dette problemet ved å å gjera fleire testar.

Lat oss fyrst definera ein funksjon for å teikna plottet.

```{code-cell}
def mkplot(fig,n,pe,sig,colour="blue"):
   dist = binom(n,pe)

   m = int(n*pe*2)
   x0 = list(range(m))
   y0 = dist.pmf(x0)
   y1 = y0*n
   x1 = np.array(x0)/n

   c0 = dist.ppf(sig)
   p0 = dist.ppf(sig)/n
   c1 = round(c0+1)
   print( c0, p0 )

   fig.plot(x1, y1, color=colour, label=f'$n={n}$')
   fig.fill_between(x1[:c1], y1[:c1], color=colour, alpha=0.15) 
```


::: {admonition} Merknad
Me har skalert $x$ og $y$ med en faktor på $n$, slik at me får feilratar
(mellom 0 og 1) i staden for feiltal (mellom 0 og $n$).
:::

Me denne funksjonen kan me raskt plotta for ulike verdiar av $n$

```{code-cell}
fig = plt.figure()
ax = fig.gca()
plt.xlabel('Feilrate')
plt.ylabel('PDF')
ax.grid(True)

mkplot( ax, 100, 0.1, 0.05 )
ax.legend()

mkplot( ax, 1000, 0.1, 0.05, colour="red" )
mkplot( ax, 10000, 0.1, 0.05, colour="green" )
ax.legend()
plt.savefig( "hyp2.svg" )
```

Me ser at di større $n$, di meir konsentrert er forventinga rundt 10%.
Dersom $n$ er stor nok, treng feilraten berre å vera litt mindre en 10%
før det er mest sannsynleg at testen klarer å forkasta nullhypotesen.

Det same prinsippet gjeld dersom du søkjer å estimera feilsannsynet $p_e$.
Di større $n$, di mindre usikkert vert estimatet.  Dersom du har lese
statistikk, kan det vera verd å rekna på kor stor $n$ du treng.
