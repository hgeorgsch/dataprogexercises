# Installasjon og kom i gang

I denne økten gjør vi datamaskinen klar for resten av kurset. Vi skal installere
Python, JupyterLab og noen sentrale pakker. Til slutt henter vi et lite prosjekt
med Git og åpner det i JupyterLab.

Du trenger ikke forstå alle kommandoene med én gang. Målet er å bli litt kjent
med arbeidsflyten og få et miljø som virker.

## Videoveiledning

Velg operativsystemet ditt. Du må være innlogget hos NTNU for å se videoene.

:::::{tab-set}
::::{tab-item} Windows 11
:sync: windows
:selected: true

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
  <iframe
    src="https://ntnu.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=6dfb3e61-a34f-466e-b8dc-b4a900a46201&amp;autoplay=false&amp;offerviewer=true&amp;showtitle=true&amp;showbrand=true&amp;captions=false&amp;interactivity=all"
    title="IIRA2001 – installasjon i Windows 11"
    style="border: 1px solid #464646; position: absolute; inset: 0; width: 100%; height: 100%; box-sizing: border-box;"
    allow="autoplay"
    allowfullscreen
    loading="lazy">
  </iframe>
</div>

[Åpne Windows-videoen direkte i Panopto](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=6dfb3e61-a34f-466e-b8dc-b4a900a46201)
::::

::::{tab-item} macOS
:sync: macos

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
  <iframe
    src="https://ntnu.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=fc89b723-ee83-40f7-94b1-b4a900a490fd&amp;autoplay=false&amp;offerviewer=true&amp;showtitle=true&amp;showbrand=true&amp;captions=false&amp;interactivity=all"
    title="IIRA2001 – installasjon i macOS"
    style="border: 1px solid #464646; position: absolute; inset: 0; width: 100%; height: 100%; box-sizing: border-box;"
    allow="autoplay"
    allowfullscreen
    loading="lazy">
  </iframe>
</div>

[Åpne macOS-videoen direkte i Panopto](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=fc89b723-ee83-40f7-94b1-b4a900a490fd)
::::
:::::

## Før du begynner

Du trenger:

- en datamaskin med Windows eller macOS
- tilgang til å installere programmer på maskinen
- en nettleser og internettforbindelse
- omtrent 45–60 minutter

Ha denne siden åpen på telefonen eller i en egen nettleserfane. Da kan du lese
kommandoene selv om nettleseren må startes på nytt underveis.

:::{important}
Velg fanen for operativsystemet ditt. Når du velger **Windows** eller **macOS**
ett sted på siden, følger de andre fanegruppene samme valg.
:::

## 1. Bli kjent med terminalen

Terminalen er et program der vi gir datamaskinen korte tekstkommandoer. På
Windows bruker vi **PowerShell**, mens programmet heter **Terminal** på macOS.

:::::{tab-set}
::::{tab-item} Windows
:sync: windows
:selected: true

1. Åpne Start-menyen.
2. Skriv `PowerShell`.
3. Åpne **Windows PowerShell** eller **Terminal** med en PowerShell-fane.

Du trenger ikke velge «Kjør som administrator».

:::{figure} ../../../images/win-powershell-sok.png
:alt: Søk etter Windows PowerShell i Start-menyen.
:width: 80%

Søk etter og åpne Windows PowerShell fra Start-menyen.
:::

:::{figure} ../../../images/win-powershell.png
:alt: Et åpent PowerShell-vindu på Windows.
:width: 80%

PowerShell er klar til å ta imot kommandoer.
:::
::::

::::{tab-item} macOS
:sync: macos

1. Trykk <kbd>Command</kbd> + <kbd>Mellomrom</kbd> for å åpne Spotlight.
2. Skriv `Terminal`.
3. Trykk <kbd>Enter</kbd>.

:::{figure} ../../../images/spotlightsok.png
:alt: Spotlight-søk etter Terminal på macOS.
:width: 80%

Søk etter Terminal med Spotlight.
:::

:::{figure} ../../../images/terminal.png
:alt: Et åpent terminalvindu på macOS.
:width: 80%

Terminal er klar til å ta imot kommandoer.
:::
::::
:::::

### Hvor er jeg?

Terminalen står alltid «i» en mappe. Kommandoen `pwd` viser hvilken mappe du er
i, mens `ls` viser innholdet i mappen.

:::::{tab-set}
::::{tab-item} Windows
:sync: windows
:selected: true

Skriv én linje om gangen og trykk <kbd>Enter</kbd> etter hver linje:

```powershell
pwd
ls
```

I PowerShell virker både `ls` og det lengre navnet `Get-ChildItem`. Vi bruker
`ls`, fordi samme korte kommando også virker på macOS.
::::

::::{tab-item} macOS
:sync: macos

Skriv én linje om gangen og trykk <kbd>Enter</kbd> etter hver linje:

```bash
pwd
ls
```
::::
:::::

:::{tip}
Teksten som allerede står foran markøren, for eksempel `PS C:\Users\Ada>` eller
`ada@MacBook ~ %`, er ledeteksten. Den skal **ikke** skrives inn når du kopierer
en kommando fra denne siden.
:::

### Flytt deg mellom mapper

`cd` er en forkortelse for *change directory*. Kommandoen `cd ..` går ett nivå
opp. Et enslig punktum betyr gjeldende mappe, og to punktum betyr mappen over.

:::::{tab-set}
::::{tab-item} Windows
:sync: windows
:selected: true

```powershell
cd ..
pwd
ls
cd ~
pwd
```

Den siste kommandoen fører deg tilbake til hjemmemappen din.
::::

::::{tab-item} macOS
:sync: macos

```bash
cd ..
pwd
ls
cd ~
pwd
```

Den siste kommandoen fører deg tilbake til hjemmemappen din.
::::
:::::

Du kan bruke <kbd>Tab</kbd> til å fullføre lange fil- og mappenavn. Skriv de
første bokstavene og trykk <kbd>Tab</kbd>. Dette sparer tid og forebygger
skrivefeil.

:::{admonition} Stopp og sjekk
:class: note
Før du går videre, skal du kunne bruke `pwd`, `ls`, `cd` og `cd ..`. Det er helt
greit å måtte se på oppskriften.
:::

## 2. Installer Python

Python er både programmeringsspråket vi skal bruke og programmet som kjører
koden vår. Vi installerer den offisielle utgaven fra
[python.org](https://www.python.org/downloads/).

:::::{tab-set}
::::{tab-item} Windows
:sync: windows
:selected: true

Python anbefaler nå **Python Install Manager** på Windows.

1. Gå til [python.org/downloads](https://www.python.org/downloads/).
2. Last ned Python Install Manager for Windows.
3. Dobbeltklikk den nedlastede `.msix`-filen og velg **Install**.
4. Lukk PowerShell og åpne det på nytt.
5. Skriv kommandoen under. Første kjøring kan samtidig installere den nyeste
   stabile Python-versjonen.

```powershell
python --version
```

Første gang kan Python Install Manager stille noen oppsettsspørsmål. Svar `y`
og trykk <kbd>Enter</kbd> når du blir spurt om å tillate lange filstier:

:::{figure} ../../../images/win-powershell-python-install.png
:alt: Python Install Manager spør om lange filstier skal tillates i Windows.
:width: 80%

Tillat lange filstier, slik at Python-pakker ikke stoppes av den gamle
grensen på 260 tegn.
:::

Du kan også bli spurt om å legge katalogen med Python-kommandoer til `PATH`.
Svar `y` her også. Lukk og åpne PowerShell på nytt dersom du får beskjed om det.

:::{figure} ../../../images/win-powershell-python-install-2.png
:alt: Python Install Manager spør om katalogen med Python-kommandoer skal legges til PATH.
:width: 80%

Legg Python-kommandoene til `PATH`.
:::

Kontroller deretter hvilke Python-versjoner installasjonsverktøyet finner:

```powershell
py list
```

Versjonsnummeret kan være nyere enn det som vises i undervisningen. Det er
normalt. Vi trenger en vanlig, stabil Python 3-versjon.

:::{figure} ../../../images/win-powershell-test.png
:alt: Kontroll av installert Python-versjon i PowerShell.
:width: 80%

En vellykket installasjon svarer med et Python-versjonsnummer.
:::

Den offisielle og oppdaterte beskrivelsen finnes i
[Python-dokumentasjonen for Windows](https://docs.python.org/3/using/windows.html).
::::

::::{tab-item} macOS
:sync: macos

1. Gå til [python.org/downloads](https://www.python.org/downloads/).
2. Last ned den nyeste stabile **macOS 64-bit universal2 installer**.
3. Dobbeltklikk `.pkg`-filen og følg standardvalgene i installasjonsprogrammet.
4. Når installasjonen er ferdig, åpner du mappen `Python 3.x` under Programmer.
5. Dobbeltklikk **Install Certificates.command**. Vent til terminalvinduet viser
   `update complete`, og lukk det.
6. Lukk Terminal og åpne det på nytt.

![Det offisielle installasjonsprogrammet for Python på macOS.](https://docs.python.org/3/_images/mac_installer_01_introduction.png)

*Skjermbilde: Python Software Foundation. Se den
[offisielle installasjonsveiledningen](https://docs.python.org/3/using/mac.html).*

Kontroller installasjonen:

```bash
python3 --version
```

Versjonsnummeret kan være nyere enn det som vises i undervisningen. Det er
normalt. Vi trenger en vanlig, stabil Python 3-versjon.

:::{important}
macOS kan også ha en eldre Python som systemet selv bruker. Ikke slett eller
endre den. Kommandoen `python3` skal etter standardinstallasjonen finne Python
fra python.org.
:::
::::
:::::

## 3. Installer Jupyter og datapakkene

Python kommer med pakkehåndtereren **pip**. Den laster ned og installerer
tilleggspakker fra Python Package Index (PyPI). Vi bruker formen
`python -m pip` fordi den gjør det tydelig hvilken Python-installasjon pakken
tilhører.

Først kontrollerer vi at pip er tilgjengelig:

:::::{tab-set}
::::{tab-item} Windows
:sync: windows
:selected: true

```powershell
py -m pip --version
```
::::

::::{tab-item} macOS
:sync: macos

```bash
python3 -m pip --version
```
::::
:::::

Installer så JupyterLab, det klassiske Notebook-grensesnittet og pakkene vi
bruker til data og figurer:

:::::{tab-set}
::::{tab-item} Windows
:sync: windows
:selected: true

```powershell
py -m pip install --upgrade pip
py -m pip install jupyterlab notebook pandas matplotlib numpy
```
::::

::::{tab-item} macOS
:sync: macos

```bash
python3 -m pip install --upgrade pip
python3 -m pip install jupyterlab notebook pandas matplotlib numpy
```
::::
:::::

Dette kan ta noen minutter og produsere mye tekst. Vent til ledeteksten kommer
tilbake. Rød tekst betyr ikke alltid at installasjonen har feilet, men den siste
linjen bør ikke inneholde `ERROR`.

Pakkene har ulike oppgaver:

| Pakke | Hva bruker vi den til? |
| --- | --- |
| `jupyterlab` | arbeidsflaten der vi åpner mapper og notebooks |
| `notebook` | støtte for Jupyter Notebook-formatet |
| `pandas` | tabeller, datavask og dataanalyse |
| `matplotlib` | figurer og visualisering |
| `numpy` | tallberegninger som pandas bygger på |

Du kan kontrollere at datapakkene kan importeres:

:::::{tab-set}
::::{tab-item} Windows
:sync: windows
:selected: true

```powershell
py -c "import pandas, matplotlib, numpy; print('Alt er klart!')"
```
::::

::::{tab-item} macOS
:sync: macos

```bash
python3 -c "import pandas, matplotlib, numpy; print('Alt er klart!')"
```
::::
:::::

Hvis du ser `Alt er klart!`, virker installasjonen. Se også
[Jupyters offisielle installasjonsside](https://jupyter.org/install) og
[pip-dokumentasjonen](https://pip.pypa.io/en/stable/user_guide/).

## 4. Installer Git

Git er et verktøy for versjonskontroll. Det kan lagre historikken til et
prosjekt og hente prosjekter fra tjenester som GitHub. I dag bruker vi
`git --version` til å kontrollere installasjonen og `git clone` til å lage en
lokal kopi av et prosjekt.

:::::{tab-set}
::::{tab-item} Windows
:sync: windows
:selected: true

Installer Git med Windows Package Manager:

```powershell
winget install --id Git.Git -e --source winget
```

Godta eventuelle spørsmål fra installasjonsprogrammet. Lukk deretter PowerShell,
åpne det på nytt og kontroller installasjonen:

```powershell
git --version
```

Hvis `winget` ikke finnes på maskinen, bruker du installasjonsfilen fra
[git-scm.com](https://git-scm.com/install/windows) og beholder standardvalgene.

:::{figure} ../../../images/winget-git.png
:alt: Git installeres fra PowerShell med Windows Package Manager.
:width: 90%

`winget` laster ned og installerer Git for Windows.
:::
::::

::::{tab-item} macOS
:sync: macos

Kontroller først om Git er installert:

```bash
git --version
```

Hvis Git mangler, åpner macOS en dialogboks for å installere Apples Command Line
Tools. Velg **Installer** og vent til installasjonen er ferdig.

:::{figure} ../../../images/xcode-git.png
:alt: macOS spør om Apples Command Line Tools skal installeres.
:width: 80%

Dialogboksen som vises når Git trenger Command Line Tools.
:::

Kjør deretter samme kommando på nytt:

```bash
git --version
```

Nå skal kommandoen vise et versjonsnummer. Hvis dialogboksen ikke åpnes og Git
fortsatt mangler, kan du starte installasjonen eksplisitt:

```bash
xcode-select --install
```

Dette er en av installasjonsmetodene som anbefales på
[Git-prosjektets offisielle macOS-side](https://git-scm.com/install/mac).
::::
:::::

## 5. Lag kursmappen

Vi samler kursarbeidet i mappen `programmering` under Dokumenter. Kommandoen
`mkdir` er en forkortelse for *make directory* og oppretter en mappe.

:::::{tab-set}
::::{tab-item} Windows
:sync: windows
:selected: true

PowerShell åpner vanligvis i hjemmemappen din. Adressen ser omtrent slik ut:

```text
C:/Users/<brukernavn>
```

Bytt ut `<brukernavn>` med brukernavnet du ser på din egen maskin. Vinkeltegnene
`<` og `>` skal ikke være med. Gå til Dokumenter og lag kursmappen:

```powershell
cd C:/Users/<brukernavn>/Documents
ls
mkdir programmering
cd programmering
pwd
```

Bruk gjerne <kbd>Tab</kbd> til å fullføre `Users`, brukernavnet og `Documents`
mens du skriver. Hvis Dokumenter ligger under OneDrive, finner du riktig mappe
med `ls` og tab-fullføring.

Hvis mappen allerede finnes, kan PowerShell vise en melding om dette. Da bruker
du bare `cd programmering` og fortsetter.

I videoen viser vi også den motsatte veien: åpne ønsket mappe i Filutforsker,
høyreklikk i mappen og velg **Åpne i Terminal**. Da starter terminalen direkte i
den mappen. Bruk `pwd` for å kontrollere hvor du er.

Du kan også åpne mappen du står i fra PowerShell:

```powershell
explorer .
```

Punktum betyr «mappen jeg står i nå». Sammenlign adressen i Filutforsker med
resultatet fra `pwd`.
::::

::::{tab-item} macOS
:sync: macos

```bash
cd ~/Documents
mkdir programmering
cd programmering
pwd
```

Hvis mappen allerede finnes, kan Terminal vise meldingen `File exists`. Da
bruker du bare `cd programmering` og fortsetter.

Åpne den samme mappen i Finder:

```bash
open .
```

Punktum betyr «mappen jeg står i nå». Sammenlign adressen i Finder med resultatet
fra `pwd`.
::::
:::::

## 6. Hent et eksempelprosjekt med Git

Vi bruker [pandas-cookbook](https://github.com/jvns/pandas-cookbook), et åpent
GitHub-prosjekt med eksempler på pandas og Jupyter Notebook. Du skal stå i
`programmering`-mappen før du kjører kommandoen.

Kommandoene er de samme på begge operativsystemene:

```bash
git clone https://github.com/jvns/pandas-cookbook.git
cd pandas-cookbook
ls
```

`git clone` laster ned prosjektet og historikken. `cd pandas-cookbook` går inn i
den nye mappen, og `ls` viser filene som ble hentet.

:::{note}
Dette er et eksisterende eksempelprosjekt, ikke kursmappen der du senere skal
levere arbeid. Noen eksempler kan være laget med eldre versjoner av pandas. I
denne økten bruker vi prosjektet først og fremst til å øve på mapper, filer og
notebooks.
:::

## 7. Start JupyterLab

Pass på at terminalen fortsatt står i `pandas-cookbook`-mappen. Start JupyterLab
med den samme Python-installasjonen som vi brukte til å installere pakkene:

:::::{tab-set}
::::{tab-item} Windows
:sync: windows
:selected: true

```powershell
py -m jupyter lab
```
::::

::::{tab-item} macOS
:sync: macos

```bash
python3 -m jupyter lab
```
::::
:::::

JupyterLab åpnes vanligvis automatisk i nettleseren. Hvis det ikke skjer,
kopierer du adressen som begynner med `http://localhost:` fra terminalen og
limer den inn i nettleseren.

:::{figure} ../../../images/first-jupyterlab.png
:alt: JupyterLab med filområdet, åpne notebooks og knappen for å opprette en ny notebook markert.
:width: 100%

Markeringene viser **filområdet** (1), **åpne notebooks** som faner i
arbeidsområdet (2), og **plussknappen** som åpner Launcher (3).
:::

Prøv dette:

1. Finn en fil som ender på `.ipynb` i filområdet til venstre.
2. Dobbeltklikk filen for å åpne den.
3. Legg merke til at dokumentet består av tekstceller og kodeceller.
4. Ikke bekymre deg dersom du ikke forstår koden ennå.

### Stopp JupyterLab

JupyterLab kjører så lenge terminalprosessen kjører. Når du er ferdig:

1. lagre eventuelle filer
2. gå tilbake til terminalen
3. trykk <kbd>Ctrl</kbd> + <kbd>C</kbd>
4. svar `y` og trykk <kbd>Enter</kbd> hvis du blir spurt

Du lukker ikke nødvendigvis JupyterLab ved bare å lukke nettleserfanen.

## Hvis noe ikke virker

::::{dropdown} `python` eller `py` finnes ikke på Windows
Lukk PowerShell og åpne det på nytt. Prøv først:

```powershell
py --version
```

Hvis dette heller ikke virker, søk etter **Manage app execution aliases** i
Windows-innstillingene og kontroller at Python-aliasene er slått på. Se
[Pythons feilsøkingsside for Windows](https://docs.python.org/3/using/windows.html#troubleshooting).
::::

::::{dropdown} `python3` peker på feil Python på macOS
Kontroller hvor kommandoen peker:

```bash
which python3
python3 --version
```

Etter standardinstallasjonen fra python.org skal den normalt finnes via
`/usr/local/bin/` og peke videre til Python-rammeverket. Lukk Terminal og åpne
det på nytt før du ber om hjelp. Ikke slett Python-versjonen som macOS selv
bruker.
::::

::::{dropdown} En pip-installasjon ender med `Permission denied`
Ikke bruk `sudo pip`. Be først om hjelp, slik at vi kan kontrollere at du bruker
Python-installasjonen fra python.org og ikke systemets Python. Ta vare på hele
feilmeldingen.
::::

::::{dropdown} `git` gjenkjennes ikke etter installasjon
Lukk terminalprogrammet helt og åpne det på nytt. Kjør så:

```bash
git --version
```

Hvis kommandoen fortsatt ikke virker, vis feilmeldingen til en faglærer.
::::

::::{dropdown} JupyterLab åpner ikke nettleseren
Se etter en adresse som begynner med `http://localhost:` i terminalen. Kopier
hele adressen, inkludert eventuell tekst etter `?token=`, og lim den inn i
nettleseren. Ikke del token-adressen med andre.
::::

## Sjekkliste før du går videre

Du er klar når du kan krysse av for alt dette:

- [ ] `python --version` på Windows eller `python3 --version` på macOS viser en
  Python 3-versjon
- [ ] pip er tilgjengelig
- [ ] `pandas`, `matplotlib` og `numpy` kan importeres
- [ ] `git --version` viser et versjonsnummer
- [ ] mappen `Dokumenter/programmering/pandas-cookbook` finnes
- [ ] JupyterLab starter og viser filene i prosjektet
- [ ] du vet hvordan JupyterLab stoppes fra terminalen

:::{admonition} Ta vare på feilmeldingen
:class: tip
Når du ber om hjelp, kopier hele kommandoen og hele feilmeldingen. Et
skjermbilde som viser både kommandoen og de siste linjene i terminalen er ofte
mer nyttig enn å si «det virker ikke».
:::
