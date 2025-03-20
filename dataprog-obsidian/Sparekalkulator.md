
# Oppgave 2: Sparekalkulator
----

Dersom vi sparer et fast terminbeløp $P$ som vi betaler inn på konto $n$ ganger i året, vi har en p.a. rente på $r$ prosent og vi sparer i $t$ år, vil sluttbeløpet på sparekontoen være gitt ved:
$$
F = P\cdot \left(\frac{\left(1+\frac{r}{n}\right)^{nt}-1}{\frac{r}{n}}\right)
$$

Lag et program som ber bruker av programmet om å taste inn terminbeløp, rente, antall innskudd/renteavregninger og antall år og gir følgende tilbakemeldinger:
* Programmet oppsummerer og gir tilbakemelding på tallene brukeren gav
* Programmet beregner og oppgir sluttbeløpet på sparekonto
* Programmet angir hvor mye av sluttbeløpet er renter og innskudd, i prosent og kroner

*(Merk at $r$ i formelen ikke er i prosent, 2% = 0.02)*

### Dersom du vil
----
Dersom du vil kan du også ta inflasjon, formueskatt ($\approx 1\%$) og skatteprosent (22% av renteinntekter) med i beregningene