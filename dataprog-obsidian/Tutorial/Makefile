%.ipynb: %.md
	jupytext --to notebook --execute "$<"
_build: intro.md
_build:
	-jupytext --to notebook --execute notebook/*.md
	jupyter-book build .

clean:
	rm -f *.ipynb
	rm -rf _build
