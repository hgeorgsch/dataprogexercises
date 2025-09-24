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

+++

+ To iskremseljarar med vagn som dei kan flytta kvar dag.
    + Mål: tena mest mogleg pengar
+ Hundrevis av kundar som vil ha iskrem på tilfeldig tidspunkt.
    + Basisstrategi: går til næraste kiosk når dei vil ha iskrem
    + Alternativ strategi: lysten på iskrem avheng av avstanden til kiosken
    + Alternativ strategi II: kan ta omsyn til køen
+ Fordeling av kundar
    + Uniform
    + TIlfeldig

+++

+ Klasser
    + Simulator
        + kontrollerer tida 
        + kontrollerer stranda
            + 1D kontinuerleg struktur
            + plasserer tilfeldige badegjestar
        + plasserer badegjestar
    + Kiosk (Kiosk 1 og Kiosk 2)
    + Badegjest
        + sannsyn for kjøp, avhengig av 
            + avstand til kiosk
            + tid frå forrige kjøp
            + lengd på køen
+ Modell 1.
    + Uniformt vær
    + Tilfeldig plasserte badegjestar
    + Kioskane vel plassering
    + Heil dag.  Tilfeldige kjøp.  Ingen kø  
+ Modell 2.
    + Små tidssteg.
    + Kjøp avheng av tid sidan forrige kjøp
    + Kø på kioskane,
+ Modell 2.
    + Badegjestane kan ta omsyn til køen.
+ Modell 3.
    + Varisjon i vêret, som fører til
    + Variasjon i tal på badegjestar
    + Lysta på iskrem
