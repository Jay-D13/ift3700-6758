# Demo 2: acquiring, exploring, and analyzing NHL data

[Version française](README.md)

This demo uses data from one Montréal–Carolina game to learn how to acquire and clean data, explore it visually, then use an LLM to help write code and analyze a table.

## Notebooks

| Notebook | What you learn and do | English | Français |
|---|---|---|---|
| **01 — Acquisition and cleaning** | Understand an API request, download and save a game's JSON, then turn it into a pandas table. Keep shots and goals, check identifiers and missing values, and export a CSV. | [Open](notebooks/en/01_data_acquisition_and_cleaning.ipynb) | [Ouvrir](notebooks/fr/01_data_acquisition_and_cleaning.ipynb) |
| **02 — Exploration and visualization** | Inspect raw events and their rink positions with widgets. Replay shots and goals, compare cumulative shots with Plotly, and export an interactive chart as HTML. | [Open](notebooks/en/02_data_exploration_and_visualization.ipynb) | [Ouvrir](notebooks/fr/02_data_exploration_and_visualization.ipynb) |
| **04 — LLM and RAG** | Understand how RAG supplies documentation passages to an LLM. Search the NHL API documentation with MiniLM and FAISS, then ask Qwen for an acquisition function and check its code and caching behavior. | [Open](notebooks/en/04_llm_and_rag.ipynb) | [Ouvrir](notebooks/fr/04_llm_and_rag.ipynb) |
| **05 — PandasAI** | Query a table in natural language with PandasAI and Qwen to produce a number, a table, and a chart. Inspect the generated code and compare the results with pandas calculations. | [Open](notebooks/en/05_pandasai.ipynb) | [Ouvrir](notebooks/fr/05_pandasai.ipynb) |

Start with notebook **01**, then follow the order in the table. Each notebook contains its own setup and execution instructions; see the [shared course setup](../README.md) for the local environment.

## Recommended hardware for notebooks 04 and 05

For these **Qwen2.5-1.5B-Instruct** notebooks, we recommend **Google Colab with a T4 GPU** if you do not have a suitable NVIDIA GPU or an Apple M-series Mac. Follow the notebook's Colab instructions.

For local use, aim for **8 GB of NVIDIA GPU VRAM** or **16 GB of unified memory on an M-series Mac**. These are practical targets, not strict minimums: requirements vary with prompt length and quantization. [Qwen's published benchmarks](https://qwen.readthedocs.io/en/v2.5/benchmark/speed_benchmark.html) report roughly 3–6 GB for the model in BF16 depending on context length; allow additional memory for the rest of the notebook. CPU execution is possible but slower.


<sub>Prepared by Jaydan Aladr and Pablo Boitel</sub>