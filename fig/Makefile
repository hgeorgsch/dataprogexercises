
svg: table1.svg table2.svg join.svg joins.svg
%.svg: %.pdf
	pdf2svg $< $@
%.pdf: %.tex
	pdflatex $< 
