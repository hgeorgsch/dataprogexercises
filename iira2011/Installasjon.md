---
tags:
    - tutorial
    - installation
---

# Installasjon python

I kurset bruker vi python som programmeringsspråk og fleire ulike
verkty til å arbeida med pythonkode.
Der er mange ulike programvarepakkar som kan brukast til å koma i gang.

Den tryggaste løysinga er å installera Python og Pip lokalt.

Der er to 


## Python og pip

Unix-system, inkl. MacOS, plar ha python førehandsinstallert.
På Windows må ein ofte installera det sjølv.
Det greiaste er sikkert å bruka 
[instruksjonane frå MicroSoft](https://learn.microsoft.com/en-us/windows/python/beginners).
Pakkehandteringsverktyet `pip` bør vera automatisk installert saman 
med python.

Når ein programmerer, vil ein måtte bruka kommandolina, ogso kjend som
terminalvindauga.
Du kan starta terminalvindauga frå startmenyane i Gnome, Windows eller
MacOS, men det kan ha ulike namn, som «terminal», «command» eller «powershell».

Du kan testa at python er installert ved å opna terminalvindauga og skriva
```bash
python --version
```
Det bør sjå omtrent slik ut
```
georg@shannon:~/git/evu/dataprogdev$ python --version
Python 3.13.5
```
Det er ikkje viktig å ha nyaste versjon, men om du har noko eldre enn 3.11,
har du eit gamalt system og sjå om du kan oppgradera.
([Versjonsstatus](https://devguide.python.org/versions/) fortel kva versjonar
som stadig er støtta.)

Det programmet som me skal bruka heile den fyrste halvdelen av kurset
heiter *Jupyter Lab*.
Dersom python er installert kan du gjera fylgjande for å installera
og testa *Jupyter Lab*.

1.  Start eit terminalvindauga.  Korleis du gjer det avheng av operativsystemet ditt.
    (Det kan heita *Command*, *Terminal*, *Cmd*, eller anna.)
2.  Skriv `pip install jupyterlab` og trykk enter.  Dersom dette ikkje verkar, kan du i staden prøva anten
    + `py -m pip install jupterlab` (Windows), eller
    + `python -m pip install jupterlab` (generelt)
3.  Skriv `jupyter lab` og trykk enter.  Dersom dette ikkje verkar, prøv
    + `py -m jupterlab` (Windows), eller
    + `python -m jupterlab` (generelt)
4.  Dette bør start Jupyter Lab i ein vevlesar (Chrome, firefox, e.l.).
    Om vevlesaren ikkje startar automatisk, vil meldingane i terminalvindauga
    gje deg ein URL som du kan kopiera og lima inn i vevlesaren din.
5.  For å testa at alt verkar kan du ta fatt på
    [](https://iirevu.org.ntnu.no/iira6001/notebooks/Fyrste%20dokument%20i%20Jupyter%20Lab) 
    og gjera oppgåvene der.

Der er mange pakkar som kan installerast med `pip`, og du vil stadig sjå
ting som ikkje verkar fordi du ikkje har alle pakkene du treng.
Det er heilt greitt å installera dei etter kvar som du treng dei, men 
nokre av dei viktigaste kan du godt instlallera med ein gong:

6.  Opna terminalvindauga igjen og køyr kommandoen

```sh
pip install matplotlib pandas scikit-learn numpy torch
```
eller (på Windows)
```
py -m pip install matplotlib pandas scikit-learn numpy torch
```

## Andre løysingar

[](Anaconda) er ein proprietær distribusjonsplatform som erstattar `pip` og gjev
tilgang til python og ei rekkje andre verkty.
Grunnen til at eg ikkje bruker det sjølv er at eg ikkje orkar å lesa lisensvilkåra,
og anaconda overskriv ein del system- og konfigurasjonsfiler utan å seia nøyaktig kva
han gjer.

Jupyter Hub er ei teneste
der du kan bruka jupyter på ein tenar utan å installera noko på eiga maskin.
NTNU har ein [intern installasjon](https://www.ntnu.no/wiki/spaces/jupyterhub/overview) 
som vert brukt i mange kurs.
Problemet med denne er at han ikkje gjev tilgang til GPU, og det vert eit problem
når me skal driva maskinlæring på billetdata.

Der finst òg andre som tilbyd Jupyter Hub utanfor NTNU, men desse kjenner eg ikkje
til.
