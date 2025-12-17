
args="{7}{49}{0.02} {49}{19}{0.052} {19}{52}{0.0192} {52}{40}{0.025} {40}{37}{0.0270} {37}{16}{0.0625} {16}{31}{0.0322} {31}{55}{0.0181} {55}{61}{0.0163}"

c=0

for i in $args
do
   c=`expr $c + 1`
   sed -e "s/%ARG%/$i/" prngx.tex > prng$c.tex
   pdflatex prng$c
   pdf2svg prng$c.pdf prng$c.svg
done
