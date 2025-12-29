---
title: Datastrukturar
tags:
  - lecture/video
css:
  - css/templates.css
---

<!-- slide template="[[tpl-titleslide]]" -->

# Datastrukturar

::: author
Hans Georg Schaathun
:::

::: footer
NTNU---Noregs Teknisk-Naturvitskaplege Universitet
:::

note:
This slide deck is used to showcase and debug the templates
and CSS styles..

---

## Primitive datatypar

- heiltal (`int`) $\ldots, -1, 0, +1, +2, \ldots$
- flyttal (`float`) t.d. $-50{,}1$, $0$, $0{,}1$, $2{,}4$,  $10{,}0$
- bolsk (`bool`) : `True` eller `False`
- teikn : t.d. `'a'`, `'z'`, `'!'`, `'7'`
- strengar (`str`) : t.d. `"Hello World!"`

---

## *Record*

|        kunde | data           |
| -----------: | :------------- |
|    `fornamn` | "Ola"          |
|  `etternamn` | "Normann"      |
| `postnummer` | 6016           |
|       `gate` | "Borgundvegen" |
|     `nummer` | 666            |


---
<!-- slide template="[[tpl-fit-table]]" -->

::: header
## *Record*
:::

|        kunde | data           |
| -----------: | :------------- |
|    `fornamn` | "Ola"          |
|  `etternamn` | "Normann"      |
| `postnummer` | 6016           |
|       `gate` | "Borgundvegen" |
|     `nummer` | 666            |

::: credit
:::

---

## Tabell (*array*)

| # | Verdi |
| :- | :- |
| 0  | `"Ola Nordmann"` |
| 1 | `"Kari Nordmann"` |
| 2 | `"John Smith"` |
| 3 | `"Jane Doe"` |
| 4 | `"Tom"` |
| 5 | `"Dick"` |
| 6 | `"Harry"` |


---
<!-- slide template="[[tpl-fit-table]]" -->

::: header
## Tabell (*array*)
:::

| # | Verdi |
| :- | :- |
| 0  | `"Ola Nordmann"` |
| 1 | `"Kari Nordmann"` |
| 2 | `"John Smith"` |
| 3 | `"Jane Doe"` |
| 4 | `"Tom"` |
| 5 | `"Dick"` |
| 6 | `"Harry"` |

::: credit
:::



---

## Tuplar

- (0,1, 2,5)
- `("Oskar", 83)`
- ( $x$, $y$ )
- `( "Ola Nordmann", "Borgundvegen 666", "6060 Ålesund", 2012-10-14)

---
<!-- slide template="[[tpl-diagram]]" -->

## Avbilding (*map*)

![[map.svg|480]]

---
<!-- slide template="[[tpl-smalltext]]" -->

## Liste

```python
[ "Ola Nordmann", "Kari Nordmann", "John Smith", "Jane Doe", ... ]
```

::: credit
:::


---
<!-- slide template="[[tpl-smalltext]]" -->

## Lister i python

```

In [2]: kunder = [ "Ola Nordmann", "Kari Nordmann", "John Smith", "Jane Doe" ]

In [3]: print( kunder[1] )
Kari Nordmann

```

::: credit
:::

---
<!-- slide template="[[tpl-quote]]" -->

![[Pandas_dataframe.png]]

::: credit
By Lucasadvent - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=131116177
:::

