#!/bin/bash
# This is to build the Jupyter Book, including generating notebook files
# from markdown.

TS="dataprog-obsidian/notebook/ exercises/Genetikk/ exercises/Jordskjelv/"
D=iira2001/notebooks/
R=`pwd`

E=iira2001/exercises/
mkdir -p $E
cp dataprog-obsidian/Exercises/* $E

for T in $TS
do
  cd $T
  ls 

  for i in *.md ; do jupytext --to notebook "$i" ; done
  cd $R

  cp $T/*.csv $D
  cp $T/*.txt $D
  cp $T/*.json $D
  cp $T/*.ipynb $D
  cp $T/*.jpg $D
done


