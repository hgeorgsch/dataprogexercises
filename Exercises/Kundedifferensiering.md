---
tags:
  - exercise
---

# Kundedifferensiering

Denne oppgåva byggjer på [Marknadssimulering](/notebooks/Marknadssimulering), som
bruker ein svært primitiv modell for kjøpsåtferd.
Me kan laga ein meir sofistikert åtferdsmodell vha. teoriar frå 
[Markedsføring Grunnkurs](https://www.ntnu.no/studier/emner/AM101108#tab=omEmnet).
Her skal me ta for oss to konsept som kan brukast, for dei som har teke kurset
i marknadsføring.

+ *Segmentering.* Me talar ofte om ulike segment av kundemassen, der kvart
  segment har liknande åtferd, som skil seg mykje frå andre segment.
+ *Elastisitet* handlar om kor prissensitiv kunden og varen er.
  Somme livsviktige varar kjøper folk uansett pris, medan luksusvarar gjerne
  er meir prissensitive.

Det er naturleg å utvida marknadssimuleringa med kundar i ulike segment og
med varar i ulike kategoriar med ulik priselastisitet.
Her skal me sjå på ei primitiv løysing.
[](Agent-basert%20Marknadssimulering) tek for seg ei objektorientert
løysing.

Lat oss gå ut frå to varekategoriar, livsnaudvendigheit og luksusvare,
og to kundesegment, snobb og navar.

::: {admonition} Oppgåve
Med utgangspunkt i [Marknadssimulering](/notebooks/Marknadssimulering), skriv
nye variantar av `kjopssannsyn()` for kvar kombinasjon av varekategori og
kundesegment, altso fire forskjellige kjøpsåtferdar.
:::

::: {admonition} Oppgåve
Lag ein ny varekatalog som skil mellom dei to varekategoriane.
:::

::: {admonition} Oppgåve
Skriv om simulatoren slik at han simulerer $n$ snobbar og $m$ navarar,
og bruker rett kjøpsåtferd for kvar varekategori.
:::

::: {admonition} Refleksjon
Sjå for deg ulike nabolag.  
På Snobbetoppen bur der 200 snobbar og 100 navarar.
På Navarseter er det omvendt, med 200 navarar og 100 snobbar.
Samanlikna optimal prissettingsstrategi for ein butikk på Snobbetoppen
og ein på Navarseter.
:::

