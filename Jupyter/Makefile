all: ipynb
ipynb: jupyter01.ipynb sim01.ipynb csv01.ipynb

J=jupytext --execute -w --to ipynb

%.ipynb: %.md
	$J "$<"
