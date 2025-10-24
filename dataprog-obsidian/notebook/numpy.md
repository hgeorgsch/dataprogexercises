---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  name: dataprog
  language: python
  display_name: dataprog
---

# numpy-biblioteket

Pandas er eit ypperleg bibliotek til å sortera og formattera data,
men det er ikkje like godt egna til å rekna på data.
Når me skal gå vidare med prediksjons- og klassifikasjonsmodellar,
vil me bruka SciKitLearn som byggjer på `numpy`.

::: {admonition} Merknad
Målet med denne innføringa er å kjenna igjen `numpy`-objekta som
dukkar opp når me bruker SciKitLearn, og å kunna konvertera
datasett mellom SciKitLearn og pandas.
Dei som vil arbeida med meir avanserte matematiske modellar i python,
vil måtte læra seg mykje meir om `numpy` og matriserekning.
:::

Hovudhensikta i `numpy` er matriserekning.  Dei som har lese litt
matematikk veit at ein matrise er eit todimensjonalt system med
talverdiar, t.d.
$$ A = 
\begin{bmatrix}
   1{,}0 & 2{,}4 & 5{,}5 & 6{,}1 \\
   0 & 2{,}0 & 1{,}0 & 2{,}1 \\
   1{,}2 & 0 & 0 & 1{,}2 \\
\end{bmatrix}$$
I `numpy` kalles dette normalt for ein *array*.
```{code-cell} ipython3
import numpy as np
A = np.array( [
   [ 1.0, 2.4, 5.5, 6.1 ]
   [ 0, 2.0, 1.0, 2.1 ]
   [ 1.2, 0, 0, 1.2 ]
   ] )
print(A)
```
Her vert *array*en definert ved ei liste av lister, der dei indre listene
vert radar i *array*en.

Den største skilnaden mellom ein *DataFrame* i pandas og ein *array*
i `numpy`, er at i ein *array* må alle elementa (tala) ha same type.
I ein *DataFrame* har søylene ofte ulik type.
Dette høyrest ut som ei stor ulempe for numpy, men det gjer det enklare
og raskare å rekna på heile datasettet.
Det er difor me treng *arrays*.


```{code-cell} ipython3
df = pd.DataFrame(A)
display(df)
```

```{code-cell} ipython3
df2 = pd.DataFrame(A, columns=['ColA', 'ColB', 'ColC', 'ColD'])
display(df2)
```

```{code-cell} ipython3
import pandas as pd
import numpy as np

# Create a DataFrame
data = {'ColA': [10, 20, 30], 'ColB': [11, 21, 31]}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Convert the DataFrame to a NumPy array
numpy_array_from_df = df.to_numpy()
print("\nNumPy array from DataFrame:")
print(numpy_array_from_df)
print(f"Type of result: {type(numpy_array_from_df)}")
```
