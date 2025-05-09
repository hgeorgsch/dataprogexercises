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
tags:
  - jupyter
  - ai/llm
---

Me kan setja opp jupyter lab med ein stor språkmodell (AI-LLM). For å få tilgang til KI-grensesnittet, installerer me jupyter-ai:
```sh
pip install jupyter-ai
```

Jupyter kan bruka ei rekkje ulike KI-platformar og språkmodellar. Dei fleste krev eit abonnement. Her skal me setja opp Ollama, som er ein virtualiseringsplatform for å køyra ulike språkmodellar lokalt. Me kan truleg få både raskare og betre svar frå KI med betalte modellar, men i tillegg til å vera gratis, gjev Ollama betre persondata. Ingen andre frå tilgang til dei dataa som me deler med KI-modellen.

Referanse: [Using jupyter-ai with ollama](https://medium.com/@kamelyoussef1996/using-jupyter-ai-with-ollama-free-local-llms-d67f62b66fcc)

# Oppsett av Ollama i docker



Eg sette opp Ollama i docker, for å slippa å stola like mykje på installasjonsscriptet til Ollama. Det krev at du har [docker installert](https://docs.docker.com/engine/install/). Me docker installert, startar me ollama med

```sh
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

No køyrer Ollama heilt utan modellar.  For å kunna bruka KI, må me lasta ein modell, t.d. llama3:
```
docker exec -it ollama ollama pull llama3
```

Me kan starta ein enkel *chatbot* for å testa modellen, slik:

```
docker exec -it ollama ollama run llama3
```

Jupyter treng tilgang til modellen over eit *WebAPI*.  Me kan testa at det verkar, slik:

```
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt":"Here is a story about llamas eating grass"
 }'
```

Det er ikkje so lett å vurdera om svaret er meiningsfullt, men om du ikkje får ei feilmelding, er det sikkert greit. Merk deg URLen i kommandoen over.  Me treng han for å konfigurera Jupyter-AI.

Til programmering kan det løna seg å sjå etter ein modell som er særleg trent for koding, t.d. deepseek-coder-v2, som er tilgjengeleg i Ollama:
```
docker exec -it ollama ollama pull  deepseek-coder-v2
```

Referanse: [Ollama in docker](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)

# KI *inline* i Jupyter

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


# Ollama utan docker


```
ollama pull   [model name]
ollama rm   [model name]
```

