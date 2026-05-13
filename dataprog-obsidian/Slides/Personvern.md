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

![[priv01.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
En av de virkelig store etiske og juridiske utfordringene i dataanalyse er personvern.
Svært ofte ønsker vi å analysere data som vi ikke eier selv.
Ofte er det snakk om personopplysninger som i tilhører den enkelte person.
Vi har slike data blott på lån med et spesifikt og avgrenset formål.

Det kan òg gjelde data som er karakterisert som åndsverk, og som dermed er underlagt opphavsrett efter åndsverksloven, men det skal vi hoppe over i dag.

Personvern har blitt et hett tema i det offentlige ordskiftet eftersom det sakte men sikkert går opp for oss hva særlig sosiale medier klarer å bruke våre data til.

I dette foredraget skal jeg gi en kort introduksjon med vekt på det som dataanalytikere trenger å ta ansvar for, når de samler inn eller benytter persondata.


---

> Alle har rett til respekt for privatlivet og familielivet sitt, for heimen sin og kommunikasjonen sin. Det må ikkje utførast husransakingar, så nær som i kriminelle tilfelle.

> Dei statlege styresmaktene skal sikre eit vern om den personlege integriteten.

[Kongeriket Noregs grunnlov](https://lovdata.no/nav/lov/1814-05-17-nn/) §102 (2014)

![[priv02.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
I Norge er  personvernet er forankret i grunnloven, og det i en langt videre forstand enn det vi gjerne tenker på i datasammenheng. Likevel, kommunikasjon er nevnt, og det er et eksempel på data.

Vi burde kanskje heller ha snakket om  *personopplysingsvern* i vår sammenheng, for å skille det fra det langt videre begrepet *personvern*.

---

> Huusinqvisitioner maae ikke finde Sted, uden i criminelle Tilfælde.

Kongeriket Noregs grunnlov §102 av 17de mai 1814

![[priv03.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Bestemmelsen om personvern kom inn i Grunnloven i 2014.  I 1814 var man blott bekymret for husransakelser.

> husinkvisisjoner må ikke finne sted uten i kriminelle tilfeller

Eidsvollsmennene så antagelig ikke for seg hvordan personopplysninger kan misbrukes.

---

[Personopplysingslova](https://lovdata.no/nav/lov/2018-06-15-38?q=personopplysingslova)
<!-- element class="[[r-fit-text]]" -->

GDPR
<!-- element class="[[r-fit-text]]" -->

![[priv04.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
I Norge er behandling av personopplysninger regulert av personopplysningsloven, som bygger på den velkjente EU-forordningen GDPR.

Det er vel verd å sette seg inn i GDPRs Artikkel 5 som på mange måter gir et overblikk, og som etablere gode etiske grunnprinsipper. 


---

Art. 5.1.a.  Lovlig behandlingsgrunnlag, rettferd og openheit
<!-- element class="[[r-fit-text]]" -->

![[priv05.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
All behandling av personopplysninger krever et behandlingsgrunnlag som forteller hvorfor behandling er lovlig. 
Informert samtykke er én form for behandlingsgrunnlag.
Når vi samler inn data til forskning og lignende, er det samtykke som gjelder.

Andre former for behandlingsgrunnlag forutsetter at personopplysningene er nødvendige for å oppfylle andre forpliktelser, som kan følge av avtaler med den registrere, av lovpålegg eller allmennhetens interesse. Databehandlerens egeninteresse gir derimot aldri noget behandlingsgrunnlag.

GDPR krever også at behanlingen er i tråd med allmenn oppfatning av rettferdighet.

Det siste punktet i art. 5.1.a er openhet, dvs. at den registrerte skal ha innsyn.

---

Art. 5.1.b.  Formålsavgrensing
<!-- element class="[[r-fit-text]]" -->

![[priv06.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Behandlingsgrunnlaget gir ingen blankofullmakt.
All registrering av personopplysninger skal ha et bestemt og avgrenset formål.
Behandlingsgrunnlaget gir anledning til å bruke data bare til det formål som er presisert i grunnlaget.

---

Art. 5.1.c. Dataminimering
<!-- element class="[[r-fit-text]]" -->

![[priv07.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
I samme spor gjelder dataminimering.
Det er ikke lov å samle inn mer data enn det som er nødvendig for å oppfylle formålet med innhentingen.
Hvis du kan klare deg uten en opplysning, skal du ikke registrere den.

---

Art. 5.1.d. Riktige data
<!-- element class="[[r-fit-text]]" -->

![[priv08.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Persondata skal være korrekte i forhold til behandlingsformålet.

I dataanalyse er dette kanskje ikke særlig relevant, siden vi gjerne analyserer situasjonen på tidspunkt da opplysningene ble samlet inn. Det er viktigere at de som driver kundebehandling forsikrer seg om at de bruker korrekte data.

---

Art. 5.1.e. Avgrensa lagring
<!-- element class="[[r-fit-text]]" -->

![[priv09.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
I tråd med formålsbegrensning og dataminimering gjelder begrenset lagring.
Det er ikke lov å lagre data lenger enn det som er nødvendig for formålet.

---

Art. 5.1.f. Integritet og konfidentialitet
<!-- element class="[[r-fit-text]]" -->

![[priv10.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Integritet og konfidensialitet er allminnelige kriterier fra informasjonssikkerhet, men de er viktige i forhold til de andre prinsippene for personvern.

Vi krever at personopplysningene skal være riktige, og det innebærer integritet.
Vi krever formålsbegrensning, og det fordrer konfidentialitet. Tilgangen må begrenses til dem som trenger dem efter formålet, og vi må for all del hindre at data blir delt med dem som ønsker å misbruke dem.

---

Art. 5.2. Ansvar
<!-- element class="[[r-fit-text]]" -->

All behandling av personopplysninger krever en behandlingsansvarlig, som vanligvis er en organisasjon og som har det juridiske ansvaret for innsamling og behandling.
Artikkel 5.2 i GDPR slår fast et ufravikelig ansvar som ligger på den behandlingsansvarlige.
Ansvaret kan ikke delegeres.
Selv om deler av arbeidet delegeres til andre databehandlere, hviler alltid ansvaret på den behandlingsansvarlige.

---
<!-- slide template="[[tpl-flex]]" bg="white" -->

![[anonymous.png]]]

!!! credit
[Anonymous icons created by Pixel perfect - Flaticon](https://www.flaticon.com/free-icons/anonymous)
:::

![[priv11.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Personopplysninger er data som kan tilskrives identifiserbare personer.
I dataanalyse er dette sjelden interessant.  Vi er interessert i makrostørrelser, og enkeltindivider er uten interesse.

Hvis vi kan klare å anonymisere dataene, så vil vi stå friere i anvendelsen.

Det kan likevel være kontroversielt å anonymisere data som er samlet inn til et begrenset formål, uten at den registrerte er blitt informert om at dataene vil bli anonymisert for andre formål. Her er der dog en del gråsoner, og reglene er strengere innenfor forskning enn de er for en bedrift som bruker dem til intern kvalitetssikring.

---
<!-- slide template="[[tpl-flex]]" bg="white" -->

![[Artificial_Intelligence_&_AI_&_Machine_Learning_-_30212411048.jpg]]
::: credit
By [vpnsrus](https://www.vpnsrus.com/)
at [flickr](https://www.flickr.com/photos/152824664@N07/30212411048/),
CC BY 2.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=95608113)
:::

![[priv12.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Anonymisering gir derimot en større utfordring enn juridiske spissfindigheter.

Det er ikke nok at dataene mangler navn og fødselsnummer.  All informasjon som kan brukes til å identifisere enkeltpersoner og små grupper må bort.

Maskinlæring har vist seg meget effektivt til å rekonstruere personidentiteter fra tilsynelatende irrelevante data, bare det er nok av dem.
Det som ser anonymt nok ut i  dag, trenger ikke å være det med neste generasjon KI.
Dess mer data vi samler inn, dess vanskeligere er det å anonymisere dem effektivt.

Hvis vi trekker ut noen få variabler per rad i datasettet, så kan anonymisering være effektivt.

---
## Slutt

![[priv13.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Jeg har valgt å styre unna detaljene her.  Der er flere grunner til det. 
I praksis, i en bedriftsammenheng, vil det være vel så viktig å forholde seg til interne regler og *policy*-dokumenter, og vanskelige etiske vurderinger må taes sammen med ledere, IT-støtte og jurister som kjenner bedriften.

Det jeg har forsøkt å få frem er de grunnprinsippene som krever medvirkning fra dem som faktisk skal bruke dataene.  Forhåpentligvis har jeg gjort det litt lettere å sette seg inn i detaljene når det blir nødvendig. 
