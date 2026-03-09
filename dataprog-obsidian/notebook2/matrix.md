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

# Lineær algebra i numpy

Hovudhensikta med `numpy` er matriserekning, so me kan sjå eit lite
døme.
Ikkje ver redd for å hoppa over dette avsnittet om matematikken vert for tung.
Eg tek det med for å gje litt meir samanheng til dei som har eit forhold til
matriser frå før.

## Aritmetikken

Lat oss definera to matriser, fyrst ein ganske enkel `A`:

```{code-cell} ipython3
import matplotlib.pyplot as plt
import numpy as np
A = np.array( [
   [ 1.0, 1.0 ],
   [ 0, 1.0 ]
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

::: {admonition} Refleksjonsspørsmål

Kva representerer verdien åt `theta`?
:::

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

## Rotasjonsmatrisa

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


## Avslutting

Matriserekning er sjølve grunnsteinen i svært mange rekneproblem,
inkl. 3D-grafikk og maskinlæring.  
Grafikkprosessorane (GPU) er utvikla spesielt for matriserekning.
I dei fleste standardoppgåver er dette bakt inn i større operasjonar
i bibliotek som `torch`, og me treng ikkje tenkja på det.
Matrisemultiplikasjon og dei andre teknikkane over treng me fyrst når 
me utviklar våre eigne matematiske modellar.
