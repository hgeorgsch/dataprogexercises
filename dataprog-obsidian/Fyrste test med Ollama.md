---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: pythonenv
  language: python
  name: pythonenv
---

```{code-cell} ipython3
%pip install jupyter_ai_magics
%pip install langchain-ollama
%load_ext jupyter_ai_magics
```

```{code-cell} ipython3
%%ai ollama:deepseek-coder-v2
Write a poem about a beginner programming in python
```

```{code-cell} ipython3
%ai list
```

```{code-cell} ipython3
%%ai ollama:deepseek-coder-v2
Please explain the code below
--
def hw():
    print("Hello World")
```

```{code-cell} ipython3

```
