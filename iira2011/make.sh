#!/bin/bash
# This is to build the Jupyter Book, including generating notebook files
# from markdown.
#
# Also requires:
# cd .. ; sh mkpynb.sh


if test x$1 = x
then

   jupyter-book clean .
   jupyter-book build .
   rsync -rv --exclude=reports --delete _build/html/ login.ansatt.ntnu.no:/home/groupswww/iirevu/iira2011staging/
else
   rsync -rv --exclude=reports --delete _build/html/ login.ansatt.ntnu.no:/home/groupswww/iirevu/iira2011/
fi
