Hans-Georg: Desse filene er duplikat av filer som ligg andre plassar i ipynb-format.

Jonas: Disse filene er ikke lenger bare duplikater av filer som ligger andre steder i `.ipynb`-format.

Mappen `notebook-norun/` inneholder MyST-markdownfiler (`.md`) som er versjonskontrollert i Git. 
Til disse finnes det også lokale `.ipynb`-filer som **ikke** skal versjonskontrolleres, men som kan inneholde ferdig kjørte outputs (grafer, tabeller, DataFrame-visninger osv.).

Poenget med denne løsningen er:

- å ha ryddig versjonskontroll i Git ved å lagre notebook-innhold som Markdown
- å kunne publisere notebooks med ferdige outputs
- å unngå at enkelte notebooks kjøres på nytt under bygging av Jupyter Book
- å kunne ferdigstille undervisningseksempler som inneholder API-nøkler, `client_secret` osv., og deretter rotere/slette disse etter publisering

## Viktig om Jupytext

MyST-markdown **lagrer ikke outputs i selve `.md`-fila**. Outputs ligger i den tilhørende `.ipynb`-fila.

Når vi synkroniserer med Jupytext, er det derfor viktig å **beholde den kjørte `.ipynb`-fila**, siden det er den som inneholder outputs.

Typisk kommando er:

```bash
jupytext --sync min_notebook.ipynb
```

Ved første ipynb->md
```bash
jupytext --set-formats ipynb,md:myst example.ipynb
```

(README delvis generert av KI)


## NB

For noen ipynb er markdown ikke nok til å rekonstruere ipynb (feks API-nøkler fjernet/rotert). Disse må i så tilfelle deles utenom.
(kopier inn fra iira6001 katalog, feks)

Dette gjelder:
   - spotify-auth
   - chatgpt-api

I andre tilfeller ønsker vi å ikke kjøre notebook fordi det er tidkrevende (store/mange api-spørringer)
