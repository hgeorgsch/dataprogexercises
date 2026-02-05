---
tags:
  - lecture/slides
---

# Web-APIer: Autentisering
## Fra åpne dører til digitale nøkkelkort

---

## Hvorfor autentisering?
* **Identifisering:** Hvem henter data?
* **Ressursstyring:** Unngå at serveren kneler (Rate limiting).
* **Personvern:** Tilgang til data som ikke er offentlig.
* **Betaling:** Noen API-er koster penger per kall.

---

## Case 1: De åpne dataene (SSB)
* **Type:** Ingen autentisering
* **Sikkerhet:** Åpent for alle.
* **Eksempel:** Statistisk sentralbyrå (SSB).
* **Bruk:** Du sender bare en `GET` eller `POST` forespørsel, og får data i retur.
* **Begrensning:** Du kan bli blokkert hvis du sender 10 000 forespørsler i sekundet.

---

## Case 2: "Nøkkelen i døra" (API-nøkler)
* **Type:** API Key / Token
* **Konsept:** En unik tekststreng du får fra leverandøren.
* **Eksempel:** OpenWeather, Google Maps, eller ChatGPT.
* **Slik virker det:**
  `headers = {"X-API-KEY": "din_hemmelige_nøkkel"}`
* **Risiko:** Hvis nøkkelen kommer på avveie, kan hvem som helst bruke din kvote/konto.

---

## Case 3: "Gullstandarden" (OAuth 2.0)
* **Type:** Delegert autorisasjon
* **Case:** Spotify eller Google Analytics.
* **Konsept:** Appen din får *lov* av brukeren til å hente data på deres vegne, uten at appen får vite brukerens passord.
* **Nøkkelord:** `Access Token` – en midlertidig nøkkel som går ut på tid.

---

## Hvordan fungerer OAuth-dansen? 💃

1. **Søknaden:** Brukeren sendes til Spotify for å logge inn.
2. **Kvitteringen:** Spotify sender brukeren tilbake med en `Authorization Code`.
3. **Vekslingen:** Python-skriptet bytter koden mot et `Access Token`.
4. **Tilgangen:** Vi bruker tokenet for å hente spillelister.

---

## Hvorfor er OAuth mer komplekst?

| Metode | Sikkerhet | Kompleksitet |
| :--- | :--- | :--- |
| **Ingen (SSB)** | Lav | 1/10 |
| **API-nøkkel** | Medium | 3/10 |
| **OAuth (Spotify)** | Høy | 8/10 |

*OAuth er sikrere fordi "nøkkelen" (tokenet) er kortvarig og begrenset til spesifikke oppgaver (scopes).*

---

## Praktisk eksempel: Spotify
I dag skal vi kode "Vekslingen":
1. Lage en autorisasjons-URL.
2. Fange opp koden i nettleseren.
3. Bytte koden i et `Access Token` ved hjelp av `requests`.

---

## Oppsummering
* **SSB:** Bare bank på, døra er ulåst.
* **API-nøkkel:** Du har din egen fysiske nøkkel.
* **OAuth:** Du må legitimere deg for å få et midlertidig adgangskort som kun virker i dag.
