Hans-Georg: Desse filene er duplikat av filer som ligg andre plassar i ipynb-format.

Jonas: Disse filene er ikke lenger duplikat av filer som ligger andre plasser i ipynb-format.
For å få kopiert ipynb i fornuftig versjonskontroll OG at de ikke kjøres etter at de er «ferdigstilte» (for sletting/vasking av API-nøkler client_secret nøkler osv) gjøres følgdende:
```bash
jupytext --set-formats md:myst,ipynb --opt sync_outputs=true min_notebook.ipynb
```

myst:markdown er laget for jupyter-notebook med outputs og metadata om kernel, tags som skip-execution osv.
Med --opt sync_outputs=true lagres også genererte grafer/figurer/dataframes i output som b64-tekst.
Det gjør versjonskontroll mer grisete, men betraktelig bedre enn ren ipynb, og lar oss konvertere til ipynb uten kjøring.

Filene kopieres til "norun/" i jupyterbooks i "nbinstall-norun.sh" og i _config.yml er norun gitt som mappe hvor ipynb ikke skal kjøres







