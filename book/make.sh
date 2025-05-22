#!/bin/bash
# This is to build the Jupyter Book, including generating notebook files
# from markdown.

T=../dataprog-obsidian/Tutorial/
N=$T/notebook
ls $T
ls $N

( cd $N ; for i in *.md ; do jupytext --to notebook "$i" ; done )

mkdir -p notebook

cp $N/*.csv notebook 
cp $N/*.json notebook 
cp $N/*.ipynb notebook 
cp $N/*.jpg notebook 

cp $T/*.md .


jupyter-book build .

rsync -av _build/html/ hasc@login.ansatt.ntnu.no:/home/groupswww/iirevu/evu2025/
