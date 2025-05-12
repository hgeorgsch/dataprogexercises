---
tags:
  - lecture/video
---

# Imperativ programmering

note: Der er mange måtar å programmera ei datamaskin på. Det paradigmet som ligg til grunn for dette kurset er *imperativ* programmering. Det er det mest kjende paradigmet, men ikkje det einaste.

Me skal prata litt om korleis datamaskina konseptuelt sett verkar. Målet er litt betre innblikk i korleis me tenkjer når me bruker Python til å instruera datamaskina.

---

![[command.webp]]

- [ ] Figur: Linsens på *clipart*

note:
Me kaller det for imperativ programmering, fordi me gjev maskina kommandoar, dvs. setningar i grammatisk imperativ.  

Maskina tenkjer ikkje. Det er programmøren som står for all tenkinga. Maskina gjer nøyaktig som kommandert, og programmøren må sjå for seg kva kvar kommando fører til.


---

<split even>
::: block
![[Alan_Turing_(1951).jpg|500]]

Alan Turing 1951 ([by Elliott & Fry](https://www.computerhistory.org/timeline/1949/) Public Domain)
:::


::: block
![[Alonzo_Church.jpg|500]]

Alonzo Church
([By Princeton University, Fair use](https://en.wikipedia.org/w/index.php?curid=6082269))
:::

</split>

note: Teorien for datamaskiner og programmering vart hovudsakleg utarbeidd på 1930-talet, om lag ti år før ein fyrst bygde maskiner som faktisk kunne køyra programma. Church og Turing definterte kvart sitt paradigme. Dei er ekvivalente i den forstand at dei kan *oppnå* det same, sjølv om ein tenkjer forskjellig.

Turingmaskina er den mest kjende modellen, og den som ligg til grunn for imperativ programmering, der me kommanderer maskina og seier nøyaktig hva ho skal gjera.  Church sin $\lambda$-kalkyle ligg til grunn for det som me i dag kaller *funksjonell programmering*, der me definerer kva eigenskaper resultatet av programmer skal ha, utan å seia korleis ein oppnår det.

Båe modellane var abstrakte matematiske konsept, men det er Turing sin modell som best svarer til dei elektroniske maskinene som ein tok til å byggja utover 1940-talet.  Imperativ programmering er stadig det dominerande tankesettet, og difor det som me vil bruka tid på her.

---
## Turingmaskina

![[Turing_Machine_Model_Davey_2012.jpg]]

Turing Machine, reconstructed by Mike Davey as seen at Go Ask ALICE at Harvard University ([Rocky Acosta](https://commons.wikimedia.org/wiki/User:Arttechlaw "User:Arttechlaw") - Own work)

note: 
Turingmaskina er som sagt ein abstrakt og matematisk modell. Biletet viser ein rekonstruert modell. 

Maskina har eit papirband som er rulla opp på to spoler som kan dra bandet att og fram gjennom lesehodet i midten. Papirbandet er minnet i maskina og delt i diskrete posisjonar der kvar posisjon kan innehalad eitt teikn.

Turingmaskina er ei *tilstandsmaskin*.  Dvs. til ei kvar tid er maskina i ei bestemt tilstand. Det som maskina gjer avheng både av tilstanda og kva som står på bandet. 

---

<!-- slide bg="white" -->

![[turinginstruction.svg|600]]

note:
På kvart tidssteg ser maskina tilstanden sin og eitt teikn på bandet. Dette avgjer både den nye tilstanden og kva teikn som vert skrive til bandet. I tillegg kan bandet flytta eit steg til høgre eller venstre.

Denne maskina er sjølvsagt absurd enkel.  Ho må òg vera uhyrleg treig sidan det tek lang tid å leita gjennom bandet. Likevel viser Turing at ho i prinsippet kan løysa mange komplekse problem.  

Alt me treng er eit minne som me kan bla igjennom og ein operasjon som verkar på to inputtverdiar, tilstanden og verdien fra bandet.

---

## von Neumann-arkitekturen

+ [ ] FIgur: Maskinarkitektur

note:
Maskin har eit minna

Ikkje berre det, programmøren må sjå for seg kva som skjer etter lange seriar med kommandoar, for kvar kommando avheng av resultatet av dei føregåande. 

---



```python=
b = 5
print(b)
```

note:
Imperativen er tydelagst i den andre lina: *print!* men den fyrste setninga er òg ein imperativ, som me lyt lesa som «lat $b$ vera lik 5». 

Dette skapar ei *tilstandsmaskin*, dvs. ei maskin som til i ein bestemt tilstand til ei kvar tid, og denne tilstanden kan endra seg for kvar instruksjon.
Variabelen `b` var udefinert før line 1. Etter line 1 har han fått ein verdi, og altso ein ny tilstand.

---

```python=
b = 5
print(b)
b = 10
print(b)
```

note:
Dette er enno tydlegare i dette dømet.  Dei to *print*-linene er identiske, men dei gjev ikkje same resultat, fordi *tilstaden* åt maskina er forskjellig.


---


- [ ] Figur: CPU og register
	+ https://slideplayer.com/slide/5101082/
	+ https://programmathically.com/how-does-a-cpu-execute-instructions-understanding-instruction-cycles/

note: Imperativ programmering svarer godt til det som skjer i dei elektroniske krinsane på prosessoren.

---

## Tilstandsmaskina

note: 

---
	
- Kontrollflyt - løkker og if

---
## Vektorprosessorar

