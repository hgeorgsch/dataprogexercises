---
tags: [exercise, simulering]
title: "Iskrem p\xE5 ei strand"
jupytext:
  cell_metadata_filter: -all
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
  formats: md:myst,ipynb
  root_level_metadata_filter: -tags,-title
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Iskrem på ei strand

Eit velkjend resultat i mikroøkonomi er at dersom der er to aktørar
i ein marknad, vil dei ofte verta meir og meir lik kvarandre.
I mange marknader løner det seg ikkje å skilja seg ut.

Krondømet er to iskremkioskar på ei strand.  Iskrem er iskrem, og badegjestane
vil stort sett gå til den næraset kiosken når dei får lyst på iskrem.
Kioskane er gjerne vognar, slik at kioskeigaren lett kan flytta dei kvar dag,
og den som har mindre enn halve marknaden vil nesten heilt sikkert flytta seg
for å få fleire kundar.

Det går an å visa matematisk at kioskane vil enda opp vegg i vegg midt på stranda,
i alle fall om badegjestane er jamnt fordelte og kioskeigarane ikkje forhandlar om 
ei ordning.
Det går an å visa det same ved hjelp av simulering.

For å oppsummera modellen, har me

## Objektorientert modell

Det er greitt å ta utgangspunkt i ein objektorientert modell på same måte som
i [](Shrimp-Game).
Me treng ei klasse for badegjest, éi for kiosk, og kanskje éi for stranda.

Stranda kan halda greie på kioskane (to) og badegjestane ($n =$?).
Ho må òg fortelja dei andre objekta når dei skal gjera noko.

Stranda, eller sjølina, er eindimensjonal, so kioskane og badegjestane vel
kvar dei står som ein verdi $x$ som t.d. er avstanden frå enden i meter.

## Fyrste modell

Det er alltid best å starta med ein enkel modell.
Lat oss gå ut frå at kvar badegjest kjøpar iskrem éin gong i laupet
av dagen, og at der berre er éin type iskrem, slik at kiosken tener
like mykje på kvart einaste sal.

På starten av dagen må altså Stranda,
+ Be kvar kiosk om å velja plass.
+ Fortelja kvar badegjest kvar kioskane står og be dei velja kva kiosk
  dei handlar i.
+ Fortelja kiosken kvar gong nokon handlar der.

Kiosken må ha ein strategi for å velja posisjon ($x$), t.d. tilfeldig,
og ein funksjon for å registrera sal.

Badegjestane må ha ein strategi for å velja plass (tilfeldig?)
og for å velja kiosk (den næraste).

::: {admonition} Oppgåve
Skriv ein fyrste prototyp basert på føresetnadene over.
Du står fritt til å gjera dine eigne val der noko er udefinert.
Køyr simuleringar og plot omsetnaden for kvar kiosk.
:::

::: {admonition} Oppgåve
I den fyrste prototypen valde kioskane tilfeldig plass på stranda.
Endra denne strategien slik at den kiosken som tener minst, flytter
nærare den som tente mest.  
Køyr simuleringar og plot omsetnaden og plasseringa for kvar kiosk.
:::

::: {admonition} Refleksjon
Er der andre strategiar ein kan prøva?
:::


## Kundestrategi

::: {admonition} Oppgåva
Endra simuleringa slik at Stranda spør badegjestane fleire gongar i
laupet av dagen om dei vil kjøpa iskrem.
Badegjestane kan so bestemme, avhengig av avstanden til næraste kiosk,
om dei vil handla eller ikkje.
:::

::: {admonition} Oppgåva
Utvid simuleringa slik at ho tek omsyn til køen ved kvar kiosk.
Badegjestane kan då velja om dei orkar å venta, går vidare til
den andre kiosken, eller droppar iskremen.
Du må sikkert ha relativt korte tidsinterval og estimera kor lang
tid kvart kjøp tek.

Korleis påverkar dette omsetnaden?
:::

::: {admonition} Refleksjon
Kan du tenkja deg andre fordelingar av badegjestar langs stranda?
:::

## Andre idéar

::: {admonition} Refleksjon
Burde simuleringa ta omsyn til vêret?
:::

## Oppsummering

Dette problemet er ein klassikar.  Dei enklaste tilfella er eigentleg
enklast å løysa matematisk, men når ein tek til å variera kiosk- og
kundestrategiane, kan ein ofte simulera tilfelle som er frykteleg 
vanskelege å løysa analuytisk.

Det er berre fantasien som set grenser.  Det som er viktig er å ha ei
god forståing av kva simuleringa representerer i røynda.  Når du gjer
endringar i simuleringa skal du forvissa deg om at du veit kva du ynskjer
å simulera.  Korleis tenkjer kioskeigarane og badegjestane i simuleringa di?

