---
tags:
  - lecture/video
---

### Hente data programmatisk

![[pythonijungel.png]]


note:

I denne videoen skal vi se på hvordan man kan hente inn data programmatisk gjennom feks python og biblioteket requests. For å oppnå dette må vi se nøyere på hvordan http-protokollen er bygget opp

---


<!-- slide template="[[tpl-fitdiagram2]]" -->
<!-- slide bg="white" -->

#### HTTP

![[osi_prot.svg ]]


::: credit
:::

note:
http - eller hypertext transfer protocol - er et sett av kjøreregler i applikasjonslaget i OSI-nettverksmodellen. 
Det er det øverste laget og henger tett sammen med programmet du faktisk ser på dataskjermen. 

---


<!-- slide template="[[tpl-fitdiagram2]]" -->
<!-- slide bg="white" -->

#### Spørring

![[client-server-http.svg]]

::: credit
:::

note:
http-protokollen beskriver hvordan en klient  kan sende en forsepørsel om en ressurs hos en tjener og hvordan tjener skal svare.

Klient og tjener er i prinsippet begge datamaskiner på et nettverk, men tjeneren er typisk en web-server av en sort og klienten er et program på datamaskinen din.

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

En klient kan sende flere typer spørringer, eller bruke flere forskjellige http-metoder - dere ser en oversikt i tabellen

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

![[http-form.svg]]
::: credit
:::
note:
Figuren viser et eksempel på en POST spørring til en ressurs som er ment for å teste http-spørringer.
Den har 3 deler merket i gult, rødt og grønt - den grønne delen er data noe data vi sender med, den ville ikke vært der om vi brukte GET-metoden

Den første linjen er kalles en request line - Den begynner med hvilken http-metode vi bruker, deretter kommer stien til ressursen vi vil ha tilgang til, og tilslutt oppgis det hvilken versjon av http-protokollen som brukes. Det er veldig viktig at man bruker samme protokoll når man kommuniserer, og det er har vært noen endringer i http-protokollen siden den først ble laget, så vi må oppgi versjonen

Feltet i rødt kalles http-headerene, og den inneholder metadata om http-spørringen. De er satt sammen som nøkkel/verdi-par, og kan feks være hvilken type klient som spør, hvilket format eller språk klienten ønsker svar på, hvilket format dataene den sender med er på, og hvor mye data som blir sendt  -- osv. Headeren som heter Host oppgir tjeneren eller serveren spørringen skal sendes til, og er den eneste som alltid er obligatorisk

Så kommer det en tom linje, eventuelt etterfulgt av noe data, om vi skal sende det. Her har jeg lagt med noe JSON-data med to felt

---

<!-- slide template="[[tpl-fitdiagram2]]" -->
<!-- slide bg="white" -->


![[http-response.svg]]
::: credit
:::

note:
Når tjeneren får http-spørringen, gjør den forhåpentligvis det den skal, og henter frem ressursen du ber om, og sender tilbake en HTTP-respons.

Den ligner på HTTP-spørringen, men i stedet for request-linjen, har vi nå en statuslinje

Den inneholder http-versionen og en statuskode, i dette tilfelle 200 OK

Ellers inneholder headeren metadata om responsmeldingen, etterfulgt av en blank linje og eventuelle data vi har forespurt. Vi ser i headeren under content-type at den har sendt tilbake text/html, og vi ser selve html-dataene i body'en i grønt. HTML er forøvrig et språk som strukturerer innholdet på en nettside.

---

### Statuskoder
<font size=6>

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

</font>
note:

Vi har mange forskjellige statuskoder, mindre enn 400 betyr at alt har gått greit

Dere kjenner kanskje igjen 404 fra når dere har tastet inn en feil URL i nettleseren

---


#### www.ntnu.no/fiskesuppe

![[404ntnu.png]]

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

Disse url-parameterene gjør det mulig å sende med litt data i GET-metoden også, for eksempel for å spesifisere hvilken data eller deler av dataene vi vil ha tak i 

Vi kan ikke sende med like mye data som i body'en til en post-spørring, og dataene er ikke godt sikret, så brukernavn og passord bør heller legges i bodien eller i headerene

---

<font size=6>

| Protokoll  | Tjener              | Port | Sti           | Parametre                     |
| ---------- | ------------------- | ---- | ------------- | ----------------------------- |
| https      | www.example.com     | 443  | /søk          | q=nettverk&lang=no            |
| http       | localhost           | 8080 | /api/data     | type=json                     |
| ftp        | ftp.ntnu.no         | 21   | /pub/ansatte/ | *(ingen)*                     |
| https      | api.weather.com     | 443  | /v1/forecast  | lat=60.4&lon=5.3&units=metric |
| mailto<br> | kontakt@eksempel.no | –    | *(ingen)*     | *(ingen)*                     |

</font>
note:
Her ser vi noen eksempler på URL

Og med det tror jeg vi skal sende noen http-spørringer så vi ser hvordan det fungerer

(Viser en demonstrasjon i terminal og åpner resultatet i nettleser)
script telnet-out.txt
telnet www.google.com 80
GET /search?qDonald+Duck+og+Co HTTP/1.1
Host: www.google.com

---

#### Oppsummert

Skal vi hente ressurser over et nettverk via HTTP må vi ha kontroll på:
+ Metode (GET eller POST)
+ Stien vi finner ressursen på
+ Hvilke eventuelle parametre vi skal sende med URL'en
+ Hvilke headere som skal sendes med
+ Hvilken data som skal sendes med (for POST spørringer)

note:
Så hva må vi ha kontroll på for å sende en http-spørring?
Vi må ha kontroll på metoden (get/post)
VI må vite stien vi finner ressursen på
Vi må ha kontroll på eventuelle parametre som skal sendes med, og hva de gjør
Hvilken headere som trengs være med
Og hvis vi det er en POST eller PUT spørring, hvilken data som kan sendes.

Dette slepper vi heldigvis å gjøre i telnet -- Det er innebygde metoder som langt på vei hjelper oss å sende slike forespørsler. I python bruker vi gjerne requests biblioteket

---
### `requests`

```python
import requests

url = "https://www.google.com/search"
url_parametre = {
"q" = "Donald Duck og kompani"
}
headers = {"User-Agent": "myApp/1.2.0"}

respons = requests.get(url, 
	parameters=url_parametre, headers=headers)
print("Status", respons.status_code)
print(respons.text)
```

note:
Her gjør vi det samme søket som i telnet.
Når vi sender en http-spørring med requests, bruker vi de innbygde .get eller .post funksjonen, og gir den byggesteinene til http-spørringen som argumenter: Url med protokoll, tjener og sti - url_parameterene som en dictionary (requests formaterer den for oss) - eventuelle headere som en dictionary (requests legger til en del for oss, slik som host, men om vi trenger kanskje å legge med ed brukerid og passord osv). Til en post spørring kunne vi også lagt til data i bodien - det er ikke gjort her men er tilsvarende lettvint.

---
### Et siste eksempel

<iframe src="https://open-meteo.com" height="600" width="900"><iframe>

note:
Forrige lille kodesnutt er ikke et godt eksempel på bruk av requests - Som et siste eksempel, skal vi se hvordan vi kan sette det vi har lært og hente inn værmeldigen fra open-meteo.com.

(Viser api-dokumentasjonen, og gjør et kall til API i python):
url = "https://api.open-meteo.com/v1/forecast"
url_parametre = {
   "latitude": 62,
   "longitude": 6,
   "hourly": "temperature_2m"
}

respons = requests.get(url, params=url_parametre)
print("Statuskode", respons.status_code)
print("Format:", respons.headers["content-type"])
data = respons.json()
df = pd.DataFrame({"time": data["hourly"]["time"], "temp": data["hourly"]["temperature_2m"]})
df["time"] = pd.to_datetime(df["time"])
df.set_index("time").plot()
plt.show()

(Ferdig kode og ser i kamera):
Det er ikke nødvendigvis lett å finne hale og ende på hvordan et web-api som det vi så fungerer, og hvordan datastrukturene de serverer er bygget opp, men om man har litt kontroll på rollen og oppbyggingen til http-protokollen, er det ganske grei skuring å sende forespørsler med et bibliotek som requests