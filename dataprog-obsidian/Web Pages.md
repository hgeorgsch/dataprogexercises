---
tags:
   - legacy/iif
---

+ URL for kursporteføljen https://iirevu.org.ntnu.no/
+ [IIRA2001 Jupyter Book](https://jonajh.folk.ntnu.no/IIRA2001H25/intro.html)
+ Innhold ligg på /home/groupswww/iirevu på login.ansatt.ntnu.no
	+ /home/groups/iirevu er tilgjengeleg for intern deling
	+ ) hvor unix-gruppe settes til overnevnte gruppe. Gruppa får skriverettigheter. Det kjøres en jevnlig jobb som rydder opp i rettighetene hvis disse settes feil. Det kan være lurt å sette umask g+w for prosesser som skal legge til filer og kataloger.
+ bas-gruppe https://bas.ntnu.no/editgroup/?id=1916562 

```htaccess
    AuthName "Tilgang til iirevu"  
    AuthType Basic  
    AuthBasicProvider ldap  
    Require ldap-attribute ntnumemberof="fs_fagkode"  

```
### Korrespondanse med Aslak Raanes på NTNU Hjelp

### 1

Det raskeste er vel å bruke «enkel samhandling», dvs. det opprettes en gruppe slik at en nettside à la https://webdrift.org.ntnu.no automatisk opprettes.  
  
Tilgang til denne kan styres vha. bas-grupper for redigering/publisering. og .htaccess à la  
  
    AuthName "Tilgang til eksempelfag"  
    AuthType Basic  
    AuthBasicProvider ldap  
    Require ldap-attribute ntnumemberof="fs_fagkode"  
  
Hvor fs_fagkode finnes i bas.  
  
Feide (dvs. openid connect eller saml) blir litt mer komplisert.  
  
Hvis dette ikke passer så kan saken settes tilbake til server slik at dere etterhvert får en halvadministert maskin.

### 2 

«Enkel samhandling» er kanskje den enkleste for brukere og drift å vedlikeholde hvis en kan opere innen de begrensningene løsningen har.   

1. Det opprettes en gruppe, f.eks. iirevu
2. De som skal kunne endre på filer legges til i denne gruppa i bas.
3. Det vi automatisk opprettes en katalog /home/groupswww/iirevu (og /home/groups/iirevu ) hvor unix-gruppe settes til overnevnte gruppe. Gruppa får skriverettigheter. Det kjøres en jevnlig jobb som rydder opp i rettighetene hvis disse settes feil. Det kan være lurt å sette umask g+w for prosesser som skal legge til filer og kataloger.
4. groupswww-katalogen vil være tilgjengelig fra https://iirevu.org.ntnu.no/ 
5. Apache-prosessen (og cgi, php osv.) kjører med overnevnte gruppe. https://webdrift.org.ntnu.no har noen applikasjoner en kan kjøre, noe som kanskje ikke er relevant siden dere har statisk materiale.

Om dette er den beste/anbefalte løsningen for deling med studenter kan sikkert diskuteres, men det er den som er enklest og mest fleksibelt å bruke/knote med.


### 3 

1. Ja. /home/groupswww/iirevu og /home/groups/iirevu er tilgjengelig fra login.ansatt.ntnu.no
2. Det er en bas-gruppe https://bas.ntnu.no/editgroup/?id=1916562 som styrer tilgang og om området eksister. Blir bas-gruppa tom, dvs. medlemmene slutter fra NTNU eller de fjernes, så slettes området automatisk
3. Flere ldap-atributter kan legges til https://httpd.apache.org/docs/current/mod/mod_authnz_ldap.html#reqattribute Det gjør det vel lettere hvis ekstern sensor har gjestebruker som er medlem av en bas-gruppe.
