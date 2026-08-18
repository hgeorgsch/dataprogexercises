---
tags:
  - session/week
author: Hans Georg Schaathun
---

# Datastrukturar og Simulering 

::: {admonition} Forkunnskapar
Dette kapittelet byggjer på
[Numeriske Metodar og Kontrollflyt](Numeriske%20Metodar%20og%20Kontrollflyt.md).
:::

+ *Perspektivføredrag* 
	+ [Kva er simulering?](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=147cd141-d681-4b2a-b0ab-b3ee00a18bf4)
      ([Slides](https://iirevu.org.ntnu.no/Slides/Kva%20er%20simulering%3f/#/))
	+ [Slumptalsgeneratorar](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=fd4e89a9-dc58-4395-accc-b3ee00a16352)
      ([Slides](https://iirevu.org.ntnu.no/Slides/Slumptalsgenerator))
	+ [Datastrukturar](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=aa7704c5-a340-4345-994d-b3ee00a1716d)
      ([Slides](https://iirevu.org.ntnu.no/Slides/Datastrukturar/))
+ *Gjennomarbeidde Døme.*
	+ [Tilfeldigheit](notebooks/Tilfeldigheit)
	+ [Marknadssimulering](notebooks/Marknadssimulering)
	+ [Listekomprehensjon](notebooks/Listekomprehensjon)
	+ [](notebooks/JSON%20og%20dict) (valfri).
      Denne øvinga er litt meir teknisk og spissfindig, og mindre praktisk,
      men ho kan gje ein nyttig illustrasjon av bruken av `dict`.
+ *Tekniske demonstrasjonar*
	+ [Demo Listekomprehensjon](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=64c29094-a428-42a5-9f3b-b3ee00dc0018)
        + [](notebooks/list-empty)
        + [](notebooks/list)
    + [Demo `dict`](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=ca95348f-dd3d-484f-b4d5-b3ee00dc3b75)
        + [](notebooks/dict-empty)
        + [](notebooks/dict)
+ *Opne Øvingar.*
    + [](Exercises/Kundedifferensiering)
    + [](Exercises/Varar%20på%20sal) (variasjonar over tidlegare oppgåver i marknadssimulering)
+ *Drilløving* på [Moodle](https://capquiz.math.ntnu.no).  
	+ CodeRunner `list` og `dict`

Kuriosa
: er arbeidsdokument.  Dei vert publiserte for dei nyssgjerrige, og viser teknikkar som eg har brukt for å laga det andre materialet til leksjonen.

+ [](notebooks/Tilfeldigheit-Demo) viser korleis plotta til føredraget om
  [Tilfeldigheit](https://iirevu.org.ntnu.no/Slides/Kva%20er%20simulering%3f/#/)
  vart lagde.

## Oppsummering

Hovudmålet denne veka er å kunna planleggja og implementera enkle
stokastiske (tilfeldige) simuleringar, samt kunna bruka nokre
grunnleggjande datastrukturar (samansette datatypar).
Dette inneber
+ Kva er simulering og kvifor er det nyttig?
+ Pseudoslumptal
+ Datastrukturar
    + `dict`
    + lister
