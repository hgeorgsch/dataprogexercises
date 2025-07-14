---
tags:
  - development
---

I have started [[2025-04-23]] to set up tutorials written in markdown and converted to Jupyter notebook.  These are found in the directory `dataprog-obsidian/Tutorial`. 

First [jupytext](https://github.com/mwouts/jupytext) must be installed using  pip. It is included in `requirements.txt` in the repo.

To set up a new markdown file for use in Jupyter, we need these two lines
```sh
jupytext --set-kernel - notebook.md             # create a YAML header with kernel metadata matching the current python executable
jupytext --set-formats md:myst notebook.md      # create a YAML header with an explicit jupytext format
```

Once this is done, the jupyter notebook file can be created with make:
```sh
make notebook.ipynb
```


It is also possible to convert the other way, or to use the py:percent format to convert to and from python scripts. It is even possible to pair files and have Jupyter notebook do live conversion.  See the [full documentation](https://jupytext.readthedocs.io/en/latest/index.html).

+ I have tried paired files, but it seems to strip metadata used in markdown but not in Jupyter.

