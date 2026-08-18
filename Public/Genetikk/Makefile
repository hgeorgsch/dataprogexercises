all: ipynb
ipynb: Genetikk.ipynb

J=jupytext --execute -w --to ipynb

%.ipynb: %.md
	$J "$<"
