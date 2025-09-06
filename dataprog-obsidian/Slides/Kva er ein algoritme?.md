---
tags:
  - lecture/video/perspective
---

# Kva er ein algoritme?

note:
*Algoritme* er et ord som vi hører stadig oftere brukt.
Algoritmene får gjerne skylden for alle dårlige beslutninger i sosiale medier og kunstig intelligens, men helst uten en presis forklaring på hva det er for noe.

Algoritmene fremstår lett, med rette eller urette, som en mystisk kraft som tar stadig større makt over livene våre.

---

<!-- slide template="[[tpl-diagram]]" -->

![[flowchart.svg]]

::: credit
:::

note:
En vanlig analogi er å se på algoritmen som en oppskrift.
Kokeboken er egentlig full av algoritmer som forklarer steg for steg hvordan man går frem for å oppnå et bestemt resultat.

Det er viktig å merke seg at algoritmen er prosedyren og ikke teksten som beskriver prosedyren.  Dét er på mange måter også den kritiske forskjellen på en algoritme og et dataprogram.  Dataprogrammet er en konkret implementasjon, skrevet i et bestemt sprog, for å kjøre på en bestemt type maskin.  Algoritmen er en abstrakt beskrivelse av hvordan programmet skal gå frem.

For å programmere ryddig og korrekt er det ofte nyttig å kunne beskrive algoritmen på forskjellige måter, slik at man ikke henger seg opp i særegenhetene i f.eks. python.  Det kan være nyttig å formulere algoritmene sine både i visuelle diagrammer, vanlig dagligsprog og matematiske formler.

La oss ta et eksempel på visuell fremstilling.  Her «algoritmen» for å lave lapper.

Denne typen diagrammer kalles gjerne flytdiagrammer; de viser flyten fra operasjon til operasjon; og de har vært mye brukt for å dokumentere programmer og algoritmer i industrien.  

Vi begynner på start.  Det første steget er å hente ingrediensene.  Parallellogrammet signaliserer I/O dvs. *input/output*.  

Romben indikerer en valgmulighet, eller *if*-sats.  Her må vi ta stilling til om vi ønsker lapper på amerikansk eller sunnmørsk manér.  Hvis vi vil ha amerikanske *pancakes* går vi til venstre og begynner med å skille eggene.  I motsatt fall går vi til høyre og pisker eggedosis.

Rektanglene er operasjoner som utføres i rekkefølge langs pilene.

Etter eggedosisen skal vi tilsette surmelk og mel vekselvis. Da ser vi at pilene går i ring. Så lenge der er mer mel elller melk igjen, må vi gå tilbake og tilsette mer.
I programmering kaller vi det en løkke, som i python gjerne skrives med *while* eller *for*.

På slutten går de to programgrenene sammen, for stekingen er den samme uansett røre. Vi har en ny løkke når vi venter på at takken skal bli varm, og periodisk må sjekke om den er varm nok.  Serveringen har jeg notert som en I/O-boks, dvs. at lappene er *output* fra oppskriften.

Dette flytdiagrammet er selvsagt litt slurvete og ufullstendig oppstilt. Det verste er sikkert at ingrediensene ikke er spesifisert. Om en maskin skulle ha kjørt programmet, ville den også hatt problem med skjønnsmessige vurderings som «litt mel» eller hvorvidt takken er *passe* varm. 

Poenget er likevel å illustrere det generelle i algoritmisk tenkning. Kontrollflyt med løkker og *if*-satser er ikke noe som bare forekommer i programkode, og kode er ikke den eneste måten å presentere programmet på.  Det er viktig å kunne heve blikket, og tenke på *hva som skjer* og ikke bare hvordan det *skrives*-

Det er heller ikke noe galt i å bruke slurvete og ufullstendige fremstillinger.  Det er som regel plassen å begynne for 

---

![[addition.png]]


note:
Det erketypiske eksempelet på algoritmer er addisjon og multiplikasjon slik som vi lærer det på barneskolen.  Vi stiller tallene pent opp, og regner ett siffer ad gangen.  Hvert siffer behandles likt, slik at vi kan bruke en løkke, og hvert siffer behandles uavhengig av det foregående, bortsett fra den lille variabelen som vi kaller mente. 

Dette er faktisk den opprinnelige betydningen av ordet *algoritme*.

---


<!-- slide template="[[tpl-twocolumn]]" -->

::: leftimage

![[Madrid_-_Ciudad_Universitaria,_Monumento_a_Muhammad_al-Juarismi_(cropped).jpg]]

:::

::: leftcredit
By Zarateman - Own work, CC0, 
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=162213187)
:::

::: rightimage

**Muḥammad ibn Mūsā al-Khwārizmī**

 محمد بن موسى الخوارزميّ**


::: 

::: rightcredit
:::

note:
Det er denne karen som har skylden får at vi sluttet å regne med romertall i Europa:
Muḥammad ibn Mūsā al-Khwārizmī.  Han var perser, men skrev på arabisk.

---
<!-- slide template="[[tpl-quote]]" -->

![[CaspianSeaDrainage_v1.png]]

::: credit
By Redgeographics - Own work, CC BY-SA 4.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=68241901)
:::

note:
al-Khwārizmī betyr «fra Khwarizmi» som er området rundt Aralsjøen på grensen mellom Khasakstan og Usbekistan.  Aralsjøen var en gang kjent som Khwarizmisjøen, og det er dette navnet som ble til algoritme på europeiske sprog, fra «alkwarisme» til «algoritme».

---

<!-- slide template="[[tpl-quote]]" -->

![[Image-Al-Kitāb_al-muḫtaṣar_fī_ḥisāb_al-ğabr_wa-l-muqābala.jpg]]

::: credit
By Al-Khwarizmi - Esposito, John L. , ed. (1999) 
*The Oxford History of Islam*, Oxford University Press ISBN: 0195107993. ;
April 2006 (upload date) by Spm, Public Domain, 
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=716423)
:::

note:
Mohammad fra Khawarismi skrev flere bøker.  En av de viktigste, som ble spredd og oversatt i Europa på 1100-tallet, forklarte hvordan man regner med posisjonssystemet, der vi har egne plasser for enere, tiere, hundreder, osv.

Disse tallene kaller vi  gjerne for arabertall i motsetning til romertall, selv om Muhammad antagelig hentet dem fra Indien.

---

![[roman.png]]

note:
Hvis vi prøver å forestille oss norditalienske renesansekjøbmenn som skulle føre sine regnskaber i romertall, og nitidig legge sammen inntekter og utgifter, er det lett å se at tallene fra Khwarizmi har hatt stor betydning for vår del av verden.

De som regnet med arabertall ble efter hvert kjent som algoritmikere, altså efterfølgere efter al-Khwarizmi, i motsetning til f.eks. abakister som brukte kuleramme.

---
<!-- slide template="[[tpl-quote]]" -->

::: credit
By Charles Babbage - Upload by Mrjohncummings 2013-08-28 15:10, CC BY-SA 2.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=28024313)
:::

---
<!-- slide template="[[tpl-quote]]" -->

![[Ada_Lovelace_portrait.jpg]]

note:
Den moderne algoritmen tilskrives gjerne Ada Lovelace, som utviklet algoritmer til *the Analytical Engine*.

::: credit
By Alfred Edward Chalon - Science Museum Group, Public Domain
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=28131684").
:::

---

# Slutt
