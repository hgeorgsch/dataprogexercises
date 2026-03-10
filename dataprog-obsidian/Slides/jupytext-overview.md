---
title: Jupyter i ulike filformat
author: Hans Georg Schaathun
date: March 2025
tags:
  - lecture/video/perspective
css:
  - css/templates.css
---

<!-- slide template="[[tpl-flex]]"  bg="lightgrey"-->

# Jupyter i ulike filformat

![[Jupyter_logo.svg]]

::: credit
Logo ved Cameron Oelsen.
BSD, 
frå [github](https://github.com/jupyter/jupyter.github.io/blob/master/assets/share.png)
:::

note:
*Notebook*-filene som vi har jobbet med i Jupyter er et utrolig fleksibelt og gjenbrukbart format.
Det er verd å ta en titt på forskjellige måter å bruke *Notebooks* på.

---
<!-- slide template="[[tpl-flex]]"  bg="lightgrey"-->

![[jupyter.svg]]

::: credit
:::

note:
Som vi vet består Jupyter Notebook-dokumentet av bokser.  
Stort sett bruker vi tre typer bokser, *markdown* og *code* som vi skriver selv, og *output* som er resultatet av å kjøre *Code*-bokser. Jupyter-programmet har en kjerne, *kernel*, som gjør jobben som tolk og kjører programmet.  Som regel tolker kjernen python, men andre kjerner for andre sprog er mulig.  Der finnes en fjerde blokktype, *raw*, men den er lite brukt.

---

## Konvertering av *Notebooks*

- jupytext   $\leftrightarrow$  `.md`, `.py`
- nbconvert $\to$ `.pdf`, `.html`
- Jupyter book $\to$ *komplett vevsted*

note:
Vi er vant til å jobbe med `ipynb`-filer som inneholder *Notebooks*.
`ipynb` bruker JSON for å representere blokkene som objekter.
Strukturen er ikke fryktelig vanskelig å forstå hvis du åpner filen i en tekst-*editor*.

Det er mulig å lagre en *Notebook* i andre formater enn JSON og `ipynb`,
og det er det jeg vil snakke om her.

Først skal vi skille mellom verktøy som typesetter en *Notebook* for presentasjon, kanskje som en rapport i PDF eller en vevside i HTML. Dette gjør det mulig å dele den ferdig kjørte *Notebook* med kolleger som ikke selv bruker python eller Jupyter.

Læringsmaterialet til kurset er lavet på denne måten, med et system som heter *Jupyter books*.  Jeg skal ikke gå inn på *Jupyter Books* i dag fordi versjon 2 nylig er kommet, og jeg kjenner bare versjon 1.  Et litt enklere verktøy for slik oversettelse er `nbconvert`, men det har jeg ikke brukt selv.

---

## jupytext

- Notebook (`ipynb`)
- py:percent
- Markdown

note:
Oversettelse til presentasjon er enveis.  Det er ikke mulig å oversette tilbake fra presentasjonsformatet til en *Notebook* som kan redigeres og kjøres på nytt.

`jupytext` gjør toveis oversettelse mellom `ipynb` og andre formater.

---

![[jupytex1demo.png]]

```
jupytext --to py:percent jupytext1demo.ipynb
```

note:
Hvis vi har en *Notebook* som vi ønsker å bruke som frittstående program, kan vi bruke py:percent-formatet.  jupytext kjører på kommandolinjen og det er en enkel kommando å konvertere ipynb til py.

---

```
# %% [markdown]
# # Tidsrekkjer og pivot
#
# Datafile: [12143_20260209-154116.csv](12143_20260209-154116.csv)
#
# Her har tidsaksen mange ulike variabler med hver sin rad på samme tidsperiode.
# Vi ønsker heller å ha variablene bortover, med egne søyler,
# slik at vi får én og bare én rad per periode.

# %%
import pandas as pd
df = pd.read_csv( "12143_20260209-154116.csv", encoding="latin1", sep=";", header=1 )
display(df)

# %% [markdown]
# Funksjonen vi trenger er `pivot`, slik.

# %%
df1 = df.pivot( index="år", columns=["statistikkvariabel","regnskapsbegrep"] )
display( df1 )

# %% [markdown]
# Til slutt er det greit å lagre den nye *DataFrame* i en ny fil.

# %%
df1.to_csv( "pivot.csv" )
```
<!-- element style="font-size: 10pt ; " -->

note:
Når vi oversetter til py:percent blir Markdown-boksene satt som kommentarer i python-koden.  Linjer som begynner med skigarden *hash* er kommentarer som blir ignorert av tolken.

Hver boks i Jupyter-dokumentet er markert med to prosenttegn, derav navnet py:percent.

*Output* er ikke med py:percent-filen, men det kan regenereres  ved å kjøre koden på nytt når den konverteres tilbake til ipynb.

---

```
(dataprog) georg@nyquist:~$  python jupytext1demo.py
      år                         statistikkvariabel  ... 1127 Randaberg  1130 Strand
0   2015                            Beløp (1000 kr)  ...         5076.0      25490.0
1   2015                            Beløp (1000 kr)  ...       196109.0     159172.0
2   2015                            Beløp (1000 kr)  ...        25735.0      32711.0
3   2015  Andel av brutto driftsinntekter (prosent)  ...            0.6          2.9
4   2015  Andel av brutto driftsinntekter (prosent)  ...           24.4         17.8
5   2015  Andel av brutto driftsinntekter (prosent)  ...            3.2          3.7
6   2016                            Beløp (1000 kr)  ...        10548.0      62268.0
7   2016                            Beløp (1000 kr)  ...       295890.0     118723.0
8   2016                            Beløp (1000 kr)  ...        52469.0      70949.0
9   2016  Andel av brutto driftsinntekter (prosent)  ...            1.2          6.5
10  2016  Andel av brutto driftsinntekter (prosent)  ...           34.7         12.3
11  2016  Andel av brutto driftsinntekter (prosent)  ...            6.2          7.4
```

note:
Når den *Notebook* er konvertert til py:percent kan vi også kjøre den gjennom python-tolken på kommando-linjen.

Dette blir en  mulig måte å utvikle frittstående programmer på.  Man kan prøve og feile i Jupyter, og konvertere til py:percent når man er fornøyd.

---


````markdown
# Tidsrekkjer og pivot

Datafile: [12143_20260209-154116.csv](12143_20260209-154116.csv)

Denne datafilen har tidsaksen mange ulike variabler med hver sin
rad på samme tidsperiode.
Vi ønsker heller å ha variablene bortover, med egne søyler,
slik at vi får én og bare én rad per periode.

```{code-cell} ipython3
import pandas as pd
from IPython.display import display
df = pd.read_csv( "12143_20260209-154116.csv", encoding="latin1", sep=";", header=1 )
display(df)
```

Funksjonen vi trenger er `pivot`, slik.

```{code-cell} ipython3
df1 = df.pivot( index="år", columns=["statistikkvariabel","regnskapsbegrep"] )
display( df1 )
```

Til slutt er det greit å lagre den nye *DataFrame* i en ny fil.

```{code-cell} ipython3
df1.to_csv( "pivot.csv" )
```
````

note:
jupytext kan også oversette til et rent markdown-format.
Kode som skal gjengis nøyaktig blir markert med omvendte apostrofer eller *backticks* i markdown. Kodeceller fra *Notebook* blir i tillegg satt med en bestemt annotering *code-cell* i krøllparenteser.

Prinsippet er akkurat det samme som for py:percent.  Vi får en korrekt fil i et eksisterende format, med blott litt ekstra annotering for å markere blokkene i Jupyter Notebook.

---

# Slutt

note:
En av de store fordelene med tekstformatene markdown og py:percent er at *output* ikke er med.  Det er nyttig ved versjonskontroll, fordi man slipper å se endringer som bare er et resultat av variasjoner i kjøringen.  Det skal vi drøfte i en anden video.

Det jeg har forsøkt å få frem her er at arbeidet du gjør i *Jupyter* kan gjenbrukes på mange forskjellige måter. Ingen har tid til å settte seg inn i alle muligehetene, men det er verd å vite at de er der.