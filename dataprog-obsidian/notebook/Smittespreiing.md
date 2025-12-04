# Smittespreiing

Kjelde : [NDLA](https://ndla.no/r/biologi-1/smittespredning---modeller/d7dd80dfac)

```{code-cell} ipython3
r1 = 3.0
t1 = 20
```

::: {admonition} Merknad
Om du vil at brukaren skal oppgje verdi til variablane, kan du bruka
`input()`-funksjonen.
Blokken over kan til dømes endrast til dette:
```ipython3
r1 = float(input("Hva er R-verdien i starten? "))
t1 = int(input("Hvor mange uker holder denne R-verdien seg? "))
```

Der er to grunnar til at eg ikkje bruker `input()` i døma.  
Den viktigaste er at `input()` ikkje verkar når eg genererer vevsider
frå Jupyter-dokumentet.  Når ein arbeider i Jupyter Lab, kan dessutan
lesaren like enkelt endra verdiane i ein kodeblokk.  

Det er derimot verd å læra seg `input()`-funksjonen når ein skal skriva
frittståande program, og mange forfattarar bruker han i Jupyter Notebook-dokument.
:::

```{code-cell} ipython3
pop = 1
liste_smittet = [1]
 
for i in range(t1):
    pop *= r1
    liste_smittet.append(pop)
 
r2 = 1.2
t2 = 30
 
for i in range(t2):
    pop *= r2
    liste_smittet.append(pop)
```
   
```{code-cell} ipython3
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.grid(True)
ax1.plot(range(len(liste_smittet)), liste_smittet)
plt.xlabel("Uker")
plt.ylabel("Nye smittede")
plt.show()
```
