#!/bin/bash

find . -name "*.ipynb" -not -path "*/.ipynb_checkpoints/*" \
  -exec bash -lc 'f="{}"; jupytext --to myst "$f"' \;
