---
tags:
  - simulering
  - session
---
*Me må sikkert dela denne i to*

+ Byggjer på  [[Simulering av kontantstraum]]
+ *Oversiktsføredrag* 
	+ [[Tilfeldigheit]]
	+ [[Datastrukturar og Kompleksitet]]
+ *Tekniske demonstrasjonar*
	+ [[Kontrollflyt]]
	+ [[Datastrukturer]]
+ *Øvingar.*
	+ [[CodeRunner Data Structures]]
	+ [[Marknadssimulering]]


# Døme: handlande kundar

* Vi simulerer en kunde som handler
* Den fyller handlekurven med varer helt til budsjettet er tomt
* Eller kunden har fått det den trenger

* Vi sier at etter hver vare kunden handler, er det 10% sjanse for at den er ferdig å handle
* Kunden trekker en tilfeldig vare hver gang

```{code-cell} ipython3
varer = {"Epler": 10.0,
         "Pærer": 15.0,
         "Bleier": 35.0,
         "Sjokolade": 6.0,
         "Melk": 20.0,
         "Rundstykker": 13.0
        }

def simuler_handling():
    handlekurv = []
    budsjett = 200
    sluttsjanse = 0.1
    total_pris = 0.0

    varenavn = list(varer.keys())

    shopper = True
    while shopper:
        vare = random.choice(varenavn)
        varepris = varer[vare]
        if budsjett > varepris:
            handlekurv.append(vare)
            total_pris += varepris
            budsjett -= varepris
        else:
            shopper = False
    
        if random.random()<sluttsjanse:
            shopper = False
    return total_pris

# print(f"""Kunden handlet følgende varer {handlekurv}
# Det koster kroner {total_pris:.1f}
# Da er det igjen {budsjett} kroner i budsjettet
# """)
```

# Oppgåve 

* Simuler voldsomt mange kunder som handler slik som i eksempelt over
* Regn ut gjennomsnittlig pris kundene handler for
* Plott hvordan fordelingen av pengebruk i butikken er

```{code-cell} ipython3
pengebruk = []
n = 10000
for _ in range(n):
    kundens_pengebruk = simuler_handling()
    pengebruk.append(kundens_pengebruk)

snitt = sum(pengebruk)/n
print(f"Kunder legger i snitt igjen {snitt:.2f} kroner per handletur")

plt.hist(pengebruk, 20)
plt.show()
```