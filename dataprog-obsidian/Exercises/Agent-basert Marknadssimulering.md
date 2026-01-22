---
tags:
  - exercise
---

# Agent-basert Marknadssimulering

::: {admonition} Bakgrunn
Denne oppgåve byggjer på problemforståinga frå
[](./Kundedifferensiering) og
den agent-baserte løysingsmetoden frå [Shrimp Game](/notebooks/Shrimp-Game).
Du bør studera båe desse problema før du freistar på oppgåvene under.
:::


::: {admonition} Oppgåve
Definer ei klasse for vare. 
I tillegg til pris, må denne klassen ha eit felt for varekategori.
I utgangspunktet er varekategoriane luksus eller naudvendigheit, men
det kan henda at du vil innføra fleire seinare.  
Vil du representera kategorien som tal eller som strengar?
:::

::: {admonition} Oppgåve
Definer ulike klasser for Snobb og Navar.  
Dei må ha ein metode for kjøpshandling, som tek omsyn til varekategorien.
Pass på at metodenamnane er dei same i båe klassene, slik at simulatoren
kan bruka dei same rutinane uansett kundeklasse.
:::

::: {admonition} Oppgåve
Skriv om simulatoren for å instantiera hhv. $m$ og $n$ kundar av kvar klasse
og simulera ein dag der alle desse kundane handlar.
:::

::: {admonition} Oppgåve
Utvid simulatoren med ein tredje varekategori og/eller eit tredje kundesegment.
:::

::: {admonition} Refleksjon
Sjå for deg ulike nabolag.  
På Snobbetoppen bur der 200 snobbar og 100 navarar.
På Navarseter er det omvendt, med 200 navarar og 100 snobbar.
Samanlikna optimal prissettingsstrategi for ein butikk på Snobbetoppen
og ein på Navarseter.
:::

