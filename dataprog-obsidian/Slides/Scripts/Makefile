%-main.tex: %.md
	pandoc -o $@ $< 
%-print.tex: %-main.tex
	cat template-head.tex $< template-head.tex > $@
%-print.pdf: %-print.tex
	pdflatex $<
