---
tags:
  - session/week
title: Klyngeanalyse med Maskinlæring
---

# Klyngeanalyse med Maskinlæring

+ *Foredrag*
    + Unsupervised Learning
+ *Gjennomarbeidede eksempler* 
    + [Kredittbruk](notebooks/clustering_creditcards)
+ *Demo* regresjon og korrelasjon i pandas:
    + [Klyngeanalyse](notebooks/Klyngeanalyse)
+ *Kuriosa*
    + [$k$-means](norun/klyngedemo) viser og forklarer
      implementasjonen av $k$-means.
      Demonstrasjonen lagar òg dei plotta som er brukt i føredraget.


::: {admonition} Open oppgåve
Test ut teknikkane og framgangsmåtane frå det gjennomarbeidede dømet
på andre datasett, t.d.
+ iris-datasettet
+ [Palmer Penguins](https://archive.ics.uci.edu/dataset/690/palmer+penguins-3.)-datasettet
+ [nett-/detaljhandel](https://archive.ics.uci.edu/dataset/352/online+retail) 
:::

## plan

+ Introduksjon til unsupervised learning 
    + sklearn: kmeans, silhouette-score, inertia, skalering, pca
    + tiltenkt bruk av datasettt generert i 
      [testfil](notebooks/data-til-kmeans-knn)
+ Gjennomarbeidet eksempel
    + Spotify, audio analyse fra uke om webapi, skisse 
      [spotify-audio-bla](notebooks/Spotify-klyngeanalyse-ny)
