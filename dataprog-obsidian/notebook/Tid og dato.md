
+ Utdrag frå øving om [[Arbeidsledige]] 2024

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCOoEr1biiaMsoejCtfdvgJAq_T6TfbjVkrc-zyfJ8ReSf8BvldJXPjyNy1gjfGVmB2hk2i39ybpaLHKDK4kTn4n2Zh-dXlaayliZoiygxhTQ3W7mC2LoxzTOARAhltRmSn84pdQdmqrbu/s1600/AD951881-737E-4F2C-AE8E-D80E280CFFD5.png">

## Tid og tidsrekkjer

Me arbeider med tidsrekkjer og tida er openbert sentral.
Der er fleire utfordringar som me må tenkja på for tidsrekkjer,
og der er særleg to som me må bruka tid på.

1.  Tid vert skrive på ulike måtar, med ulike presisjonsnivå.
    Måler me i sekund eller i år, f.eks.?
2.  Når me skal samanlikna tidsseriar, treng med kompatible
    tidsaksar.  Dersom tidsseriane er observert på ulike tidspunkt,
    må me finna ein måte å gjera dei samanliknbare.
3.  Tidsseriar med svært hyppige observasjonar kan ofte gje mykje
    tilfeldig støy.  Ofte løner det seg å rekna gjennomsnitt over
    lengre periodar.

For å kunna løysa desse tre utfordringane, treng med ein datatype for
tid.  Me treng ein type som let python forstå samanhengen mellom 
ulike einingar, som sekund, månad og år. 
Månad er særleg problematisk sidan februar ikkje er like lang som juli.
Me må kunna skilja mellom tidspunkt og tidsperiode.
Me treng og teknikkar for å lesa alle dei representasjonane som me
finn i disribuerte datasett og lesa dei inn i dei valde datatypane.
    
Her skal me studera to typar, `datetime` eller `pandas.Period`.
Fyrstnemnde er ein del av kjernedistribusjonen av python, medan den
andre er ein del av pandas.

## Tid og data i python

::: {admonition} Merknad
Det er mogleg at me treng desse to linene for å få norsk
vising.  Det må sjekkast.
```
import locale
locale.setlocale(locale.LC_ALL, "nb_NO.utf8")
```
:::

For å starta med eit enkelt døme, lat oss sjå korleis me
finn tida akkurat no.

```{code-cell} ipython3
import datetime

dato_og_tid = datetime.datetime.now()
dato = datetime.date.today()

print("I dag er datoen", dato)
print("Mer nøyaktig er vi nå", dato_og_tid)
```

::: {admonition}
Kva er skilnaden mellom metodane `now()` og `today()`?
:::

```{code-cell} ipython3
from zoneinfo import ZoneInfo
#Vi kan lage et spesifikt tidspunkt eller dato:

min_dato = datetime.date(1990,4, 23) #År, måned, dag
print("Jeg valgte dato: ", min_dato)

tid = datetime.datetime(2024,12,13,12, tzinfo=ZoneInfo("Europe/Oslo")) #År, måned, dag, time, minutt, sekund, tzinfo=TIDSSONE
print("Mappeinnlevering stenger", tid)

#Vi kan også lage en ENDRING I TID:
#datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
utsettelse = datetime.timedelta(days=1, hours=4)
ny_tid = tid+utsettelse
print("Ny tid for mappeinnlevering:", ny_tid)

#Vi kan sammenligne tider/datoer
print(ny_tid > tid)
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Fordelen med en slik datatype er at biblioteket selv kan holde kontroll på tidssoner og denslags
* Biblioteket lar oss plusse/trekke fra tider eller datoer med hverandre
* Vi kan sammenligne tid/datoer som betyr at vi lett kan sortere de

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

# Formattere dato ut

* vi bruker `min_tid.strftime("FORMATTERINGSSTRENG")` for å formatere en dato eller tid
* Formateringsstrenger er litt som en f-streng, men vi limer inn feks året for `"%Y"` i stedet for `f"{year}"`

| Formatkode | Beskrivelse                          | Eksempel (med dato: 2024-10-21 15:30:45) |
| ---------- | ------------------------------------ | ---------------------------------------- |
| `%a`       | Forkortet ukedag                     | Man                                      |
| `%A`       | Fullt navn på ukedag                 | Mandag                                   |
| `%w`       | Ukedag som tall (Søndag=0, Mandag=1) | 1                                        |
| `%d`       | Dag i måneden (nullutfylt)           | 21                                       |
| `%b`       | Forkortet månednavn                  | Okt                                      |
| `%B`       | Fullt månednavn                      | Oktober                                  |
| `%m`       | Måned som tall (nullutfylt)          | 10                                       |
| `%y`       | År (to siffer)                       | 24                                       |
| `%Y`       | År (fire siffer)                     | 2024                                     |
| `%H`       | Time (nullutfylt, 24-timers klokke)  | 15                                       |
| `%I`       | Time (nullutfylt, 12-timers klokke)  | 03                                       |
| `%p`       | AM/PM                                | PM                                       |
| `%M`       | Minutter (nullutfylt)                | 30                                       |
| `%S`       | Sekunder (nullutfylt)                | 45                                       |
| `%f`       | Mikrosekunder (nullutfylt)           | 000000                                   |
| `%z`       | Tidsforskjell fra UTC                | +0000                                    |
| `%Z`       | Tidsnavn (timezone)                  | UTC                                      |
| `%j`       | Dagnummer i året (001-366)           | 295                                      |
| `%U`       | Ukenummer (Søndag som første dag)    | 43                                       |
| `%W`       | Ukenummer (Mandag som første dag)    | 43                                       |
| `%c`       | Lokal dato og tid                    | Man 21 Oct 15:30:45 2024                 |
| `%x`       | Lokal dato (kort format)             | 21.10.2024                               |
| `%X`       | Lokal tid (kort format)              | 15:30:45                                 |
| `%%`       | Et prosenttegn                       | %                                        |

```{code-cell} ipython3
print("Mappen skal leveres: ", ny_tid.strftime("Senest klokken %H:%M %A den %d."))
print(ny_tid.strftime("%c"))
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

## Lese inn et datoformat
* Enda mer nyttig er det å kunne lese inn tid/dato skrevet i rare formater
* Da bruker vi samme tabell som for `strftime`, men bruker `datetime.datetime.strptime(dato, "FORMATERINGSSTRENG")`

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
dato_inn = "21/04/1987"
dato_lest = datetime.datetime.strptime(dato_inn, "%d/%m/%Y")
print("Dato som datetime objekt:", dato_lest)
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Period i pandas

* Pandas har en egen klasse/type for å jobbe med perioder og tidsintervall
* Vi jobber da med spenn av tid, pandas kaller det `frekvenser`

| Frekvenskode | Beskrivelse              | Eksempel                               |
|--------------|--------------------------|----------------------------------------|
| `A` or `Y`   | Årlig (Year-End)          | 2024                                  |
| `Q`          | Kvartalsvis               | 2024Q1                                |
| `M`          | Månedlig                  | 2024-10                               |
| `W`          | Ukentlig (Søndag)         | 2024-42 (42. uke, sluttdato Søndag)  |
| `W-MON`      | Ukentlig (Mandag)         | 2024-42 (42. uke, sluttdato Mandag)  |
| `D`          | Daglig                    | 2024-10-21                            |
| `B`          | Virkedag (uten helger)    | 2024-10-21                            |
| `H`          | Time                     | 2024-10-21 15:00                      |
| `T` or `min` | Minutt                    | 2024-10-21 15:30                      |
| `S`          | Sekund                    | 2024-10-21 15:30:45                   |
| `L`          | Millisekund               | 2024-10-21 15:30:45.123               |
| `U`          | Mikrosekund               | 2024-10-21 15:30:45.123456            |
| `N`          | Nanosekund                | 2024-10-21 15:30:45.123456789         |

```{code-cell} ipython3
#pd.Period('verdi', freq='frekvenskode')
periode = pd.Period('2024-10-21 15:00', freq='Q') #Verdien er en gyldig tekststreng i en periode med frekvens freq=..
langt_frem = periode+26
langt_frem
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

### pd.PeriodIndex
* Vi vil som regel ha mange perioder som indeks i et dataset
* Da kan vi bruke:
  *  `pd.PeriodIndex([«liste med perioder»], freq='frekvenskode')`
  *  `pd.period_range('2024-01', '2025-05', freq='M')` ie (start, slutt, frekvens) 
  *  `pd.period_range('2024-01', periods=12, freq='Q')` ie (start, antall perioder, frekvens)

*Vi har også en `pd.date_range(start, perioder, frekvens)` om vi vil ha `datetime` i stedet*

```{code-cell} ipython3
tidserie = pd.period_range('1980Q1', periods=15, freq="Q")
tidserie2 = pd.period_range('1980', '2000', freq='M')
tidserie2
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

### Konvertere mellom `datetime` og `Period`

* Ofte trenger man å konvertere mellom `datetime` og `Period`
* Kanskje har man brukt `strptime(...)` til å lese inn riktig dato først
* Vi bruker da `df['date'].dt.to_period('frekvenskode')`
* Skal vi gå andre veien bruker vi `df["periode"].to_timestamp()`

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Det er mye mer vi kunne sett på her
* Tid/dato kan bli uhyre komplisert i det virkelige liv
