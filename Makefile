# This is a little hacked up, but serves to remember the most
# critical syntax for juptext and jupyter-books

%.ipynb: %.md
	jupytext --to notebook --execute "$<"
_build: intro.md
_build: 
	sh make.sh

clean:
	rm -f notebook/*.ipynb
	rm -rf _build
