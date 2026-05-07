---
tags:
  - session/week
title: Klyngeanalyse med Maskinlæring
---

# Klyngeanalyse med Maskinlæring

+ *Perspektivforedrag* (Denne gongen er føredraget lagt ut som 
  foilar med lydspor; det kan henda at du må starta avspelinga manuelt;
  det kjem an på lesaren din.)
    + [Klyngeanalyse](https://iirevu.org.ntnu.no/Slides/Klyngeanalyse-slides/)
+ *Gjennomarbeidd døme* 
    + [Klyngeanalyse](notebooks/Klyngeanalyse)
      er ein enkel demonstrasjon av
      $k$-*means* og $k$-*nearest neighbour* på tilfeldige data.
    + [Kredittbruk](notebooks/clustering_creditcards)
      viser grundig utforsking av kredittkortkundedata.
+ *Kuriosa*
    + [$k$-means](norun/klyngedemo) viser og forklarer
      implementasjonen av $k$-means.
      Demonstrasjonen lagar òg dei plotta som er brukt i føredraget.

      Matematisk sett er $k$-*means* ein svært enkel algoritme
      å setja seg inn i.
      Dersom du ikkje er van med matriserekning, kan det likevel
      for tungt til å forsvara tida.


::: {admonition} Open oppgåve
Test ut teknikkane og framgangsmåtane frå det gjennomarbeidede dømet
på andre datasett, t.d.
+ iris-datasettet
+ [Palmer Penguins](https://archive.ics.uci.edu/dataset/690/palmer+penguins-3.)-datasettet
+ [nett-/detaljhandel](https://archive.ics.uci.edu/dataset/352/online+retail) 
:::

## Uferdige døme

+ Introduksjon til unsupervised learning 
    + sklearn: kmeans, silhouette-score, inertia, skalering, pca
    + tiltenkt bruk av datasettt generert i 
      [testfil](notebooks/data-til-kmeans-knn)
+ Gjennomarbeidet eksempel
    + Spotify, audio analyse fra uke om webapi, skisse 
      [spotify-audio-bla](notebooks/Spotify-klyngeanalyse-ny)
