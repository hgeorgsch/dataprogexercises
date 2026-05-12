---
title: Personvern
author: Hans Georg Schaathun
date: Mai 2026
tags:
  - lecture/video/perspective
css:
  - css/templates.css
---

# Personvern

note:
En av de virkelig store etiske og juridiske utfordringene i dataanalyse er personvern.
Svært ofte ønsker vi å behandle data som vi selv eier.
Ofte er det snakk om personopplysninger som i prinsippet tilhører den enkelte person.
Vi har slike data blott på lån med et spesifikt og avgrenset formål.

Det gjelder også data som kan være karakterisert som åndsverk, og som dermed er underlagt opphavsrett efter åndsverksloven, men det skal vi hoppe over i dag.

Personvern har blitt et hett tema i det offentlige ordskiftet eftersom det sakte men sikkert går opp for oss hva særlig sosiale medier klarer å bruke våre data til.

I dette foredraget skal jeg gi en kort introduksjon med vekt på det som dataanalytikere trenger å ta ansvar for, når de samler inn eller benytter persondata.


---

> Alle har rett til respekt for privatlivet og familielivet sitt, for heimen sin og kommunikasjonen sin. Det må ikkje utførast husransakingar, så nær som i kriminelle tilfelle.

> Dei statlege styresmaktene skal sikre eit vern om den personlege integriteten.

[Kongeriket Noregs grunnlov](https://lovdata.no/nav/lov/1814-05-17-nn/) §102 (2014)

note:
I Norge er  personvernet er forankret i grunnloven, og det i en langt videre forstand enn det vi gjerne tenker på i datasammenheng. Likevel, kommunikasjon er nevnt, og det er et eksempel på data.

Vi burde kanskje heller ha snakket om  *personopplysingsvern* i vår sammenheng, for å skille det fra det langt videre begrepet *personvern*.

---

> Huusinqvisitioner maae ikke finde Sted, uden i criminelle Tilfælde.

Kongeriket Noregs grunnlov §102 av 17de mai 1814

note:
Bestemmelsen om personvern kom inn i Grunnloven i 2014.  I 1814 var man blott bekymret for husransakelser.

> husinkvisisjoner må ikke finne sted uten i kriminelle tilfeller

Eidsvollsmennene så antagelig ikke for seg hvordan personopplysninger kan misbrukes.

---

[Personopplysingslova](https://lovdata.no/nav/lov/2018-06-15-38?q=personopplysingslova)
<!-- element class="[[r-fit-text]]" -->

GDPR
<!-- element class="[[r-fit-text]]" -->

note:
I Norge er behandling av personopplysninger regulert av personopplysningsloven, som bygger på den velkjente EU-forordningen GDPR.

Det er vel verd å sette segg inn i GDPRs Artikkel 5 som på mange måter gir et overblikk, og som etablere gode etiske grunnprinsipper. 


---

Art. 5.1.a.  Lovlig behandlingsgrunnlag, rettferd og openheit
<!-- element class="[[r-fit-text]]" -->

note:
All behandling av personopplysninger krever et behandlingsgrunnlag som forteller hvorfor behandling er lovlig. 
Samtykke er én form for behandlingsgrunnlag er informert samtykke.
Når vi samler inn data til forskning og lignende, er det samtykke som gjelder.

Andre former for behandlingsgrunnlag forutsetter at personopplysningene er nødvendige for å oppfylle andre forpliktelser, som kan følge av avtaler med den registrere, av lovpålegg eller allmennhetens interesse. Databehandlerens egeninteresse gir derimot aldri noget behandlingsgrunnlag.

GDPR krever også at behanlingen er i tråd med allmenn oppfatning av rettferdighet.

Det siste punktet i art. 5.1.a er openhet, dvs. at den registrerte skal ha innsyn.

---

Art. 5.1.b.  Formålsavgrensing
<!-- element class="[[r-fit-text]]" -->

note:
Behandlingsgrunnlaget gir ingen blankofullmakt.
All registrering av personopplysninger skal ha et bestemt og avgrenset formål.
Behandlingsgrunnlaget gir anledning til å bruke data bare til det formål som er presisert i grunnlaget.

---

Art. 5.1.c. Dataminimering
<!-- element class="[[r-fit-text]]" -->

note:
I samme spor gjelder dataminimering.
Det er ikke lov å samle inn mer data enn det som er nødvendig for å oppfylle formålet med innhentingen.
Hvis du kan klare deg uten en opplysning, skal du ikke registrere den.

---

Art. 5.1.d. Riktige data
<!-- element class="[[r-fit-text]]" -->

note:
Persondata skal være korrekte i forhold til behandlingsformålet.

I dataanalyse er dette kanskje ikke særlig relevant, siden vi gjerne analyserer situasjonen på tidspunkt da opplysningene ble samlet inn. Det er viktigere at de som driver kundebehandling forsikrer seg om at de bruker korrekte data.

---

Art. 5.1.e. Avgrensa lagring
<!-- element class="[[r-fit-text]]" -->

note:
I tråd med formålsbegrensning og dataminimering gjelder begrenset lagring.
Det er ikke lov å lagre data lenger enn det som er nødvendig for formålet.

---

Art. 5.1.f. Integritet og konfidentialitet
<!-- element class="[[r-fit-text]]" -->

note:

---

Art. 5.2. Ansvar
<!-- element class="[[r-fit-text]]" -->

---
<!-- slide template="[[tpl-flex]]" bg="white" -->

![[anonymous.png]]]

!!! credit
[Anonymous icons created by Pixel perfect - Flaticon](https://www.flaticon.com/free-icons/anonymous)
:::