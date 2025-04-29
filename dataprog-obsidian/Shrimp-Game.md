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

## AE201808 Næringsøkonomi  

Competition and cooperation in oligopolies: 

 “The Shrimp Game” 
----

The game 

* Atari, BMI and Commodore own the only three shrimp boats on the island of New Ålesund.  

* Each shrimper incurs the same cost of $5.00 per pound of shrimp they catch (this includes the opportunity cost of time) and each can catch at most 75 pounds per day.  

* At the end of each day, they bring their catch to the only market on the island where price is determined by market demand and the supply of fish, and all shrimp is sold. All shrimp goes bad after one day, so a shrimper cannot keep shrimps off the market and sell them the next day.  

    The mayor of New Ålesund is also the supervisor of this market. He/she controls the pounds caught by each shrimper and announces the day’s price for shrimp. 

*    Let QA, QB, and QC denote Atari’s, BMI’s and Commodore’s catch, respectively. Once each has decided when to stop fishing and has brought his or her shrimp to market, the price is determined by the following equation:  

$$ P (Q_A, Q_B, Q_C)  =  45 – [ 0.2 \times (QA + QB + QC ) ] $$

* Each shrimper agrees that the above equation correctly predicts the market price of shrimp, and each tries to catch enough shrimp so as to maximize his or her dollar profits.  

* The profits $\pi$ for each shrimper equals the number of pounds caught multiplied by its profit margin, that is:   

$$ \pi_A (Q_A, Q_B, Q_C) = Q_A \left[ P (Q_A, Q_B, Q_C) – 5 \right]$$

* The three shrimpers have a history of family feuds and no personal contact. Each will have to set its shrimp production for the day without knowing what levels the other two shrimpers set. However, as described above, at the end of each day the production levels that were set by each shrimper will become public knowledge. 

+++

# Simuleringsoppgave i Python :)
* Vi vil lage et pythonprogram som simulerer ulike strategier fiskerene kan velge
* Feks:
  - Fisk så mye som mulig
  - Fisk tilfeldig mengde
  - Se på hvor mye konkurrentene har tidligere har fisket, og fisk optimal mengde (*Cournot modellen*)


```{code-cell} ipython3

```
