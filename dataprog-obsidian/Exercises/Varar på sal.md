---
tags:
   - exercise
   - legacy/iif
---

+ `Oppgave5-JH-LF.ipynb`

#### Oppgave 5.1: Varer på salg

Vi ønsker å undersøke hvordan det å sette varer på tilbud påvirker salg og omsetning

* Anta at en butikk ar et knippe produkter til en viss pris
* Når en kunde kommer inn i butikken er det en viss sjanse knyttet til hvert produkt for at kunden kjøper det
* Dersom varene kommer på salg øker denne sjansen

* Gjør noen antagelser om hvor mange kunder som kommer innom butikken hver dag
* Når en kunde kommer inn i butikken har de et visst budjsett som vi trekker tilfeldig fra en passende fordeling
  - Her kan dere bruke feks `random.gauss()`,`numpy.random.normal()`, `random.uniform()`
* Kunden ser så gjennom produktene og kjøper de basert på tilfeldighet (produktets parametre) og om de har penger igjen i budsjettet

* Sammenlign salg og omsetning for en måned med og uten produkter på tilbud
* Du velger selv hvordan sjansen for salg skal øke med tilbudsrate -- men den logistiske modellen er en god kandidat
* Fremstill resultatet av simulering grafisk med `matplotlib`


# Oppgave 5.2: Simulere markedsdynamikk

1. Set opp en markedsmodell for et gode:
 
* Tilbud: $Q_s = a - bP+\epsilon_s$
* Etterspørsel $Q_d = c + dP +\epsilon_d$
Her er:
* $Q_d =$ Kvantum etterspurt
* $Q_s =$ Kvantum "tilbudt"
* $P = $ Pris
* $a,b,c,d =$ Konstanter dere bestemmer
* $\epsilon_d, \epsilon_s = $ "Sjokk" i markedet for tilbud og etterspørsel

Velg fornuftige verdier for $a,b,c$ og $d$

2. Implementer tilfeldig sjokk i markedet
   * Velg $\epsilon_d$ og $\epsilon_s$ tilfeldig fra en normalfordeling med middelverdi 0 og et passende standardavvik
   * Her kan du bruke `random.gauss(..)` eller numpy sin `np.random.normal(...)`

3. Simuler markedet over tid
   * Simuler et visst antall perioder (feks 50)
   * For hver periode skal du:
     - Regne ut nye markedssjokk $\epsilon_d$ og $\epsilon_s$
     - Bestemme likevektsprisen $P^*$
     - Bestemme likevektskvantumet $Q^*$
4. På et gitt tidspunkt simulerer vi **en** intervensjon (?) i markedet (Feks halveis i simuleringen):
   * Skatt: Øk etterspørselfunksjonens $a$ for å simulere økt beskatning på produksjon
   * Subsidier: Minsk etterspørselfunksjonens $a$ for å simulere subsidier til produksjon
   * Innfør en makspris eller minimumspris
   * Fortsett simuleringen med oppdatert modell for markedsdynamikken

5. Plot resultat med matplotlib
   * Plot likevektspris og likevektskvantum over tid
