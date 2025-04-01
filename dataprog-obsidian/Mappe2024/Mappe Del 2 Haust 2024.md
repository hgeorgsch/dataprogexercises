Andre del av mappen dreier seg om dataanalyse og web-APIer.

Du skal legge ved 2 programmer hvor du gjør noe interessant med 1 eller
flere datasett.

Programmene kan undersøke en problemstilling, utforske data, teste en
hypotese eller gjøre noe annet nyttig.

Vi vil gjerne at du i ett av programmene bruker et web-api til å hente
dataene du trenger fra nettet.

Det ene programmene kan basere seg kun på bruk av et web-api og ikke
dataanalyse.

# Oppgave {#oppgave .unnumbered}

Skriv to pythonprogrammer:

## Program 1: Dataanalyse fra SSB eller Eurostat {#program-1-dataanalyse-fra-ssb-eller-eurostat .unnumbered}

1.  Et av programmene må bruke data fra SSB eller Eurostat

2.  Dere står ellers fritt til hva du vil bruke dataene til, eller hva
    innholdet i oppgaven er, feks

    -   Utforske og visualisere data

    -   Undersøke en problemstilling

    -   Teste en hypotese

    -   Lage en prediktiv modell

3.  I et 1 av programmene ser vi gjerne at dere bruker et web-api eller
    bibliotek til å hente data programmatisk

## Program 2: Helt fri dataanalyse {#program-2-helt-fri-dataanalyse .unnumbered}

1.  I det andre programmet kan du bruke data fra hvilken som helst kilde

    -   Vi krever at det er *ekte* data, dere kan altså ikke generere
        den selv

    -   Dere kan hente faglig relevant data direkte fra feks, SSB,
        Eurostat [OECD](https://data-explorer.oecd.org/) eller
        [IMF](https://www.imf.org/en/Data)

    -   Dere kan også hente faglig relevant data fra et
        tredjepartsbibliotek slik som *yfinance*

    -   Dere **MÅ** ikke nødvendigvis lage et faglig relevant program --
        er dere interessert i fotballstatistikk, sjakk-ratinger, gaming
        eller annet er det helt innafor:

        -   Lag et program, analyser data som *du synest er
            spennende/interessant* og vis selvstendig bruk av python

        -   [kaggle.com](www.kaggle.com) inneholder en hel del data som
            kanskje kan være nyttig i slike tilfeller

    -   Dersom du har en kul idé til et program som bruker et web-api,
        men som ikke faller innen kategorien dataanalyse kan dette
        sikkert godkjennes, men *hør med foreleser for sikkerhets skyld*

# Oppgavetips og eksempler {#oppgavetips-og-eksempler .unnumbered}

Du kan, litt som i første del av mappen, ta utgangspunkt i
øvingsoppgaver og eksempler fra timene.

## Utforske data {#utforske-data .unnumbered}

I timen skal vi laste inn et datasett fra SSB med populasjonsdata fra
kommunene i Norge og plottet endring i populasjonsstørrelse for noen
kommuner.

Fraflytting fra Nord-Norge har lenge vært en bekymring (se feks.
[h]()ttps://www.nrk.no/tromsogfinnmark/ungdommen-vil-flytte-fra-nord-norge-1.16346169denne
artikkelen fra nrk), dette kunne vært et utgangspunkt for et
pythonprogram som utforsker populasjonsdata. Du kan for eksempel plotte
grafer for netto innflytning, populasjonsstørrelse i ulike regioner og
se om man finner denne fraflytningstrenden. Kanskje kan det være
interessant å sette dette i sammenhengen med aldersfordelingen også.

En god oppgave kommenterer selvfølgelig også funnene.

## Problemstilling {#problemstilling .unnumbered}

I eksempelet over har vi kanskje ikke noe spørsmål vi vil finne svar på.
I forskning kalles et spørsmål man vil finne svar på en problemstilling.
Vi har i timen hentet data om arbeidsledighet og åpnede konkurser, og
undersøkt om det er en sammenheng mellom de to. Vi skal også undersøke
om det er en sammenheng mellom fraflytting fra en kommune og
arbeidsledigheten/sysselsettingen i en øving. Man kan se etter (lineære)
sammenhenger mellom to statistiske variabler ved å regne ut
korrelasjonen mellom de, slik som i timen. Man kan også plotte grafer,
prikkeplott eller histogram å se etter sammenhenger.

Det finnes mange interessante ting å undersøke om henger sammen, feks:
Strømpris og prisen på aluminium, strømpris i Europa og strømpris i
Norge, styringsrente og inflasjon osv.

## Hypotesetesting {#hypotesetesting .unnumbered}

Fra statistikken har dere lært å teste hypoteser. Mulige hypoteser å med
data fra SSB teste er \"folk med høyere utdanning har høyere lønn\"

## Nyttige program {#nyttige-program .unnumbered}

Du kan også lage et program av praktisk nytte, eller som du synes er
artig. Vi har eller vil gjennomgå et program som regner om mellom ulike
valutaer med ferskest mulige kurser.

# Øvrig innhold {#øvrig-innhold .unnumbered}

I tillegg til pythonprogrammene, skal det leveres en rapport. Vi vil ha
beskrevet hva målet med hvert program er, hva ideen var, eller hva
problemstillingen er.

I tillegg trenger vi en del hvor dere reflekterer og diskuterer
resultatene. Hva har du funnet ut? Hvordan fungerer programmet ditt?

# Tilbakemelding {#tilbakemelding .unnumbered}

Basert på erfaringer på medstudentvurderingen til del 1, skal vi kjøre
en ny runde på del 2 også. Mer info kommer
