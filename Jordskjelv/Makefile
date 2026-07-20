all: Jordskjelv.ipynb

J=jupytext --execute -w --to ipynb

%.ipynb: %.md
	$J "$<"
