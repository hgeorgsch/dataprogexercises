---
tags:
  - lecture/video
css:
  - custom.css
---

# Slumptalsgenerator

---

![newton](https://pbs.twimg.com/media/D2EZ4DwVAAApNdd?format=jpg&name=900x900)

note:
Mange simuleringer handler om tilfeldige prosesser.
I tillegg er der mange prosesser som i teorien er deterministiske,
men som er så kaotiske at vi ikke klarer å modellere dem deterministisk.
Da er det òg naturlig å bruke tilfeldige prosesser som modell.

---

Stokastiske prosesser

note:
I statistikken kaller vi gjerne slike tilfeldige prosesser for
*stokastiske* prosesser.  Enkelt sagt er «stokastisk» blott
et penere ord for tilfeldig.

---
<!-- slide template="[[tpl-quote]]" -->

![[Casino_de_Monte-Carlo_(49582351802).jpg]]

::: credit
By Matthew Hartley from Helmshore, Lancashire, United Kingdom - Casino de Monte-Carlo, CC BY-SA 2.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=87646413)
:::

note:
I simuleringsliteraturen, blir tilfeldige simuleringer gjerne
kalt for *Monte Carlo-simuleringer* efter de kjente kasinoene
i Monte Carlo, med spill som roulette.

---

![[6sided_dice_(cropped).jpg]]


note:
Terningkast og andre tilfeldige prosesser er vanskeleg for datamaskiner.
Maskinene er konstruerte for å vera fullt ut deterministiske system.
Virkeleg slump må derfor komme utanfrå, som *input*.

Det er mulig å få det til, ved å måle ørsmå variasjoner i
tastefrekvensen fra brukeren, eller i temperaturen i rommet,
eller spenning på strømnettet.
Der er derimot en grense for hvor mye slump man kan hente ut
på denne måten på kort tid.
Store simuleringer krever ofte mer slump.

---
<!-- slide template="[[tpl-diagram]]" -->

![[prng.svg]]

::: credit
:::

note:
I praksis bruker vi som regel såkalte *pseudo-tilfeldige* tall.
Det er matematiske formler som gjør at vi kan regne ut lange serier
med tall som *ser tilfeldige ut* uten faktisk å være det.

På norsk kaller vi det gjerne for en slumptallsgenerator.
På engelsk kalles det en
*pseudo-random number generator* eller forkortet PRNG.

Slumptallsgeneratoren er det som vi kaller en endelig tilstandsmaskin.
Den har en tilstand $s_i$, og en funksjon som genererer en ny
tilstand $s_{i+1}$ hver gang vi ber om et slumptall.

I teorien kan vi bruke tilstanden $s$ som et slumptall, men ofte
vil vi ha slumptall fra en anden definisjonsmengde.
Da trenger vi en ekstra funksjon som oversetter tilstanden til
riktig utfallsrom.

---

$$ s_i = a\cdot s_{i-1} + c \mod p $$

$$ y_i = \frac{s_i}{p} $$

note:
Det mest kjente tilfellet er lineær kongruens.
Her regner vi ut tilstanden ved å gange med et tall $a$ og ta resten
ved divisjon med et tall $p$.
Dersom vi velger $a$ og $p$ fornuftig, vil føgen av tall $s_i$
se tilfeldig ut.

---

$$ s_i = 7\cdot s_{i-1} \mod 97 $$

note:
For å ta et leketøyseksempel, kan vi prøve å gange med syv
og dele på syvognitti.
Syvognitti er primtall, noe som gjerne er en god idé.

---
<!-- slide template="[[tpl-diagram]]" -->

![[prng1.svg]]

::: credit
:::

note:
Vi kan starte med en vilkårlig tilstand, si tretten, og se hvilke
tall vi får.

Først enognitti.

---
<!-- slide template="[[tpl-diagram]]" -->

![[prng2.svg]]

::: credit
:::

note:
Så femogfemti.

---
<!-- slide template="[[tpl-diagram]]" -->

![[prng3.svg]]

::: credit
:::

note:
Firognitti.

---
<!-- slide template="[[tpl-diagram]]" -->

![[prng4.svg]]

::: credit
:::

note: 
Seksogsytti

---
<!-- slide template="[[tpl-diagram]]" -->

![[prng5.svg]]

::: credit
:::

note:
Syvogførr.

---
<!-- slide template="[[tpl-diagram]]" -->

![[prng6.svg]]

::: credit
:::

note:
Åttogtredve

---
<!-- slide template="[[tpl-diagram]]" -->

![[prng7.svg]]

::: credit
:::

note:
... og toogsytti.

Den nøyaktige formelen er ikkje viktig for oss.  Det som er greitt
å hugsa er at når me har bestemt den første tilstanden $s_0$, som
vi gjerne kaller frøet eller *seed*, så vil slumptalsgeneratoren
gi oss en *uendelig* følge med tilfeldigaktige tal.

Der er mange kjente slumptallsgeneratorer, og lineær kongruens er 
ikke den beste, blott den best kjente.
Vi pleier derimot ikke være så kresne på slumptallsgeneratorene
i simulering.  Hvis du skal lave lotterier, som nødvendigvis må
være rettferdige, er det langt viktigere at slumptallene ikke
bare ser tilfeldige men også er umulige å forutsi.

De strengeste kravene til slumptall gjelder i kryptografi, som
f.eks. brukes til å sikre pengeoverføringer og sensitive
personopplysninger.

---
<!-- slide template="[[tpl-diagram]]" -->

![[cycle.svg]]

::: credit
:::

note:
Python uses the Mersenne Twister as the core generator.

It produces 53-bit precision floats and has a period of 
$2^{19937}-1. 

---
<!-- slide template="[[tpl-smalltext]]" -->

![[6sided_dice_(cropped).jpg|300]]

```python
import random
def terning():
    return random.randint(1,6)
```

```
In [5]: [ terning() for _ in range(10) ]
Out[5]: [5, 1, 2, 6, 6, 4, 3, 3, 4, 3]
```

::: credit
Illustrasjon ved Diacritica - Own work, CC BY-SA 3.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=99768017)
:::

note:
Når vi skal bruke slumptall i python, trenger vi ikke bekymre oss
om alt som foregår inni slumptallsgeneratoren.
Der finnes flere biblioteker som implementerer slumptall, men vi
skal bruke et som heter `random`.

Hvis vi skal simulere en terning, f.eks. kan vi bruke funksjonen
`randint` og be om et tall mellom 1 og 6.
Når vi laver en liste ved å kalle slumptallsfunksjonen flere ganger,
får vi en serie som ser tilfeldig ut.

---
<!-- slide template="[[tpl-smalltext]]" -->

```python
In [5]: [ random.randint(1,6) for _ in range(10) ]
Out[5]: [5, 1, 2, 6, 6, 4, 3, 3, 4, 3]
```

![[diskretuniform.svg]]

::: credit
:::

note:
Terningen er et eksempel på en uniform fordeling, der
alle verdier er like sannsynlige.
Fordelingen er diskret, dvs. at der bare en enkelte
punkter som forekommer; vi får bare heltall og ikke
desimaltallene imellom.

---
<!-- slide template="[[tpl-smalltext]]" -->

```
In [6]: [ random.random() for _ in range(10) ]
Out[6]:
[0.27342233990237175,
 0.6593076643597294,
 0.30352522077434463,
 0.6338120567326603,
 0.19204871254768463,
 0.3400966630690264,
 0.6469617118607379,
 0.2050789573379762,
 0.3011348077423164,
 0.6835356020355947]
```

![[kontuniform.svg]]

::: credit
:::

note:
Hvis vi vil ha desimaltall, kan vi bruke funksjonen `random()`
som gir et tall mellom 0 og 1.
Dette er også en uniform fordeling, der alle verdier er like
sannsynlige, men den er kontinuerlig og ikke diskret.

---
```
In [1]: import random

In [2]: [ random.random()*100-50 for _ in range(10) ]
Out[2]:
[-39.035627812290464,
 -8.432549451508578,
 5.600303172592014,
 -30.240236134220456,
 -18.705629447346116,
 29.174098952378884,
 -14.896927031712046,
 -9.60240063073671,
 28.873011654664353,
 7.719162441908011]

```

note:
Hvis vi trenger tall fra et andet intervall en null til én, er det 
vanlig å ordne det ved å skalere resultatet.  For å få et tall mellom 
pluss/minus femti, kan vi gange med hundrede og trekke fra femit.

---

<!-- slide template="[[tpl-smalltext]]" -->

```
In [9]: [ random.gauss() for _ in range(10) ]
Out[9]:
[0.3532421321764088,
 -0.9522801582478694,
 0.986347684715697,
 1.1307086907223498,
 -1.0509678395676072,
 0.274450618106159,
 0.6089163638569696,
 -0.38565740512221974,
 1.3538055582579855,
 -0.34163923642131283]
```

![[gauss.svg]]

::: credit
:::

note:
Vi kan også få slumptall fra fordelinger som ikke er uniforme.
Vi skal ikke gå inn på alle, men kan se på normalfordeling,
eller gaussfordelingen, som er så mye brukt.

Funksjonen `random.gauss()` gir et tall som er normalfordelt
med standardavvik 1 rundt en middelverdi på 0.


---

## Frøet

note:
Som me nemnde over, må slumptala starta med eit frø.
Om me ikkje oppgjev eit frø, vil maskina freista å finna noko
tilfeldig, t.d. dei minst signifikante sifra i systemklokka.

Lat oss køyra nokre eksperiment.
Me kan laga ein serie med tilfeldige tal ved å bruka
listekomprehensjon.

---
<!-- slide template="[[tpl-smalltext]]" -->

```
In [3]: [ random.randint(1,10) for i in range(12) ]
Out[3]: [3, 9, 6, 6, 9, 4, 6, 2, 9, 9, 7, 4]

In [4]: [ random.randint(1,10) for i in range(12) ]
Out[4]: [3, 9, 4, 9, 4, 5, 9, 5, 1, 8, 1, 7]

In [5]: [ random.randint(1,10) for i in range(12) ]
Out[5]: [8, 7, 6, 5, 3, 1, 2, 8, 1, 9, 6, 6]
```
<!-- element class="largercode" -->

::: credit
:::

note:
Vi kan bruke slumptallsgeneratoren uten å tenke på frøet.
Da får vi nye tall hver gang.

---
<!-- slide template="[[tpl-smalltext]]" -->

```
In [12]: random.seed(42)

In [13]: [ random.randint(1,10) for i in range(12) ]
Out[13]: [2, 1, 5, 4, 4, 3, 2, 9, 2, 10, 7, 1]

In [14]: [ random.randint(1,10) for i in range(12) ]
Out[14]: [1, 2, 4, 4, 9, 10, 1, 9, 4, 9, 7, 4]

In [15]: [ random.randint(1,10) for i in range(12) ]
Out[15]: [8, 10, 5, 1, 3, 7, 6, 5, 3, 4, 6, 2]
```
<!-- element class="largercode" -->

::: credit
:::

note:
Hvis vi ønsker å sette frøet selv, bruker vi `random.seed()`.
Her starter vi frøet på 42, og genererer tre forskjellige lister
med tilfeldige tall.

---
<!-- slide template="[[tpl-smalltext]]" -->

```
In [6]: random.seed(42)

In [7]: [ random.randint(1,10) for i in range(12) ]
Out[7]: [2, 1, 5, 4, 4, 3, 2, 9, 2, 10, 7, 1]

In [8]: random.seed(42)

In [9]: [ random.randint(1,10) for i in range(12) ]
Out[9]: [2, 1, 5, 4, 4, 3, 2, 9, 2, 10, 7, 1]

In [10]: random.seed(42)

In [11]: [ random.randint(1,10) for i in range(12) ]
Out[11]: [2, 1, 5, 4, 4, 3, 2, 9, 2, 10, 7, 1]
```
<!-- element class="largercode" -->

::: credit
:::

note:
Hvis vi setter frøet til 42 før hver liste vi genererer,
ser vi at alle listene blir like.  Hver gang vi laver en
tilfeldig liste, har vi startet slumptallsgeneratoren på
det samme punktet.

Dette kan være særs nyttig ved simulering, fordi det lar
oss kjøre den eksakt samme simuleringen flere ganger.
Særlig når vi skal kvalitetssikre koden vår eller leter
efter feil, kan det være greitt å kunne sammenligne kjøringer
uten tilfeldige faktorer.

Det er derimot viktig at man ikke setter frøet i utide.
Om du tilbakestiller frøet midt i en simulering, vil ikke
fortsettelsen se like tilfeldig ut som starten.


---

# Slutt

note:
Det var alt for denne gang.  Ikke glem å teste på egen hånd.
