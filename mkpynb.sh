#!/bin/bash
# This is to build the Jupyter Book, including generating notebook files
# from markdown.

TS="dataprog-obsidian/notebook/ exercises/Genetikk/ exercises/Jordskjelv/ work/"
DS="iira2001/notebooks/ iira6001/notebooks/"
R=`pwd`

ES="iira2001/exercises/ iira6001/exercises/"
for E in $ES
do
    mkdir -p $E
    cp dataprog-obsidian/Exercises/* $E
done

for T in $TS
do
  cd $T
  ls 

  for i in *.md ; do jupytext --to notebook "$i" ; done
  cd $R

  for D in $DS
  do
    cp $T/*.csv $D
    cp $T/*.txt $D
    cp $T/*.json $D
    cp $T/*.ipynb $D
    cp $T/*.jpg $D
    cp $T/*.svg $D
  done     
done


