---
tags:
  - exercise
  - legacy
---

# Eksportdata

Datasett : https://www.ssb.no/en/utenriksokonomi/utenrikshandel/artikler/import-og-eksport-alle-land-og-varenummer

Dette datasettet er ikkje det enklaste å arbeida med, men det er ein interessant utfordring som kan settja fleire ulike programmeringsferdigheiter på prøve.

Det som gjer det vanskeleg er at kvar line gjeld anten import eller eksport, éin vare, eitt land og éin periode. For å finna eksporten til eit spesifikt land i kvar periode, må ein summera over landa,
og skal ein ha data om éin vare, må ein summera over land.

I tillegg er innhaldet i tabellen kryptiske kodar.  Desse kodane er forklarte på sida, men det er litt arbeide å setja seg inn i.

::: {admonition} Oppgåve
Før du kan starta må du sjølvsagt lasta inn fila med pandas.  Studer fila i ein teksteditor eller bruk forlaringa frå SSB til å gjera dette rett.
:::

Der er mange spørsmål ein kan stilla.  Dette er berre nokre døme i stigande vanskegrad.

::: {admonition}  Oppgåve
Vel éin vare og eitt land, og filtrer ut eksportdata for denne varen til dette landet.
Plott eksportverdien over tid.
:::

::: {admonition}  Oppgåve
Vel eitt land, kva er den totale eksportverdien til dette landet for kvar periode?
Kva er den totale importverdien?

Plott eksport og import over tid.  Utviklar dei seg likt?
:::

::: {admonition}  Oppgåve
Vel éin vare og summer opp eksportverdien over dei siste fem åra for kvart land.
Lag eitt søylediagram som samanliknar eksporten til dei ulike landa.
:::

::: {admonition}  Oppgåve
Korleis utviklar handelsbalansen seg over tid?
Set saman data og lag relevante plott.
:::
