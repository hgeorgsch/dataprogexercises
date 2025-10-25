#Gravitasjonsmodell for eksport/import
Man kan forsøke å modellere handelsflyt $F$ som tyngdekraften:
$$
F = G\frac{M_1M_2}{d^2}
$$
hvor $G$ er en konstant, de *økonomiske massene* $M_1$, $M_2$ er landenes GDP, og $d$ er avstanden mellom landene

## Dataset
Vi må sette sammen 3 ulike dataset:

    * SSB har meget utfyllende tabeller for eksport/import
    * Vi trenger dataset med landenes GDP -- (Vedlagt fra verdensbanken)
    * Vi trenger data som lar oss beskrive $d$ avstanden mellom landene (vedlagt fra ()[https://www.cepii.fr/cepii/en/bdd_modele/bdd_modele_item.asp?id=6]

## Oppgaver

### Innhenting

    * Det å finne datasett/kilder kunne være en egen oppgave

#### Handelsflyt

    * Handelsflyt kan finnes fra SSB om man kun ser på norge
    * Eurostat vil ha handelsdata innnen eurosonen, osv
    * Handelsflyt kan også måles på forskjellige måter, kroner/ører, kg, varer, tjenester

#### Økonomisk masse

    * GDP kan også hentes fra flere kilder, og måles på flere måter
    * Verdensbanken har bla åpne dataset

#### Distanse

    * En utfordring

### Prepping/vasking/forarbeid
    
    * Vesentlig arbeid med vasking 
    * Vi må slå sammen datapunkt, kanskje med ulike landkoder og forskjellig formatering. 
    * SSB har egne koder for varegrupper og kvantum - hva gjør man her
    * Ikke nødvendigvis lett å flette sammen de 3 datasettene til 1

### Analyse

    * Legge inn egen data kolonne for handelsflyten $F$ -- hvordan beskrives denne?
    * Stemmer modellen?
    * Når stemmer den bra/dårlig
    * Interessante outliers

### Praktiske ferdigheter

Vi kan prøve oss på og øve på mange praktiske aspekter ved databehandlig

    * Ulike grafiske fremstillinger
    * Velge ut deler av datasettet på ulike måter
        - Filtrere på  GDP
        - Filtrere på avstand
        - Filtrere lokasjon (innad EU osv)
osv osv osv


### Diskusjon

Hva kan vi i arbeidet vårt finne ut og lære om handelsflyt mellom land?
Dersom studentene henter inn egne dataset og gjør egne valg i hvordan modelleringen foregår, vil diskusjonen muligens (sikkert) variere.
Dersom vi prepper dataset for de kan man også undersøke forskjellige **ting** (hvilke? - undersøk)




