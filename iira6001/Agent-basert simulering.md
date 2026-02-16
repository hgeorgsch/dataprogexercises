---
tags:
  - simulering
  - session
title: Agent-basert simulering
---

# Agent-basert simulering

::: {admonition} Forkunnskapar
Dette kapittelet byggjer på
[Datastrukturar og Simulering](Datastrukturar%20og%20Simulering.md).
:::

Objektorientert programmering har vakse fram som den dominerende
metoden for å handtera både komplekse datamodellar og komplekse
programsystem.  Denne veka er eit forsøk på ei svært kort innføring
og oversikt.

+ *Oversiktsførelesing*:
	+ [Objektorientert modellering og programmering](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=9d3d90fc-bb4b-4858-8dce-b3ee00a17df8)
      [(foilar)](https://iirevu.org.ntnu.no/Slides/Objektorientert%20modellering%20og%20programmering)
+ *Utarbeidde døme*
    + [](notebooks/LoanClass) viser objektorientert programmering på
      simulering av kontantstraum, og dermed ikkje agent-basert simulering
    + [](notebooks/Shrimp-Game) er eit døme på 
      agent-basert simulering.
+ *Demovideo*
    + [Klasser og Objekt](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=d951c890-877c-4c59-97a3-b3ed00d25c05)
        + [](notebooks/class-empty)
        + [](notebooks/class)
+ *Opne øvingar*
    + [Iskrem på ei strand](notebooks/Iskrem%20på%20ei%20strand)
    + [](exercises/Agent-basert%20Marknadssimulering)

## Oppsummering

Målet denne veka er å kunna modellera simuleringsproblem som agentar
og kunna implementera dette med objekt-orientert programmering.
Dette inneber
+ Modellering med agentar som handlard uavhengig av kvarandre 
+ Klasser og objekt i python

Objekt-orientert programmering er ikkje berre nyttig i agent-basert 
simulering.
Der er mange komplekse problem som vert enklare å modelera med
objekt-orientert tankesett.
Når ein har relativt få og veldefinerte variablar, 
som me stort sett har i dataanalysa i dette kurset,
er det derimot gjerne enklare å modellera dei som matriser.

