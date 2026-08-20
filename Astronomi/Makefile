all: ipynb

ipynb: Astronomi.ipynb 

J=jupytext --execute -w --to ipynb

%.ipynb: %.md
	$J "$<"
