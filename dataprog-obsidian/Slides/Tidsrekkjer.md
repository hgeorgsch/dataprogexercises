---
tags:
  - lecture/video
css:
  - css/templates.css
---

<!-- slide template="[[tpl-quote-header]]" -->
## Tidsrekkjer

![[arbeidsledige.svg]]

::: credit
Hans Georg Schaathun
:::

---

- Tidsrekkja inneber *to* ting
	1. Tid som indeks
	2. Numerisk søyle
- *DataFrame* i pandas kan innehalda fleire tidsrekkjer

---

## Læringsmål

- Repetisjon
	- Utdrag frå datasett: filtrering på fleire søyler.
    - Numeriske søyler
- Nytt stoff
	- Tidssøyler
	- Byte av indeks.
	- Frekvens og gruppering av radar.
	- Fletting av datasett på tid.
- Om me rekk det
	- Manglande data og NaN (not a number).

---

## Problem 1.

> Korleis handterer me ... 

1. ulik presisjon (år, kvartal, månad, dag, tidspunkt)?
2. ulik representasjon som `2025-10-20` eller `20. okt 2025`?
3. ulike tidssonar?
