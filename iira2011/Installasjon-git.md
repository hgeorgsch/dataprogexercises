---
tags:
    - tutorial
    - installation
---

# Installera git

Git er eit versjonskontrollsystem.
Det er ein open standard, og der er mange ulike verkty som kan handtera `git`. 
Korleis du ynskjer å installera det, avheng i stor grad av kva andre verkty og
system du nyttar.  Her gjev me nokre få døme som skal vera tilstrekkeleg for å
koma i gang med `git` i kurset.

## Git i Windows

Der er mange måtar å installera `git` på.
Den som me ser på her ser ut til å bruka MicroSoft sin eigen
distribusjon.
Du treng nesten heilt sikkert Administrator-tilgang for å gjera
dette.

1.  Installer [winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
2.  Bruk `winget` til å installera `git `

```
winget install --id Git.Git -e --source winget
```

## Git i linux

I Ubuntu og Debian er `git` namnet på ei pakke i pakkehandteringsløysinga `apt`.
Ein installerer slik
```sh
sudo apt-get install git
```
Andre linux-distribusjonar har andre pakkehandteringsverkty, men det skal vera
tilsvarande enkelt.

## Git via Anaconda

Git er som sagt et versjonskontrollsystem man bruker når mange skal jobbe med samme kodebase. 
Det er også en grei måte å dele eller distribuere kode med.
Git blir ofte installert automatik på mac, men følg instruksjonene under, så er vi sikker.

1. Åpne Anaconda navigator som du installerte i forrige steg
2. Åpne jupyterlab
3. I jupyterlab, åpne en terminal (macos) eller powershell(windows)
4. Kopier inn og kjør følgende linje i terminalen:

```bash
conda install anaconda:::git
```

:::{figure} jupyterlab-fig.png
Trykk på jupyterlab -- da åpnes det i en fane i nettleseren din
:::

:::{figure} terminal-fig.png
Åpne en terminal i jupyterlab -- noen ganger kalles the powershell
:::


