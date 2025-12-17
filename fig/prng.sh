
args="{13}{91}{0.0110} {91}{55}{0.0182} {55}{94}{0.0106} {94}{76}{0.0132} {76}{47}{0.0213} {47}{38}{0.0263} {38}{72}{0.139} {72}{19}{0.0526} {19}{36}{0.0277} {36}{58}{0.0172}"


c=0

for i in $args
do
   c=`expr $c + 1`
   sed -e "s/%ARG%/$i/" prngx.tex > prng$c.tex
   pdflatex prng$c
   pdf2svg prng$c.pdf prng$c.svg
done
