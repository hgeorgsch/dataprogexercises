---
title: Moglegheitene i kunstig intelligens
tags:
  - topic/machinelearning
css:
  - css/templates.css
---
# Moglegheitene i kunstig intelligens


---

1956
<!-- element class="[[r-fit-text]]" -->

note:
Kunstig intelligens er et vagt og tvetydig begrep, og det er gjort ganske bevisst. 

Målet var hele tiden å kunne lave maskiner som kan avlaste mest mulig av vårt tankearbeide, på samme måte som dampmaskiner, støvsugere, vaskemaskiner har avlastet fysiske oppgaver.

---
<!-- slide template="[[tpl-flex]]" -->


![[MCCARTHY.png]]

::: credit
[Ukjend](https://www.nytimes.com/2011/10/26/science/26mccarthy.html), Public Domain,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=193100524)
::: 

note:
McCarthy var matematiker

---
<!-- slide template="[[tpl-flex]]" -->

![[Herbert-A-Simon-1978.jpg]]


::: credit
By Rochester Institute of Technology - News & Events 1981 at the RIT Digital Archive, 
Public Domain,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=115626765)
:::

note:
Herbert Simon var psykolog

---
<!-- slide template="[[tpl-flex]]" -->

![[C.E._Shannon._Tekniska_museet_43069_(2x3_crop).jpg]]
::: credit
Ukjend opphavsmann, Tekniska Museet of Sweden, Item 43069 via Flickr, CC BY 2.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=190273293)
:::

note:
Claude Shannon var ingeniør

---
<!-- slide template="[[tpl-flex]]" -->

![[DonaldMacKay1952.jpg]]

::: credit
By
[Welcome Collection](https://wellcomeimages.org/indexplus/obf_images/d3/8b/a35b81c8d9cedb039c233045c097.jpgGallery)
https://wellcomeimages.org/indexplus/image/L0030978.html, 
CC BY 4.0, via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=135924397)
:::

note:
Donald MacCrimmon MacKay var fysiker

---

# Tradisjonar

1. *Pattern Recognition*  $\to$  Maskinlæring
2. *Computational Logic*
3. Generativ KI

---

$$
\begin{align}
& \text{Alle mennesker er dødelege} \\
& \text{Sokrates er menneske} \\
\hline
\therefore\;\; & \text{Sokrates er dødeleg}\\
\hline
\hline
\end{align}
$$

---
<!-- slide template="[[tpl-flex]]" -->

![[Red_semantica_clasica.png]]

::: credit
By N. Perez-Corona - Own work, CC BY-SA 3.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=27105106)
:::

---

Analytisk
<!-- element class="[[r-fit-text]]" -->

note:
Analytisk kunnskap. *Computational Logic* kan ikkje seia noko som ikkje
direkte fylgjer av eksisterande proposisjonar

Dette er akkurat som andre reknemaskiner.


---
<!-- slide template="[[tpl-flex]]" -->

![[metastatis.png]]

::: credit
Grøvik, E., Yi, D., Iv, M. _et al._ Handling missing MRI sequences in deep learning segmentation of brain metastases: a multicenter study. _npj Digit. Med._ **4**, 33 (2021).
[DOI](https://doi.org/10.1038/s41746-021-00398-4)
:::

note:
1. Klassifikasjon
2. Regresjon 

---
<!-- slide template="[[tpl-flex]]" bg=lightgray"-->

## Diabetes

![[Pancreas_insulin_beta_cells.png]]

::: credit
By United States Department of Health and Human Services: National Diabetes Information Clearinghouse (NDIC) - http://diabetes.niddk.nih.gov/dm/pubs/diagnosis/, 
Public Domain, via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=25539437)
:::

---
<!-- slide template="[[tpl-flex]]" bg=lightgray"-->

![[icecream.png]]

::: credit
Miriam Wolff
:::

---

$X \to \boxed{\text{samanheng}} \to Y$
<!-- element class="[[r-fit-text]]" -->

---
<!-- slide template="[[tpl-flex]]" bg=lightgray"-->

![[ann.png]]

::: credit
Miriam Wolff
:::

---

- Det nevrale nettverket imiterer samanhengen $X \mapsto Y$
- Reknar ut $X\mapsto \hat Y$ (estimat)
- <span class="ntnupurple"> *loss function*</span> måler avviket mellom $Y$ og $\hat Y$

---
Analytisk $\to$ Syntetisk
<!-- element class="[[r-fit-text]]" -->

---

## Trening

- Start med modell $M$ med tilfeldige vekter
	- Treningssett $(X_1,Y_1), (X_2,Y_2),(X_3,Y_3),\ldots$
- Gjenta
	1. Object $X$ (inn) og $Y$ (ut)
	2. Mat $X$ inn i $M$ $\mapsto$ y
	3. Rekn ut  $\text{loss}(Y, y)$
	4. Juster vektene i $M$
	5. Gjenta med nytt objekt
- Gjenta fleire epokar med dei same objekta

---

## Hyperparameter

- Talet på epokar
- *læringsrate* - kor raskt endrar ein vektene?
- satsstorleik (fleire bilete for kvar vektoppdatering)
- *dropout rate* (dropp enkelte vekter)
- vektforfall (unngå store vekter)
	

---
<!-- slide template="[[tpl-flex]]" -->

> Kunstig intelligente systemer utfører handlinger,
fysisk eller digitalt, basert på tolkning og behandling
av strukturerte eller ustrukturerte data, i den hensikt
å oppnå et <span class="ntnupurple">gitt mål</class>
        
::: credit
[Nasjonal strategi for kunstig intelligens](https://www.regjeringen.no/no/dokumenter/nasjonal-strategi-for-kunstig-intelligens/id2685594/?ch=3)
:::

---
## Målet

- Ei maskin som predikerer $Y$  gjeve $X$

---

> Kva bør eg ha til middag i dag?

> Kor mange barneskular treng me i Ålesund?

---

Stor språkmodell $=$ Prediksjonsmodell
<!-- element class="[[r-fit-text]]" -->

---

- morgenstund har ...
+ pølse med ...
+ her er det bare å bøye seg i ...

---
## Sannsynsmodellar

---

- forutseia kva som skje (prediksjon)
- typebestemme objekt (klassifikasjon)
- segmentering av bilete (t.d. metastasar)
- oppdaga avvik (anomalideteksjon)
- reguleringsteknikk 

---
<!-- slide template="[[]]"="[[tpl-flex]]" -->

![[A_Horseshoe_Einstein_Ring_from_Hubble.jpeg]]

::: credit
By Lensshoe_hubble.jpg: ESA/Hubble & NASAderivative work: Bulwersator (talk) - Lensshoe_hubble.jpg, Public Domain,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=17750437)
:::

---

gjer-det-sjølv
<!-- element class="[[r-fit-text]]" -->

---

1. Annotering $\to$ datasett
2. Trening $\to$ modell
3. Testing $\to$ evaluering
4. Bruk $\to$ resultat

---

## Utfordringar

1.  Annotering er tidkrevjande
2. Trening krev reknekraft
	1. Mellomstore datasett krev GPU
	2. Store data krev dedikerte datasenter
3. Testing krev kompetanse og kritisk sans	
	1. Statistikk og domenekunnskap
	2. Kva er godt nok for oss?
4. ... men bruken er gjerne automatisert
	

---

Spørsmål?
<!-- element class="[[r-fit-text]]" -->
