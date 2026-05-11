
svg: ontology.svg
pdf: ontology.pdf

I=../../dataprog-obsidian/Slides/slidefig/

install: ontology.svg 
	cp $^ $I

%.svg: %.pdf
	pdf2svg $< $@
%.pdf: %.tex
	pdflatex $< 
