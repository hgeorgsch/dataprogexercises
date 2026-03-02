---
tags:
  - lecture/video/perspective
  - topic/machinelearning
  - lecture/stub
css:
  - css/templates.css
---

# Kva er ein modell?

note:
Dataanalyse handler ofte om å konstruere modeller, enten det er konvensjonelle, statistiske modeller eller mer komplekse maskinlæringsmodeller.

---
<!-- slide template="[[tpl-diagram]]" -->

![[sampling.svg]]

::: credit
:::

note:
I de fleste tilfeller arbeider vi med datasett som beskriver et begrenset utvalg av en større populasjon.
Skal du gjøre en markedsundersøkelse, kan du kanskje spørre tusen potentielle kunder, men det er umulig å spørre alle potentielle kunder.
Skal du forsøke å forutsi hvor sannsynlig det er at en potentiell lånekunde vil misligholde lånet, må du bruke data om historiske lån. Det er umulig å få data om fremtidige og potentielle lånekunder.

I utvalgsstatistikken må vi skille mellom deskriptiv statistikk, som beskriver utvalget vårt, og statistisk inferens, som bruker utvalget til å beskrive populasjonen.

Deskriptiv statistikk er relativt enkelt og beskrivelsene av utvalget er eksakte. I noen tilfeller har vi også tilgang til populasjonsdata, som gjøre det mulig med deskriptiv statistikk på populasjonen. Det gjelder gjerne arbeidsledighetsdata, eksportdata og skattetall, som myndighetene registrerer for hele befolkningen.

Statistisk inferens er mer utfordrende, fordi kunnskap om utvalget aldri gir eksakt kunnskap om populasjonen.

---
<!-- slide template="[[tpl-diagram]]" -->

![[mlloan.svg]]

::: credit
:::

note:
Hva mener vi med en modell?

Statistiske modeller i statistikken søker å beskrive en populasjon.
Hvor stor andel av velgerne vil stemme KrF?  Hvor stor andel av kundene
er fornøyde?

I maskinlæring snakker vi gjerne om prediksjonsmodeller.
Gitt tilgjengelige data om situasjonen i dag, ønsker vi å forutsi ett
eller andet fenomen i fremtiden.
F.eks. sannsynligheten for at en gitt kunde vil misligholde et lån.

I kunstig intelligens kan vi snakke om beslutningsmodeller.
Gitt tilgjengelig informasjon, bør eller bør vi ikke beslutte å gi kunder lån?

Selv om der er en åbenbar sammenheng mellom prediksjon og beslutning,
er der en vesentlig forskjell.
Prediksjonsmodellen er rent deskriptiv, mens beslutningsmodellen er normativ.
Vi skal holde oss til prediksjonsmodeller.

---
<!-- slide template="[[tpl-ntnu]]" -->

**modell**
$\sim$
*selektiv representasjon av et system som presist og konsist viser de egenskaper som vi er interesserte i*.

note:
Jeg tenker på en modell som en
*selektiv representasjon av et system som presist og konsist viser de 
egenskaper som vi er interesserte i*.

I maskinlæring er den interessante egenskapen, sammenhengen mellom en samling
innvariabler på den ene siden og en eller flere utvariabler på den andre.

Når jeg sier at modellen er selektiv, betyr det at vi gjerne laver 
forskjellige modeller for hver analyse, avhengig av hvilke egenskaper vi 
er interessert i.  

---
<!-- slide template="[[tpl-twocolumn]]" -->

::: leftimage
![[GeorgeEPBox_(cropped).jpg]]

:::

::: leftcredit
Bilete ved DavidMCEddy at en.wikipedia, CC BY-SA 3.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=115167166)
:::

::: rightimage
> Alle modellar er feil, men somme er nyttige.
<!-- element style="font-size: 160% ;" --> 
:::

::: rightcredit
:::

note: 
Det er eit kjent ordtak at alle modeller er feil, men at noen modeller er nyttige. Det tilskrives gjerne George Box som brukte det i en artikkel i 1976.

Dette er en konsekvens av at modellen er selektiv og tilpasset en bestemt analyse som vi ønsker å gjøre.  Når vi fremhever de vi ser som nyttig, aksepterer vi også feil og unøyaktigheter ved andre sider av modellen.
Hvis vi prøver å gjøre alt perfekt, blir modellen så kompleks at vi ikke klarer å analysere den.

Eller hvis vi driver med maskinlæring, at modellen blir for tung til å kjøre.


---

# Slutt

note:
Dette bringer oss til det som er den mest sentrale utfordringen i statistikk, maskinlæring og modellering for øvrig.
Hvordan vet vi at modellen er riktig nok?
Hvordan måle sannsynligheten og størrelsen på feilene som modellen gjør?

Det er tema for neste video.  Hei så lenge.