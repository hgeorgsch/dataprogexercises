
svg: table1.svg table2.svg join.svg joins.svg sampling.svg
pdf: table1.pdf table2.pdf join.pdf joins.pdf sampling.pdf

%.svg: %.pdf
	pdf2svg $< $@
%.pdf: %.tex
	pdflatex $< 
