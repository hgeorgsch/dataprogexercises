%.ipynb: %.md
	jupytext --to notebook --execute "$<"
_build: intro.md
nb:
	-jupytext --to notebook --execute notebook/*.md
_build: nb
	jupyter-book build .

clean:
	rm -f *.ipynb
	rm -rf _build
