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

## Forbetring av programmet

## Gjenbrukbare funksjonar

## Avslutting
