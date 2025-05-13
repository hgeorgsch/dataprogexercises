#!/bin/sh
# This is to build the Jupyter Book, including generating notebook files
# from markdown.

( cd notebook ; for i in *.md ; do jupytext --to notebook "$i" ; done )
jupyter-book build .

rsync -av _build/html/ hasc@login.ansatt.ntnu.no:/home/groupswww/iirevu/evu2025/
