#!/bin/bash
# This is to build the Jupyter Book, including generating notebook files
# from markdown.
#
# Also requires:
# cd .. ; sh mkpynb.sh

jupyter-book build .

rsync -av --delete _build/html/ hasc@login.ansatt.ntnu.no:/home/groupswww/iirevu/iira2001/
