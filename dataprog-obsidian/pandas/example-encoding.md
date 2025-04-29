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

```{code-cell} ipython3
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

SSBENC="ISO-8859-1"

df = pd.read_csv("laksedata.csv", encoding=SSBENC, sep=";", header=1) #Funker med UTF-8
df["uke"] = df["uke"].map(lambda x: datetime.datetime.strptime(x+"-1", "%YU%W-%w"))

sns.set_theme()
sns.lineplot(data=df.query("varegruppe == 'Fersk oppalen laks' and '2004' < uke < '2006'"), x="uke", y="Vekt (tonn)")
#df["uke"] = df["uke"].dt.to_period("W")
df = df.set_index([ "varegruppe","uke"])
df_fersk = df.loc["Fersk oppalen laks"]
df_fersk_A = df_fersk.groupby(by=df_fersk.index.year).mean()
plt.show()
sns.lineplot(data=df_fersk, y="Kilopris (kr)", x="uke")
```

```{code-cell} ipython3
streng = "2023U52"
streng2 = streng +"-1"
ukedato = datetime.datetime.strptime(streng2, "%YU%W-%w")
ukedato
```
