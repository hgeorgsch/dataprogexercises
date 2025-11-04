# 28.okt: Programmatisk innhenting av data

## MÅL

En skikkelig kjekk ting å kunne bruke python til er å hente inn data *programmatisk*.
For å komme i gang med dette må vi:

* Først lære litt om nettverskprotokoller, og spesielt: *HTTP*
* Vi trenger å vite litt om JSON-formatet, og python dictionaries
* Vi trenger å vite litt om hva en URL er
* Vi må kunne bruke python-biblioteket `requests` og `pyjstat`

Etter dette skal vi se nærmere på flere *web API* som lar oss hente inn data programmatisk

## Nettverksprotokoller og API

- Vi tar en rask titt på disse slidsene -- trykk 'S' for å se «manuskriptet»:
   - [Datakilder og nettverksprotokoller](https://jonajh.folk.ntnu.no/Datakilder%20og%20nettverksprotokoller/#/)
   - [HTTP og WebAPI](https://jonajh.folk.ntnu.no/HTTP%20og%20Web-API/#/)

### Video med eksempel:

Slides om HTTP og WebAPI har en video under produksjon [her](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=180787ec-ec88-42af-98d4-b34e0096cff1)

Det var litt sen informasjon om forelesning tirsdag og lavt oppmøte, så jeg gjorde et forsøk på opptak.
Mikrofonen gikk dessverre tom for strøm midt første time, men vi fikk ladet den litt opp til andre time.

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%">
	<iframe src="https://ntnu.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=17ea9a0a-69f8-4d4a-8705-b38400a0c41d&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&captions=false&interactivity=all" style="border: 1px solid #464646; position: absolute; top: 0; left: 0; width: 100%; height: 100%; box-sizing: border-box;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player" aria-description="IIRA2001H25-Json-Protokoller-Requests"></iframe>
</div>


## JSON, Python dictionaries og jsonstat

- Se egen jupyter notebook: [](../notebook/)


## URL

- En URL eller *«Uniform resource locater»* er en måte å oppgi plasseringen til en ressurs.
- Vi kjenner dem i dagliglivet som "nettaddresser"
- Når vi skal hente data fra steder på internett eller gjennom et API må vi kunne bygge slike URL-strenger

Generelelt har de formen
```
protokoll://tjener/sti/til/reesurs/på_tjener?parameter1=noe&parameter2=Noe+Annet
```

Vi trenger å ha litt kontroll på:
- tjener:
   - Hvor dataene vår befinner seg på internett: Feks `www.ssb.no` eller `www.ec.europa.eu` (eurostat)
- Stien på tjeneren
    - Hvor på tjeneren vi finner ressursen
    - På www.ssb.no ligger tabell 14406 om barn sin fritid på stien `/statbank/table/14406/`
    - I en nettleser kan vi se på tabellen ved å skrive inn [https://www.ssb.no/statbank/table/14406/](https://www.ssb.no/statbank/table/14406/)
- URL parametre
    - Etter stien kan vi legge ved *parametre*
        - Vi legger først til `?` som kalles en separator
        - Deretter kommer flere "felt" eller "nøkkel/verdi"-par som kalles *url-parametre*
        - Disse har egen "tegnkoding" som kalles URL-encoding
        - Vi burde bruke et programmeringsbibliotek til å bygge slik parametre




## Requests og pyjstat

- Se egen jupyter notebook



# OPPGAVE:

- Let gjennom eurostat og last inn noen interessante dataset programmatisk med `requests`
- Se om du kan vaske og klargjøre dataene for videre behandling

Ikke heng deg opp i analyse, øv i første omgang på å hente inn og klargjøre noen dataset.
Jo flere jo bedre -- øvelse gjør mester, men prøv å lese inn minst 3

Om du har tid å lyst kan du kanskje lage en funksjon `def hent_eurstatdata(tabellkode):` som automatisk henter den aktuelle tabellen fra eurostat med requests,
leser den inn med `pyjstat`og returnerer et pandas dataframe



