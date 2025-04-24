
( cd notebook ; for i in *.md ; do jupytext --to notebook "$i" ; done )
jupyter-book build .
