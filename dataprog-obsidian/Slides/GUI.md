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




---
<!-- slide template="[[tpl-flex]]" bg="lightblue" -->

![[MVC-Process.svg]]
::: credit
iBy RegisFrey - Own work, Public Domain,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=10298177)
:::

---

note:
