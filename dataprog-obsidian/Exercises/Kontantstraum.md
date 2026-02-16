---
title: Kontantstraum
author: Hans Georg Schaathun
tags:
  - exercise
  - simulering
  - topic/loop
---


# Kontantstraum (oppgåver for vidarekomande)

Desse oppgåvene byggjer vidare på [](/notebooks/Simulering%20av%20kontantstraum).
Dei skal ikkje krevja nye programmeringsteknikkar, men gjev øving i å variera
å kombinera og variera teknikkane frå det opprinnelege dømet.
Den enklaste måten å arbeida på, er å samanlikna kvar ny oppgåve med kjende
oppgåver og døme.  Reflekter fyrst over kva som er nytt i det nye problemet,
og deretter over kva du kan endra i løysinga for å passa det nye problemet.

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

::: {admonition} Oppgåve
Sparing liknar på lån, men der er ein stor skilnad.  Me sparer gjerne månadleg,
men renter på bankinnskot kjem årleg.  Rentene på nye innskot avheng av når på
året pengane vart setne inn.

Lag ei simulering der du sparer $s$ (kr) den fyrste i kvar månad, og får
rente 31. desember.
Du kan ordna dette med ei ytre løkke som tel år, og ei indre løkke som tel
månader innanfor året.  Den indre løkka må då halda greie på kor stor del
av året kvart innskot får renter for, medan den ytre løkka berre reknar
saldo frå nyttår til nyttår.
:::


:::{admonition} Oppgåve
Sjå på dømet med rentedringar (i [](/notebooks/Simulering%20av%20kontantstraum)).
I røynda kjem ei renteendring sjelden aleine.  
Kan henda burde sannsynlegheita for renteauke auka når den fyrste renteendringa
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

:::{admonition} Oppgåve
Sjå for deg årleg sparing der du sparer eit beløp $s$ kvart
år i tillegg til årleg rente $r$.
Kor mykje har du då spart opp etter $n$ år?

Du kan svara på dette spørsmålet ved å simulera sparinga på same måte som
me har simulert lån.

Dei som har lese matematikk veit at me kan rekna ut sluttsaldoen som ei
geometrisk rekkje.

$$S_n = \sum_{i=1}^{n} s\cdot (1+r)^i = \frac{1-(1+r)^n}{r}(1+r)s$$

Rekn ut sluttsaldoen $S_n$ både gjennom ei simulering og vha. formelen
for geometriske rekkjer.  Plott båe utrekningane for kvart år.
Får du same svar?
:::

::: {hint}
Dersom du får ulike svar i dei to utrekningane, er det ofte pga. forvirring
når på året du sparer og når du får renter.  T.d. må ein ta stilling
til om du sparer 1. januar, og får renter på desse pengane allereie fyrste år,
eller om du sparer 31. desember og ikkje får renter på desse pengane før etter
andre år.
:::

::: {admonition} Oppgåve
   Når ein planlegg lån og sparing, lyt ein òg ta omsyn til inflasjon og skatt
   (22% inntektsskatt).  Har du riktig mykje pengar, skal du kanskje tenkja
   på formueskatt ($\approx 1\%$) i tillegg.

   Utvid simuleringa med inntektsskatt og evt. inflasjon og formueskatt.
:::

