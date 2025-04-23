---
tags:
  - development
---

I have started [[2025-04-23]] to set up tutorials written in markdown and converted to Jupyter notebook.  These are found in the directory `dataprog-obsidian/Tutorial`.

To set up a new markdown file for use in Jupyter, we need these two lines
```sh
jupytext --set-kernel - notebook.md             # create a YAML header with kernel metadata matching the current python executable
jupytext --set-formats md:myst notebook.md      # create a YAML header with an explicit jupytext format
```

Once this is done, the jupyter notebook file can be created with make:
```sh
make notebook.ipynb
```

