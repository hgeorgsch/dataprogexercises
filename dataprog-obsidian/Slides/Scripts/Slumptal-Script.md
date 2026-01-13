---
title: Slumptalsgenerator
author: Hans Georg Schaathun
date: 14. januar 2025
tags:
  - lecture/video/script
---

(newton)

Mange simuleringer handler om tilfeldige prosesser.
I tillegg er der mange prosesser som i teorien er deterministiske,
men som er så kaotiske at vi ikke klarer å modellere dem deterministisk.
Da er det òg naturlig å bruke tilfeldige prosesser som modell.


(tekst)

I statistikken kaller vi gjerne slike tilfeldige prosesser for
*stokastiske* prosesser.  Enkelt sagt er «stokastisk» blott
et penere ord for tilfeldig.

(kasino)

I simuleringsliteraturen, blir tilfeldige simuleringer gjerne
kalt for *Monte Carlo-simuleringer* efter de kjente kasinoene
i Monte Carlo, med spill som roulette.

(terning)

Terningkast og andre tilfeldige prosesser er vanskeleg for datamaskiner.
Maskinene er konstruerte for å vera fullt ut deterministiske system.
Virkeleg slump må derfor komme utanfrå, som *input*.

Det er mulig å få det til, ved å måle ørsmå variasjoner i
tastefrekvensen fra brukeren, eller i temperaturen i rommet,
eller spenning på strømnettet.
Der er derimot en grense for hvor mye slump man kan hente ut
på denne måten på kort tid.
Store simuleringer krever ofte mer slump.

(diagram)

I praksis bruker vi som regel såkalte *pseudo-tilfeldige* tall.
Det er matematiske formler som gjør at vi kan regne ut lange serier
med tall som *ser tilfeldige ut* uten faktisk å være det.

På norsk kaller vi det gjerne for en slumptallsgenerator.
På engelsk kalles det en
*pseudo-random number generator* eller forkortet PRNG.

Slumptallsgeneratoren er det som vi kaller en endelig tilstandsmaskin.
Den har en tilstand $s_i$, og en funksjon som genererer en ny
tilstand $s_{i+1}$ hver gang vi ber om et slumptall.

I teorien kan vi bruke tilstanden $s$ som et slumptall, men ofte
vil vi ha slumptall fra en anden definisjonsmengde.
Da trenger vi en ekstra funksjon som oversetter tilstanden til
riktig utfallsrom.

$$ s_i = a\cdot s_{i-1} \mod p $$

$$ y_i = \frac{s_i}{p} $$

Det mest kjente tilfellet er lineær kongruens.
Her regner vi ut tilstanden ved å gange med et tall $a$ og ta resten
ved divisjon med et tall $p$.
Dersom vi velger $a$ og $p$ fornuftig, vil følgen av tall $s_i$
se tilfeldig ut.

For å generere tilfeldige tall mellom 0 og 1, kan vi simpelthen dele tilstanden modulusen $p$

$$ s_i = 7\cdot s_{i-1} \mod 97 $$

For å ta et leketøyseksempel, kan vi prøve å gange med syv
og dele på syvognitti.
Syvognitti er primtall, noe som gjerne er en god idé.

(diagram 1)

Vi kan starte med en vilkårlig tilstand, si tretten, og se hvilke
tall vi får.

Først enognitti.

(diagram 2)

Så femogfemti.

(diagram 3)

Firognitti.

(diagram 4)

Seksogsytti

(diagram 5)

Syvogførr.

(diagram 6)

Åttogtredve

(diagram 7)

... og toogsytti.

Den nøyaktige formelen er ikkje viktig for oss.  Det som er greitt
å hugsa er at når me har bestemt den første tilstanden $s_0$, som
vi gjerne kaller frøet eller *seed*, så vil slumptalsgeneratoren
gi oss en *uendelig* følge med tilfeldigaktige tal.

Der er mange kjente slumptallsgeneratorer, og lineær kongruens er 
ikke den beste, blott den best kjente.
Vi pleier derimot ikke være så kresne på slumptallsgeneratorene
i simulering.  Hvis du skal lave lotterier, som nødvendigvis må
være rettferdige, er det langt viktigere at slumptallene ikke
bare ser tilfeldige men også er umulige å forutsi.

De strengeste kravene til slumptall gjelder i kryptografi, som
f.eks. brukes til å sikre pengeoverføringer og sensitive
personopplysninger.

(syklus)

En anden ting som vi skal merke oss er at slumptallsgeneratoren har
et endelig antall tilstander.  
Før eller siden kommer den til å gjenta seg selv.

Slumptallsgeneratoren er det som vi kaller en endelig tilstandsmazkin.
Den har et endelig antall tilstander.
Leketøyseksempelet vårt har 90 tilstander.
Det fælger av den matematiske formelen at for en gitt tilstand er det alltid
en bestemt tilstand som følger efter, og når vi genererer tilstrekkelig mange
tall, går vi i ring.  Slumptallsfølgen gjentar seg.

Fordi vi valgte koeffisientene $a$ og modulusen $p$ fornuftig i vårt eksempel,
blir alle tilstandene brukt, og vi kan generere 90 tilfeldige tall før rekkefølgen
blir gjentatt.  Det er ikke alltid tilfellet.
Antallet tilstander før de gjentar seg selv, kaller vi gjerne for perioden til
generatoren.

(Mersenne Twister)

Standardbiblioteket i python bruker en slumptallsgenerator som heter
Mersenne Twister.
Den har en periode på $2^{19937}-1$ tilstander før den gjentar seg selv.
Hvis du skriver denne lengden ut i titallssystemet, får vi om lag 6000 sifre.

(kode)

Når vi skal bruke slumptall i python, trenger vi ikke bekymre oss
om alt som foregår inni slumptallsgeneratoren.
Der finnes mange biblioteker som tilbyr ulike slumptallsgeneratorer.
Standardbiblioteket som bruker Mersenne Twister, heter `random`.

Hvis vi skal simulere en terning, f.eks. kan vi bruke funksjonen
`randint` og be om et tall mellom 1 og 6.

(histogram)

Terningen er et eksempel på en uniform fordeling, der
alle verdier er like sannsynlige.
Fordelingen er diskret, dvs. at der bare enkelte
punkter som forekommer; vi får bare heltall og ikke
desimaltallene imellom.

(uniform)

Hvis vi vil ha desimaltall, kan vi bruke funksjonen `random()`
som gir et tall mellom 0 og 1.
Dette er også en uniform fordeling, der alle verdier er like
sannsynlige, men den er kontinuerlig og ikke diskret.

(normalfordeling)

Vi kan også få slumptall fra fordelinger som ikke er uniforme.
Vi skal ikke gå inn på alle, men kan se på normalfordeling,
eller gaussfordelingen, som er så mye brukt.

Funksjonen `random.gauss()` gir et tall som er normalfordelt
med standardavvik 1 rundt en middelverdi på 0.

(Frøet)

Som vi nevnte, må slumptallene alltid med et frø.
Vi kan bruke slumptallsgeneratoren uten å tenke på frøet.
Da vil maskinen prøve å finne noe tilfeldig som kan brukes
som frø, f.eks. de siste sifrene fra klokkeslettet.

(eksempel)

Vi har dog muligheten til å sette frøet, eller *seed*.
Hvis vi f.eks. sette frøet til 42 før vi henter slumptall,
får vi alltid de samme tallene.

Dette kan være særs nyttig ved simulering, fordi det lar
oss kjøre den eksakt samme simuleringen flere ganger.
Særlig n[r vi skal kvalitetssikre koden vår eller leter
efter feil, kan det være greitt å kunne sammenligne kjøringer
uten tilfeldige faktorer.

Det er derimot viktig at man ikke setter frøet i utide.
Om du tilbakestiller frøet midt i en simulering, vil ikke
fortsettelsen se like tilfeldig ut som starten.

(slutt - ingen foil)

Det var alt for denne gang.  
Jeg har lavet en video til med mer inngående demonstrasjon av 
funksjonene i python.
