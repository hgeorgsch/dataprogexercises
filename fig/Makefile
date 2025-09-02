
svg: table1.svg table2.svg
%.svg: %.pdf
	pdf2svg $< $@
%.pdf: %.tex
	pdflatex $< 
