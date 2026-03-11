---
jupytext:
  formats: md:myst,ipynb,py:percent
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Eit fyrste frittståande program

Denne øvinga tek utgangspunkt i 
[](notebooks/Fyrste%20datasett%20med%20CSV) som me
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

## Gjenbrukbare funksjonar

## Avslutting
