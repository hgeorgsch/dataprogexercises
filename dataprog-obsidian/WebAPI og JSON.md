---
tags:
   - stub
   - json
---

+ JSON er ein `dict`
	+ verdiar kan vera `dict`, liste, streng eller tal
	+ hierarki av objekt
	+ `json`-biblioteket
+ Mange filformat byggjer på JSON
	+ bestemte attributtar må vera med
	+ Døme
		+ JSON-stat
		+ Jupyter Notebook
		+ linked data (JSON-LD)

+ JSON
	+ [[skadde-binomial]]
	+ [[utdanning]]


+ SSB bruker JSON-stat
	+ JSON-fomrat spesialdesigna for statistiske data
+ [pyjstat](https://pypi.org/project/pyjstat/)
  
```ipython3
import pandas as pd  
from pyjstat import pyjstat  
  
# Example: Reading from a URL  
url = "http://json-stat.org/samples/oecd-canada.json"  
dataset = pyjstat.Dataset.read(url)  
df = dataset.to_data_frame()  
print(df.head())
```