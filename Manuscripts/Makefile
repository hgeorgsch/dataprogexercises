take0312: 0702model-print.pdf 0703eval-print.pdf 0801automatisering-print.pdf 0802jupytext-print.pdf 0803git-print.pdf
new: 0401flyttal-print.pdf 0402pivot-print.pdf 0403frekvens-print.pdf
all: 0501oo-print.pdf 0201sim-print.pdf 0202slump-print.pdf 0203struct-print.pdf
%-main.tex: %.md
	pandoc -o $@ $< 
%-print.tex: %-main.tex
	cat template-head.tex $< template-tail.tex > $@
%-print.pdf: %-print.tex
	pdflatex $<
