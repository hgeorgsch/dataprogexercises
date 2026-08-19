# Fremdriftsplan for IIRA2001-boka

Denne planen gjelder utviklingen av kursboka i `iira2001-book2`. Den studentrettede
semesterplanen hører hjemme i `markdown/fremdrift.md` og behandles som en egen
innholdsoppgave.

## Mål

Målet er å lage en publiseringsklar og vedlikeholdbar Jupyter Book 2-bok for
«Programmering og data i økonomiske fag» (IIRA2001). Boka skal knytte
programmeringsgrunnlag til økonomisk relevante problemstillinger, først gjennom
simulering og deretter gjennom innhenting, bearbeiding og analyse av data.

Før første ordinære publisering skal boka:

- ha en tydelig struktur og progresjon med læringsmål for hver hoveddel
- kunne bygges lokalt uten feil eller manglende sider
- ha kjørbare og reproduserbare kodeeksempler
- inneholde øvinger som støtter de sentrale læringsmålene
- ha dokumentert bygge- og publiseringsflyt

## Nå-situasjon (28. juli 2026)

- Jupyter Book 2.1.6 og øvrige Python-avhengigheter er låst med `uv`.
- `myst.yml` definerer et første innholdstre med programmering og pandas.
- Lokal bygging fullføres, men varsler om at `markdown/ovinger.md` mangler.
- `index.md` og `markdown/fremdrift.md` inneholder foreløpige tekster.
- De seks planlagte fagkapitlene i `markdown/` er tomme.
- `notebooks/pandas-demo.ipynb` er en liten teknisk demonstrasjon, ikke et ferdig
  undervisningskapittel.
- `make.sh` kombinerer bygging og publisering og viser til et gammelt steg i
  katalogen over.

## Arbeidsfaser

### 1. Teknisk grunnmur

**Leveranse:** Et rent, dokumentert og repeterbart bokbygg.

- rette opp manglende sider og avklare endelig filstruktur
- skille lokal bygging, forhåndsvisning og publisering i egne kommandoer
- dokumentere oppstart, bygging og vanlige feil i `README.md`
- kontrollere at genererte byggfiler og lokale hemmeligheter ikke versjoneres
- velge hvordan notebooks skal kjøres og valideres under bygging

**Ferdig når:** En ny utvikler kan klone prosjektet, installere med `uv` og bygge
boka uten advarsler ved å følge README-en.

### 2. Pedagogisk arkitektur

**Leveranse:** En godkjent innholdsfortegnelse og en felles kapittelmal.

- konkretisere læringsmål, forkunnskaper og forventet progresjon
- avgrense hoveddelene simulering/programmering og dataanalyse
- bestemme rekkefølgen mellom Python-grunnlag, simulering og pandas
- definere en kapittelmal med motivasjon, læringsmål, teori, eksempler,
  egenaktivitet, oppsummering og øvinger
- lage den studentrettede semesterplanen i `markdown/fremdrift.md`

**Ferdig når:** Alle planlagte kapitler har tittel, læringsmål, plassering i
progresjonen og anslått undervisningsomfang.

### 3. Pilotkapittel og arbeidsflyt for innhold

**Leveranse:** Ett komplett kapittel som fungerer som mønster for resten.

- velge ett avgrenset tema med både forklaring, kode og øvinger
- avklare når innhold skal være MyST Markdown, notebook eller en kombinasjon
- etablere stil for kode, figurer, tabeller, merknader og kildehenvisninger
- teste kapittelet i nettvisning og på små skjermer
- justere kapittelmal og byggeoppsett etter erfaringene

**Ferdig når:** Pilotkapittelet kan undervises fra, og strukturen kan gjenbrukes
uten særtilpasning.

### 4. Produksjon og migrering av innhold

**Leveranse:** Første komplette faglige versjon av boka.

- fylle kapitlene etter vedtatt rekkefølge og mal
- flytte inn eldre materiale kontrollert, ett tema om gangen
- omskrive eksempler til konsistent språk, datasett og Python-versjon
- knytte simuleringer og dataanalyser til økonomiske problemstillinger
- føre kilde, lisens og lokal plassering for hvert datasett

Materiale utenfor `iira2001-book2` kopieres eller migreres først når det er valgt
ut eksplisitt. Arbeidet i denne planen skal ellers holde seg i denne katalogen.

**Ferdig når:** Alle kapitler i innholdsfortegnelsen har fagtekst, kjørbare
eksempler og tilhørende egenaktivitet.

### 5. Øvinger og kvalitetssikring

**Leveranse:** Et konsistent og testet undervisningsopplegg.

- lage øvinger på flere vanskenivåer og angi hvilke læringsmål de dekker
- avklare plassering og tilgang for løsningsforslag
- kjøre notebooks fra et rent miljø og kontrollere deterministiske resultater
- kontrollere interne lenker, kryssreferanser, figurer og alternativ tekst
- språkvask og kontroll av begrepsbruk på norsk og engelsk
- prøve boka med studenter eller kolleger og prioritere funnene

**Ferdig når:** Bygget er rent, eksemplene kan reproduseres, og kritiske funn fra
faglig og pedagogisk gjennomgang er lukket.

### 6. Publisering og forvaltning

**Leveranse:** En versjonert utgivelse med enkel oppdateringsrutine.

- etablere trygg publisering uten at deploy er del av standard byggkommando
- gjennomføre en testpublisering og kontrollere lenker og navigasjon
- merke første utgivelse og føre en kort endringslogg
- avtale rutine for feilrettinger og revisjon etter undervisningsukene
- samle forbedringsforslag til neste semester i en prioritert backlog

**Ferdig når:** Publisert bok samsvarer med den testede versjonen, og neste
oppdatering kan gjøres med en dokumentert prosess.

## Prioritert arbeidsliste

| Prioritet | Oppgave | Fase | Status |
|---|---|---:|---|
| P0 | Avklare læringsmål, hovedstruktur og semesterprogresjon | 2 | Første utkast klart |
| P0 | Fjerne varselet om manglende `markdown/ovinger.md` | 1 | Ikke startet |
| P0 | Dokumentere lokal installasjon og bygging | 1 | Ikke startet |
| P0 | Skille bygging fra publisering i skript | 1 | Ikke startet |
| P1 | Lage og godkjenne kapittelmal | 2 | Ikke startet |
| P1 | Velge og ferdigstille ett pilotkapittel | 3 | Ikke startet |
| P1 | Bestemme strategi for kjøring og testing av notebooks | 1 | Ikke startet |
| P1 | Kartlegge og prioritere eldre materiale som skal migreres | 4 | Ikke startet |
| P2 | Produsere resterende kapitler og øvinger | 4–5 | Ikke startet |
| P2 | Etablere kvalitetskontroll og testpublisering | 5–6 | Ikke startet |

## Foreslåtte milepæler

Datoer settes når undervisningsstart, tilgjengelig arbeidstid og omfanget av
gjenbrukbart materiale er avklart.

1. **M1 – Stabilt grunnprosjekt:** Fase 1 er ferdig.
2. **M2 – Godkjent bokdesign:** Innholdsfortegnelse, læringsmål og kapittelmal er
   vedtatt.
3. **M3 – Pilot klar:** Ett komplett kapittel er prøvd og godkjent.
4. **M4 – Innhold komplett:** Alle planlagte kapitler og øvinger finnes i første
   fullstendige versjon.
5. **M5 – Publiseringsklar:** Kvalitetssikring, testpublisering og dokumentasjon er
   ferdig.

## Beslutninger som må tas tidlig

- Hvilke læringsmål og temaer er obligatoriske i IIRA2001 denne gangen?
- Når starter undervisningen, og hvilke milepælsdatoer følger av det?
- Hvilket eksisterende materiale skal migreres, oppdateres eller utelates?
- Skal notebooks kjøres ved hvert bygg, i en egen kontrolljobb eller publiseres
  med lagrede resultater?
- Hvor skal datasett, løsningsforslag og eventuelle lærerressurser ligge?
- Skal publisering fortsatt skje til NTNUs server med `rsync`, eller skal en annen
  publiseringsløsning brukes?

## Vedlikehold av planen

Planen oppdateres når en oppgave starter eller avsluttes. Nye ønsker legges først
i arbeidslisten og prioriteres før de tas inn i en aktiv fase. Etter hver milepæl
revurderes omfang, rekkefølge og risiko.
