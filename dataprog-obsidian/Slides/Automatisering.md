---
title: Automatisering
author: Hans Georg Schaathun
date: March 2025
tags:
  - lecture/video/perspective
css:
  - css/templates.css
---

<!-- slide template="[[tpl-quote-header]]" -->
# Automatisering

![[Escher_Waterfall.jpg]]

::: credit
By M. C. Escher - Official M. C. Escher website,
Fair use (Old-50) via 
[Wikimedia Commons](https://en.wikipedia.org/w/index.php?curid=3473571)
:::

note:
Hensikten med datamaskiner er å automatisere av arbeidsoppgaver.

Ferdigkjøpt programvare lar oss automatisere de mest grunnleggende og
standardiserte oppgavene, som å regne ut gjennomsnitt eller tegne et
søylediagram.  

Når vi skal levere en månedlig markedsanalyse for vår egen virksomhet 
må vi derimot legge en god del manuelt arbeide på toppen.  
Standardprogrammene vet ikke hvordan våre data ser ut eller hva som
er relevant for vår virksomhet.
Hva om vi kunne skrive progravaren som lar oss levere samme analyse
med oppdaterte datasett hver måned, uten å gjøre alle de manuelle 
stegene på nytt?

I denne videoen skal vi prate litt om hva vi må tenke på for å få det
til.

---
<!-- slide template="[[tpl-flex]]" bg="lightgreen" -->

![[Refund_icon.svg]]

::: credit
By [k4r573n](https://openclipart.org/detail/212888/refund-icon), CC0
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=54502596)
:::

note:
Utfordringen er å skrive koden slik at den er gjenbrukbar.
Det er lettere sagt enn gjort, fordi vi gjerne programmerer vår første prototype ved å teste på ett datasett, og så løser vi alle de problemer som er spesielle for dét datasettet uten å skille mellom det som er spesielt og det som er generelt.

---
<!-- slide template="[[tpl-flex]]" -->

![[gjenbrukbar.png]]

::: credit
:::

note:
Det første man skal lære seg er antagelig å strukturere *notebooks* i Jupyter slik at det er lett å bytte ut parametre og datasett og kjøre rapporten på nytt på andre data.
I en typisk dataanalyse er det gjerne navnet på datafilen, og perioden. Hvis vi samler alle disse parametrne i en boks i starten av dokumntet, der vi definerer variabler, er det lett å endre dem for å lave nye rapporter.

Det som er viktig å tenke på er *hva* vi vil trenge å endre, og sørge for at vi bruker variabler for alle de verdier som skal kunne endre.

Hvis vi må gå gjennom hele dokumentet for å endre verdier her og der, blir det vanskelig å gjenbruke.

---
<!-- slide template="[[tpl-flex]]" -->

![[Generic_error_message.svg]]

::: credit
ved OmegaFallon (vektorisering av eit bilete av Andreia Gaita)
CC BY-SA 4.0, 
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=141743812)
:::

note:
Den neste utfordringen er å skrive koden slik at den er robust for feil og variasjoner. 
Hvor mye vet vi om de inndata som programmet får neste gang?

Hva skjer hvis brukeren skriver feil?
Hva skjer om der er variasjoner i datasettene som blir brukt?
Hva hvis dataleverandøren legger til nye søyler i datasettet?

---
<!-- slide template="[[tpl-twocolumn]]" -->

::: leftimage
![[The_Thinker,_Rodin.jpg]]
:::
::: leftcredit
By AndrewHorne (talk) - Self-photographed 
Public Domain,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=15582363)
:::
::: rightimage
![[1902_Wright_Brothers'_Glider_Tests_(13066000785).jpg]]
:::
::: rightcredit
By NASA on The Commons - 1902 Wright Brothers' Glider Tests, No restrictions,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=43723040)
:::

note:
Der er to forskjellige tilnærminger for å skrive robust kode:
den analytiske og den eksperimentelle.

Analytikeren kan prøve å tenke gjennom alt som kan skje i praksis, og kartlegge hele spekteret av mulig inndata, for nitidige å skrive *if*-satser for hver en tenkelig variant.

Praktikeren vil gjerne bare teste de datasett som er tilgjengelig, og rette feilene efter hvert som de blir oppdaget.

Det beste er som regel å bruke begge tankesett. Hvis vi bare prøver og feiler, blir koden ofte rotete og det er begrenset hvor mange eksempler vi kan teste. Hvis vi bare tenker analytisk bruker vi gjerne endeløst med tid på tilfeller som aldri forekommer i praksis, men det er lettere å holde struktur på koden.

Så er der selvsagt en kost-nytte-avveining å gjøre.  Skal du dele koden med andre, bør den være mer robust enn om du bare skal bruke den selv.  Når du bruker den selv, så vet du gjerne hva som skjer når det går galt, og kan rette efter hvert. 

Det er viktig å være bevisst på robustheten, men prioriteringene må være opp til den enkelte i hvert enkelte konkrete tilfelle.

---
<!-- slide template="[[tpl-twocolumn]]" -->

::: leftimage
![[GRASS_6.1_GUI.png]]
:::

::: leftcredit
By M. Neteler - GRASS 6.1 Screenshots, CC BY-SA 2.5,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=1380762)
:::

::: rightimage
![[cli.png]]
:::
::: rightcredit
:::

note:
Det er ikke alltid *Jupyter Lab* er rett løsning.  Prinsippene for gjenbrukbar og robust kode er de samme, men det er ikke alltid ønskelig å måtte starte Jupyter og tukle med et stort dokument hver gang man ønsker å gjenbruke kode. Av og til ønsker vi å lave frittstående programmer.

Vi skal ikke snakke så mye om grafiske brukergrensesnitt ennu; ikke før vi har en bedre forståelse for selve innmaten. Det er mye vi kan få til med kommandolinjegrensesnitt.

---
<!-- slide template="[[tpl-flex]]" bg="white" -->

![[filter.svg]]

::: credit
:::

note:
Svært mange nyttige program fungerer som filter eller transformasjoner.
De tar én fil inn, kanskje i CSV, og spytter en anden fil ut, kanskje et plott i SVG-format.

Dette er en god plass å begynne når man skal lære seg å bruke python utenfor Jupyter.
Slike programmer blir ofte korte og oversiktlige fordi de bare gjør én ting, men den ene tingen kan ofte være meget nyttig.

---

- `filter.py`

```python
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv( "09535fastlege.csv",
                  sep=";", encoding="latin1",
                  header=1 )

df = df.set_index("år")
print(df)

df["0 Hele landet Alle aldre"].plot()
plt.savefig( "plott.svg" )

```

note:
Et frittstående program i python er en fil med navn som slutter på `.py`.
Vi kan bruke nesten all kode som vi bruker i Jupyter.
Bare noen få ting blir anderledes.

Plott blir ikke vist automatisk.  I et filter bruker vi gjerne `savefig` for å skrive figuren til fil.

Dessuten har Jupyter en del funksjoner som blir lastet automatisk fra `IPython`-pakken.
I et frittstående program må vi eksplisitt importere dem.  Det gjelder f.eks. `display`-funksjonern som vi ofte bruker på *DataFrames*.

Koden i py-filen kan du skrive i en hvilken som helst tekst-*editor*, men den må lagres i ren tekst.  En vanlig feil er å bruke et tekstbehandlingsprogram som lagrer teksten med formatering.  Det vanligste er å bruke en IDE - *Integrated Development Enviroment* - som VSCode eller Spyder, men det skal vi komme tilbake til i en anden video.

---
<!-- slide template="[[tpl-flex]]" -->

![[filter.png]]
::: credit
:::

note:
Når vi kjører et frittstående program, må vi kjøre det gjennom en tolk eller *interpreter*.
Den vanlige tolken for python heter rett og slett python, og vi kan kjøre den fra kommandolinjen eller terminalvinduet.

Det er tolken som oversetter den relativt brukervennlige python-koden til maskininstruksjoner som kan kjøre på CPU-en i maskinen.

---

# Slutt

note:
Det er ganske stor forskjell på å skrive programkode som bare skal kjøre én gang i ett Jupyter-dokument, og kode som skal kjøres om og om igjen med forskjellige inndata.
Det krever omtanke å skrive koden slik at den er gjenbrukbar, og ennu mer omtanke om koden skal tåle skjødesløs omgang fra brukere som ikke vet hvordan koden er skrevet.

Dét er verd å tenke på, enten du skriver kode for andre eller bare trenger å bruke din egen kode omigjen om en måned eller et år.

Der finnes en del kodestandarder og *design patterns* som skal gjøre det enklere å holde orden. Særlig hvis man er flere utviklere som skriver på de samme programmene, er det viktig å være enige om standarder for å holde orden.  Det har derimot ingenting å sette seg inn i standarder som er større enn de programmene man skriver. Derfor lar jeg slike standarder ligge til en anden gang.