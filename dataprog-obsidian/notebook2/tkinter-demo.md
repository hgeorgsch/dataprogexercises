---
jupytext:
  formats: ipynb,py:percent,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
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
:tags: [skip-execution]

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
:tags: [skip-execution]

root = tk.Tk()
root.title( "Testvindauga" )

btn = tk.Button(root, text = "Trykk her" ,
             fg = "red", command=callback)
btn.grid(column=1, row=0)

root.mainloop()
```

Her definerer me ein knapp som er ein instans av klassa `Button`.
Argumenta fortel at knappen høyrer til vindauga `w`, at han skal ha ei bestemt tekst i ein bestemt farge, og sist men absolutt ikkje minst, han har `callback`-funksjonen vår som kommando.

::: {admonition} Refleksjonsspørsmål
Kva skjer når du trykker på knappen?
Skjer der noko anna om du trykker fleire gongar?
:::

Legg merke til at knappen ikkje dukkar opp utan ein geometrihandsamar.  Her har me brukt `grid` som er greitt
for å leggja til fleire element i eit rutenett.

+++

## Eigne klasser

Det første dømet hadde berre to grafiske element, rotvindauga og knappen.
Nyttige program har langt fleire, og det vert lett rot.
Det er god skikk å laga eigne klasser for kvart vindauga.
Det kan sjå slik ut

```{code-cell} ipython3
:tags: [skip-execution]

class Vindauga(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title( "Testvindauga" )
        btn = tk.Button(self, text = "Trykk her" ,
             fg = "red", command=self.callback)
        btn.grid(column=1, row=0)
    def callback(self):
        print( "No skjedde der noko!" )
root = Vindauga()
root.mainloop()
```

Her lager me heilt enkelt ei eiga klasse som arvar `Tk` som me brukte i det fyrste dømet.
Fordi `Vindauga` sjølv set opp alle elementa i vindauga og har `callback`-funksjonen som ein metode, får me samla all koden som høyrer til same vindauga på ein plass.

Der er eitt nytt elemenet her som me (truleg) ikkje har sett før: 
`super().__init__()`. 
Ho kaller konstruktøren frå superklassa `Tk`, og dette er heilt
kritisk for at `Vindauga` skal oppføra seg som eit `Tk`-vindauga.
Det må gjerast før me kan bruka metodar som `title`.

::: {admonition} Oppgåve
Køyr kodeboksen over.  Skjer det same sist?
:::

+++

## Tekstboks i vindauga

Det er litt teit at GUI-programmet vårt skriv i terminalen eller i *Notebook*.
Me kan laga ein tekst-*widget* som viser teksta, og samstundes visa korleis me legg fleire *widgets* inn i vindauga vårt.

```{code-cell} ipython3
:tags: [skip-execution]

class TekstVindauga(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title( "Tekstdøme" )
        self.geometry("500x500")
        btn = tk.Button(self, text = "Trykk her" ,
             fg = "red", command=self.callback)
        btn.grid(column=2, row=3)
        self.txt = tk.Text(self, bg="white",width=200, height=150)
        self.txt.grid(column=2, row=4)
    def callback(self):
        self.txt.insert(tk.INSERT, "No skjedde der noko!\n" )
root = TekstVindauga()
root.mainloop()
```

## Opna ei fil

Biblioteket `tkinter` har *widgets* for det meste.
For å få vindauga vårt til å gjera noko, kan me starta med
å opna ei fil med `askopenfilename()`. Dette krev ein annan modul fro `tkinter`.

```{code-cell} ipython3
from tkinter.filedialog import askopenfilename
```

For å testa kan me skriva om klassa vår med ein ny *callback* som bruker
`askopenfilename()`.

```{code-cell} ipython3
:tags: [skip-execution]

class FilVindauga(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title( "Fildialogdøme" )
        self.geometry("500x500")
        btn = tk.Button(self, text = "Opna fil" ,
             fg = "red", command=self.openFile)
        btn.grid(column=2, row=3)
        self.txt = tk.Text(self, bg="white",width=200, height=150)
        self.txt.grid(column=2, row=4)
    def openFile(self):
        self.txt.delete('1.0', tk.END)
        filePath = askopenfilename( filetypes=[
              ("Comma separated values", ".csv"),
              ("All Files", "*.*")])
        with open(filePath, 'r') as askedFile:
            fileContents = askedFile.read()

        self.txt.insert(tk.INSERT, fileContents)

root = FilVindauga()
root.mainloop()
```

::: {admonition} Oppgåve
Køyr vindauga og sjå om du finn ei fil du kan opna.
Kva skjer?
:::

::: {admonition} Refleksjonsspørsmål
Sjå over koden over.  Skjøner du kva alle linene gjer?
:::

::: {hint}
Me har ikkje brukt konstruksjonen med `if open(...) ...` tidlegare.
Me har stort sett brukt ferdige rutinar frå SciKitLearn og pandas.
Her laster me råfila som ein streng utan å tolka han i det heile.
Dette krev to steg. Fyrst må fila opnast, og so kan ho lesast.

Konstruksjonen med `with` handterer ein del feil dersom `open()` ikkje
lukkast med å opna fila.  Me kunne ha skrive `askedFile = open(filePath, 'r')`
i staden, men det er god kotyme å bruka `with` på denne måten.
Legg merke til modusen `'r'` som tyder at fila vert opna for lesing (r for *read*)
og ikkje skriving.
:::

+++

## Visa *pandas*-data

Tekstboksen i vindauga over er primitiv og utan formattering.
Sidan me har arbeidd mykje med data i pandas i dette kurset
skal me sjå om me kan visa ein *DataFrame* pent.
Då treng me 
[pandastable](https://pandastable.readthedocs.io/en/latest/description.html).

Det er ikkje sikkert `pandastable` er installert, so her køyrer
me `pip` fyrst for å vera sikre.  Utropsteiknet `!` er ein sokalla
*shell escape* som sender resten av lina til eit *shell*, dvs. same
kommandotolk som me elles bruker i terminalvindauga.

```{code-cell} ipython3
!pip install pandastable
import pandas as pd
import pandastable as pdtab
```

```{code-cell} ipython3
:tags: [skip-execution]

class PandaVindauga(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title( "Fildialogdøme" )
        self.geometry("500x500")
        btn = tk.Button(self, text = "Opna fil" ,
             fg = "red", command=self.openFile)
        btn.grid(column=2, row=3)
        self.model = pdtab.TableModel()
        self.table = Table(self, dataframe=self.mode )
        self.table.grid(column=3, row=3)
        self.table.show()
        self.txt.grid(column=2, row=4)
    def openFile(self):
        filePath = askopenfilename( filetypes=[
              ("Comma separated values", ".csv"),
              ("All Files", "*.*")])

        df = pd.read_csv( filePath )
        self.model.setup(df)

root = PandaVindauga()
root.mainloop()
```

## Avrunding
