all: nb01 nb02 nbml norun

N=norun/intro-simulering.ipynb norun/sklearn-demo

norun: .force
	mkdir -p $@
	$(MAKE) $N

I=../dataprog-obsidian/notebook
J=../exercises
K=../dataprog-obsidian/notebook2

nbml: .force nbml/Evaluering.ipynb nbml/SVM.ipynb
	mkdir -p $@
	jupytext -o $@/fld.ipynb $K/"Fisher Linear Discriminant in sklearn.md"


nb02: .force nb02/Arbeidsledige.ipynb nb02/plot1empty.ipynb nb02/plot1.ipynb nb02/ssbfile.ipynb nb02/ssbfile-empty.ipynb
	mkdir -p $@
	jupytext -o $@/Genetikk.ipynb $J/Genetikk/Genetikk.md
	cp $J/Genetikk/*.txt $@
	jupytext -o $@/Jordskjelv.ipynb $J/Jordskjelv/Jordskjelv.md
	cp $J/Jordskjelv/*.txt $@
	cp $J/Jordskjelv/*.jpg $@
	jupytext -o $@/csv01.ipynb $I/"Fyrste datasett med CSV".md
	jupytext -o $@/time.ipynb $I/"Tid og dato".md

nb01: .force nb01/control-empty.ipynb nb01/control.ipynb nb01/Smittespreiing.ipynb nb01/Halveringsmetoden.ipynb
	mkdir -p $@
	jupytext -o $@/fyrstedok.ipynb $I/"Fyrste dokument i Jupyter Lab.md"
	jupytext -o $@/simkontant.ipynb $I/"Simulering av kontantstraum.md"

nb02/%.ipynb: $I/%.md
	jupytext -o $@ $<
nb01/%.ipynb: $I/%.md
	jupytext -o $@ $<
nbml/%.ipynb: $K/%.md
	jupytext -o $@ $<

norun/%: ../iira6001/norun/%
	cp $< $@

.force:
