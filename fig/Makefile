
svg: table1.svg table2.svg join.svg joins.svg
pdf: table1.pdf table2.pdf join.pdf joins.pdf

%.svg: %.pdf
	pdf2svg $< $@
%.pdf: %.tex
	pdflatex $< 
