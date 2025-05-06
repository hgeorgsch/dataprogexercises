
# EVU programmering og data i økonomiske fag


Tanker om formål og fremgang

### Mål med kurset/kompetanser/ferdigheter og kunnskap

+ Ferdigheter:
	+ Bruke python selvstendig i faglig sammenheng
		+ Pandas
		+ Grafisk fremstilling
		+ Simulering
		+ Maskinlæring
		+ Beregning/light

Ferdigheter i #pandas krever ferdigheter eller forkunnskaper i generell python/programmering. 

+ Lister og dictionaries: Meget viktig
	+ Lage de med løkker og komprehensjoner
	+ Gå igjennom de og velge ut deler av de manuelt
	+ Hente ut metadata - unike verdier, lengder, datatyper
	+ Traversere datastrukturen for å finne relevante deler
+ Variabler og datatyper: Meget viktig
	+ Forstå viktigheten av å ha kontroll på *datatypene* til datapunktene
		+ Forskjell på heltall og flyttall
		+ Tekststrenger og hvordan disse lagres (tegnkoding)
		+ Representere tid og perioder
	+ Tilordning og refering til variabler - forandre de gjennom funksjonskall, direkte
+ Boolsk aritmetikk: viktig
	+ Relevant for filtrering og uthenting av data - men ofte ganske intuitivt
	+ God innsikt i "spørringene" blir viktig når det blir mer komplisert å hente ut data
+ Kontrollflyt: mindre viktig
	+ noe bruk av if-else, continue, men vi kan gjøre mye uten dette
+ Plotting med pyplot/seaborn: Mindre viktig
	+ Innebygde plot-funksjoner krever veldig lite av forkunnskaper
	+ Vi bruker ikke innebygd plot-api for full kontroll av figurer (nødvendig)
+  Funksjoner: mindre viktig
	+ Vi kan gjøre det meste uten å være veldig drevne i å lage egne funksjoner, men må kunne enkle funksjoner

Viktig eller mindre viktig i denne sammenhengen er relevant for hvor ønskelig det er  at disse forkunnskapene er på plass i forkant. Dette slik at man ikke må lære rimelig forskjellige konsepter parallelt med mye hopping frem og tilbake.

For å bruke pandas godt og effektivt burde man kunne «tenke funksjonelt» og transformere dataframes med `map()` og `apply()` og bruke funksjoner til å strukturere programmeringen.
Lambdauttrykk blir også nyttig. Dette trenger ikke være fullstendig på plass *før* man setter i gang med pandas

Gode ferdigheter i dataanalyse vil også bety gode ferdigheter i et eller flere plottebibliotek (pyplot, seaborn), men dette kan komme senere. 

### Vi ønsker å begynne med pandas og ekte data nesten umiddelbart

Spørsmålet er hva er minimumsstedet man må være før man begynner med pandas, og hvorvidt kan ekte data i en csv-fil lastet inn gjennom pandas være kontekst eller bakteppe for å lære de generelle programmeringsferdighetene


   + Om filen er «perfekt formatert» trenger `pd.read_csv()` kun filnavn -- tegnkoding, og alt annet kan komme senere (kanskje ta med -- index = ..)
   + Om filen er «perfekt formatert» trenger man ikke nødvendigvis deale med datatyper og vasking
   + Lese ut kolonner, rader eller datapunkt gjøres med `.loc["rad", "kolonne"]`, eller bare `df["kolonne"]` - greit helt til man begynner å slice
   + Legge til kolonner: kan gjøres med `.map()`, krever litt funksjoner, med listekomprehensjoner
   + Plotte -- innebygd `.plot()` kan kreve ingen ekstra arbeid
   + Deksriptiv statistikk: Krever ingenting annet enn kall til API (describe, mean, min, max osv)

#### Første datasett:

   + Studenten kan definere egne funksjoner av den «matematiske typen» (ingen sideefekkter eller avhengighet av global state)
   + Studenten kan lage enkle lister med listekomprehensjon
   + Studenten kan litt om datatyper, og er komfortabel med tilordning av variabel

Vi gir forhåndspreparert ekte dataset med indeks og 1 kolonne, eventuelt indeks og 2 kolonner - Eks: Arbeidsledighet, åpnede konkurser.
Vi henter ut nøkkeltall og plotter kolonner (linjeplott)

Vi kan bruke første datasett som bakteppe til å lære om ullike datatyper

#### Andre steg:

Studenten kan en del om datastrukturer og hvordan man manipulerer og lager disse.
Vi kan da lage nedbetalingsplan for et lån i et pandas dataframe.

Eventuelt kan vi ha pandas som bakteppe:
Vi vil lage en nedbetalingsplan -- hvordan strukturerer vi slik data, hvordan behanlder vi dette i pandas
Vi vil føre oversikt over saldo på konto for kunder -- hvordan strukturerer vi slik data, hvordan behandler vi dette i pandas

##### Kan vi bruke ekte data?
Oppgaveidé:
Studentene samler in data om hverandre i kurset (eventuelt kan vi anonymisere).
Oppgaven kan være å strukturere data som navn, alder, yrke, utdanning osv - og deretter fremstille denne dataen

Kanskje kan man finne faktisk innsikt om man henter inn data som "Hvor «flink» er du?" + "Hvor «flinke» er medstudentene dine" eller noe annet

Vi kan også problematisere hvordan vi skal anonymisere datainnhentingen eller andre aspekter ved persondata



### Introdusere Løkker

[[Simulering av kontantstraum]] er godt utgangspunkt for å introdusere løkker. Pandas baserer seg på vektorisering -- Vi kunne kanskje ha sammenlignet hurtighet mellom pandas sine vektoriserte varianter (feks legge til ny kolonne med map el.) og en "bruteforce"-iterasjons-variant


