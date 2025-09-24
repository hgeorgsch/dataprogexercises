#!/bin/bash
# This is to build the Jupyter Book, including generating notebook files
# from markdown.

T=dataprog-obsidian/notebook/
D=iira2001/notebooks/
R=`pwd`

cd $T
ls 

for i in *.md ; do jupytext --to notebook "$i" ; done

cd $R

cp $T/*.csv $D
cp $T/*.txt $D
cp $T/*.json $D
cp $T/*.ipynb $D
cp $T/*.jpg $D

