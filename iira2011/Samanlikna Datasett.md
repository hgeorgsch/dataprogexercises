---
title: Samanlikna Datasett
tags:
  - session
  - statistics
  - csv
---

# Samanlikna Datasett

::: {admonition} Forkunnskapar
Dette kapittelet byggjer på [](veke-CSV).
:::

Denne veka skal me halda fram der me slapp i forrige veke.
og skal no samanlikna data frå ulike datasett.  


+ *Perspektivførelesing*
    + [Flyttal og NaN](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=06906544-38f4-4769-a348-b3f600b5ed9b)
	  [(foilar)](https://iirevu.org.ntnu.no/Slides/Flyttal%20og%20NaN/)
+ *Gjennomarbeidde Døme.*
    + [](nb02/Jordskjelv) som demonstrerer animasjon og plotting oppå kart. (valfri)
+ *Demovideo*
    + [Melt og pivot](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=bbd31244-1c04-4d7a-a7cf-b3f400bc9a25)
        + [Datasett 05307](./notebooks/05307_andel-roykere.csv)
        + [Kode](./notebooks/Melt-pivot)

## Oppsummeringa

Målet dei siste to vekene har vore å kunna henta datasett frå eksterne
kjelder og behandla dei fritt i python.
Dette er vanskeleg fordi data vert formatterte på ulike måtar og der er 
ofte meir data enn me er interessert i.
Dessutan må me kunna zetja saman data frå ulike datasett som ikkje alltid
er eins formatterte.

Der finst inga generell oppskrivt for å formattera data.  Ein må faktisk
sjå på det konkrete tilfellet, og forstå både kva ein har i datasettet og
kva ein treng.  Det hjelper med øving og erfaring.

Denne veka har me sett særskilt på å
+ aggregera data for å sameina datasett på ulike tidsskalaer.
+ setja saman ulike datasett i éin *DataFrame* i pandas.
+ bruken av *melt*, *pivot* og multiindeks.

