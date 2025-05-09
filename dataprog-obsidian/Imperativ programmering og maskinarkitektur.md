---
tags:
  - lecture/video
---
# Imperativ programmering

note: Der er mange måtar å programmera ei datamaskin på. Det paradigmet som ligg til grunn for dette kurset er *imperativ* programmering. Det er det mest kjende, men ikkje det einaste.

Me skal her sjå på korleis datamaskiner konseptuelt sett verkar. Målet er ei betre forståing av korleis me tenkjer når me bruker Python til å instruera datamaskina.

---

- [ ] Figur: Kommando

note:
Me kaller det for imperativ programmering, fordi me gjev maskina kommandoar, dvs. setningar i grammatisk imperativ.

---

```python
b = 5
c = b*2
print(b)
```


note:
Imperativen er tydelagst i den siste lina: *print!*
Dei andre setninga lyt ein lesa som «lat $b$ vera lik 5» og «lat $c$ vera lik $b\cdot2$.  Det er òg imperativar.

Dette skapar ei *tilstandsmaskin*, dvs. ei maskin som til i ein bestemt tilstand til ei kvar tid, og denne tilstanden kan endra seg for kvar instruksjon.

Her er tilstanden definert ved variablane. Før programmet startar er `b` og `c` «tomme» eller meiningslause. Den fyrste lina gjev `b` ein verdi, og dermed ein ny tilstand.

---

```python
b = 5
print(b)
b = 10
print(b)
```

note: Dette vert enno tydlegare i dette dømet, der variabelen `b` sjølv endrar tilstand. Dei to *print*-linene er identiske, men resultatet er forskjellig, fordi maaskina har endra tilstand.

---


- [ ] Figur: CPU og register
	+ https://slideplayer.com/slide/5101082/
	+ https://programmathically.com/how-does-a-cpu-execute-instructions-understanding-instruction-cycles/

note: Imperativ programmering svarer godt til det som skjer i dei elektroniske krinsane på prosessoren.

---

## Turingmaskina

![[Turing_Machine_Model_Davey_2012.jpg]]

Turing Machine, reconstructed by Mike Davey as seen at Go Ask ALICE at Harvard University ([Rocky Acosta](https://commons.wikimedia.org/wiki/User:Arttechlaw "User:Arttechlaw") - Own work)

note: forklar korleis turingmaskina verkar

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

note: Teorien for datamaskiner og programmering vart hovudsakleg utarbeidd på 1930-talet, om lag ti år før ein fyrst bygde maskiner ein kunne programmera på. Church og Turing definterte kvart sitt paradigme, og Turing viste seinare at dei er ekvivalente, i den meininga at dei kan løysa dei same problema.

Turingmaskina er den mest kjende. 

---

## Tilstandsmaskina

note: 

---

## Outline

- Konseptuell forståing av imperativ programmering
	- Kontrollflyt - løkker og if
- Prosessorarkitektur (register og instruksjon)
	- Vektorprosessorar

note: treng meir arbeide her
