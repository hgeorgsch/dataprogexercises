#!/bin/bash
# This is to build the Jupyter Book, including generating notebook files
# from markdown.
#
# Also requires:
# cd .. ; sh mkpynb.sh


if test x$1 = x
then
    rm -rf _build

    rm -f notebooks/forelesing*
    rm -f notebooks/forelesning*

    jupyter-book build --html .

else
   rsync -rv --delete _build/html/ login.ansatt.ntnu.no:/home/groupswww/iirevu/iira6001/
fi
