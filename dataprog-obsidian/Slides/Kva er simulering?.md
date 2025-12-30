---
tags:
  - lecture/perspective
css:
   - css/templates.css
---

# Kva er simulering?

note:
Et av de viktigste bruksområdene for programmering i økonomiske fag er simulering,
men hva mener jeg egentlig når jeg sier simulering?

---

*Kva skjer dersom ... ?*

note:
Simulering er en øvelse i spørsmålet *hva skjer hvis ...*?

---
<!-- slide template="[[tpl-flex]]" -->

![[Maler_der_Grabkammer_der_Nefertari_003.jpg]]

::: credit
By Maler der Grabkammer der Nefertari - The Yorck Project (2002) 10.000 Meisterwerke der Malerei (DVD-ROM), distributed by DIRECTMEDIA Publishing GmbH. ISBN: 3936122202., Public Domain,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=154294)
:::

note:
Simulering er i prinsippet et spill.

I det gamle Egypt spilte faroene gjerne *Senet* for å forberede seg på livet efter døden.

Ved å simulere hendelsene og utfordringene som ventet dem skulle de kunne gjøre bedre valg og få et bedre liv i det hinsidige.

Jeg skal ikke påstå at egypterne hadde en presis modell av det hinsidige, men spillet er likevel et simuleringsspill, og vi kan forestille oss at det har vært brukt, ikke bare som en lek, men som et verktøy for å forstå en komplisert situasjon gjennom en forenklet modell.

---
<!-- slide template="[[tpl-flex]]" -->

![[KnightsTemplarPlayingChess1283.jpg]]

::: credit
By Alphonse le Sage (Alfonso X) - "Livre des Echecs" (Libro de Ajedrez, dados y tables), Public Domain,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=2664091)
:::

note:
Sjakk er et mer kjent eksempel. Sjakkbrikkene er selvsagt en meget primitiv modell av virkelige soldater, men spillet er likefullt en simulering av et slag.

---
<!-- slide template="[[tpl-flex]]" -->

![[SARS-CoV-2_without_background.png]]

::: credit
Av Alissa Eckert, MS; Dan Higgins, MAM – This message is number 23312 in the Public Health Image Library (PHIL) of the CDC., Offentlig eiendom,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=86444014)
:::

note:
Vi har aldri hørt så mye om simulering som vi gjorde under koronapandemien.

Folkehelseinstituttet brukte matematiske modeller for smittespredning, og kjørte simuleringer for å forutsi forventet smittespredning ved ulike regimere, med énmeters- eller tometersregler, og ulike maksgrenser for antall gjester på en samling.

Datasimuleringer kan håndtere langt mer komplekse regler og spille langt flere trekk enn vi kan i spill som senet og sjakk, og dermed er det mulig å lave meget realistiske simuleringe. Det er ikke enkelt, og det krever både fagkompetanse i domenet som skal simuleres, og teknisk og matematisk kompetanse.

---

<!-- slide template="[[tpl-flex]]" -->

![[Economics_circular_flow_cartoon.jpg|800]]

::: credit
By [United States Government](http://en.citizendium.org/wiki/File:Economics_circular_flow_cartoon.jpg), Public Domain,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=16387337)
:::

note:
Simulering blir også brukt i mange slags økonomiske fagfelt og planarbeid.
Markedssimuleringer kan brukes for å teste mulige produktendringer, prisendringer eller lovendringer.
Demografiske simuleringer gjør det mulig å kartlegge behov for skoler og sykehjem i fremtiden.
Ved å simulere ulike bedrifter i aksjemarkedet, kan man teste ulike simuleringsstragier.

---

<!-- slide template="[[tpl-flex]]" -->

![[2487_cline_vr_studio_20190318.jpg]]]

::: credit
By Geofflambeth - Own work, CC BY-SA 4.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=81083269)
:::

note:
Forutsetningen for at simuleringen skal være nyttig er at vi kan leve oss inn i den virkeligheten som simuleringen skal efterligne. Vi må ha en forestilling om hva som er mulig og hva som er sannsynlig hypotetiske situasjoner. Hvis vi ikke tror på resultatet av simuleringen, kan vi ikke bruke det.

---

<!-- slide template="[[tpl-flex]]" -->

![[Ludo-3.jpg]]]

::: credit
By Micha L. Rieser, Attribution, 
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=3226060)
:::

note:
Ludo er og blir et barnespill, fordi vi ikke klarer å leve oss inn i historien til familien som skal rømme fra fengselet og komme hjem uten å bli fakket. Om det er fordi reglene er for enkle eller fantasien vår for dårlig, kan sikkert diskuteres.

---


```python
rentesats = 0.045
saldo = 1000000

for i in range(2025,2051):
  saldo = saldo + saldo*rentesats
print(saldo)
```

note:
Spare- og lånekalkulatoren som vi har jobbet med i dette kurset er et enkelt eksempel
på en simulator.
Ved å se for oss saldoen på kontoen, og simulere transaksjonene år for år,
eller dag for dag, blir modellen konkret og enkel å eftergår,
selv uten å skjønne den matemtiske teorien for geometriske rekker.

---

| Dato | Tekst | Endring | Saldo |
| :- | :- | -: | -: |
| 1. jan. 2025 | Sparing | +1000 | 1000 |
| 31. des. 2025 | Sparing | +4%$\cdot$1000 | 1040 |
| 1. jan. 2026 | Sparing | +1000 | 2040 |
| 31. des. 2025 | Sparing | +4%$\cdot$2040 | 2136 |
| 1. jan. 2027 | Sparing | +1000 | 3136 |

note:
Avhengig av hvilke data vi lagrer underveis i simuleringen, kan vi
skrive resultatet enten som sluttsaldoen eller som en simulert
kontoutskrift, som om det var en ekte konto.

De aller fleste simuleringer handler om prosesser som går over tid.
Uten snarveier for å spå fremtiden, beregner vi hver eneste lille hendelse som skjer, 
tidspunkt for tidspunkt.

Selvsagt vil ikke alle simuleringer være like enkle og presise som sparekalkulatoren.
Vi må ofte forenkle og definere *omtrentlig* hva vi forventer i hver periode, men ved å brekke problemet opp i mindre, tidfestede hendelser, blir det likevel enklere å forstå og å argumentere for. 

---

<!-- slide template="[[tpl-twocolumn]]" -->

::: leftimage

![[Ida_Wolden_Bache_på_Sentralbanksjefens_årstale_2018_(174929).jpg]]

:::

::: leftcredit
Ida Wolden Bache i 2918;
ved Tore Sætre - eige arbeide, CC BY-SA 4.0, via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=66492744)
:::

::: rightimage
![[6sided_dice_(cropped).jpg]]
:::

::: rightcredit
By Diacritica - Own work, CC BY-SA 3.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=99768017)
:::

note:
Og hvis vi vil gjøre det mer realistisk kan du gjøre rentenivået til en variabel og legge til mer eller mindre tilfeldige renteendringer hvert år.

Så lenge du har en forestilling om situasjonen som skal simuleres, 
er der ingen grense for hvor detaljert modellen  kan bli.

Dersom du mangler den forestillingen, og ikke har en hensikt med simuleringen,
blir resultatet alltid dårlig og uinteressant. 

Du må ha en historie å fortelle med simuleringen.
