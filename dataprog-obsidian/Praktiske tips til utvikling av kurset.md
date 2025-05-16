---
tags:
  - development
---

+ Jupyter to run git  [[/assets/hent-innhold.ipynb]] (teke frå 2024)

+ [[Fyrste test med Ollama]]

## Jupytext og Jupyter Books

+ [[jupytext]] to manage conversion between Jupyter notebook and markdown
+ Jupyter Books to make web pages
	+ video with Iframes
		+ https://teachbooks.io/manual/external/sphinx-iframes/README.html


## Virtual Environment

+ jupyter lab arvar ikkje det virtuelle køyremiljøtet frå foreldreprosessen.  I staden må ein definera ein ikernel.
+ Dette krev av det virtuelle køyremiljøet har eins namn, sidan det vert lagra i notebook/md:myst-filene.
+ I kurset kaller me kjernen for `dataprog`
+ Installera `ipykernel`  https://janakiev.com/blog/jupyter-virtual-envs/
+ EIn mogleg installasjonssekvens er denne:

```
pip install --user ipykernel
python -m venv dataprog
. dataprog/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=dataprog
```

+ Ein treng ikkje ha det virtuelle køyremiljøet i arbeidskatalogen.  Det kan liggja kvar som helst.