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
| Metode  | Beskrivelse                                        |
| ------- | -------------------------------------------------- |
| GET     | Henter ressurser/data                              |
| POST    | Sender data til serveren (ofte for å opprette noe) |
| PUT     | Erstatter en ressurs helt                          |
| PATCH   | Oppdaterer deler av en ressurs                     |
| DELETE  | Sletter en ressurs                                 |
| HEAD    | Samme som GET, men uten responsbody                |
| OPTIONS | Returnerer støttede metoder for en ressurs         |
| CONNECT | Etablerer en tunnel til serveren                   |
| TRACE   | Returnerer det mottatte requestet (debugging)      |
note:

En klient kan sende flere typer spørringer

---

### HTTP spørringer
| Metode   | Beskrivelse                                        |
| -------- | -------------------------------------------------- |
| **GET**  | Henter ressurser/data                              |
| **POST** | Sender data til serveren (ofte for å opprette noe) |
| PUT      | Erstatter en ressurs helt                          |
| PATCH    | Oppdaterer deler av en ressurs                     |
| DELETE   | Sletter en ressurs                                 |
| HEAD     | Samme som GET, men uten responsbody                |
| OPTIONS  | Returnerer støttede metoder for en ressurs         |
| CONNECT  | Etablerer en tunnel til serveren                   |
| TRACE    | Returnerer det mottatte requestet (debugging)      |
note:
I praksis trenger vi stort sett kun å bry oss med GET-metoder som henter ressurser/data og POST som sender data til tjeneren, i vårt tilfelle er det ofte snakk om en "handleliste" som beskriver hvilke data vi vil ha tak i.

---

# Oppbygging
