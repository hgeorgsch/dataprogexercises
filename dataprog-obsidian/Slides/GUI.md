---
title: Grafiske brukargrensesnitt
author: Hans Georg Schaathun
tags:
  - lecture/video/perspective
css:
  - css/templates.css
---

# Grafiske brukargrensesnitt

note:
Når me tek til å tenkja på frittståande program, er der sikkert mange
som tenkjer hovudsakleg på grafiske brukargrensesnitt eller GUI.

Interaktivitet er krevjande, fordi programmereren gir over so mykje
kontroll til brukaren.  I staden for å fylgja ein fast serie med
instruksjonar for å gjera ein beregning, treng ein rutinar som hoppar
rundt i koden for å gjera det som brukaren ber om.

Moderne GUI-bibliotek har god støtte for å handtera interaksjon, og
eg skal gå gjennom nokre av dei grunnleggjande konsepta.

---
<!-- slide template="[[tpl-flex]]" bg="lightblue" -->

![[Example_of_a_GUI.png]]

::: credit
Sikon at English Wikipedia.  GPL, 
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=141041371).
:::

note:
Et grafisk brukergrensesnitt består av et utall komponenter.
Der er et eller flere vindu, men der er også knapper, radioknapper,
tekstfelter, *input*-felter og rammer som grupperer andre komponenter.

Komponentene er ikke uavhengige av hverandre.  Bortsett fra vinduet, er
alle komponentene en del av en større komponent, og de henger sammen.
Når vinduet lukkes, forsvinner også alle de andre komponentene.


---
<!-- slide template="[[tpl-flex]]" bg="lightgrey" -->


![[guihierarchy.svg]]


::: credit
:::


note:
For å få dette systemet av komponenter til å fungere, er
GUI-programmering i python er objektorientert.
Kvar einaste GUI-komponent er eit objekt som har sine eigne metodar
for å interagera med andre komponentar.

Komponentene blir ordnet i et hierarki, med ett vindu på toppnivå.
I `tkinter` for python, har dette toppvinduet klassen `Tk`.
Alle andre komponenter har en foreldrekomponent.

---

- Instansiering: `btn = Button(root, text = "Trykk her")`
- *Layout*: `btn.pack()`

note:
For å få en ny komponent på skjermen trengs *to* steg.
Det første er instansieringen.  
Vi må lave objektet i python.
Når vi instansierer en komponent, gir vi alltid foreldrekomponenten som argument.

Det andre er *layout management*.  Vi må fortelle komponenten
hvordan den skal plasseres i foreldrekomponenten.
Der er mange forskjellige *layout managers* å velge mellom;
`pack()` er den aller enkleste.  Den bare pakker alle komponentene sammen
der det er plasse.
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

`mainloop` vil kjøre i uendelig løkke helt til vinduet blir lukket.
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
