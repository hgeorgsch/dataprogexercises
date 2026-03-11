---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  language: python
  name: dataprog
  display_name: dataprog
---

# Konvertering mellom scikitlearn og pandas

I øvinga [](Linear%20Regression%20in%20SciKitLearn) brukte
me berre SciKitLearn.  Her skal me ta for oss det same
datasettet, men studera det i pandas.

+++

## Datasettet

Me hentar datasettet som før.  Denne koden er kopiert frå 
[den forrige øvinga](Linear%20Regression%20in%20SciKitLearn).

```{code-cell} ipython3
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
```

Me hugsar kanskje at me 442 rader.  Den avhengige variabelen finst
it `target`-feltet, medan `data` har ti uavhengige variablar (søyler).

```{code-cell} ipython3
print(diabetes.data.shape)
print(diabetes.target.shape)
```

::: {admonition} Refleksjon
Hugsar du korleis datasettet ser ut?
Du må gjerna leggja til ein kodeblokk for å skriva ut utsnitt.
:::

Før me går vidare, importerer me dei biblioteka som me treng.

```{code-cell} ipython3
import numpy as np
import pandas as pd
```

+++

## Fyrste konvertering

I `numpy` er der funksjonar for å setja saman fleire matriser til ei større matrise:
`hstack` gjer det horisontalt og `vstack` vertikalt.
Det kan t.d. sjå slik ut
```python
data = np.hstack( [ diabetes.target, diabetes.data ] )
```

::: {admonition} Oppgåve
Lag ein kodeblokk og køyr kodelina over.  Kva skjer?

Kva tyder feilmeldinga?
:::

I `numpy` må me skilja mellom ein vektor eller ein-dimensjonal *array*,
ein to-dimensjonal *array* med éi søyle, og ein to-dimensjonal *array* med
ein rad, sjølv om gjerne tenkjer på alle tre som vektorar.
Difor må me transformera `diabetes.target` til éi søyle.

```{code-cell} ipython3
target = diabetes.target.copy()
print( target.shape )
```

Her ser me at `target` berre har uttrekking i éin dimensjon.

```{code-cell} ipython3
target.shape = (442,1)
print( target.shape )
```

No har me utstrekking i to dimensjonar.    Det kan me òg sjå slik.

```{code-cell} ipython3
print( target )
```

::: {admonition} Merknad
Teknikken over er eit *hack*, men han illustrerer eit poeng.
Tala i matrisa er lagra berre som éi rekkje med tal.
Det er `shape`-attributten som fortel `numpy` korleis serien skal 
delast opp i radar og søyler, og denne attributten kan me endra som
me vil.
:::

::: {admonition} Merknad
Me kan òg definera `target` slik:
```
target = diabetes.target[:,np.newaxis]
```
Her indekserer me, fyrst alle element i den fyrste dimensjonen med `:`, og
deretter ein ny dimensjon som vert oppretta med `np.newaxis`.
:::

No er både `target` og `diabetes.data` to-dimensjonale *arrays* med 442 radar.
Me kan setja dei saman slik:

```{code-cell} ipython3
data = np.hstack( [ target, diabetes.data ] )
print( data )
```

::: {admonition} Oppgåve
Konverter `data` til ein `DataFrame` og skriv han ut med `display`.
Sjå [](./numpy) om du ikkje hugsar korleis.
:::

+++

## Søyleindeks

```{code-cell} ipython3
df = pd.DataFrame( data )
display( df )
```

No har du sannsynlegvis ein `DataFrame` utan søyleoverskrifter.
Det kan me fiksa ved å setja `columns`, slik
```
df.columns = [ "col1", "col2", ... ]
```

Du hugsar kanskje at når me skreiv ut innhaldet i `diabetes`-objektet, 
so såg me ein `feature_names`-attributtet.  Det er namna på ut-variablane
i  `data`.
I tillegg må me ha eit namn på den fyrste søyla, med `target`.

::: {admonition} Oppgåve
Bruk koden over til å endra søylenamn og skriv ut `df` igjen.
Ser søylene bra ut?
:::

+++

## Avrunding

::: {admonition} Oppgåve
Lag eit *scatter-plot* som samanliknar målvariabele (`target`) med BMI.
Er der samanheng?
:::

::: {admonition} Oppgåve
Plott ein eller fleire andre søyler mot målvariabelen.  Ser du samanhengar?
:::

::: {admonition} Refleksjonsspørsmål
Er der andre funksjonar frå *pandas* som du kunne ha brukt for å kasta ljos over
datasettet?
:::
