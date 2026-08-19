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

# numpy-biblioteket

Pandas er eit ypperleg bibliotek til å sortera og formattera data,
men det er ikkje like godt egna til å rekna på data.
Når me skal gå vidare med prediksjons- og klassifikasjonsmodellar,
vil me bruka SciKitLearn som byggjer på `numpy`.

::: {admonition} Merknad
Målet med denne innføringa er å kjenna igjen `numpy`-objekta som
dukkar opp når me bruker SciKitLearn, og å kunna konvertera
datasett mellom SciKitLearn og pandas.
Dei som vil arbeida med meir avanserte matematiske modellar i python,
vil måtte læra seg mykje meir om `numpy` og matriserekning.
:::

Hovudhensikta i `numpy` er matriserekning.  Dei som har lese litt
matematikk veit at ein matrise er eit todimensjonalt system med
talverdiar, t.d.

$$A = 
\begin{bmatrix}
   1{,}0 & 2{,}4 & 5{,}5 & 6{,}1 \\
   0 & 2{,}0 & 1{,}0 & 2{,}1 \\
   1{,}2 & 0 & 0 & 1{,}2 \\
\end{bmatrix}$$
I `numpy` kalles dette normalt for ein *array*.

```{code-cell} ipython3
import numpy as np
A = np.array( [
   [ 1.0, 2.4, 5.5, 6.1 ],
   [ 0, 2.0, 1.0, 2.1 ],
   [ 1.2, 0, 0, 1.2 ]
   ] )
print("Verdi:\n", A)
print("Type:", type(A))
```

Her vert *array*en definert ved ei liste av lister, der dei indre listene
vert radar i *array*en.  Denne lista av lister vert mata inn til 
konstruktøren når me instantierer *array*-objektet.

Dersom du har litt matematikkbakgrunn og er interessert i korleis  `numpy`
fungerer heilt generelt, kan du ta ein titt på øvinga [](./matrix).

## Matriser og *DataFrame*

Den største skilnaden mellom ein *DataFrame* i pandas og ein *array*
i `numpy`, er at i ein *array* må alle elementa (tala) ha same type.
I ein *DataFrame* har søylene ofte ulik type.
Dette høyrest ut som ei stor ulempe for numpy, men det gjer det enklare
og raskare å rekna på heile datasettet.
Det er difor me treng *arrays*.

Me kan sjå den kva datatype elementa har i `dtype`-attributten, slik:

```{code-cell} ipython3
print(A.dtype)
```

Ein *array* kan lesast inn i ein ny *DataFrame* utan vidare.

```{code-cell} ipython3
import pandas as pd
df = pd.DataFrame(A)
display(df)
```

Me ser raskt at datainnhaldet er det same.
Det som kanskje er uvant er at søylene ikkje har overskrifter, 
slik som me er vane med.
Ein *array* har ingen overskrifter eller *labels*.

Det går an å definera søyleoverskrifter når me definerer ein *DataFrame*.

```{code-cell} ipython3
df2 = pd.DataFrame(A, columns=['ColA', 'ColB', 'ColC', 'ColD'])
display(df2)
```

For å visa konvertering motsett veg, kan me raskt definera ein enkel
*DateFrame*, slik:

```{code-cell} ipython3
data = {'ColA': [10, 20, 30], 'ColB': [11, 21, 31]}
df3 = pd.DataFrame(data)
display(df3)
```

Konvertering til `numpy` *array* ser då slik ut:

```{code-cell} ipython3
B = df3.to_numpy()
print(B)
print(f"Type: {type(B)}")
print(f"Elementtype: {B.dtype}")
```

Det er mogleg å ha teiknstrengar i `numpy` *arrays*, men då vert elementtypa `object`, og ingenting vert kjent igjen som tal.
Me kan raskt testa dette òg.

```{code-cell} ipython3
dd = {'ColA': [ "a", "b", "c"], 'ColB': [11, 21, 31]}
df4 = pd.DataFrame(dd)
C = df4.to_numpy()
print(C)
print("Type:", C.dtype)
```

::: {admonition} Oppgåve
Last inn eitt av datasetta som du har arbeidd med tidlegare i pandas,
og konverter innhaldet til ein `numpy` *array*.
Kva datatype vert resultatet?
:::

::: {admonition} Oppgåve
Sannsynlegvis fekk du ikkje ein numerisk *array* i forrige oppgåve.
Formater datasettet slik at alle søylene er talverdiar og lag
ein *array* av dette resultatet.
Kva datatypar får du no?
:::

Ta vare på resultata dine på desse oppgåvene.  Du treng dei når du seinare skal sjå på datasetta i SciKitLearn.

::: {hint}
For å formattera datasettet kan du anten ta eit utsnitt ved å indeksera dei
søylene du vil ha med, eller bruka `drop()`-metoden for å fjerna dei du ikkje
vil ha.
I tillegg må du sjå om der er søyler med talverdiar som pandas har tolka som
strengar.
:::

## Avslutting

Det kan verka underleg å bruka tid på `numpy` *arrays*, når `pandas`.
`DataFrame` allereie gjev oss ei ryddig representasjon av datasetta.
Matrisene er ei meir primitiv framstilling.

Det er nettopp fordi det er ein primitiv representasjon at `numpy` er so
ekstremt nyttig.  
Det gjer `numpy` egna til å dela datasett mellom ulike bibliotek som gjer ulike
ting.  `DataFrame` er ei `pandas`-greie, og treng me ein funksjon som `pandas`
ikkje har, må me som regel omsetja datasettet til ein anna datatype.
Her er `numpy` standarden.

