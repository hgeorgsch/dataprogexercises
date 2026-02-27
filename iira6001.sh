#!/bin/sh
# This is to build the Jupyter Book for IIRA6001, including generating notebook files
# from markdown.

TS="dataprog-obsidian/notebook/ exercises/Genetikk/ exercises/Jordskjelv/"
DS="iira6001/notebooks/"
R=`pwd`

for T in $TS
do
   sh nbinstall.sh $T
done


( cd iira6001 ; sh make.sh )

