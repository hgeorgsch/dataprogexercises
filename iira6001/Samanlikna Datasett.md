---
title: Samanlikna Datasett
tags:
  - session
  - statistics
  - csv
---

# Samanlikna Datasett

::: {admonition} Forkunnskapar
Dette kapittelet byggjer på [](CSV%20og%20Deskriptiv%20Statistikk).
:::

Denne veka skal me halda fram der me slapp i forrige veke.
og skal no samanlikna data frå ulike datasett.  


+ *Perspektivførelesing*
    + Flyttal og NaN
	  [(foilar)](https://iirevu.org.ntnu.no/Slides/Flyttal%20og%20NaN/)
    + Tidsrekkjer og *pivot*
	  [(foilar)](https://iirevu.org.ntnu.no/Slides/Tidsrekkjer%20og%20pivot/)
    + Tidsrekkjer og frekvens
	  [(foilar)](https://iirevu.org.ntnu.no/Slides/Tidsrekkjer%20og%20frekvens/)
+ *Gjennomarbeidde Døme.*
	+ [Samanlikning av tidsrekkjer](notebooks/Arbeidsledige%20og%20Konkursar) 
    + [Jordskjelvdata](notebooks/Jordskjelv) som demonstrerer animasjon og plotting oppå kart. (valfri)
+ *Demovideo*
    + [Melt og pivot](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=bbd31244-1c04-4d7a-a7cf-b3f400bc9a25)
+ Kuriosa
    + [](notebooks/Tidsrekkjer-demo) viser datasettet og tabellane
      frå tidsrekkjer og *pivot*.

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

