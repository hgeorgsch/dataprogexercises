---
tags:
  - legacy/iif
  - pickle
---


+ Dette kjem frå ein gamal versjon av [[Konseptuell forståing av  pandas]]


+ [x] Bør me introdusera `pickle`? #primitives/pickle 📅 2025-05-07 ✅ 2025-05-08
	+ Neppe !


```{code-cell} ipython3
# EKSEMPEL

import pandas as pd
import numpy as np
import pickle

with open("HPcharacters.pickle", "rb") as file:
    HPdata = pickle.load(file)

df = pd.DataFrame(HPdata)
df
```

```{code-cell} ipython3
df = df.drop(columns=["id", "alternate_names", "gender", "wand", "actor", "alternate_actors", "image"])
df
```
