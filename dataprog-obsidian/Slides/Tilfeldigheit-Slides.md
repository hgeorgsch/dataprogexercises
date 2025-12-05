---
tags:
  - lecture/video
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

Stoakstiskte prosesser

note:
I statistikken kaller vi gjerne slike tilfeldige prosesser for
*stokastiske* prosesser.  Enkelt sagt er «stokastisk» blott
et penere ord for tilfeldig.

---

Monte Carlo-simuleringer

note:
I simuleringsliteraturen, blir tilfeldige simuleringer gjerne
kalt for *Monte Carlo-simuleringer* efter de kjente kasinoene
i Monte Carlo, med spill som roulette.

---

+ Slumptal


note:
Slump, eller tilfeldighet, er vanskeleg for datamaskiner, som er
konstruerte for å vera fullt ut deterministiske system.
Virkeleg slump må derfor komme utanfrå, som *input*.

Det er mulig å få det til, ved å måle ørsmå variasjoner i
tastefrekvensen fra brukeren, eller i temperaturen i rommet,
eller spenning på strømnettet.
Der er derimot en grense for hvor mye slump man kan hente ut
på denne måten på kort tid.
Store simuleringer krever ofte mer slump.

---

+ *Pseudo-random numbers*

note:
I praksis bruker vi som regel såkalte *pseudo-tilfeldige* tall.
Det er matematiske formler som gjør at vi kan regne ut lange serier
med tall som *ser tilfeldige ut*.

---

$$ s_i = a\cdot s_{i-1} \mod p $$

note:
Det mest kjente tilfellet er lineær kongruens.

Her starter vi med ett tall $s_0$, som vi gjerne kaller frøet eller *seed*.
Når vi har ett tall $s_{i-1}$, kan vi regne ut det neste tallet $s_i$ ved
å gange med en konstant $a$ og ta resten ved divisjon med $p$.

Dersom vi velger $a$ og $p$ fornuftig, vil føgen av tall $s_i$
se tilfeldig ut.

Den nøyaktige formelen er ikkje viktig for oss.  Det som er greitt
å hugsa er at når me har det fyrste talet, eller **frøet** (*seed*),
så vil slumptalsgeneratoren gi oss en *uendelig* følge med
tilfeldigaktige tal.

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
<!-- slide template="[[tpl-twocolumn]]" -->

::: leftimage

```python
import random
def terning():
    return random.randint(1,6)
```

```
In [5]: [ terning() for _ in range(10) ]
Out[5]: [5, 1, 2, 6, 6, 4, 3, 3, 4, 3]
```

:::

::: leftcredit
:::

::: rightimage
![[6sided_dice_(cropped).jpg]]
:::

::: rightcredit
By Diacritica - Own work, CC BY-SA 3.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=99768017)
:::


---

histogram uniform diskret

---

histogram uniform kontinuerleg

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

---

histogram Gauss

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

---

## Frøet

Som me nemnde over, må slumptala starta med eit frø.
Om me ikkje oppgjev eit frø, vil maskina freista å finna noko
tilfeldig, t.d. dei minst signifikante sifra i systemklokka.

Lat oss køyra nokre eksperiment.
Me kan laga ein serie med tilfeldige tal ved å bruka
listekomprehensjon.

```{code-cell} ipython3
test = [ random.randint(1,10) for i in range(8) ]
print(test)
```

::: {admonition} Oppgåve
Køyr cella over fleire gongar.  Får du dei same tala 
kvar gong?
:::

Me kan velja frø med `random.seed()`, slik:

```{code-cell} ipython3
random.seed(42)
test = [ random.randint(1,10) for i in range(8) ]
print(test)
```

::: {admonition} Oppgåve
Køyr cella over fleire gongar.  Får du no dei same tala kvar gong?
:::

::: {admonition} Oppgåve
Endra frøet (42) til ein annan verdi.  Får du stadig same talrekkje?
:::

::: {admonition} Refleksjon
Kva har me lært av eksperimenta over?
:::


---


```python
klasse = [ "Arne", "Bente", "Cecilie", "Denis", "Emil", "Freya",
        "Gyda", "Holger", "Inger", "Jens", "Kim", "Line", "Merete",
        "Nina", "Olga", "Petter", "Quentin", "Ruth", "Stine", 
        "Tore", "Unni", "Vidar", "Webjørn", "Xavier", "Yngve",
        "Zacharias", "Ægir", "Ølvar", "Åmund" ]

n = len(klasse)
indekser = [ random.randint(0,n-1) for _ in range(3) ]

referansegruppe = [ klasse[x] for x in indekser ] 

print( referansegruppe )
```

---

Ofte vil de sjå liknande kode skrive med ein `for`-løkke i staden
for listekomprehensjon.  Det ser slik ut.

```{code-cell} ipython3
liste = []
while len(liste) < 7:
   idx = random.randint(0,n-1) 
   person = klasse[idx] 
   liste.append( person )

print( liste )
```


::: {admonition} Refleksjon
Me har sikkert sett mindre av `while` enn av `for`.
Kva gjer `while`-lina over?
Korleis ville du ha skrive løkka om som ei `for`-løkke?
:::

No er det mogleg å leggja til ein test for å hindra duplisering,
ved å bruke `in`- eller `not in`-operatoren.

```{code-cell} ipython3
liste = []
while len(liste) < 7:
   idx = random.randint(0,n-1) 
   person = klasse[idx] 
   if person not in liste:
      liste.append( person )

print( liste )
```

`random.choice()`

