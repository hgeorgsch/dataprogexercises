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
vert radar i *array*en.

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
og konverter innhladet til ein `numpy` *array*.
Kva datatype vert resultatet?
:::

::: {admonition} Oppgåve
Sannsynlegvis fekk du ikkje ein numerisk *array* i forrige oppgåve.
Formatter datasettet slik at alle søylene er talverdiar og lag
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

+++

## Litt lineær algebra

Hovudhensikta med `numpy` er matriserekning, so me kan sjå eit lite
døme.
Ikkje ver redd for å hoppa over dette avsnittet om matematikken vert for tung.
Eg tek det med for å gje litt meir samanheng til dei som har eit forhold til
matriser frå før.

Lat oss definera to matriser, fyrst ein ganske enkel `A`:

```{code-cell} ipython3
import matplotlib.pyplot as plt
A = np.array( [
   [ 1.0, 1.0 ],
   [ 0, 1.0 ],
   ] )
print(A)
```

I den andre matrisa skal me bruka trigonometriske funksjonar,
Grunnen er at me etterpå skal bruka ho som ei rotasjonsmatrise,
men det kjem me tilbake til.

```{code-cell} ipython3
theta = np.pi/3
print( theta )
R = np.array( [
   [ np.cos(theta), -np.sin(theta) ],
   [ np.sin(theta), np.cos(theta) ],
   ] )
print(R)
```

Me har grunnleggjande aritmetikk på matriser, t.d. pluss og minus.

```{code-cell} ipython3
print("Pluss:\n",A+R)
print("Minus:\n",A-R)
```

Multiplikasjon er meir komplisert

```{code-cell} ipython3
print("Med *:\n",A * R)
print("Medd @:\n",A @ R)
```

Gangeteiknet multipliserer element for element, slik at elementet øvst til høgre i produktet er produktet av dei to elementa øvst til høgre i `A` og `R`. Dette er ikkje matrisemultiplikasjon, slik det er definert i matematikken.  Matrisemultiplikasjon skriv me med `@`.

Me skal ikkje bruka tid på å forklara aritmetikken, men me skal gje eit raskt døme på ein viktig bruk av matrisemultiplikasjon.  Fyrst legg merke til at `theta` vart definert som $\pi/3$ som (i radianar) svarer til ein vinkel på 60°.  Matrisa `R` definerer ein rotasjon på 60°.  For å sjå dette må me sjå for oss `A` som ei liste med to punkt i 2D.  Lat oss seia at me lèt radane definere punkt.

Me kan indeksera radar og element i matriser omtrent som me indekserer lister.

```{code-cell} ipython3
print( A[0,:] )
print( A[1,:] )
```

Når me skriv `A[0,:]` får me den nullte raden og alle søylene (`:`).
Cella over skriv altso ut dei to punkta våre.

Me kan plotta desse to punkta med matplotlib.

```{code-cell} ipython3
plt.plot( A[:,0], A[:,1], "rx" )
plt.xlim( -1.2, +1.2 )
plt.ylim( -1.2, +1.2 )
plt.xticks( [ -1, 0, +1 ] )
plt.yticks( [ -1, 0, +1 ] )
```

::: {hint}
Her har eg brukt `xlim`, `ylim`, `xticks` og `yticks` for å få
kontroll med kva område aksene viser.  Om du lurer på korleis
dei verkar, so kan du byta ut tala og sjå kva som skjer.
:::

::: {admonition} Refleksjonsspørsmål
I `plot`-lina trekk eg ut søylene frå matrisa (t.d. `A[:,1]`).
Kvifor gjer eg det?  Kva tyder dei to fyrste argumenta til `plot`?
:::

No kan me sjå kva rotasjonsmatrisa gjer når me gangar på høgre side.
```{code-cell} ipython3
B = A @ R
plt.plot( A[:,0], A[:,1], "rx" )
plt.plot( B[:,0], B[:,1], "b+" )
plt.xlim( -1.6, +1.6 )
plt.ylim( -1.6, +1.6 )
plt.grid()
```

Her har me plotta radane i `B=A@B` saman med radane i `A`.
Dvs. at kvar rad i `B` er resultatet av ein rad frå `A` gonga med `R`.
Om du ser i figuren ser me at eitt blått punkt er resultatet av å
rotera eit raudt punkt 60° om origo.  
Dvs. du finn eit raudt og eit blått punkt med same avstand til origo,
og dersom du dreg liner frå origo til kvart punkt, er vinkelen mellom dei
60°.

::: {admonition} Oppgåve
Utvid `A` med fleire punkt og rotér dei. Ser det riktig ut i figuren?
:::

::: {admonition} Oppgåve
Definer andre rotasjonsmatriser ved å endra `theta`.  Korleis verkar
dei på punkta i `A`?
:::

