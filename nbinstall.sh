#!/bin/sh

D="iira6001/notebooks/"
T=$1

for i in $T/*.md 
do
   jupytext --to notebook --execute "$i" 
done
cd $R

cp $T/*.csv $D
cp $T/*.txt $D
cp $T/*.json $D
cp $T/*.ipynb $D
cp $T/*.jpg $D
cp $T/*.svg $D
cp $T/*.png $D
