---
jupytext:
  formats: ipynb,py:percent,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Fyrste GUI i python

Her skal eg vise eit lite døme på korleis ein kan laga eit
GUI med `tkinter`.
Det går an å testa kodesnuttane i Jupyter, men om du faktisk
skal bruka GUI-programmet til noko, vil du nok heller gjera 
det som eit frittståande program.
Me bruker Jupyter her for å gjera det lett å kommentera kvar
kodesnutt.

::: {admonition} Oppgåve
Test kodesnutten under, og legg merke til kva som skjer.
Kva gjer `mainloop` og kva gjer `print`?
:::

```{code-cell} ipython3
import tkinter as tk
w = tk.Tk()
w.mainloop()
print( "mainloop" )
```

Sannsynlegvis vil du ikkje sjå noka utskrift frå `print`,
men at eit tomt vindauga dukkar opp på skjermen.

::: {admonition} Oppgåve
Lukk det tomme vindauga. Kva skjer no?
:::

Vonleg ser du no utskrifta frå `print`.
Dette viser eit viktig prinsipp i GUI-programmet:
`mainloop`, som er heile kjernen i å få eit grafisk
vindauga på skjermen, er eit sokalla *blocking call*.
Det blokkerer programmet og ingenting meir skjer før
vindauga er ferdig, dvs. lukka.

Programkoden til eit GUI er ikkje ein sekvens av kodeliner
som vert køyrde i rekkjefylgje slik som me er vane med.
I staden må me laga funksjonar som vindauga kan køyra 
etter kvart som brukaren trykkar på knappar eller vel
funksjonar frå menyar.

Dette tyder òg at alle elementa og funksjonane i vindauga må definerast før me køyrer `mainloop`.

+++

## *callback*-funksjonar

I eit GUI-program er der mykje som skjer under panseret.
Når brukaren trykkar på ein knapp, skjer der ein hending,
*Event*.
Programmet har definert lyttarar, *Listeners*, som er satt
til å lytta til spesifikke *Events* og køyra bestemte funksjonar,
som me kallar *callbacks* når hendinga inntreff.

Me treng ikkje grava i *Listeners* og *Events* for å få programmet til å fungera, men *callbacks* må me skriva.
Lat oss definera ein dum funksjon som me kan bruka til testing.

```{code-cell} ipython3
def callback():
    print( "No skjedde der noko!" )
callback()
```

Den verkar, men det var heller ikkje mykje som kunne gå galt.
Lat oss laga eit nytt vindauga med ein knapp, der me bruker
`callback`-funksjonen.

```{code-cell} ipython3
w = tk.Tk()
w.title( "Testvindauga" )

btn = tk.Button(w, text = "Trykk her" ,
             fg = "red", command=callback)
btn.grid(column=1, row=0)

w.mainloop()
```

Her definerer me ein knapp som er ein instans av klassa `Button`.
Argumenta fortel at knappen høyrer til vindauga `w`, at han skal ha ei bestemt tekst i ein bestemt farge, og sist men absolutt ikkje minst, han har `callback`-funksjonen vår som kommando.

::: {admonition} Refleksjonsspørsmål
Kva skjer når du trykker på knappen?
Skjer der noko anna om du trykker fleire gongar?
:::

Legg merke til at knappen ikkje dukkar opp utan ein geometrihandsamar.  Her har me brukt `grid` som er greitt
for å leggja til fleire element i eit rutenett.

```{code-cell} ipython3

```
