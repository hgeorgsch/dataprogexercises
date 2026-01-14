%.tex: %.md
	pandoc -o $@ $< 
%.pdf: %.tex
	pdflatex $<
