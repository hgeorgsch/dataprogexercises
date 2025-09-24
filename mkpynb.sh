#!/bin/bash
# This is to build the Jupyter Book, including generating notebook files
# from markdown.

T=dataprog-obsidian/notebook/
$D=iir2001/notebooks/

cd $T
ls $T

for i in *.md ; do jupytext --to notebook "$i" ; done

cp $T/*.csv $N
cp $T/*.txt $N 
cp $T/*.json $N
cp $T/*.ipynb $N
cp $T/*.jpg $N

