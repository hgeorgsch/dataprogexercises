all: 0501oo-print.pdf 0201sim-print.pdf 0202slump-print.pdf 0203struct-print.pdf
%-main.tex: %.md
	pandoc -o $@ $< 
%-print.tex: %-main.tex
	cat template-head.tex $< template-tail.tex > $@
%-print.pdf: %-print.tex
	pdflatex $<
