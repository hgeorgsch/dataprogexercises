---
tags:
  - lecture/video
---

<!-- slide template="[[tpl-fitdiagram2]]" -->
### Hente data programmatisk

![[pythonijungel.png]]
::: credit
Bilde generert av DALL-E
:::

note:

I denne videoen skal vi se på hvordan man kan hente inn data programmatisk gjennom feks python. For å gjøre dette trenger vi å se på http-protokollen, og hvilke dataformat vi får tilbake.

---


<!-- slide template="[[tpl-fitdiagram2]]" -->
<!-- slide bg="white" -->

#### HTTP

![[osi_prot.svg]]


::: credit
:::

note:
http - eller hypertext transfer protocol - er et sett av kjøreregler i applikasjonslaget i OSI-nettverksmodellen. 

---


<!-- slide template="[[tpl-fitdiagram2]]" -->
<!-- slide bg="white" -->

#### Spørring

![[client-server-http.svg]]

::: credit
:::

note:
Den beskriver hvordan en klient  kan sende en forsepørsel om en ressurs hos en tjener og hvordan tjener skal svare.

Klient og tjener er i prinsippet begge datamaskiner på et nettverk, men tjeneren er typisk en web-server av en sort og tjeneren er et program på datamaskinen din.

Feks kan klienten være nettleseren din som sender en forespørsel om å få nyhetsforsiden til www.nrk.no, som da er tjeneren.

Eller klienten kan være et pythonskript, som sender en forespørsel om å få månedlige byggevareindekser fra 1980 til 2000 til ssb sitt web-grensesnitt for slike forespørsler (SSB er da tjeneren)

---

### HTTP spørringer

<font size="6">

| Metode   | Beskrivelse                                 |
|----------|---------------------------------------------|
| **GET**      | Henter ressurser/data                       |
| **POST**     | Sender data til serveren (ofte for å opprette noe) |
| PUT      | Erstatter en ressurs helt                     |
| PATCH    | Oppdaterer deler av en ressurs                |
| DELETE   | Sletter en ressurs                            |
| HEAD     | Samme som GET, men uten responsbody           |
| OPTIONS  | Returnerer støttede metoder for en ressurs    |
| CONNECT  | Etablerer en tunnel til serveren              |
| TRACE    | Returnerer det mottatte requestet (debugging) |


</font>

note:

En klient kan sende flere typer spørringer

---

### HTTP spørringer

<font size="6">

| Metode   | Beskrivelse                                 |
|----------|---------------------------------------------|
|==**GET**==      | ==Henter ressurser/data==                       |
| ==**POST**==     | ==Sender data til serveren (ofte for å opprette noe)== |
| PUT      | Erstatter en ressurs helt                     |
| PATCH    | Oppdaterer deler av en ressurs                |
| DELETE   | Sletter en ressurs                            |
| HEAD     | Samme som GET, men uten responsbody           |
| OPTIONS  | Returnerer støttede metoder for en ressurs    |
| CONNECT  | Etablerer en tunnel til serveren              |
| TRACE    | Returnerer det mottatte requestet (debugging) |


</font>

note:
I praksis trenger vi stort sett kun å bry oss med GET-metoder som henter ressurser/data og POST som sender data til tjeneren, i vårt tilfelle er det ofte snakk om en "handleliste" som beskriver hvilke data vi vil ha tak i.

---

<!-- slide template="[[tpl-fitdiagram2]]" -->
<!-- slide bg="white" -->
##### Oppbygging

![[http-form.svg]]
::: credit
:::
note:
Figuren viser et eksempel på en POST spørring til en ressurs som er ment for å teste http-spørringer.
Den  3 deler, siden den skal sende med data, om man ikke trenger det, består den av kun de 2 første delene i gult og rødt.

Den første linjen er kalles en request line - Den begynner med hvilken http-metode vi bruker, deretter kommer til stien til ressursen vi vil ha tilgang til, og tilslutt oppgis det hvilken versjon av http-protokollen som brukes. Det er veldig viktig at man bruker samme protokoll når man kommuniserer, og det er har vært noen endringer i http-protokollen siden den først ble laget.

Feltet i rødt kalles http-headerene, og den inneholder metadata om http-spørringen, slik som hvilken type klient som spør, hvilket format eller språk tjeneren ønsker svar på, hvilket format dataene den sender med er på, og hvor mye data som blir sendt  -- osv. Headeren som heter Host oppgir tjeneren eller serveren spørringen skal sendes til, og er den eneste som alltid er obligatorisk

Så kommer det en tom linje, eventuelt etterfulgt av noe data, om vi skal sende det

---

<!-- slide template="[[tpl-fitdiagram2]]" -->
<!-- slide bg="white" -->

#### HTTP-respons

![[http-response.svg]]
::: credit
:::

note:
Når tjeneren får http-spørringen, gjør den forhåpentligvis det den skal, og henter frem ressursen du ber om, og sender tilbake en HTTP-respons.

Den ligner på HTTP-spørringen, men i stedet for request-linjen, har vi nå en statuslinje

Den inneholder http-versionen og en statuskode, i dette tilfelle 200 OK

Ellers inneholder headeren metadata om responsmeldingen, etterfulgt av en blank linje og eventuelle data vi har forespurt

---

### Statuskoder

| Kode | Navn                  | Beskrivelse                   |
| ---- | --------------------- | ----------------------------- |
| 200  | OK                    | Forespørsel vellykket         |
| 201  | Created               | Ressurs opprettet             |
| 204  | No Content            | Vellykket, men ingen innhold  |
| 400  | Bad Request           | Klienten sendte ugyldig data  |
| 401  | Unauthorized          | Mangler gyldig autentisering  |
| 403  | Forbidden             | Tilgang nektet                |
| 404  | Not Found             | Fant ikke ressursen           |
| 500  | Internal Server Error | Serveren krasjet eller feilet |

note:

Vi har mange forskjellige statuskoder, mindre enn 400 betyr at alt har gått greit

Dere kjenner kanskje igjen 404 fra når dere har tastet inn en feil URL i nettleseren

---

#### www.ntnu.no/fiskesuppe
<iframe src="https://www.ntnu.no/fiskesuppe" title="tittel her" width="600px" height="600px"></iframe>

---

#### URL

<font size=5> protokoll://tjener:port/sti/til/ressurs?parametere=4&lang=en
</font>
+ Uniform resource locator

note:

Og når vi først nevnt URL - Vi bruker ofte URL eller nettaddresser om hverandre, men det er ikke helt det samme. URL er en forkortelse for uniform resource locator - og er en måte å oppgi plassering til en eller annen ressurs på internett (som oftest)

Protokollen forteller hvordan vi skal få tak i ressursen

tjeneren-delen er ip-addressen eller domenenavnet til tjeneren som har ressursen.
Etter dette kommer et kolon og et port-nummer, dette er ofte valgfritt, når vi henter nettsider brukes automatisk port 80 eller 443

Stien er plasseringen til ressursen vi vil ha tak i på tjeneren.

Etter plasseringen kan vi faktisk sende med data om feks. hvilket språk vi vil ha en nettside på -- eller i tilfelle hvor vi henter om feks arbeidsledighet, hvilke årstall vi er interessert i. Dataene har et spesielt format (URL-encoding) - Det er best å bruke egne bibliotek for å bygge de 


---

| Protokoll  | Tjener              | Port | Sti           | Parametre                     |
| ---------- | ------------------- | ---- | ------------- | ----------------------------- |
| https      | www.example.com     | 443  | /søk          | q=nettverk&lang=no            |
| http       | localhost           | 8080 | /api/data     | type=json                     |
| ftp        | ftp.ntnu.no         | 21   | /pub/ansatte/ | *(ingen)*                     |
| https      | api.weather.com     | 443  | /v1/forecast  | lat=60.4&lon=5.3&units=metric |
| mailto<br> | kontakt@eksempel.no | –    | *(ingen)*     | *(ingen)*                     |

note:
Her ser vi noen eksempler på URL

Og med det tror jeg vi skal sende noen http-spørringer så vi ser hvordan det fungerer

---

#### Avslutningsvis

Skal vi hente ressurser over et nettverk må vi altså sende egnede http-forspørsler
Vi trenger å ha kontroll på:
+ Metode (GET eller POST)
+ Stien vi finner ressursen på (URL'en)
+ Hvilke eventuelle parametre vi skal sende med URL'en
+ Hvilke headere som skal sendes med
+ Hvilken data som skal sendes med (for POST spørringer)

note:

Dette slepper vi heldigvis å gjøre i telnet -- Det er innebygde metoder som langt på vei hjelper oss å sende slike forespørsler. I python bruker vi gjerne requests biblioteket

---
### `requests`

```python
import requests

url = "www.google.com/search"
url_parametre = {
"q" = "Donald Duck og kompani"
}

respons = requests.post(url, parameters=url_parametre)
print(respons.text())
```