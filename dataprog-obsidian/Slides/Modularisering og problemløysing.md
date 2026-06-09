---
title: Modularisering og Problemløysing
tags:
  - lecture/video/perspective
  - topic/machinelearning
css:
  - css/templates.css
---


# Modularisering og Problemløysing

---

## Oppsummering

1. Statistikk og prediksjon
2. Simulering av modeller
3. Automatisering av beregninger

---

## Algoritmen

$\mathit{input} \to \boxed{\text{Metode}} \to \mathit{output}$
<!-- element class="[[r-fit-text]]" -->

---

## Funksjonen

```
def metode(input):
    """
	Denne funksjonen skal illustrere modularisering når vi programmerer.
	- input må være et veldefinert objekt
	- output er en optimal løsning på metoden
    """
    ...
	output = ...
	return output
```

---

## Modularisering

1. Funksjonar
2. Klasser
3. Modular


---

## Klasser

```
class Klassami:
   def __init__(self,namn):
       self.namn = namn
   def __str__(self):
       return namn
   ...
objektetmitt = Klassami("Et namn skal barnet ha")
```

note:
- Strukturerer (komplekse) *objekt* 
	- data som høyrer saman
- .... saman med *metodar* som verker på objektet



---


## Modular

```
import modulenmin as mm
```

- Einkvan `.py`-fil kan vera ein modul
- Søkjesti
	- same katalog
	- prosjekt (venv)
	- installasjon med `pip`
	- systeminstallasjon

---

## Design

1. Identifiser problem som går igjen
2. Definer problemet *presist*
	1. generelt $\leftarrow$ dekkjer so mykje som mogleg
	2. spesielt $\leftarrow$ enklast mogleg å forstå
3. Løys problemet i ein funksjon eller ei klasse
4. Samla funksjonane dine i ein eller fleire modular

---

Ikkje overdriv
<!-- element class="[[r-fit-text]]" -->

---

## High cohesion

- veldefinerte grensesnitt (*input/output*)
- veldefinert hensikt (ved metoden)
- enklast mogleg 
- komplekse metodar vert delte opp


---

## Low coupling

- mest mogleg uavhengige modular
- enklast moglege grensesnitt
- ei endring skal ikkje krevja andre endringar


---

## Døme

- Månadsrekneskap  $\to$ `class`
- Hente inn og ryddar datasett $\to$ `def`
- Kombinera fleire datasett $\to$ `def`
- Kakediagram over kostnadstypar $\to$ `def`
- Plott for utgifter og inntekter over tid $\to$ `def`

---
<!-- slide template="[[tpl-ntnu]] -->

## Lagarbeid

- kode under arbeid $\to$ `git`  
- bibliotek $\to$ PyPI $\to$ `pip`

*eller interne tenarar*
<!-- element class="ntnupurple" -->

---

## Struktur

+ Hva gjør koden?
+ Korleis skal inndata sjå ut?
+ Korleis ser utdata ut?

---

Spørsmål?