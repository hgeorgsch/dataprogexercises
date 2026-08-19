---
title: Smittespreiing
author: Hans Georg Schaathun
tags:
  - exercise
  - simulering
  - topic/loop
jupytext:
  cell_metadata_filter: -all
  formats: md:myst,ipynb
  root_level_metadata_filter: -title,-author,-tags
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

# Smittespreiing

::: {admonition} Kjelde
Dømet er basert på ein
[artikkel frå NDLA](https://ndla.no/r/biologi-1/smittespredning---modeller/d7dd80dfac).
Du kan lesa meir om modellen der.
:::

Under pandemien høyrde me mykje om det $r$-talet, som eit mål for kor
raskt smitten vert spreidd.
Enkelt forklart er det slik at kvar person som vert smitta, gjev smitta
vidare til $r$ andre personar i gjennomsnitt.
Dette gjev oss ein modell som me kan simulera.

## Parameter

Lat oss fyrst definera parametrane.  Me treng eit $r$-tal som 
me kaller `r1` og talet `t1` på periodar som me skal simulera.
Me kan tenkja på `t1` som veker.

```{code-cell} ipython3
r1 = 3.0
t1 = 20
```

::: {admonition} Oppgåve
Om du vil at brukaren skal oppgje verdi til variablane, kan du bruka
`input()`-funksjonen.
Blokken over kan til dømes endrast til dette:
```ipython3
r1 = float(input("Hva er R-verdien i starten? "))
t1 = int(input("Hvor mange uker holder denne R-verdien seg? "))
```

Byt ut definisjonane av `r1` og `t1` slik at du bruker `input()`
og test det.
:::

::: {admonition} Merknad
Der er to grunnar til at eg ikkje bruker `input()` i døma.  
Den viktigaste er at `input()` ikkje verkar når eg genererer vevsider
frå Jupyter-dokumentet.  Når ein arbeider i Jupyter Lab, kan dessutan
lesaren like enkelt endra verdiane i ein kodeblokk.  

Det er derimot verd å læra seg `input()`-funksjonen når ein skal skriva
frittståande program, og mange forfattarar bruker han i Jupyter Notebook-dokument.
:::

## Modellen

Storleiken som me skal modellera er talet på smitta personar.  
Me tenkjar oss at det heile startar med éin smitta person.
I tillegg må me ha ein liste over talet på smitta personar
på kvart tidspunkt hittil i simuleringar.
Dette kan me definera slik.

```{code-cell} ipython3
pop = 1
liste_smittet = [1]
```

Sjølve simuleringa må vera ei løkke som itererer over `t1`
periodar.  I kvar runde smittar `pop` personar `r1*pop`
nye personar, medan dei `pop` personane vert friske 
(eller døyr).
 
```{code-cell} ipython3
for i in range(t1):
    pop *= r1
    liste_smittet.append(pop)
```

::: {admonition} Oppgåve
Lag eit plott over veksten i talet på smitta so langt.
:::

::: {hint}
Me har sjølvsagt `liste_smittet` som $y$-verdiar til plottet,
men me har ikkje definert ei liste som kan brukast som $x$-verdiar.
Det er alltid mogleg å bruka `range(len( liste_smittet ) )` for
å laga seg $x$-verdiar som kan brukast.
:::

## Periode 2

Dette $r$-talet er ikkje konstant.  Når me tek omsyn til smitta
ved å halda meir avstand (einmeter, tometer), går $r$-talet ned.
Når me vert leie av tiltaka kan $r$-talet gå opp.

Lat oss simulera ein periode til, med nytt $r$-tal `r2`.
Legg merke til at den nye perioden held fram der den fyrste stoppa,
slik at me ikkje redefinerer `pop` og `liste_smittet`.
 
```{code-cell} ipython3
r2 = 1.2
t2 = 30
 
for i in range(t2):
    pop *= r2
    liste_smittet.append(pop)
```

::: {admonition} Oppgåve
Her har me to nesten identiske `for`-løkker.  Koden vert enklare å lesa
om me bruker ein funksjon i staden for å gjenta kode.
Skriv ein funksjon `smittesim(liste_smittet,r,t)` som erstattar `for`-løkka.
Funksjonen kan ta `liste_smittet` inn, leggja til nye datapunkt, og returnera
den utvida lista.
:::

::: {hint} 
Eg nemnde ikkje `pop` i oppgåva over, men `pop` vil alltid vera lik
det siste elementet i lista.  Me kan difor finna `pop` som
`liste_smittet[-1]`.
:::

## Plotting

Til slutt kan me plotta det heile, slik.
   
```{code-cell} ipython3
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.grid(True)
ax1.plot(range(len(liste_smittet)), liste_smittet)
plt.xlabel("Uker")
plt.ylabel("Nye smittede")
plt.show()
```

::: {admonition} Oppgåve
Prøv deg fram med andre $r$-tal, anten i standen for dei over, eller ved
å leggja til ein periode.  Kva skjer når $r<1$?
:::
