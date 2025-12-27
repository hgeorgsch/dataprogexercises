#! /bib/sh
# (C) 2025: Hans Georg Schaathun <georg@schaathun.net>
# Create figures for the PRNG talk «Slumptalsgenerator»

args="{13}{91}{0.94} {91}{55}{0.57} {55}{94}{0.97} {94}{76}{0.78} {76}{47}{0.48} {47}{38}{0.39} {38}{72}{0.74} {72}{19}{0.20} "

c=0

for i in $args
do
   c=`expr $c + 1`
   sed -e "s/%ARG%/$i/" prngx.tex > prng$c.tex
   pdflatex prng$c
   pdf2svg prng$c.pdf prng$c.svg
done

pdflatex prng.tex
pdf2svg prng.pdf prng.svg

pdflatex cycle.tex
pdf2svg cycle.pdf cycle.svg

cp cycle.svg prng*.svg ../dataprog-obsidian/Slides/slidefig/
