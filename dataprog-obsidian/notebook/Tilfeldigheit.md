---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.2
kernelspec:
  name: dataprog
  language: python
  display_name: dataprog
---

# Slumptalsgenerator


Mange simuleringar handlar om tilfeldige prosessar, eller prosessar
som er so kaotiske at me ikkje forstår heile samanhengen, og difor
må tenkja på dei som tilfeldige.

Slump, eller tilfeldighet, er vanskeleg for datamaskiner, som er
konstruerte for å vera fullt ut deterministiske system.
Verkeleg slump må difor koma utanfrå, som *input*.
Dette er mogleg ved å henta data frå skjerm og tastatur, og særleg 
då frå ørsmå variasjonar i tida mellom tastetrykk, men der er grenser
for kor mykje slump me kan henta ut på denne måten.
Store simuleringar krev meir slump enn me klarer å henta ut på 
denne måten.

I praksis bruker me difor som regel sokalla *pseudo-tilfeldige* tal.
Det er matematiske formlar som gjer at me kan rekna ut lange seriar
med tal som *ser tilfeldige ut*.
Det mest kjente tilfellet er lineær kongruens, der det $i$te talet
i serien er definert som
$$ s_i = a\cdot s_{i-1} \mod p $$
der $\mod p$ gjev resten ved divisjon med $p$, og $a$ og $p$ er
høveleg valde konsantar.

Den nøyaktige formelen er ikkje viktig for oss.  Det som er greitt
å hugsa er at når me har det fyrste talet, $s_0$, som me gjerne
kaller **frøet** (*seed*), vil slumptalsgeneratoren gje oss ei
*uendeleg* rekkje med tilfeldigaktige tal.

![newton](https://pbs.twimg.com/media/D2EZ4DwVAAApNdd?format=jpg&name=900x900)

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

## Litt større oppgåva

Nedanståande oppgåve er eit døme som illustrerer korleis ganske
enkle og grunnleggjande teknikkar kan setjast saman til relativt
store program.

::: {admonition} Oppgåve (roulette)

Lag ein funksjon som simulerer eit roulette-spel.
Då treng du fleire funksjonar.

1. Skriv ein funksjon som genererer eit tilfeldig tal.
   Vanleg roulette gjev tal frå 0 til 36.

Me treng ein funksjon som vurderer om ein innsats vinn og kor
mykje han vinn.  Her er der mange tilfelle å vurdera,
og mange måtar å gjera det på, so lat oss ta eit døme.

Roulette har mange rutar å satsa på, m.a. raudt og svart,
der kvart tal utanom 0 er farga anten raudt eller sort.
Desse tala er definert slik,

```python
red = [ 32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3 ]
black = [ 15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26 ]
```

2. Skriv ein funksjon som sjekkar om du vinn.  Dvs. om du satsar på
   raudt, og talet som kjem opp er 27, skal du kunna skriva
   `win(27,"red")` og få ut `True`.  Her kan du bruka `in`- eller
   `not in`-konstruksjonen som me såg tidlegare.

3. Utbetalinga når du vinn, inklusive refusjon av innsatsen, er 
   36 delt på talet på vinnartal.  Der er 18 raude og 18 sorte
   tal, so om du satsar $x$ kroner på raudt, og vinn, får du
   tilbake $x\cdot 36/18=2x$.  Skriv ein `payoff`-funksjon.
   Dersom du satsa tre kroner på raudt og 27 vinn, skal du
   `payoff(27,"red",3)` gje 6, og om 15 (svart) vinn, skulle han
   gje 0.

Merk at du gjer koden meir generell om du reknar utbetalinga
ut frå lengda på lista med tal som er satsa på, heller enn
å hardkoda `2*x`.  Vinstfaktoren for raudt er t.d.
`36/len(red)`.

4. Skriv ein funksjon for å spela, som tek inn innsatsen,
   triller kula, og returnerer utbetalinga.  Dvs. du skal
   kunna kalla `play("red",3)` for å satsa tre kroner på
   raudt.  Denne funksjonen må bruka funksjonane over,
   og returnera 0 om raudt ikkje vinn.

5. Køyr ein simulering der du speler 1000 gongar og satsar
   ei krone på raudt kvar gong.  Kor mykje taper eller vinn
   du netto?  

6. Du kan godt køyra simuleringa frå 5 fleire gongar og
   rekna gjennomsnitt.

Du kan halda fram å byggja på programmet for å opna for andre
innsatsar, på jamne og ujamne tal, på intervall, hjørne, rekkjer,
etc.

:::

