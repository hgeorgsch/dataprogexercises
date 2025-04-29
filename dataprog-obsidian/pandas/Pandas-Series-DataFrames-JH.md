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



* Når vi behandler store mengder data og data fra ulike kilder trenger vi å ha kontroll på hvordan dataen vår representeres internt i datamaskinen
```python
data = np.array([..... ], dtype=«numpy datatype»)
```
* `numpy` har flere ulike datatyper vi kan bruke


| **Type**       | **Name**     | **Description**                                                   |
| -------------- | ------------ | ----------------------------------------------------------------- |
| Integer        | `int8`       | Integer (-128 to 127)                                             |
| Integer        | `int16`      | Integer (-32,768 to 32,767)                                       |
| Integer        | `int32`      | Integer (-2,147,483,648 to 2,147,483,647)                         |
| Integer        | `int64`      | Integer (-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807) |
| Unsigned Int   | `uint8`      | Unsigned integer (0 to 255)                                       |
| Unsigned Int   | `uint16`     | Unsigned integer (0 to 65,535)                                    |
| Unsigned Int   | `uint32`     | Unsigned integer (0 to 4,294,967,295)                             |
| Unsigned Int   | `uint64`     | Unsigned integer (0 to 18,446,744,073,709,551,615)                |
| Floating Point | `float16`    | Half precision floating point                                     |
| Floating Point | `float32`    | Single precision floating point                                   |
| Floating Point | `float64`    | Double precision floating point                                   |
| Complex Number | `complex64`  | Complex number (real and imaginary as `float32`)                  |
| Complex Number | `complex128` | Complex number (real and imaginary as `float64`)                  |
| Boolean        | `bool_`      | Boolean (True or False)                                           |
| String         | `string_`    | Fixed-size string data                                            |
| Unicode String | `unicode_`   | Fixed-size Unicode string data                                    |

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

### DataFrame-data
* Merk at dersom vi forandrer datavariabelen, forandres også pandas serien
* Vi sier at dataframen inneholder «refererer» til data som er lagret et annet sted
* Dersom dette ikke er ønskelig kan vi bruke `copy=True` når vi lager serien
* Av og til vil vi ha en kopi som ikke forstyrrer «datakilden»
* Av og til vil vi ikke gjøre det slik -- det er raskere og bruker mindre minne

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
dataserie = pd.Series(data, name=navn, index=indeks, copy=True)
print(dataserie)
data[2]=66
dataserie
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}



## Attributter
* Pandas Series objekter har ulike *atributter*

+++ {"editable": true, "slideshow": {"slide_type": "fragment"}}

| **Attribute**      | **Description**                                                                 |
|--------------------|---------------------------------------------------------------------------------|
| `index`            | The index (labels) of the Series.                                               |
| `values`           | The values (data) of the Series as a NumPy array.                               |
| `name`             | The name of the Series.                                                         |
| `dtype`            | The data type of the values in the Series.                                      |
| `size`             | The number of elements in the Series.                                           |
| `shape`            | The dimensionality of the Series (always a single dimension).                   |
| `empty`            | Returns `True` if the Series is empty (i.e., has no elements).                  |
| `nbytes`           | The total number of bytes consumed by the Series' elements.                     |
| `hasnans`          | Returns `True` if there are any `NaN` values in the Series.                     |
| `is_unique`        | Returns `True` if all values in the Series are unique.                          |
| `is_monotonic`     | Returns `True` if the Series is sorted in increasing order.                     |
| `str`              | Provides access to string methods (if the Series contains strings).             |
| `dt`               | Provides access to datetime methods (if the Series contains datetime objects).  |
| `T`                | The transpose of the Series (no effect for 1D data, but included for consistency). |

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: subslide
---
print(dataserie.name)
print(dataserie.values)
print(dataserie.index)
print(dataserie.nbytes)
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

## Metoder
* Pandas Series objekter har flere nyttige *metoder*

+++ {"editable": true, "slideshow": {"slide_type": "fragment"}}

| **Metode**            | **Beskrivelse**                                                                  |
|-----------------------|----------------------------------------------------------------------------------|
| `head(n)`             | Returnerer de første `n` elementene i Series (standard er 5).                     |
| `tail(n)`             | Returnerer de siste `n` elementene i Series (standard er 5).                      |
| `unique()`            | Returnerer unike verdier i Series.                                                |
| `value_counts()`      | Returnerer antall forekomster av unike verdier i Series.                          |
| `describe()`          | Genererer beskrivende statistikk som antall, gjennomsnitt, std, min og maks.      |
| `sum()`               | Returnerer summen av elementene i Series.                                         |
| `mean()`              | Returnerer gjennomsnittet av elementene i Series.                                 |
| `median()`            | Returnerer medianen av elementene i Series.                                       |
| `min()`               | Returnerer minimumsverdien i Series.                                              |
| `max()`               | Returnerer maksimumsverdien i Series.                                             |
| `std()`               | Returnerer standardavviket til Series.                                            |
| `sort_values()`       | Sorterer Series etter verdiene.                                                   |
| `sort_index()`        | Sorterer Series etter indeksen.                                                   |
| `apply(func)`         | Anvender en funksjon element for element på Series.                               |
| `map(func)`           | Mapper verdier i Series ved hjelp av funksjon eller dictionary.                       |
| `dropna()`            | Fjerner `NaN`-verdier fra Series.                                                 |
| `fillna(value)`       | Fyller inn `NaN`-verdier med en spesifisert verdi.                                |
| `astype(dtype)`       | Endrer datatypen til Series til spesifisert datatype.                             |
| `clip(lower, upper)`  | Begrenser verdier til et spesifisert område (nedre og øvre grenser).              |
| `between(left, right)`| Returnerer True for verdier mellom spesifiserte grenser.                          |
| `shift(periods)`      | Skifter verdiene med et spesifisert antall perioder.                             |
| `cumsum()`            | Returnerer den kumulative summen av elementene i Series.                          |
| `cumprod()`           | Returnerer det kumulative produktet av elementene i Series.                       |
| `rolling(window)`     | Gir glidende beregninger med et gitt vindu                                          |
| `expanding()`         | Gir ekspanderende beregninger (f.eks. kumulative beregninger).               |
| `resample(rule)`      | Resampler tidsseriedata i henhold til en spesifisert frekvens.                    |
| `plot()`              | Plotter dataen i Series ved hjelp av Matplotlib.                                  |

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: subslide
---
print(dataserie.describe())
dataserie.dropna()
```


