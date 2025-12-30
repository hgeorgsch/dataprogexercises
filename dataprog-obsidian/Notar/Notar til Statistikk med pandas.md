

+ Føredrag: [[Statistikk med pandas]]

+ *Basert på førelesingsnotat frå veke 41/2024.  Sjå nokre andre notat og oppslagstabellar i [[Pandas-Series-DataFrames-JH]]*
+ [[Døme med pickle]]
* Pandas er et bibliotek for python for å manipulere og analysere data
	* me brukte det fyrst i [[Fyrste datasett med CSV]]
* Vi importerer pandas med som regel med `import pandas as pd`
* Pandas er bygd på numpy, så man trenger ofte også å bruke numpy
	
* Vi bruker pandas til å laste inn eller lage datasett
    - Rydde opp i data
    - Få det over på annet format
    - Gjøre statistikk
    - Plotte data
* Dersom vi mangler noe data for en indeks bruker vi `np.NaN`som data
    
---
<img src="img/dfnavn1.jpg" width="550">


![dataframe_indeksnavn](img/dfnavn2.png)

---

```{code-cell} ipython3
sdata = {"frukt": ["epler", "pærer", "moreller", "rips"], "produksjon": [12,23,1,9], "subsidiert": [True, False, True, False], "pris": [10, 25, 40, 5]}
df_bilde = pd.DataFrame(sdata)
df_bilde
```

```{code-cell} ipython3
---
slideshow:
  slide_type: skip
---
sdata2 = { "produksjon": [12,23,1,9], "subsidiert": [True, False, True, False], "pris": [10, 25, 40, 5]}
df_bilde2 = pd.DataFrame(sdata2, index = ["epler", "pærer", "moreller", "rips"])
df_bilde2
```


---

### Oppgave 1:

* Lag dataserien under i pandas:
![oppg1](img/series_oppg1.png)

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
data = np.array([187,177,195,159], dtype="float64")
indeks = ["Per", "Pål", "Espen", "Askeladd"]
navn = "EventyrfigurHøyde"
dataserie = pd.Series(data, name=navn, index=indeks, copy=True)
dataserie
```



---

### Oppg 5:
Ta utgangpunkt i tabellen over for å lage tabellen under
![oppg5](img/df_oppg5v2.png)

les [her](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html) for å finne ut hvordan du legger til en kolonne med `insert`

```{code-cell} ipython3
df_land.rename(columns=({"innbyggere": "populasjonsstørrelse"}), inplace=True)
df_land.drop(index=['NO'], inplace=True)
df_land.insert(2,"arbeidsledighet", ["1.0%","4.9%","3.2%","1.6%","12.5%" ])
df_land.loc["DE", "populasjonsstørrelse"]  = 83
df_land.loc["US"] = ["USA", 300, "50%"]
df_land
```

---

### DataFrame-data
* Merk at dersom vi forandrer datavariabelen, forandres også pandas serien
* Vi sier at dataframen inneholder «refererer» til data som er lagret et annet sted
* Dersom dette ikke er ønskelig kan vi bruke `copy=True` når vi lager serien
* Av og til vil vi ha en kopi som ikke forstyrrer «datakilden»
* Av og til vil vi ikke gjøre det slik -- det er raskere og bruker mindre minne

```{code-cell} ipython3
ddataserie = pd.Series(data, name=navn, index=indeks, copy=True)
print(dataserie)
data[2]=66
dataserie
```

---

### DataFrame-data
* Merk at dersom vi forandrer datavariabelen, forandres også pandas serien
* Vi sier at dataframen inneholder «refererer» til data som er lagret et annet sted
* Dersom dette ikke er ønskelig kan vi bruke `copy=True` når vi lager serien
* Av og til vil vi ha en kopi som ikke forstyrrer «datakilden»
* Av og til vil vi ikke gjøre det slik -- det er raskere og bruker mindre minne

```{code-cell} ipython3
ddataserie = pd.Series(data, name=navn, index=indeks, copy=True)
print(dataserie)
data[2]=66
dataserie
```
