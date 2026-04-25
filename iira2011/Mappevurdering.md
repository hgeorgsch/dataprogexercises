---
tags:
  - assessment
  - practical-info
---

# Mappevurdering

+ **Frist** Sjå eksamensplan
+ **Innlevering** i Inspera

Vurdering (studiepoeng og karakter) vert basert på ei innlevert mappe,
der kandidaten viser fram utvalde arbeid frå semesteret og reflekterer
over korleis dei er nyttige i praktisk virke.
I tillegg er det eit obligatorisk arbeidskrav å presentera og drøfta
éi oppgåve mappa vert presentert munnleg på midtvegssamlingsa.

## Mappeinnleveringa

Mappa må leverast som ein ZIP-fil

+ Del 1: *essay* med utgangspunkt i ei simulering
      (Jupyter Notebook-format).
      Dette skal visa at kandidaten meistrar grunnleggjande programmering,
    + **Minstekrav** viser bruk av løkker, vilkårssatsar (*if*) og variablar.
    + Meir avanserte studentar vil gjerne bruka funksjonar til å forenkla koden og
      klasser og objekt til agent-basert simulering.
+ Del 2: *essay* med utgangspunkt i analyse av eitt eller fleire datasett
      (Jupyter Notebook-format).  Dette skal visa at kandidaten kan bruka python
      til dataanalyse.
    + **Minstekrav** viser innlasting, formattering og visualisering av datasett.
    + Der er mange tema som kan visa høgare måloppnåing, inkl. samanstilling av datasett frå
      ulike kjelder, aggregering av data i større tidsintervall og klassifikasjon og regresjon med
      maskinlæring.
+ Del 3: refleksjonsnotat (1-2 sider) der kandidaten oppsummerer kurset
      og den verdien det har for vidare virke.
      (Jupyter Notebook eller PDF)
+ Deklarasjonsskjema for KI; sjå
  [Kunstig intelligens i studentoppgaver](https://i.ntnu.no/wiki/-/wiki/Norsk/Kunstig+intelligens+i+studentoppgaver)
+ Vedlegg: alle datafiler (t.d. CSV) som trengst for å køyra koden.

Det er ikkje venta at Del 1 og Del 2 har same omfang.
Éin av delane bør visa djupna i eige interesseområde.
Den andre delen skal visa breidd, slik at båe hovudområda i pensum er
dekte.
Kandidaten har ansvar for å visa både breidde- og djupnakunnskap i
faget.

Bå midtvegs- og avslutningssamlinga vil me ha eit seminar der
deltakarane presenterer og drøftar arbeidet til Del 1 og Del 2
i mappa.
Det er ein føresetnad for å levera mappe til vurdering at ein
gjer dette minst ein av gongane.
Sjølv om tanken er at ein drøfter og for innspel til arbeid
som ein planlegg å bruka i mappa, står ein fritt til å bruka
anna materiale i innleveringa, dersom ein ynskjer det.
Sjå [obligatorisk arbeidskrav](Oblig) for meir informasjon.


## *essay*-formatet

Når me bruker ordet *essay* om dokumenta som inngår i mappa, so er det
med ei viss tilsikta tvityding.  Opprinneleg er ordet fransk og tyder
forsøk, men på engelsk tyder det gjerne skulestil.  

Hovudpoenget som me understreker ved å bruka ordet er
1.  *Essayet* er ein frittstående tekst som kan lesast utan å sjå
    oppgåveteksta.
2.  *Essayet* er fagleg og velbegrunna, men ikkje tunglest.
3.  *Essayet* er ein samanhengande tekst som tek lesaren med i resonnementet.
    Kvar idé skal vera ei naturleg og logisk vidareføring av det som kjem forut.
4.  *Essayet* tek for seg eit problem som er verd å drøfta.

Programmeringskoden skal vera ein del av resonnementet som ligg til grunn for *essayet*.
Resonnementet kan ta for seg ein modell, ein teori eller eit datasett, og koden
bidreg med utrekningar, t.d. med simulering av modellar, testing av teoriar eller
visualisering av datasett.  Koden er verdilaus utan eit resonnement som gjev
ein modell å koda, og like verdilaus utan eit resonnement som tolkar resultata
som kjem ut.  

Det tyder sjølvsagt ikkje at ein skal ta lett på koden.
*Essayet* skal argumentera for at programmeringskoden gjer som han skal.
For kvar einaste kodeblokk vil normalt ha 
1.  ein innleiande *essay*-blokk som forklarer kva ein ynskjer å oppnå med koden,
    gjerne med ei skildring av modellen og konsepta som ein nyttar
2.  koden som løyser problemet,
3.  ein test eller ei utskrift som viser at koden gjer noko, 
5.  ei forklaring på korleis koden stemmer med problemet eller modellen
    som vert drøfta, samt
4.  ei tolking av testen eller utskrifta, med refleksjon som tek stilling
    til om dette er som venta eller om noko er feil.

Når ein har mykje å seia, er det alltid best å seia éin ting åt gongen.
Difor bør kodeblokkane ikkje vera for lange dersom ein kan unngå det.
Det er sjølvsagt ikkje råd å dela opp funksjons- og klassedefinisjonar,
og då treng ein kanskje kommentar<r i sjølve koden.  Likevel er
det slik at ein bør testa kvar funksjon og metode for seg.

Dette er eit kurs i programmering, men det skal helst vera eit kurs
i bruka programmeringa til noko nyttig og interessant, og kunna
forsikar seg om at resultatet korrekt.
Det er dette *essay*-formatet skal visa.


## Kunstig Intelligens (og juks)

Kunstig Intelligens (store språkmodellar) kan gjera store delar
av programmeringsarbeidet, men der er òg ting KI ikkje kan gjera.
Difor er KI generelt eit lovleg verkty, og vurderinga legg størst
vekt på det som KI ikkje kan gjera.
Me skal vera særleg nøye med å
1.  forklara kva du ynskjer å oppnå med programmeringskoden,
    Koden skal ha ei tydleg hensikt.
2.  testa og validera all programmeringskode.  Korleis *veit* du
    at koden gjer det du ynskjer?
3.  vurdera og reflektera over resultata.
    Kva kan me læra av resultate?
4.  visa til kjelder der du har henta materiale frå andre.

Røynsler frå liknande emne viser at KI ikkje får toppkarakterer på denne
typen oppgåver, men ståkarakter er mogleg.  Ein av funksjonane til det
obligatoriske arbeidskravet er å sikra at alle som leverer mappa, har 
den minimumsforståinga som krevst for å få emnet godkjend.

Dersom du bruker KI i stor grad er det naturleg å reflektera over
det i refleksjonsnotatet.  Kva kan KI gjera godt, og kva treng
du å tenkja på sjølv.

Merk at det er **juks** å bruka arbeide (tekst, modellar, kode) frå andre
utan å oppgje kjelde.  Dette prinsippet er det same uansett om arbeidet kjem
frå kunstig intelligens, medstudentar, bøker eller tilfeldige diskusjonar på
nettet.  
So lenge kjeldene er oppgjevne, er alt *lov*, men det kan stadig vera **slett arbeide**.  
Godt arbeide er kjenneteikna ved eigen validering og grunngjeving, 
kontekstualisering og bruk av fleire kjelder saman med eigne idéar.

## Refleksjonsnotatet

Refleksjon i denne samanhengen er sjølvrefleksjon, dvs. eit kritisk blikk
korleis du løyser oppgåva, kvifor du ynskjer å løysa ho, og kva du lærer av det.

Det er viktig å bruka refleksjonen til å framheva læringsutbytet du har hatt
gjennom arbeidet med oppgåva.  Målet med kurset er ikkje at de skal læra akkurat
det som me har planlagt, men at de skal læra noko som vil vera nyttig for dykk.
Av og til kjem det av ei utfordring litt på sida av planen, men det gjer det ikkje
mindre verdifullt.  For å få uttelling for det som de har strevd med, so må de
reflektera over utbytet dykkar.

Likeeins er det viktig å framheva det som er verdifullt for dykk.  Sensuren skal
leggja vekt på det som har verdi for dykk, og ikkje det som sensor finn verdifullt
i si eiga kontekst.  Det tyder sjølvsagt ikkje at me kan gå utanom læringsutbyta
i emneskildringa, men dei er vage nok til at de kan framheva på ulike ting i
refleksjonen.


## Vurderingskriterium

Mappa vert vurdert etter seks aspekt som oppsummert i tabellen, der fire av dei vert vurdert
to gongar, ein gong på Del 1 og ein Del 2.
Ståkarakter (E) krev at kvart aspekt vert vurdert tilfredstillande (E eller betre).
Dvs. anten Del 1 eller Del 2 må vera tilfredsstillande etter alle fire aspekt, og
i tillegg må originalitet og refleksjon vera tilfredsstillande.
Dersom dette er tilfredsstilt, vert karakteren fastsett som gjennomsnitt av aspekta 
og avrunda etter vanlege avrundingsreglar.

Mappa vert vurdert som ein heilskap, og det er opp til kandidaten å velja ut oppgåver som demonstrerer breidd og djupna. Som kriteria under viser er det ein del av læringsmålet å sjå den praktiske verdien i *eigen* karriere.

| Aspekt       | Ikkje greidd (F/0)                                                                       | Greidd under tvil (E/1)                                                                           | Dugleg (C/3)                                                                                                                | Imponerande (A/5)                                                                              |
| :----------- | :--------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| Teknisk nivå (per del) | Mappa viser ikkje tilstrekkelege teknikkar til å løyse meiningsfulle, praktiske problem. | Mappa viser dei programmeringskonstruksjonane som er nemnde som minstekrav. | Mappa viser kompetent bruk av python med variasjon i teknikkane som vert brukte. | Mappa viser stor breidd og djup forståing av teknikkar og konsept.                             |
| Testing og validering (per del) | Der er lite eller ingen forklaring til koden.[^tv]  | Koden er stort sett forklart, men overflatisk og utan overtyding. | Koden er stort sett forklart og testa.  Der er ingen tvil om at kandidaten veit kva som føregår.  | Koden er grundig testa og det er sjelden tvil om at alt er korrekt. |
| Kodekvalitet (per del) | Der er mykje feil i koden, og koden gjer ikkje det teksta seier.                    | Koden er korrekt[^kor], men vond for lesaren å forstå.                                                  | Koden er lesbar[^les], med stort sett god bruk av variabelnamn og kommentarar, sjølv om nokon løysingar kan vera unødig tungvinte. | Koden er plettfri og lesarvenleg, med god bruk av effektive og enkle løysingar der det er råd. |
| Analyse (per del) | Der er lite eller ingen tolking av resultat.                                             | Resultat er kommentert på ein fornuftig om ikkje innsiktsfull måte.                               | Mappa bruker resultat til å seia noko konstruktivt og nyttig om problemet, særleg i Del 2.                                  | Mappa viser kreativ og innsiktsfull analyse av resultata.                                      |
| Originalitet (samla)| Oppgåvene i mappa er kopi av kjende døme mest utan variasjon.                                 | Mappa inneheld enkle men tydelege variasjonar over utleverte øvingar og døme                                   | Mappa bruker gjennomgåtte teknikkar i nye kombinasjonar og på nye datasett, i minst ein av dellane.                                | Mappa viser stor variasjon og originalitet både i løysingsteknikkar og spørsmål.               |
| Refleksjon (Del 3)   | Refleksjon manglar.                                                                      | Kandidaten freister å sjå kurset i sin yrkes- eller studiekontekst, men refleksjonen vert knapp og overflatisk. | Kandidaten har gjort kursinnhaldet til sitt eige, og har konstruktive døme på praktisk verdi av kurset.                     | Kandidaten er kreativ og visjonær i sin refleksjon over framtidig nytte av kurset.             |


## Kommentarar

&nbsp;

[^tv]: Testing og validering vert vurdert ekstra strengt for å hindra ukritisk bruk av kunstig intelligens.  
      For å få ståkarakter, må kandidaten forklara og validera koden slik at det er tydeleg
      at dei sjølv har teke stilling til han og kan gå god for at han er korrekt.
[^kor]: Korrekt kode innber at koden gjer det som *essayet* seier at han skal gjera.
[^les]: Koden skal fremst vera lesbar for dei som kan litt mindre enn kandidaten sjølv.
      Om ein skriv eit omfattande *essay* og viser fleire avanserte teknikkar,
      treng ein ikkje utdjupa dei mest trivielle teknikkane.
      Det som har vore utfordrande å få til, krev kommentar og gjerne refleksjon 
      over læringsopplevinga.  
      Skriv ein kortare og enklare, må ein kanskje kommentera kode som går ukommentert
      i lengre og meir avanserte *essays*.
