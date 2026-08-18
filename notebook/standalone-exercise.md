---
jupytext:
  formats: md:myst,ipynb,py:percent
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

# Eit fyrste frittståande program

Denne øvinga tek utgangspunkt i 
[](./Fyrste%20datasett%20med%20CSV) som me
skal skriva om som eit frittståande program.
Den opprinnelege øvinga startar med å lesa inn ein CSV-fil og
sluttar med å skriva ut ei reformater fil.

## Fyrste prototyp

Eg har laga ein fyrste prototyp
som du kan lasta ned og køyra direkte frå kommandolina.
Du treng
+ [programmet i py-format](/konvertering.py)
+ [CSV-fila](EXR20250401.csv)

::: {admonition} Oppgåve
Last ned dei to filene og plasser dei i ein ny prosjektkatalog
(mappe) til denne øvinga.
:::

Dersom du vil laga prototypen sjølv, kan du lasta ned
`jupytext` og konvertera den gamle øvinga sjølv.
```sh
cp "Fyrste datasett med CSV.md" konvertering.md
pip install jupytext
jupytext --to py:percent konvertering.py
```

## Forenkling av koden

I resten av øvinga må du gjerne bruka Spyder eller ein annan
IDE, men eg skriv med utgangspunkt i Jupyter lab.

::: {admonition} Oppgåve
Opna `konvertering.py` i Jupyter lab.
Du får då eit redigeringsvindauga for rein tekst, og ikkje
*Notebook*-formatet som du er van med.

Ser koden grei ut?
Du må gjerne klippa bort kommentarar som du ikkje treng.
:::

::: {admonition} Oppgåve
Opna terminalvindauga i Jupyter og køyr programmet.
```sh
python konvertering.py
```
Merk at arbeidskatalogen i terminalvindauga er den same som
i filnavigatøren *då terminalvindauga vart opna*.
Du må stå i rett katalog for å finna filene, både programfila
og datafila.
:::

::: {admonition} Refleksjonsoppgåve
Har programmet ditt laga ei ny fil?
Opna fila i Jupyter eller i eit rekneark.
Ser ho ut som ho skal?
:::

## Kommandolineargument

Det seier seg sjølv at me ynskjer å kunna bruka programmet på
ulike filer, og brukaren skal ikkje måtta redigera koden for å
få det til.

::: {admonition} Oppgåve
Endra blokken som definerer filnamna i `konvertering.py` til 
fylgjande.
```python
innfil = input( "Fil som skal konverterast" )
utfil = input( "Filnamn til resultatet" )
```
Køyr programmet igjen.  Kva skjer?
:::

Eit alternativ til interaktiv *input* er argument på kommandolina.

::: {admonition} Oppgåve
Endra blokken som definerer filnamna i `konvertering.py` til 
fylgjande.
```python
import argparse
parser = argparse.ArgumentParser(description="Konverter valutakursdata.")

parser.add_argument("infile", type=str, help="Input file.")
parser.add_argument("outfile", type=str, help="Output file.")
args = parser.parse_args()

innfil = args.infile
utfil = args.outfile
```
Køyr programmet igjen.  Kva skjer?
:::

::: {admonition} Oppgåve
Om du køyrde programmet som før, fekk du sikkert ei feilmelding som
seier at programmet treng argument.
Køyr det på nytt som
```sh
python konvertering.py EXR20250401.csv konvertert.csv
```
Kva skjer no?
:::

::: {admonition} Refleksjonsspørsmål
Ser du kva dei ulike kodelinene i det nye dømet gjer?
Kva slags objekt er `parser`?  Eller `args`?
:::

::: {hint} 
Biblioteket `argparse` gjer ganske mykje sjølv om me berre treng 
nokre få liner for å få det til å verka.

Me instantierer to objekt.
Det fyrste er `parser` som har ansvar for å tolka alt som står på 
kommandolina og for å gje feilmeldingar når argumenta er ugyldige.
Me kan definera alle dei argumenta som me forventar med `add_argument()`.

Det andre objektet `args` er resultatet når `parser` tolkar kommandolina.
Alle argumenta som me har definert er tilgjengelege som attributtar i 
`args`.

Der er mykje meir ein kan gjera.  Det går an å søkja opp dokumentasjonen,
men eg plar søkja etter døme og prøva meg fram.
:::

::: {admonition} Oppgåve
Kva skjer når du køyrer programmet med `--help`, slik:
```sh
python konvertering.py --help
```
:::

::: {admonition} Oppgåve
Last ned oppdaterte data frå Noregs Bank og test programmet på dei.
:::

::: {admonition} Refleksjonsspørsmål
Samanlikna løysinga med den interaktive `input()`-funksjonen
og løysinga med kommandolineargument.
Når vil du føretrekkja interaktive program og når er det best
å bruka kommandolineargument?  Kva har du bruk for i framtida?
:::

## Forbetring av programmet

I det opprinnelege dømet laga me berre søyler for pund sterling og danske kroner.
Dei andre søylene var ei oppgåve for lesaren.
Dei fleste har sikkert laga søyler for dei valutaane som fanst akkurat i eksempelfila, 
men eit gjenbrukbart program skal helst verka for andre filer med andre valutaar.
Det skal vera råd å gjera, men me må eksperimentera litt.
Lat oss fyrst lasta inn fila og fiksa dei enklaste tinga.

```{code-cell} ipython3
import pandas as pd
df = pd.read_csv("EXR20250401.csv", sep=";")
df['dato'] = pd.to_datetime(df['TIME_PERIOD'], format='%Y-%m-%d')
df['kurs'] = df['OBS_VALUE'].str.replace(',', '.')
df['kurs'] = pd.to_numeric(df['kurs'])
display(df)
```

For å finna ut kva valutaar som er representerte, kan me bruka
`unique()`-metoden, slik.

```{code-cell} ipython3
valutaar = df["BASE_CUR"].unique() 
print( valutaar )
```

I staden for den gamle koden som ser spesifikt på DKK og GBP, 
kan me bruka ei løkke for å bla gjennom lista over valutaar.
Me treng ikkje vita kva valutaar det er tale om, det ser programmet når det les inn fila.  Løkka vår bruker berre variablane som er definerte. Det kan sjå slik ut.

```{code-cell} ipython3
lst = []
for valuta in valutaar:
    valdf = df[ df["BASE_CUR"] == valuta ]
    valdf = valdf.reset_index()
    valdf[valuta] = valdf["kurs"]
    valdf = valdf.filter( items= [ "dato", valuta ] )
    lst.append( valdf )
display( lst[2] )
```

::: {admonition} Refleksjonsspørsmål
Kjenner du att innmaten i `for`-løkka frå programmet me allereie
hadde?  Sjå om du finn det.  Kva er forandra for at koden
skal verta generell?
:::

::: {admonition} Oppgåve
Kva slags data er `lst`.
Prøv med `print`.
Om utskrifta vert svært lang, kan duskriva ut typen og kanskje
lengda åt `lst`, eller berre skriva ut det fyrste elementet.
:::

+++

Eg skal røpa at `lst` er ei liste med *DataFrames*.
Me kan laga ei ny løkke som går gjennom lista og flettar alt saman til éi ny *DataFrame*.

```{code-cell} ipython3
nydf = lst[0]
for valdf in lst[1:]:
    nydf = pd.merge( nydf, valdf, on="dato" )
display( nydf )
```

::: {admonition} Oppgåve
Bruk koden over til å forbetra programmet `konvertering.py`, slik at alle valutaane er med i ut-fila.
Test at resultatet vert som det skal.
:::

::: {admonition} Oppgåve
Hent filer med andre valutaar frå Noregs Bank og test at
programmet ogso verkar på dei.
:::

+++

## Gjenbrukbare funksjonar

Programmet som me har skrive, gjer alt i éin blokk.
Slike program kaller me gjerne *scripts*.
Somme oppgåver kunne ha vore nyttige å skriva som funksjonar
som kan gjenbrukast i andre program.

I dette avsnittet skal eg visa eit triks som gjer at den
same fila kan brukast både som eit *script* og som ein
modul som kan lastast med `import`.

Det fyrste me då må gjera er å skilja definisjonar, som 
er nyttige å importera, og kommandoar som me ikkje vil ha 
køyrd ved `import`.  Det viktigaste er å skilja ut I/O, men
òg tunge utrekningar skal me unngå ved `import`.

Dei fleste utrekningane kan me gjera i funksjonar (definert
med `def`).  I programmet vårt er der i alle fall to operasjonar
som passar godt i eigne definisjonar.  Det fyrste er søylereformateringa, der me definerer `kurs` og `dato`.
Det andre er utflatinga, der me lagar tabellen med éi søyle
per kurs.

Dei neste to oppgåvene kan vera tunge.  Det er mykje kode
som skal redigerast og då går det lett i ball.
Det er ingen grunn til å fortvila om du ikkje får det til
fyrste gongen.  Hopp heller vidare til
løysinga og bruk ho som døme neste gong du skal skriva
eit program som òg skal kunna brukas som modul.

::: {admonition} Oppgåva
Lag to funksjonar `reformatCols()` og `currencyCols()` ved
å bruka eksisterande kode.  Kvar funksjon skal ta ein *DataFrame* inn og gje ein *DataFrame* ut.
Flytt båe funksjonsdefinisjonane til toppen av fila, like
under `import` og bruk funksjonskall der operasjonane vert
utførde.
Test at programmet stadig verkar.
:::

No er det mogleg å bruka `import konvertering` for å 
få tilgang til funksjonane (`konvertering.reformatCols` og
`konvertering.currencyCols`) i andre filer.
I alle fall i teorien.
Det kan vera at `argparse` skapar krøll når du gjer det.

For at dette skal fungera godt, må me flytta resten av koden,
som ikkje er funksjonar eller `import` inn i ein blokk som
berre vert køyrd når fila vert brukt som *script*.
Standardmåten å gjera dette på er ein *if*-sats som ser slik ut:
```python
if __name__ == "__main__":
   ...
```

::: {admonition} Oppgåva
Sett inn *if*-lina over etter funksjonsdefinisjonane og
rykk inn all etterfylgjande kode i ein blokk under `if`.
Test at programmet stadig verkar.
:::

::: {admonition} Løysinga
Eg har laga denne løysinga: [konverteringsscript.py](/konverteringsscript.py).
:::

## Avslutting

Eg har freista å visa tre ulike triks for å gjera koden som me tidlegare har
gjort i Jupyter Notebook meir gjenbrukbar.
Kvart triks kunne ha vore ei øving i seg sjølv.
Når eg har gjort alt i eitt døme, er det for å gje eit overblikk, slik at ein
kan slå opp teknikkane når ein treng dei.
Eg trur fullt og fast at det meste av dette er best lært ved behov, og ikkje
bruka mykje tid på å terpa grunnteknikkar som ein berre kanskje treng.

