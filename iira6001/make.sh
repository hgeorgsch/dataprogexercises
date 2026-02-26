#!/bin/bash
# This is to build the Jupyter Book, including generating notebook files
# from markdown.
#
# Also requires:
# cd .. ; sh mkpynb.sh


rm -rf _build

rm -f notebooks/forelesing*
rm -f notebooks/forelesning*

jupyter-book build .


#rsync -av --delete _build/html/ hasc@login.ansatt.ntnu.no:/home/groupswww/iirevu/iira6001/
if test x$1 = x-i
then
   rsync -rv --delete _build/html/ login.ansatt.ntnu.no:/home/groupswww/iirevu/iira6001/
fi
