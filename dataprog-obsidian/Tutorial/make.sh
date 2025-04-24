#!/bin/sh
# This is to build the Jupyter Book, including generating notebook files
# from markdown.

( cd notebook ; for i in *.md ; do jupytext --to notebook "$i" ; done )
jupyter-book build .
