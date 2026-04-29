ipynb: kontantstraum.ipynb
all: pdf ipynb
pdf: kontantstraum.pdf

%.pdf: %.ipynb
	python -m nbconvert --to pdf $<
%.ipynb: %.md
	python -m jupytext --to ipynb --execute $<
