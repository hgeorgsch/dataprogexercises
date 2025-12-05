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

## Sannsynsfordelinger

---

## Tilfeldige tal i python

Der er fleire bibliotek som kan gje oss slumptal.
Det mest grunnleggjande er `random`.

```{code-cell} ipython3
import random

tilfeldig_tall = random.random()

print(f"Mitt tilfeldige tall er {tilfeldig_tall:.4f}")
```

::: {admonition} Refleksjon
1. Kva gjer dei ulike linene over?

2. Kva slags tal vert generert?

3. Køyt cellen eit par gongar.  Kva trur du er den største og minste
   verdien `random.random()` kan generera?
:::

::: {admonition} Oppgåve
I `print`-satsen bruker me ein notasjons som kan henda er ny,
i `{tilfeldig_tall:.4f}`, for å få pen formattering av utskrifta.

1.  Kva tyder 4-talet?  Endra det (t.d. til 3 eller 6), og sjå kva som
    skjer når du køyrer cella på nytt.
2.  Kva skjer om du fjerner formatteringa `:.4f` og berre skriv
    `{tilfeldig_tall}`?
:::

::: {hint}
Om du vil vera heilt sikker på kva funksjonen er meint å gjera,
kan du slå opp i
[dokumentasjonen](https://docs.python.org/3/library/random.html).

Eg vil likevel råda dykk til å prøva dykk fram med kodedøme, både
for å testa om de forstår dokumentasjonen rett og for å få forståinga
inn i fingrane.  Dessuten hender det, om enn sjeldan, at der er feil
i dokumentasjonen.
:::

## Tilfeldige heiltal

Koden over, med `random.random()` genererte flyttal i intervallet $[0,1)$.
Me kan òg generera heiltal

```{code-cell} ipython3
import random

tal = random.randint(-1,+1)

print( f"Eg trilte {tal}")
```

::: {admonition} Oppgåve
Køyr cella fleire gongar.  Kva verdiar kan
`random.randint(-1,+1)` gje?
:::

::: {admonition} Oppgåve
Skriv ein line som simulerer eit terningkast (vanleg sekssida terning).
:::

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

## Kombinasjonar

Når me forstår korleis slumptalsfunksjonane fungerar kvar for
seg, kan me setja dei saman til meir komplekse program.
T.d. kan me kasta to terningar

```{code-cell} ipython3
import matplotlib.pyplot as plt

def terning():
    return random.randint(1,6)

def dobbelterning():
    return terning()+terning()

print( dobbelterning() )
```

Ei nyttig øving i stokastisk (tilfeldig) simulering er å køyra
mange gongar for å sjå fordelinga av resultat.

```{code-cell} ipython3
mange_kast = [ dobbelterning() for _ in range(10000) ]

plt.hist(mange_kast, bins=11)
```

::: {admonition} Refleksjon
Kva gjer koden over?
:::

::: {hint}
Understreken (`_`) er sikkert ny notasjon.
Me bruker understreken i staden for et variabelnamn som
me ikkje skal bruka vidare.

I koden over skal me gjenta 10.000 gongar, og `for`-syntaksen
i python krev at me tilordnar ein variabel, sjølv om me ikkje
treng han.  Då kan me skriva `_` i staden. 
:::

Ofte treng me tilfeldige verdiar som ikkje er tal.
Kan henda skal me dra tilfeldige personar frå ei liste.
Dette kan gjerast på mange måtar.  Her er eitt døme.

```{code-cell} ipython3
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

::: {admonition} Refleksjon
1. Kva gjer koden over?
2  Kva gjer du for å finna ei referansegruppe med fem elevar?
3. Ser du potentielle problem med koden?  Du kan freista å
   køyra mange gongar for å sjå om du får feil eller dårlege
   resultat.
:::

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

::: {admonition} Oppgåve
Dette kunne ha vore gjort enklare.  Der er faktisk
ein funksjon `random.choice()` som lèt oss plukke eit
tilfeldig element frå ei liste.

Skriv om koden over for å bruka `random.choice()` i
staden for å gjera det i to steg ved å trekkja indeksen
fyrst.  
Om du ikkje kan gissa korleis du gjer det, kan du søkja på 
nettet etter eit døme.
:::

## Andre fordelingar

Både `random.random()` og `random.randint()` dreg uniformt
fordelte tal.  Om du leiter litt, finn du funksjonar som gjev
andre sannsynsfordelingar, t.d. normalfordeling.

```{code-cell} ipython3
tall = random.gauss(mu=3, sigma=1.5)
mange_tall = [ random.gauss(mu=3, sigma=1.5) for _ in range(10000) ]

plt.hist(mange_tall, bins=40)
plt.show()
```

Om du ikkje har lesa nok statistikk, skal du ikkje dvela ved denne
oppgåva.

