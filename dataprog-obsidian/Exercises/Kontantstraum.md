---
title: Simulering av kontantstraum
author: Hans Georg Schaathun
tags: [exercise, simulering, loop]
---


# Kontantstraum - Oppgåver for vidarekomande

Desse oppgåvene byggjer på [](Simulering%20av%20kontantstraum).

:::{admonition} Oppgåve
So langt har me sett på annuitetslån, der terminbetalinga er eit fast beløp.
Tenk i staden på eit serielån, der du betaler rentene pluss eit fast 
nedbetalingsbeløp.
Lag eit plott som samanliknar utviklinga på serie- og annuitetslån.
:::

:::{admonition} Oppgåve
Me har simulert årlege terminar, noko som ikkje er særleg vanleg i røynda.
Lag simuleringar med månadleg rentekapitalisering og terminbetaling.
:::

:::{admonition} Oppgåve
I røynda kjem ei renteendring sjelden aleine.  
Kan henda vore burde sannsynlegheita for renteauke auka når den fyrste renteendringa
skjer, og ikkje gå ned før me ser ein rentenedgang.
Endra `loan3`-funksjonen for å simulera dette.

Det er litt plunder å få til, men du kan t.d.
1. Innføra ein variabel `terskel` og seia at me får renteoppgang når 
    `slump <= terskel`.
2. Kvar gong renta går opp eller ned, kan du justera `terskel`.
3. Slumptal frå 1 til 10 er kanskje for grovkorna, men du kan auka spennet til 100
    eller 1000.
4. Du kan laga ein tilsvarande terskel for rentenedgang.
:::

## Lukka formel

1. Geometrisk rekkje - lukka form
    1. plott og samanlikna

+ Problem.
    + lån med årleg rente
    + Sjå [[Sparekalkulator]]
+ Relativt enkelt problem.
    + kan løysast analytisk, om du kan litt matematikk
    + kan løysast i rekneark, om du har god orden
    + me løyser det her for å demonstrera nokre grunnleggjande programeringskonsept og korleis me kan leika med ulike tankeeksperiment
    + med litt røynsle og litt kreativitet er der inga grense for kva de kan gjera
        + vert det komplekst nok, får de til meir med programmering enn med rekneark
---
tags:
  - exercise
  - stub
---

# Oppgave 2: Sparekalkulator


Dersom vi sparer et fast terminbeløp $P$ som vi betaler inn på konto $n$ ganger i året,
vi har en p.a. rente på $r$ prosent og vi sparer i $t$ år, vil sluttbeløpet på sparekontoen være gitt ved:
$$
F = P\cdot \left(\frac{\left(1+\frac{r}{n}\right)^{nt}-1}{\frac{r}{n}}\right)
$$

Lag et program som ber bruker av programmet om å taste inn terminbeløp, rente, antall innskudd/renteavregninger og antall år og gir følgende tilbakemeldinger:
* Programmet oppsummerer og gir tilbakemelding på tallene brukeren gav
* Programmet beregner og oppgir sluttbeløpet på sparekonto
* Programmet angir hvor mye av sluttbeløpet er renter og innskudd, i prosent og kroner

*(Merk at $r$ i formelen ikke er i prosent, 2% = 0.02)*

### Dersom du vil

Dersom du vil kan du også ta inflasjon, formueskatt ($\approx 1\%$) og skatteprosent (22% av renteinntekter) med i beregningene
