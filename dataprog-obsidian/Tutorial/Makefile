%.ipynb: %.md
	jupytext --to notebook --execute "$<"

_build:
	jupyter-book build .

clean:
	rm -f *.ipynb
	rm -rf _build
