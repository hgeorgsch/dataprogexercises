---
tags:
  - session/week
author: Hans Georg Schaathun
---

# Numeriske Metodar og Kontrollflyt

Me freistar å gje eit par forskjellige innfallsvinklar til kvart tema.
Vekesprogrammet inneheld difor forskjellige ressursar som kan brukast på ulikt vis.

Perspektivføredraga føreset at du har arbeidd litt med oppgåvene frå
[opningssamlinga](Opningssamling.md), slik at du kjenner nokre av dei
grunnleggjande strukturane i python.

Perspektivføredrag
: er meint å gje eit konseptuelt overblikk eller kontekst.  Her tek me eit steg tilbake og freistar å sjå forbi detaljane. Me vonar at det fungerer å sjå desse litt avslappa når ein har tid til overs.  

1. Programmering og korleis me tenkjer
    + [Imperativ programmering og maskinarkitektur](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=8b24c615-b2da-4b5e-acf1-b3ed00d06d8e)
      [(Slides)](https://iirevu.org.ntnu.no/Slides/Imperativ%20programmering%20og%20maskinarkitektur)
    + [Kva er ein algoritme?](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f1ebdcd5-cbd6-426f-90f2-b3ed00d06ee2)
      [(Slides)](https://iirevu.org.ntnu.no/Slides/Kva%20er%20ein%20algoritme%3f/)
    + [Flytdiagram](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=bd097e14-50f6-4926-9aac-b3ed00d06f05)
    + [Exact Instructions Challenge](https://www.youtube.com/watch?v=cDA3_5982h8) ved Josh Darnit
1. Program i Python
    + [Struktur og syntaks i Python](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=6fafcc25-cbb0-4666-8250-b3ed00d06f2f)
    + [Kontrollflyt i Python](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=6c928dbb-3b2a-4cd4-bcfc-b3ed00d06e62)
    + Båe føredraga bruker [Python Tutor](https://pythontutor.com/) som du òg kan prøva ut sjølv.
    + [Foilar](https://iirevu.org.ntnu.no/Slides/Kontrollflyt%20i%20Python) til delar av føredraga

Gjennomarbeidde døme
: er den viktigaste læringsaktiviteten.  Dei viser nye teknikkar i kontekst med oppgåver og spørsmål som oppmodar til fikla med og variera koden for forstå kva som føregår.

+ [](notebooks/Simulering%20av%20kontantstraum) frå opningssamlinga.
      Du bør gjera ferdig denne før du startar på noko nytt.
+ [Halveringsmetoden](notebooks/Halveringsmetoden)
  viser numerisk likningsløysing.  Dette koplar programmeringa til
  matematikk, men om du ikkje er interessert i matematikken er det
  kanskje like greit å hoppa over det.
+ [](notebooks/Smittespreiing)

Demonstrasjonsvideoane
: fokuserer på tekniske detaljar. Dette er videoar som krev meir konsentrasjon, og ein bør absolutt testa ut dei teknikkane som vert demonstrert på eiga hand, før ein gløymer dei. Det er best å sjå dei saman med øvingane.  Me har freista å visa dei vesentlege teknikkane i dei gjennomarbeidde, og demonstrasjonsvideoane skal primært gje ei ny vinkling meir enn nytt stoff.

+ [Demo Kontrollflyt](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=af53d7b8-1435-4957-9ae6-b3ee00cb13fc)
  viser korleis ein lastar ned øvinga og korleis ein bruker variablar,
  vilkår (*if*) og løkker (*for*) i python.
  Denne vart lang (nesten 30 min.) og kanskje litt for omstendeleg,
  men hopp over det som vert for trivielt.
    + [](notebooks/control-empty)
    + [](notebooks/control)

Drilloppgåver
: fokuserer på grunnteknikkar og vert automatisk retta.  Me vil ikkje oppfordra til å leggja stor vekt på desse, men nokon finne dei nyttige tidleg i kurset.

+ Drilloppgåvene finn du på [Moodle](https://capquiz.math.ntnu.no) (CodeRunner).
  Der er to sett denne veka:
    + Øving 1: Variabler og datatyperQuiz
    + Øving 2: Funksjoner, løkker og listerQuiz

Opne oppgåver
: er meir krevjande oppgåver, der ein må kombinera teknikkane og skriva meir kode frå botnen av.

+ [Kontantstraum](Exercises/Kontantstraum)

Utkast til oppgåver
: desse oppgåvene er uferdige, men kan gje idéar til dei som er på jakt etter meir.

+ [](Exercises/Kundedata)
+ [](notebooks/Folkevekst)

Der er rikeleg med oppgåver, og me reknar ikkje med at nokon rekk å gjera alt.
Hensikta med oppgåvene er å visa eit breidt utval av løysingar til etterlikning,
og kvar og ein må leggja vekt på det som dei finn nyttigast og mest interessant.

## Oppsummering

Hovudmålet denne veka er å læra å bruka dei mest grunnleggjande konsepta
i imperativ programmering.
+ Variablar og tilordningar
+ Bolske uttrykk med `==`, `<`, `>`
+ Vilkårssatsar med `if` og `else`
+ Løkker med `for` og gjerne `while`
+ Utskrift med `print`
+ Plotting med `matplotlib`

Det er mykje stoff, og ein kan lett missa motet om ein er
oppteken av å hugsa detaljane.
Det er derimot med programmeringssspråk som med andre språk,
at me lærer dei ved å sjå korleis dei vert brukte.
Detaljane kjem av seg sjølv når ein bruker språket.
