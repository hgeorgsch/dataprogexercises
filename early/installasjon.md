# Installasjon python

Dere trenger å installere anaconda og git. 
Anaconda er en distribusjon av python som kommer ferdiginstallert med en haug pakker og biblioteker vi har bruk for. Deriblant utviklermiljøet **jupyterlab** og **jupyter notebook**

*git* er et versjonskontrollsystem som vi sannsynligvis bruker for å "dele" ressurser


## Anaconda

1. Last ned Anaconda [her](https://www.anaconda.com/download/success)
   - Velg riktig versjon, mac eller windows, og intel eller m-prossessor for mac.
   - Du kan sjekke om du har intel eller apple-silicon prosessor slik som på bildet [under](fig-sjekk)

:::{figure} sjekk-prosessor.png
:name: fig-sjekk
Trykk på eplet oppe til venstre og «about this mac» eller «Om denne maskinen»
:::

2. Følg installasjonsinstruksen og godta standardinstillingene
3. Start Anaconda navigator - første gang vil du bli spurt om å oppdatere, gjør dette.
   - Du vil kanskje også bli spurt om å lage eller logge på en konto -- dette er ikke nødvendig

:::{figure} oppdater.png
:name: fig-oppdater
Trykk ja til å oppdatere - vinduet om innlogging kan dere krysse ut
:::

:::{note}
- Vi skal lære å bruke *programmeringsspråket* python.
- Man kan programmere i ulike *programmeringsmiljø* slik som `vim`, vs-code eller pycharm.
- Vi skal i all hovedsak bruke **jupyterlab**
- Vi kan få installert det aller meste vi trenge gjennom anaconda
:::


## Git

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




