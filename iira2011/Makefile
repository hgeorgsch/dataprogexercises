all: nb01

I=../dataprog-obsidian/notebook
nb01: .force nb01/control-empty.ipynb nb01/control.ipynb
	mkdir -p $@
	jupytext -o $@/fyrstedok.ipynb $I/"Fyrste dokument i Jupyter Lab.md"
	jupytext -o $@/simkontant.ipynb $I/"Simulering av kontantstraum.md"

nb01/%.ipynb: $I/%.md
	jupytext -o $@ $<


.force:
