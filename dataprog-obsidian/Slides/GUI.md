---
title: Grafiske brukargrensesnitt
author: Hans Georg Schaathun
tags:
  - lecture/video/perspective
css:
  - css/templates.css
---



<!-- slide template="[[tpl-flex]]" bg="lightblue" -->

# Grafiske brukargrensesnitt

![[Example_of_a_GUI.png]]

::: credit
Sikon at English Wikipedia.  GPL, 
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=141041371).
:::

note:
Når vi tenker frittståande program, er der sikkert mange
som tenker på grafiske brukergrensesnitt eller GUI.

Interaktivitet er krevande, fordi programmereren gir over so mye
kontroll til brukeren.  I stedet for å følge en fast serie med
instruksjoner for å gjøre en beregning, må programmet hoppe rundt til ulike rutiner alt efter hva brukeren ber om.

Moderne GUI-biblioteker har god støtte for å håndtere denne interaksjonen, og jeg skal gå gjennom noen av de grunnleggende konseptene.

Et grafisk brukergrensesnitt består av et utall komponenter.
Der er et eller flere vindu, men der er også knapper, radioknapper,
tekstfelter, *input*-felter og rammer som grupperer andre komponenter.

Komponentene er ikke uavhengige av hverandre.  Bortsett fra vinduet, er
alle komponentene en del av en større komponent, og de henger sammen.
Når vinduet lukkes, forsvinner også alle de andre komponentene.
Når brukeren trykker send, må beskjeden gå til vinduet som også må ha orden på innholdet i alle inputtboksene og tilstanden på radioknappene.


---
<!-- slide template="[[tpl-flex]]" bg="lightgrey" -->


![[guihierarchy.svg]]


::: credit
:::


note:
For å få dette systemet av komponenter til å fungere, er
GUI-programmering i python er objektorientert.
Hver eineste GUI-komponent er et objekt som har sine egne metoder
for å interagere med andre komponente.

Komponentene blir ordnet i et hierarki der noen komponenter inneholder andre komponenter.  På toppen ligger selve vinduet, som inneholder andre komponenter.  Rammer brukes gjerne til å gruppere andre komponenter, særlig radioknapper må grupperes.
Nederst i hierarkiet finner vi typisk inputtkomponenter, tekstfelter og lignende.
Bortsett fra hovedvinduet har alle komponentene en foreldrekomponent.

Merk at dette hierarkiet beskriver objekter som eier hverandre, og ikke klasser som arver hverandre.
Arvehierarkiet er også viktig.  Alle GUI-komponentene tilhører den samme overordnede klassen, slik at et objekt kan inneholde et andet objekt uten å vite eksakt hvilken klasse det har. 

---

- Instansiering:
	- `btn = Button(root, text = "Trykk her")`
- *Layout*:
	- `btn.pack()`

note:
For å få en ny komponent på skjermen trengs *to* steg.
Det første er instansieringen.  
Vi må lave objektet i python.
Når vi instansierer en komponent, gir vi alltid foreldrekomponenten som argument.

Det andre er *layout management*.  Vi må fortelle komponenten
hvordan den skal plasseres i foreldrekomponenten.
Der er mange forskjellige *layout managers* å velge mellom;
`pack()` er den aller enkleste.  Den bare pakker alle komponentene sammen
der det er plass.
Andre *layout managers* gir mer kontroll over plasseringen.

---

```python
root = Tk()
root.mainloop()
```

note:
Rotvinduet er spesielt, siden det er forfader til alle de andre komponentente.
Vi instansierer som regel uten argumenter, og for å få vinduet opp på
skjermen, kaller vi `mainloop()`-metoden.

Det vanligste GUI-biblioteket i python heter `tkinter` og her heter klassen for rotvinuder `Tk`.  

`mainloop` vil kjøre i uendelig løkke helt til vinduet blir lukket.
Programmet vil ikke fortsette så lenge vinduet eksisterer.
Dvs. at vi må sette opp alle komponentene og funksjoner som bestemmer hva
de skal gjøre, før vi starter `mainloop`.
Vi kan ikke prøve oss frem linje for linje som vi er vant med i Jupyter Lab.
Ingenting skjer på skjermen før alt er satt sammen og `mainloop` kan startes.


---

## *callback*

```python
btn = Button(root, text = "Trykk her", command=callback )
```

note:
Vi trenger altså bare to linjer for å få et vindu på skjermen, og to linjer til for å få en knapp, men det er ikke særlig interessant uten at noe skjer når vi *trykker* på knappen.

Den enkleste måten å få ting til å skje er å bruke såkalte
*callback*-funksjoner.  

GUI-komponenter som `Button` tar gjerne et argument `command`
som er en funksjon som skal kjøres hver gang knappen trykkes.
Dette gir knappen en mulighet til å ringe oss tilbake når
den blir trykket, ved hjelp av *callback* funksjonen.

En slik *callback*-funksjon kan gjøre hva som helst.  Endre
datamodellen, åpne et nytt vindu, skrive ut ny informasjon på
skjermen.

---

Event handling

note:
Så langt har vi bare snakket om det visuelle.
Vi har nok til å få GUI-komponentene til å dukke opp på skjermen,
men så langt *gjør* de ingenting.

Den mekanismen som får ting til å skje i et GUI-program kalles
gjerne for *Events* og *Event* handling.
De åbenbare *Events* er at brukeren trykker på en tast på tastaturet,
flytter på musen eller trykker en museknapp.
Slike *Events* blir fanget opp av GUI-komponentene, som gjerne genererer
nye *Events*.
En GUI-knapp vil oppdage når brukeren trykker på musen med pekeren oppå
knappen, og da genereres en ny *Event* som sier at denne GUI-knappen er
trykket.

*Events* kan også genereres når andre ting skjer.  F.eks. kan datamodellen
generere en *Event* når den blir endret, for å fortelle andre komponenter
at visningen må oppdateres.

Der er tilfeller hvor vi trenger å definere våre egne *Events*,
men ofte kan vi la *Events* bli under panseret, og klare oss med
*callback*-funksjoner.
Vi kan også definere variabler som kaller en *callback*-funksjon når
de blir endret.

---

::: credit
By Bild von bere von awstburg auf Pixabayhttps://pixabay.com/de/photos/die-dschungel-von-chiapas-1865639/ - https://pixabay.com/de/photos/die-dschungel-von-chiapas-1865639/Derivative work fromFile:Chiapas_Rainforest.jpg, CC0, https://commons.wikimedia.org/w/index.php?curid=105447521
:::

+ *low coupling*
+ *high cohesion*

note:
Store program har en tendens til å bli en jungel av klasser og funksjoner
med uklar hensikt.  Man snakker ofte om spaghettikode.

---
<!-- slide template="[[tpl-flex]]" bg="lightblue" -->

![[MVC-Process.svg]]
::: credit
ved RegisFrey - Own work, Public Domain,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=10298177)
:::


---

note:
