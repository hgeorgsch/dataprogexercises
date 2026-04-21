---
title: git og github
---

# git og github

::: {admonition} Oppgåve
Installer `git`.

Dersom du bruker ei jobbmaskin, må du kanskje bruka eit internt
programvaresenter.

Dersom du har alle rettar på maskina, kan du bruka den generelle
instruksjonen: [](Installasjon-git).
:::

::: {admonition} Oppgåve
Opna [git.ntnu.no](https://git.ntnu.no/).  Du loggar inn på same måte som andre
NTNU-tenester.
:::

## Klona eit git-repo frå andre


::: {admonition} Oppgåve
Opprett *Personal Access Token* (PAT).

+ Sjå [skjermbilete](https://www.geeksforgeeks.org/git/how-to-generate-personal-access-token-in-github/)

Pass på å kopiera PAT; git vil ikkje visa koden på nytt når du har forlate sida.
:::

::: {admonition} Oppgåva
Opna eit terminalvindauga for å klona eit git-repo.

Fyrst, for å få git til å lagra PAT, kan du bruka fylgjande kommando.
```sh
git config --global credential.helper store
```

Klone demo-repoet, slik
```sh
git clone https://git.ntnu.no/iirevu/iira6001demo.git
```

Her vert du beden om brukarnamn og passord.  Bruk det vanlege brukarnamnet,
emn i staden for passord, bruker du PAT.
:::


## Laga sitt eige git-repo

::: {admonition} Oppgåve
Opna [git.ntnu.no](https://git.ntnu.no/) og finn brukarprofilen din øvst til høgre.
Vel *repositories* i menyen.

Du har sikkert ingen *repositories* enno, men du kan trykka på den grøne *New*-knappen.

Gje det nye *repository* eit namn og ein beskriving.  Du må òg setja *owner* til brukarnamnet dit.
Du kan velja å laga nokre standardfiler (README, LICENSE), men det treng me ikkje tenkja på no.
:::
