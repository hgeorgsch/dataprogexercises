import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv( "1054.csv", encoding="latin1", sep=";" )

idx = list(df.columns)[-1]

df[idx] = pd.to_numeric(df[idx],errors="coerce")
df1 = df[ df["statistikkvariabel"] == "Arbeidsledige (1000 personer)" ]
df1 = df1[ df1["kjønn"] == "0 Begge kjønn" ]
df1 = df1[ df1["alder"] == "15-74 15-74 år" ]
df1 = df1[ df1["type justering"] == "T Trend" ]

arbdf = df1.copy()

arbdf = arbdf.rename( columns={ idx : "arbeidsledige" } ) 
print(arbdf)

print(arbdf.describe())
print(arbdf["arbeidsledige"])

arbdf["arbeidsledige"] = arbdf["arbeidsledige"].astype(np.double)

arbdf.plot()
plt.savefig("test20okt.svg")
