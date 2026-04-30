ipynb: kontantstraum.ipynb boligpris.ipynb
all: pdf ipynb
pdf: kontantstraum.pdf boligpris.pdf

%.pdf: %.ipynb
	python -m nbconvert --to pdf $<
%.ipynb: %.md
	python -m jupytext --to ipynb --execute $<
