
ROOT := $(abspath .)

all:
	for nb in $(shell find . -name '*.ipynb'); do \
		out=$${nb%.ipynb}.md; \
		echo "Executing $$nb → $$out"; \
		PROJECT_ROOT=$(ROOT) jupytext --to markdown --execute -o "$$out" "$$nb"; \
	done
