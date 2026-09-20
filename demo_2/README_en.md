# Demo 2: explore an NHL game

This session covers acquisition, cleaning, exploration and visualisation using events from one NHL game.

- [French notebook](notebooks/fr/00_session.ipynb)
- [English notebook](notebooks/en/00_session.ipynb)

## Google Colab

1. Open [Google Colab](https://colab.research.google.com/) and upload the chosen notebook.
2. Select a CPU runtime, then **Run all**.
3. If Colab requests a restart after the `uv` installation, restart the session and run all cells again.

## Local execution

From the repository root:

```sh
git pull --ff-only
uv sync
uv run jupyter lab
```

Select the `.venv` kernel, then use **Restart Kernel and Run All**.

## Session outline

The session starts with an API request and a JSON file, builds a pandas shot table, lets students inspect events on a rink, then creates a replay and a cumulative-shot chart.

The first run downloads game `2025030311` into `data/raw`. Later runs reuse this cache. One game illustrates the method but cannot establish conclusions about a team or an entire season.
