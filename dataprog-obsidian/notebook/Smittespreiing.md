# Smittespreiing

Kjelde : [NDLA](https://ndla.no/r/biologi-1/smittespredning---modeller/d7dd80dfac)

```{code-cell} ipython3
r1 = float(input("Hva er R-verdien i starten? "))
lengde_r1 = int(input("Hvor mange uker holder denne R-verdien seg? "))
```

```{code-cell} ipython3
pop = 1
liste_smittet = [1]
 
for i in range(lengde_r1):
    pop *= r1
    liste_smittet.append(pop)
 
r2 = float(input("Hva er R-verdien i neste fase? "))
lengde_r2 = int(input("Hvor mange uker holder denne R-verdien seg? "))
 
for i in range(lengde_r2):
    pop *= r2
    liste_smittet.append(pop)
```
   
```{code-cell} ipython3
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.grid(True)
ax1.plot(xliste, liste_smittet)
plt.xlabel("Uker")
plt.ylabel("Nye smittede")
plt.show()
```
