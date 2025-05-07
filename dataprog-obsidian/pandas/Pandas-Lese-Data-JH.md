---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Hente og lese inn data til pandas

+ byggjer på [[Filhandtering]]

## CSV + Pandas

* Vi bruker pandas til å lese og lagre csv-filer
* `pd.read_csv("filnavn")`
* `read_csv` har **haugevis** med keyword arguments for å lese rare og potensielt føkka csv-filer
* Vi burde i de fleste tilfeller klare oss med:
    - `encoding = "input-enc"` feks `"utf-8"`
    - `sep = "separator"` feks `","` eller "`\t`" (tab)
    -  `header = rad` feks `header=0`dersom første rad gir kolonnenavnene
    -  `index_col = «kolonnenummer»` Angir hvilken av kolonnene som skal brukes som indeks (nummer eller etikette) 

```{code-cell} ipython3
import pandas as pd

BB_df= pd.read_csv("blackboard.csv", encoding="utf-16", sep="\t")
BB_df = BB_df.set_index("Unnamed: 0")
BB_df.index.name = None


#Alternativt
BB_df= pd.read_csv("blackboard.csv", encoding="utf-16", sep="\t", index_col=0)
BB_df
```


* Filen vi har lastet inn er klasselisten fra blackboard
* på iirmoodle.it.ntnu.no er det mulig å melde folk opp i fag ved å laste *opp* en csv-fil
* `moodle_example.csv` viser hvordan denne filen skal se ut

```{code-cell} ipython3
moodleEx_df = pd.read_csv("moodle_example.csv")
moodleEx_df
```


### Opppgave 1

* Lag et dataframe fra "blackboard.csv" som er formatert slik moodle vil ha det

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
data = {"username": BB_df["Brukernavn"], "firstname": BB_df["Fornavn"], "lastname": BB_df["Etternavn"]}
datatest = pd.DataFrame(data)

#Med for-løkke
#ny_data = []
#for bruker in datatest["username"]:
#    ny_data.append(f"{bruker}@stud.ntnu.no")
#datatest["email"] = ny_data

#Med listekomprehensjon
#datatest["email"] = [f"{bruker}@stud.ntnu.no" for bruker in data["username"]]

#Med apply/map:
#datatest["email"] = datatest["username"].apply(lambda bruker: f"{bruker}@stud.ntnu.no")

#Med pandas sin serialisering av dataseries
datatest["email"] = datatest["username"]+"@stud.ntnu.no"
datatest
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Vi lagrer et dataframe til csv med `df.to_csv("filnavn.csv", **kwargs)`
* når vi ser `**kwargs` på denne måten, betyr det at her kommer «keyword arguments»
* Vi kan se i [dokumentasjonen](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) får å finne hvilke «kwargs» funksjonen tar

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
datatest.to_csv("moodle_formatert.csv", index=False)
```


* Det er mye å holde styr på i Pandas, og vi går ikke igjennom alle aspekter
* Ha en [cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) for hånden
* Slå opp i diverse [tutorials](https://pandas.pydata.org/pandas-docs/stable/getting_started/tutorials.html)
* Spesielt [denne](https://www.skytowner.com/explore/pandas_recipes_reference) kan være kjekk (Pandas oppskrifter :) )

