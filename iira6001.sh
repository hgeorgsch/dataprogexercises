#!/bin/sh
# This is to build the Jupyter Book for IIRA6001, including generating notebook files
# from markdown.

TS="dataprog-obsidian/notebook/ exercises/Genetikk/ exercises/Jordskjelv/"
DS="iira6001/notebooks/"
R=`pwd`

ES="iira6001/exercises/"
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
    cp $T/*.png $D
  done     
done


( cd iira6001 ; sh make.sh )

