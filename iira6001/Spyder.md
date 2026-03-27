---
title: Spyder eller andre IDEar
---

# Spyder eller andre IDEar

Dei fleste som programmerer bruker ein IDE som står for 
*Integrated Development Environment*.  Føremonen med IDEen er
at ein har alt på ein plass, og brukargrensesnittet hjelper oss
med å organsiera prosjekt med mange filer.

Der er mange IDEar som støttar python.  Dei mest kjende er PyCharm,
Spyder og VSCode.  Det er mykje smak og behag, og dersom du arbeider
saman med andre som bruker ein bestemt IDE, so kan det løna seg å velja
den same.

I øvinga tek eg utgangspunkt i Spyder, mest fordi det er open kjeldekode og
kan installerast med `pip`.   Dei fleste IDEar er proprietære og krev at ein
set seg inn i lisensvilkåra, sjølv om lisensen ofte er gratis.
Eg trur at du vil ha nytte av demovideoen med `Spyder` sjølv om du bruker ein
annan IDE.

+ Demo Spyder

## Oppgåve i Spyder

::: {admonition} Oppgåve
Installer og start Spyder frå kommandolina.
```python
pip install spyder
spyder
```
:::

::: {admonition} Oppgåve
Start eit nytt prosjekt (*Projects*-menyen) med ein høveleg katalog.
:::

::: {admonition} Oppgåve
Ta utgangspunkt i ei gamal oppgåve, t.d. [](notebooks/Arbeidsledige),
og kopierer datafila (CSV) som vert brukt inn i prosjektkatalogen som 
du bruker i Spyder.
:::

::: {admonition} Oppgåve
Lag ei ny programfil og gje ho eit høveleg namn (kanskje `arbeidsledige.py`).
Skriv eit kort program som
1. importerer pandas 
2. laster inn CSV-fila
3. skriv ut datasettet med `print` 
Køyr programmet.  Kva skjer?
:::

::: {admonition} Oppgåve
Utvid programmet slik at datasettet vert formattert med tanke på å plotta
ei tidsrekkje.  Bruk den same koden som me brukte i den opprinnelege øvinga.
Skriv ut med `print` for å testa.
:::

::: {admonition} Oppgåve
Utvid programmet med eit plott.
1. importer `pyplot`
2. lag plottet med same kode som me brukte i Jupyter Notebook

Køyr programmet.  Kva skjer?
:::

::: {admonition} Oppgåve
Opna kommandolina, utanfor Spyder, og finn prosjektkatalogen din.
(Bruk `cd` for å byta katalog.)

Køyr programmet frå kommandolina, t,d.
```sh
pytjon arbeidsledige.py
```

Kva skjer?
:::

::: {tip} 
Spyder har automatisk vising av plott, på same måte som Jupyter Lab.
Når programmet køyrer på kommandolina, skjer det derimot ikkje.
Ein kan bruka `show()` (frå pyplot) for å visa plottet på skjermen
eller `savefig()` for å lagra det som ei grafikkfil.
:::

::: {admonition} Oppgåve
Legg til `plt.show()` i programmet ditt, lagra og køyr på nytt
from kommandolina.  Kva skjer?
:::

::: {admonition} Oppgåve
Legg til `plt.savefig( "arbeidsledige.png" )` i programmet ditt,
i staden for `plt.show()`.
Køyr programmet.  Kva skjer?

(Du kan godt testa både frå kommandolina og frå Spyder.)

Sjekk innhaldet i katalogen og opna grafikkfila i eit egna program.
:::

## Avrunding

Det kan vera viktig å hugsa på at program kan oppføra seg forskjellig
i Spyder og utanfor.  Det gjelder særleg grafiske element som plott.
Det kan løna seg å ha eit terminalvindauga ope ved sidan av Spyder, for
å kunna testa.
