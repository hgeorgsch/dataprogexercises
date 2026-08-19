# Forelesningsnotater – uke 35

Dette er et skjelett for fagnotatene om logistisk vekst og funksjoner.

## Fra løst regnestykke til modell

Den logistiske modellen kan skrives som

:::{math}
:label: uke35-logistisk-vekst

P_{t+1} = P_t + rP_t\left(1 - \frac{P_t}{K}\right),
:::

der $P_t$ er populasjonen i dag, $r$ er vekstraten og $K$ er maksimal
populasjon.

```python
populasjon = 100
vekstrate = 0.10
maks_populasjon = 1000

vekst = vekstrate * populasjon * (1 - populasjon / maks_populasjon)
ny_populasjon = populasjon + vekst
```

## Hvorfor trenger vi funksjoner?

Her kan vi vise hvordan gjentatte kopier av samme formel blir vanskelige å
vedlikeholde, og deretter samle beregningen:

```python
def neste_populasjon(populasjon, vekstrate, maks_populasjon):
    vekst = vekstrate * populasjon * (1 - populasjon / maks_populasjon)
    return populasjon + vekst
```

## Begreper

Parameter
: Navnet som står i funksjonsdefinisjonen.

Argument
: Verdien som sendes inn når funksjonen kalles.

Returverdi
: Resultatet funksjonen sender tilbake med `return`.

:::{admonition} Skal fylles ut
:class: note

Legg inn flere funksjonseksempler, typiske feil og en gradvis overgang fra den
matematiske modellen til Python-koden.
:::
