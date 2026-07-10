I=kontantstraum.ipynb boligpris.ipynb
ipynb: $I
all: pdf ipynb
pdf: kontantstraum.pdf boligpris.pdf

%.pdf: %.ipynb
	python -m nbconvert --to pdf $<
%.ipynb: %.md
	python -m jupytext --to ipynb --execute $<

install: $I
	cp $I ../iira6001/Mappedemo/
