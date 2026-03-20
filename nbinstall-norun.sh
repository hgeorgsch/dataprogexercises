#!/bin/sh

D="iira6001/norun/"

for T 
do

  for i in $T/*.md 
  do
    jupytext --from md_myst --to notebook "$i" 
  done

  cp $T/*.csv $D
  cp $T/*.txt $D
  cp $T/*.json $D
  cp $T/*.ipynb $D
  cp $T/*.jpg $D
  cp $T/*.svg $D
  cp $T/*.png $D
done
