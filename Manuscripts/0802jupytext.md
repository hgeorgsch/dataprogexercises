(Jupyter i ulike filformat)

*Notebook*-filene som vi har jobbet med i Jupyter er et utrolig fleksibelt og gjenbrukbart format.
Det er verd å ta en titt på forskjellige måter å bruke *Notebooks* på.

(jupyter)

Som vi vet består Jupyter Notebook-dokumentet av bokser.  
Stort sett bruker vi tre typer bokser, *markdown* og *code* som vi skriver selv, og *output* som er resultatet av å kjøre *Code*-bokser. Jupyter-programmet har en kjerne, *kernel*, som gjør jobben som tolk og kjører programmet.  Som regel tolker kjernen python, men andre kjerner for andre sprog er mulig.  Der finnes en fjerde blokktype, *raw*, men den er lite brukt.

(Konvertering av *Notebooks*)

Vi er vant til å jobbe med `ipynb`-filer som inneholder *Notebooks*.
`ipynb` bruker JSON for å representere blokkene som objekter.
Strukturen er ikke fryktelig vanskelig å forstå hvis du åpner filen i en tekst-*editor*.

Det er mulig å lagre en *Notebook* i andre formater enn JSON og `ipynb`,
og det er det jeg vil snakke om her.

Først skal vi skille mellom verktøy som typesetter en *Notebook* for presentasjon, kanskje som en rapport i PDF eller en vevside i HTML. Dette gjør det mulig å dele den ferdig kjørte *Notebook* med kolleger som ikke selv bruker python eller Jupyter.

Læringsmaterialet til kurset er lavet på denne måten, med et system som heter *Jupyter books*.  Jeg skal ikke gå inn på *Jupyter Books* i dag fordi versjon 2 nylig er kommet, og jeg kjenner bare versjon 1.  Et litt enklere verktøy for slik oversettelse er `nbconvert`, men det har jeg ikke brukt selv.

(jupytext)

Oversettelse til presentasjon er enveis.  Det er ikke mulig å oversette tilbake fra presentasjonsformatet til en *Notebook* som kan redigeres og kjøres på nytt.

`jupytext` gjør på den andre siden toveis oversettelse mellom `ipynb` og andre formater.

(demo)

Hvis vi har en *Notebook* som vi ønsker å bruke som frittstående program, kan vi bruke py:percent-formatet.  jupytext kjører på kommandolinjen og det er en enkel kommando å konvertere ipynb til py.

(markdown)

Trikset som jupytext bruker er å la alle markdown-boksene bli til kommentarer i
python-koden.
Linjer som begynner med skigarden *hash* er kommentarer som blir ignorert av tolken,
og de kan derfor brukes til alle typer tekst for menneskelige lesere.

For å kunne oversette tilbake til `ipynb`-format, må også boksene markeres.
Her bruker jupytext to prosentegn for å markere starten på hver boks,
derav navnet py:percent.
Når boksen ikke er kode, kommer bokstypen like efter prosenttegnene.

*Output* er ikke med py:percent-filen, men det kan regenereres  
ved å kjøre koden på nytt når den konverteres tilbake til ipynb.

(køyring)

Når den *Notebook* er konvertert til py:percent kan vi også kjøre den gjennom python-tolken på kommando-linjen.

Dette blir en  mulig måte å utvikle frittstående programmer på.  Man kan prøve og feile i Jupyter, og konvertere til py:percent når man er fornøyd.

(md)

jupytext kan også oversette til et rent markdown-format.
Kode som skal gjengis nøyaktig blir markert med omvendte apostrofer eller *backticks* i markdown. Kodeceller fra *Notebook* blir i tillegg satt med en bestemt annotering *code-cell* i krøllparenteser.

Prinsippet er akkurat det samme som for py:percent.  Vi får en korrekt fil i et eksisterende format, med blott litt ekstra annotering for å markere blokkene i Jupyter Notebook.

(Slutt)

En av de store fordelene med tekstformatene markdown og py:percent er at *output* ikke er med.  Det er nyttig ved versjonskontroll, fordi man slipper å se endringer som bare er et resultat av variasjoner i kjøringen.  Det skal vi drøfte i en anden video.

Det jeg har forsøkt å få frem her er at arbeidet du gjør i *Jupyter* kan gjenbrukes på mange forskjellige måter. Ingen har tid til å lære seg å bruke alle muligehetene, men det er verd å vite at de er der.
