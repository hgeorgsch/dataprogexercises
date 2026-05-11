
S=ontology.svg infosecorg.svg
svg: $S
pdf: ontology.pdf

I=../../dataprog-obsidian/Slides/slidefig/

install: $S
	cp $^ $I

%.svg: %.pdf
	pdf2svg $< $@
%.pdf: %.tex
	pdflatex $< 
