---
tags:
    - tutorial
    - installation
---

# Installasjon python


I kurset bruker vi python som programmeringsspråk og fleire ulike
verkty til å arbeida med pythonkode.
Me tilrår å installara *Anaconda* som er eit distribusjonsmiljø
for det meste som finst av pythonverkty.
Ved å installera siste utgåve av Anaconda, er me trygge på at du
har ein ny versjon av python, alle biblioteka me treng, samt
*Jupyter Lab* som er det fyrste verktyet me treng.

Der er eitt aber med anaconda.  Det er ikkje fri programvare.
Der er lisensvilkår å lesa, og om ein skal bruka det i ein stor
bedrift, treng ein betalt lisens.
Dei som ikkje kan eller vil installera Anaconda, kan installera
Python og pip, og bruka pip til å installera andre pakkar som
trengst.  Sjå under Anaconda.


::: {warning}
Der er sådd tvil om kva lisens som gjeld for Anaconda ved NTNU
og dette er eg i ferd med å sjekka ut.
:::

::: {admonition} Merknad
Miniconda er ein lettvektsutgåve av anaconda, og sjølve miniconda
er gratis.  Problemet er at ein bruker miniconda for å lasta ned
andre pakkar frå anaconda-platformen, og det er ikkje lett å sjå
kva som krev betalt lisens.
:::

::: {admonition} Merknad
Dersom du installerer python på andre måtar, so skal du sjå til
at du ogso har Jupyter Lab og at du kan installera
popolære bibliotek som torch, pandas, scikit-learn, m.fl. ved behov.
Det er alt me treng.
:::


## Anaconda

1. Last ned [Anaconda](https://www.anaconda.com/download/success)
   - Vel riktig versjon, mac, Linux eller windows,
     og evt. intel eller m-prossessor for mac.
   - Du kan sjekka om du har intel eller apple-silicon-prosessor 
     slik som på [biletet under](fig-sjekk)

:::{figure} sjekk-prosessor.png
:name: fig-sjekk
Trykk på eplet oppe til venstre og «about this mac» eller «Om denne maskinen»
:::

2. Fylg installasjonsinstruksen og godtak standardinstillingane
3. Start Anaconda Navigator - fyrste gongen spør han om
   å oppdatera; gjer det
   - Kan henda spør han òg om å laga eller logga inn på ein konto;
     det treng du ikkje

:::{figure} oppdater.png
:name: fig-oppdater
Trykk ja for å oppdatera - vindauga om innlogging kan dere kryssa ut.
:::

:::{note}
Anaconda er alt me treng den fyrste halvdelen av kurset.
Når du har installert, kan du gå
[](notebooks/Fyrste%20dokument%20i%20Jupyter%20Lab) for å
sjå om det verka, men dette skal me prata meir om på
[Opningssamlinga](Opningssamling).
:::

## Python og pip

Unix-system, inkl. MacOS, plar ha python førehandsinstallert.
På Windows må ein ofte installera det sjølv.
Det greiaste er sikkert å bruka 
[instruksjonane frå MicroSoft](https://learn.microsoft.com/en-us/windows/python/beginners).

Pakkehandteringsverktyet `pip` bør vera automatisk installert saman 
med python.
Når me ikkje har Anaconda eller miniconda, er det `pip` me bruker
for å installera alt anna tilbehør til python.

Når ein bruker Python utan anaconda, vil ein måtte bruka kommandolina,
ogso kjend som terminalvindauga.
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

Eitt problem som du vil støyta på når du ikkje har Anaconda, er at
mange bibliotek som me bruker, må lastast ned eitt og eitt.
Det er like greitt å installera dei viktigaste med ein gong.

6.  Opna terminalvindauga igjen og køyr kommandoen

```sh
pip install matplotlib pandas scikit-learn numpy torch
```
eller (på Windows)
```
py -m pip install matplotlib pandas scikit-learn numpy torch
```
