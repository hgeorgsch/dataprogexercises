---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  name: dataprog
  language: python
  display_name: dataprog
---


# JSON og `dict`

---

Man lager `set` på akkura samme måte

```{code-cell} ipython3
import json
with open("kundedata1.json", 'r') as file:
    kundedata = json.load(file)


alle_etternavn = {kunde["etternavn"] for kunde in kundedata}
etternavn_H = {kunde["etternavn"] for kunde in kundedata if kunde["etternavn"][0] == 'H'}
print(etternavn)

```

+ Kan bli vanskelig å lese eller for komplisert
+ Dictionary av alle kunder med etternavn som begynner på 'H'

```{code-cell} ipython3
H_klubben = { navn: [kunde["fornavn"] for kunde in kundedata if kunde["etternavn"] == navn] 
             for navn in etternavn_H }

def finnKunde(etternavn):
    treffliste = []
    for kunde in kundedata:
        if etternavn == kunde["etternavn"]:
            treffliste.append(kunde)
    if treffliste == []:
        print(f"Ingen kunder med etternavn '{etternavn}' funndet")
        return None
    else:
        print(f"Vi fant {len(treffliste)} kunder med etternavn '{etternavn}'")
        return treffliste

H_klubben = { navn: finnKunde(navn) for navn in etternavn_H}

with open("kundedata_test.json", 'w') as file:
    json.dump(H_klubben, file)
```

---

## Oppg:

* Bruk komprehensjon til å lage en dictionary som inneholder allekunder med startsaldo større enn 120,000
* Dictionary skal bestå av nøkler som tilsvarer etternavnet til kundene, og verdiene skal være en liste med kundene på samme format som originalt

+ lag liste med rike kunder
+ lag set med etternavnene
+ lag dictionary med kunder { kundensetternavn: [liste med kunder]}

```{code-cell} ipython3
grense = 120e3
rike_kunder = [ kunde for kunde in kundedata if kunde["startsaldo"] > grense]
etternavn_rik = {kunde["etternavn"] for kunde in rike_kunder}
data_rike_kunder = {navn: [kunde for kunde in rike_kunder if kunde["etternavn"] == navn] for navn in etternavn_rik}
```

```{code-cell} ipython3
data_rike_kunder
```
