%.ipynb: %.md
	jupytext --to notebook --execute "$<"
_build: intro.md
_build: 
	sh make.sh

clean:
	rm -f notebook/*.ipynb
	rm -rf _build
