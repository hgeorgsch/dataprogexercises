---
title: Automatisering
author: Hans Georg Schaathun
date: March 2025
tags:
  - lecture/video/perspective
css:
  - css/templates.css
---

<!-- slide template="[[tpl-quote-header]]" -->
# Automatisering

![[Escher_Waterfall.jpg]]

::: credit
By M. C. Escher - Official M. C. Escher website,
Fair use (Old-50) via 
[Wikimedia Commons](https://en.wikipedia.org/w/index.php?curid=3473571)
:::

note:
Hensikten med datamaskiner er å automatisere av arbeidsoppgaver.

Ferdigkjøpt programvare lar oss automatisere de mest grunnleggende og
standardiserte oppgavene, som å regne ut gjennomsnitt eller tegne et
søylediagram.  

Når vi skal levere en månedlig markedsanalyse for vår egen virksomhet 
må vi derimot legge en god del manuelt arbeide på toppen.  
Standardprogrammene vet ikke hvordan våre data ser ut eller hva som
er relevant for vår virksomhet.
Hva om vi kunne skrive progravaren som lar oss levere samme analyse
med oppdaterte datasett hver måned, uten å gjøre alle de manuelle 
stegene på nytt?

I denne videoen skal vi prate litt om hva vi må tenke på for å få det
til.

---
<!-- slide template="[[tpl-flex]]" bg="lightgreen" -->

![[Refund_icon.svg]]

::: credit
By [k4r573n](https://openclipart.org/detail/212888/refund-icon), CC0
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=54502596)
:::

note:
Utfordringen er å skrive koden slik at den er gjenbrukbar.
Det er lettere sagt enn gjort, fordi vi gjerne programmerer vår første prototype ved å teste på ett datasett, og så løser vi alle de problemer som er spesielle for dét datasettet uten å skille mellom det som er spesielt og det som er generelt.

---
<!-- slide template="[[tpl-flex]]" bg="lightgreen" -->

![[gjenbrukbar.png]]

::: credit
:::

note:
Det første man skal lære seg er antagelig å strukturere *notebooks* i Jupyter slik at det er lett å bytte ut parametre og datasett og kjøre rapporten på nytt på andre data.
I en typisk dataanalyse er det gjerne navnet på datafilen, og perioden. Hvis vi samler alle disse parametrne i en boks i starten av dokumntet, der vi definerer variabler, er det lett å endre dem for å lave nye rapporter.

Det som er viktig å tenke på er *hva* vi vil trenge å endre, og sørge for at vi bruker variabler for alle de verdier som skal kunne endre.

Hvis vi må gå gjennom hele dokumentet for å endre verdier her og der, blir det vanskelig å gjenbruke.

---
<!-- slide template="[[tpl-flex]]" -->

![[Generic_error_message.svg]]

::: credit
ved OmegaFallon (vektorisering av eit bilete av Andreia Gaita)
CC BY-SA 4.0, 
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=141743812)
:::

note:
Den neste utfordringen er å skrive koden slik at den er robust for feil og variasjoner. 
Hva skjer hvis brukeren skriver feil?
Hva skjer om der er variasjoner i datasettene som blir brukt?
Hva hvis dataleverandøren legger til nye søyler i datasettet?

---
<!-- slide template="[[tpl-twocolumn]]" -->

::: leftimage
![[The_Thinker,_Rodin.jpg]]
:::
::: leftcredit
By AndrewHorne (talk) - Self-photographed 
Public Domain,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=15582363)
:::
::: rightimage
![[1902_Wright_Brothers'_Glider_Tests_(13066000785).jpg]]
:::
::: rightcredit
By NASA on The Commons - 1902 Wright Brothers' Glider Tests, No restrictions,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=43723040)
:::

note:
Der er to forskjellige tilnærminger for å skrive robust kode:
den analytiske og den eksperimentelle.

