#!/bin/bash
# This is to build the Jupyter Book, including generating notebook files
# from markdown.

NS="notebooks"

for N in $NS
do
   ( cd $N ; for i in *.md ; do jupytext --to notebook "$i" ; done )
done


jupyter-book build .

rsync -av _build/html/ hasc@login.ansatt.ntnu.no:/home/groupswww/iirevu/iira2001/
