---
title: Anaconda
tags:
    - tutorial
    - installation
---

# Anaconda

Anaconda er ein distribusjonsplatform for å installera tilleggspakkar og verkty
for å arbeida med python.  Det har vore populært fordi ein får alt 
i eitt, men det er proprietært, og ein lyt setja seg inn i lisensvilkåra.

::: {warning}
Der er sådd tvil om kva lisens som gjeld for Anaconda ved NTNU
og dette er eg i ferd med å sjekka ut.
:::

::: {admonition} Miniconda
Miniconda er ein lettvektsutgåve av anaconda, og sjølve miniconda
er gratis.  Problemet er at ein bruker miniconda for å lasta ned
andre pakkar frå anaconda-platformen, og det er ikkje lett å sjå
kva som krev betalt lisens.
:::

## Installera Anaconda

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

