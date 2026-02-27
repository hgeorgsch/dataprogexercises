

# Tidsrekkjer og frekvens

Hei.

Du vet forhåpentligvis allerede hva en tidsrekke er, et numerisk signal langs en tidsakse.

I denne videoen skal jeg problematisere tidsaksen.

(`20. okt. 2025`)

Den første utfordringen er representasjon.

På norsk kan vi skrive 20. oktober 2025, eller forkorte 20. okt 2025, eller skrive 20/10/25.
FN anbefaler 2025-10-20, men amerikanerne skrive 10/20/2025.  Ikke en gang engelskmennene er enige med amerikanerne og skriver dagen først som oss.

Når vi laster ned en tidsserie kan vi risikere å finne alle disse skrivemåtene og mange flere.

(from datetime import datetime)

Ingen av strengformatene gjør det noe enkelt å regne på tid.
Hvis vi skal ha maskinen til å formattere tidsaksen pent i et plott, eller holde rede på hvor lange tidsperioder er i forhold til hverandre, er vi nødt til å bruke en datatype som maskinen forstår som tid.

I python har vi to som er viktige.  Den generelle typen `datetime` representerer tidspunkt.
I pandas har vi også typen `Period` som representerer perioder, og som dermed er mer egnet for mange tidsrekker.

Internt i maskinen er gjerne tidspunkt representert som sekunder efter 1. januar 1970, men det spiller ingen rolle når vi bruke datetime, fordi typen har de metodene vi trenger for å oversette mellom visningsformater.

(tidssoner)

`datetime`-typen kan også håndtere ulike tidssoner og sommertid.
Jeg skal ikke gå inn i alle detaljene her.  Da er det bedre at dere ser på øvelsene eller referansemanualene.

(periode)

Tidsaksen i tidsserier kan ta to ulikeformer.  Ta værdata som et eksempel.

Når vi måler temperaturen, så måler vi den helst på ett bestemt tidspunkt.
Temperaturen på et bestemt sted klokken syv om morgenen den 1ste januar er veldefinert.

Derimot gir det ingen mening å måle nedbøren kl. syv om morgenen.  Det regnet som faller akkurat på slaget syv er neglisjerbart, og matematikerne vil is null. Det som gir mening er å måle nedbør over en periode, f.eks. 24h fra midnatt til midnatt, eller 1h mellom seks og syv.

Hvis vi oppgir temperaturen den 1ste januar må vi regne med at folk spør hva vi mener.
Når målte vi?  Eller er det et gjennomsnitt?  Minimum?  Maksimum?

(units of time)

Når vi formatterer tidsserier, er vi nødt til å tenke på oppløsningen på tidsaksen.
Ønsker vi å måle hver time, eller hvert år?

Av og til har vi behov for å sammenligne tidsserier fra datasett med forskjellig oppløsning.
Det  er overraskende enkelt å få til i pandas.

Periodetypen lar oss definere indekser med ulik periodelengde.  Kanskje har vi ett datasett med månedlige data og ett med kvartalsvise data.  Hvis vi skal sammenligne de to, er det naturlig å oversette de månedlige data til kvartalsdata.  Det gjør vi i tre steg.

(`df["kvartal"]`)

Først definerer vi en ny søyle som der vi oversettter månedsperiodene til kvartalsperioder.  Da vil vi få et datasett med tre observasjoner per kvartal.

Derefter grupperer vi dataene som har samme kvartal.  Det gir oss et spesielt *group by*-objekt i pandas.

Vi trenger ikke tenke så mye på hva *group by*-data er for noe.  Det som er vesentlig er steg 3 der vi velger en aggregeringsfunssjon, f.eks. gjennomsnitt, maksimum eller sum, og så bruker vi den for å slå sammen hver gruppe til én rad.

Prinsippet er at vi først definerer en ekstra søyle som representere

(kurve)

Det er ikke bare ved sammenligning at vi kan ønske oss *lavere* oppløsning på tidsserien.
Hvis vi gjør spottmålinger eller svært hyppige målinger får vi ofte svært mye tilfeldig variasjon.  Det kan være vanskelig å se trenden, fordi tilfeldige variasjoner fra dag til dag overskygger helhetsbildet.

Har vi periodedata kan det av og til være nyttig å oversette til lengre perioder for å glatte ut tilfeldige variasjoner. Har man punktdata, er det ikke uvanlig å regne et glidende gjennomsnitt, der hvert punkt erstattes med gjennomsnitt over en periode.


(Slutt)

Tid kan være vanskeiig, og jeg har bare pekt på noen få men forhåpentligvis nyttige teknikker.
