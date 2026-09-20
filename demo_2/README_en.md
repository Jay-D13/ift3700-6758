# Demo 2: from the NHL API to a pandas table

This first part introduces the **data acquisition and cleaning** objective of project milestone 1. It guides you through using the API with a single game: Montréal–Carolina, May 21, 2026 (`2025030311`) (🥲).

## Getting started

Follow the [shared setup instructions](../README.md): from the root of `ift3700-6758`, run `uv sync`, then select the kernel from the shared `.venv`.

Open the [guided notebook](notebooks/en/01_data_acquisition_and_cleaning.ipynb). It uses pandas and requests, which are declared in the shared environment. You should have some basic familiarity with Jupyter cells, lists, and dictionaries; no API experience is required.

## Session

| Part | Activity |
|---|---|
| A | Understand clients, servers, GET requests, URLs, and JSON responses |
| B | Download one game, check the response, and save the JSON |
| C | Reload the file and explore dictionaries and lists |
| D | Flatten events with `pd.json_normalize` and inspect the table |
| E | Keep shots and goals, name columns, and check identifiers and missing values |
| F | Export a CSV and explain the pipeline stages |

Two short exercises include expandable answers. The ending distinguishes the completed steps from the remaining project requirements: multiple seasons, player names, empty-net information, and strength situations.

## Before the session

Run the notebook once with an internet connection, then restart the kernel and run all cells again. The second run should reuse the local file. The `data/raw` and `data/processed` folders are created relative to the kernel’s working directory; the notebook displays their full paths. They are ignored by Git.

Keep the downloaded JSON so you can distribute it separately if the API is unavailable in class. Students can place it at the displayed path, then continue with part C. No data files are included in the repository.

During preparation, the API returned **339 events**, including **42 `shot-on-goal` and 8 `goal` events**, giving **50 retained rows**. These numbers are checkpoints for this game, not constants to enforce for every game; the provider may correct its data.
