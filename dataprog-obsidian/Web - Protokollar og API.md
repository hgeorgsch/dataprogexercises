---
tags:
  - lecture/video
  - api
---




+ HTTP-protokollen
	+ GET 
	+ POST
	+ SSL http vs. https
	+ Text- and binary protocols
+ What is a protocol?
+ Program som gjev primitiv tilgang til protokollen
	+ telnet
	+ curl
	+ anna?
+ Filformat
	+ HTML
	+ JSON
+ API - Application Programming Interface
	+ Web API
	+ Filtilgang
	+ Sanntidskommunikasjon
+ Modularisering av tenester
	+ REST
	+ Micro-Services vs. Monolittiske tenester

Relevant ressurs [[WebAPI-Requests-JH]]
#### Skisse av narrativ:

### Intro
 - Hvor mye og hva slags data kan man finne «ute på det store internett» - morsomme, eller inspirerende eksempler
	 - [Avviste personlige bilskilt CA (vanity plates)](https://github.com/veltman/ca-license-plates/blob/master/applications.csv)
	 - [Dataset med alle offentlige toalett i Australia, med addresse ](https://data.gov.au/dataset/ds-dga-553b3049-2b8b-46a2-95e6-640d7986a8c1/details)
	 - [database](https://www.dolthub.com/repositories/Liquidata/bad-words/data/master/bad_words) av stygge ord, slik som kussekryller (dansk) eller  QI'yaH (klingon)
	 - Eller hva med [denne](https://data.world/shruti-prabhu/shark-attacks/workspace/file?filename=attacks.csv) med ~6000 registrerte haiangrep, deriblant [Odd ingebretsen](https://www.nrk.no/stor-oslo/haisommer-i-oslofjorden-1.2984539)
 -  Eksempler på dataset som oppdateres ofte:
	 - Finans, transport, vær, eiendom, nyheter, seismologisk data, sport
	 - [Liten oversikt](https://github.com/bytewax/awesome-public-real-time-datasets)
- Når trenger man «fersk» data? Hvordan får man tak i fersk data 
- Belys hvorfor man trenger å hente data programmatisk
	- Når data oppdateres ofte - finans, vær osv
	- Når det varierer hvilken data man vil ha - mindre relevant?

### Protokoller
-  Hvordan kan python snakke med ressurser over internett?
- Protokoller fra etikette, SNL: *Protokoll er en fellesbetegnelse for alt som har å gjøre med høytidelige former, formaliteter, [seremoniell](https://snl.no/seremoniell) og [etikette](https://snl.no/etikette), særlig på [kongehusets](https://snl.no/Det_norske_kongehuset) og [utenriksvesenets](https://snl.no/Utenrikstjenesten) område. Både protokoll og etikette gjelder praktiske kjøreregler for sosial omgang, både når det gjelder god oppførsel, takt og tone, skikk og bruk. Regelverket kan ha relevans både i offentlig og privat sammenheng.*

#### Protokoller innen IT
- OSI-modellen - hva som skjer i lagene og noen protokoller de kanskje har hørt om (TCP,. IP, DNS, Ethernet, MAC)
- HTTP-protokollen: Hvordan laster vi inn forsiden til feks nrk.no?
	- Gjerne en enkel vevside hvor vi kan gjøre det samme med telnet (evt curl)
	- Meget kort om HTML-format her?
* HTTP spørring: GET PUT POST osv
* HTTPS/SSL nevnes kanskje her
*  Responskoder, og evt andre interessante detaljer man ikke ser så ofte?
*  Praktisk eksempler med telnet og/eller curl som viser litt hva som skjer i bakgrunnen
	* telnet og example.com
	* telnet httpbin.org
```bash
telnet example.com 80

GET / HTTP/1.1
Host: example.com


```
For å lagre output til fil i tillegg (Så vi kan vise html i en nettleser):
```bash
script -c "telnet example.com 80" output.txt
```
POST med httpbin:
```bash
POST /post HTTP/1.1
Host: httpbin.org
Content-Type: application/x-www-form-urlencoded
Content-Length: 13

name=Student
```


*  Litt om html/json/xml avhengig av hva telnet/curl gir oss å se på

### Hvordan bruke feks http-protokoll til å hente data?
#### API
- 