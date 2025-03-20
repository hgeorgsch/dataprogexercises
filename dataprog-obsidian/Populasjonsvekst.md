
# Oppgave 1: Populasjonsvekst
----

Ta utgangspunkt i eksempelet fra plenumsøkten om populasjonsveksten på Island og skriv følgende program:

* Programmet spør bruker etter:
    - Navn på området (eg. Island, Finmark osv)
    - Vekstrate
    - Startår
    - Sluttår
    - Populasjon ved startår
* Programmet beregner populasjonsstørrelse ved sluttår
* Programmet oppsummerer og gir tilbakemelding om størrelsene som er gitt
* Programmet angir populasjon ved sluttår
* Programmet angir hvor mye populasjonen har vokst absolutt (antall folk) og relativt (prosent)

Populasjonsveksten antas beskrevet av den logistiske ligningen som sist:

$$
P(t) = \frac{K}{1+Ae^{-rt}}
$$
Her er:
* $P(t)$: Populasjon ved tiden t
* $t$ er tiden
* $r$ er relativ vekstrate, feks 2%
* $K$ er makskapasiteten til populasjonen
* $e$ er eulers tall: $e\approx 2,71828$

$A$ er en koeffisient definert ved:
$$
A = \frac{K-P_0}{P_0}
$$
Hvor $P_0$ er populasjonen ved $t=0$


+  Tillegg veke 2
	+ makspopulasjon
+ Tillegg veke 3  `Oppgave3(kladd)-JH.ipynb` 
	+ likningsløysing/krossingspunkt