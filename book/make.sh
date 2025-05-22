#!/bin/sh
# This is to build the Jupyter Book, including generating notebook files
# from markdown.

T=../dataprog-obdsidian/Tutorial/
N=$T/notebook

( cd $N ; for i in *.md ; do jupytext --to notebook "$i" ; done )

mkdir -p notebook
cp $N/*.{csv,json,ipynb} notebook 

cp $T/*.md .


jupyter-book build .

rsync -av _build/html/ hasc@login.ansatt.ntnu.no:/home/groupswww/iirevu/evu2025/
