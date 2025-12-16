---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  name: dataprog
  language: python
  display_name: dataprog
---

# Listekomprehensjon

Her skal me gje nokre døme på listekomprehensjon, med utgangspunkt oi
dømet frå [](Simulering av kontantstraum).
Listekomprehensjon gjev oss ein kompakt måte å samla opp resultat i
ei liste.
Lat oss kjapt importera PyPlot og setja opp parametre for startsaldo,
rentesats og tidsperiode.

```{code-cell} ipython3
import matplotlib.pyplot as plt
start = 10000
rente = 0.04
tid = list(range(20))
```

Her reknar me kun med forrenting på startbeløpet og ingen periodisk 
sparing.
Saldoen etter $y$ år er då $s\cdot (1+r)^y$ der $s$ er startsaldoen
og $r$ er rentesatsen.
Dette kan me implementera som ein python-funksjon, slik.

```{code-cell} ipython3
def saldomedrente(start,years):
   return start*(1+rente)**years
```

Dersom me skal plotta saldoen som ein funksjon av tiden, må me
på ein eller annan måte laga oss ei liste med alle saldoane.
Dette kan me gjera med ein `for`-løkke slik:

```{code-cell} ipython3
y = [ ]
for i in tid:
   saldo = saldomedrente(start,i)
   y.append( saldo )
plt.plot(tid,y)
plt.show()
```

Med kan like gjerne gjera det med listekomprehensjon.
Da kan det sjå slik ut:

```{code-cell} ipython3
y = [ saldomedrente(start,i) for i in tid ]
plt.plot(tid,y)
plt.show()
```

Det som tek fire liner med `for`-løkka, kan me altso skrive som èi line
med listekomprehensjon.

## Andre døme

Teksta på $x$-aksen er ikkje heilt god.  Det er betre om me har dato
på dei punkta som faktisk er observert, eller evt. kvart andre eller kvart
femt punkt.
Me kan bruka listekomprehensjon til å laga ei liste med dei tekstene me
vil ha, t.d. annakvart år frå 2023, med dato fyrste i fyrste.
Det kan sjå slik ut.

```{code-cell} ipython3
start_aar = 2023
tid_aar = [ f"01.01.{start_aar+t}" for t in tid if t%2 == 0 ]
print(tid_aar)
```

Kvart element i `tid_aar` er no ein streng.
Uttrykket `t%2` er resten ved divisjon med 2, dvs. 1 for oddetal og 0 for
partal.

For å bruka desse tekstene, må me bruka `xticks`-funksjonen, t.d. som under.
Her treng me eit argument `ticks` som fortel kva merke som vert brukt;
her annakvart merke.
Tekstene vert definerte i `labels`-argumentet, og til sist roterer me
tekstene 45°.  
For å gjera det tydeleg at me har bestemte observasjonspunkt, bruker me
eit søylediagram i staden for ei kurve.

```{code-cell} ipython3
plt.bar(tid, y)
plt.xticks(ticks=range(0,len(tid_aar)*2,2), labels=tid_aar, rotation=45) 
plt.show()
```

## Oppsummering

Ofte er slike listekomprehensjonar lette å lese, skriva og forstå.
Ein skal likevel ikkje overdriva.
Somme tider er ei *for*-løkke som byggjer opp lista med `append` enklare.
Det er viktig å fokusera på å skriva koden slik at han er lett å lesa.  Di vanskelegare koden er å lesa, di fleire feil vil ein gjera.
