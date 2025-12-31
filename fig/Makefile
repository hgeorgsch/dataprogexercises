
svg: table1.svg table2.svg join.svg joins.svg sampling.svg object.svg
pdf: table1.pdf table2.pdf join.pdf joins.pdf sampling.pdf object.pdf

I=../dataprog-obsidian/Slides/slidefig/

oo: object.svg inheritance.svg
	cp $^ $I

%.svg: %.pdf
	pdf2svg $< $@
%.pdf: %.tex
	pdflatex $< 
