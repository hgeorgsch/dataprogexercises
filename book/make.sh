#!/bin/bash
# This is to build the Jupyter Book, including generating notebook files
# from markdown.

T=../dataprog-obsidian/Tutorial/
NS="notebook Genetikk Jordskjelv"
ls $T

for N1 in $NS
do
   N=${T}/${N1}
   ( cd $N ; for i in *.md ; do jupytext --to notebook "$i" ; done )
   mkdir -p $N1

   cp $N/*.csv $N1 
   cp $N/*.json $N1 
   cp $N/*.ipynb $N1 
   cp $N/*.jpg $N1 
done


cp $T/*.md .


jupyter-book build .

rsync -av _build/html/ hasc@login.ansatt.ntnu.no:/home/groupswww/iirevu/evu2025/
