# Python setup: manual venv, then uv

**Optional standalone exercise.** To run the course notebooks, follow the [shared repository setup](../../README.md): one `uv sync` from `ift3700-6758` is enough. For the exercise below, copy the whole `demo_1` folder somewhere **outside the repository**, keeping its name. Every mention of `demo_1` below refers to that separate copy. The exercise creates and deletes its own `.venv`; it is not the setup procedure for the shared course environment.

**Run every terminal command from `demo_1`, the folder containing `python/` and `notebooks/`.** Open that whole folder in your editor. If your terminal is in `demo_1/python`, run `cd ..` once.

Both phases use `demo_1/.venv`. Scripts stay in `python/`; French notebooks are in `notebooks/fr/` and English notebooks are in `notebooks/en/`.

Before class, install **Python 3** and VS Code's **Python** and **Jupyter** extensions. We'll install uv in step 6. Start with no environment activated.

For a fresh demonstration, use a teaching copy without generated environment/configuration files. If you already have `pyproject.toml` and `uv.lock` and just want to run notebooks, skip to **Returning later**.

## Phase 1: manual setup

### 1. Create the environment

macOS / Linux:

```sh
python3 --version
python3 -m venv .venv
```

Windows PowerShell:

```powershell
py -3 --version
py -3 -m venv .venv
```

The version should be Python 3.x. This creates `.venv` using that Python; it does not activate it.

**What does `-m` mean?** It runs a Python module as a program using the interpreter you selected. Here, `python3 -m venv` runs Python's environment-creation module. Later, `python -m pip` runs pip with the activated environment's Python.

### 2. Activate it

macOS / Linux:

```sh
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Check:

```sh
python -c "import sys; print(sys.executable)"
```

**What does `-c` mean?** It runs the Python code inside the quotes directly, without needing a `.py` file. Here, the code imports `sys` and prints the path of the Python executable running it.

The path should point inside `demo_1/.venv`. Activation applies only to this terminal.

If PowerShell blocks activation, use Command Prompt with `.venv\Scripts\activate.bat`, or replace `python` below with `.\.venv\Scripts\python.exe`.

### 3. Install packages and check

```sh
python -m pip install numpy pandas
python python/check_environment.py
```

`python -m pip` installs into the selected Python environment. The check should end with **PASS**.

Activation is optional if you name the interpreter directly: `.venv/bin/python python/check_environment.py` on macOS/Linux, or `.\.venv\Scripts\python.exe python/check_environment.py` on Windows.

### 4. Save installed versions

```sh
python -m pip freeze > requirements-venv.txt
```

This saves the installed versions in the root folder as the manual exercise snapshot.

## Phase 2: reset

### 5. Deactivate and remove the environment

Close programs using the environment, then run `deactivate` (skip this if you never activated it).

macOS / Linux:

```sh
python3 python/reset_environment.py
```

Windows PowerShell:

```powershell
py -3 python/reset_environment.py
```

The script deletes only `demo_1/.venv`. Scripts, notebooks and the snapshot remain. Run it with base Python, never with `uv run`.

## Phase 3: rebuild with uv

**Stay in `demo_1`.** uv will create the shared environment for the scripts and notebooks.

### 6. Install uv

Skip installation if `uv --version` already works.

macOS / Linux ([Astral installer](https://docs.astral.sh/uv/getting-started/installation/)):

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows PowerShell:

```powershell
winget install --id=astral-sh.uv -e
```

Reopen your terminal, return to `demo_1`, then check:

```sh
uv --version
```

### 7. Initialize the project once

```sh
uv init --bare --python 3
```

This creates `pyproject.toml` in the root using an available Python 3 interpreter. Skip `uv init` if `pyproject.toml` already exists.

**Why `--bare`?** It creates only the minimal `pyproject.toml`, without starter code, a README, a `.python-version` file, or Git initialization. Plain `uv init` also works, but creates a fuller starter project. We use `--bare` because this demo already has its scripts, notebooks, and README. Neither command installs the dependencies yet; that happens in the next step.

### 8. Add packages and check

```sh
uv add numpy pandas
uv run python/check_environment.py
```

`uv add` records dependencies, creates `uv.lock`, and rebuilds `.venv`. The check should end with **PASS** again. No activation is needed.

| File/folder | Purpose |
|---|---|
| `pyproject.toml` | Project requirements |
| `uv.lock` | Resolved dependency versions |
| `.venv/` | Installed environment; can be recreated |

## Phase 4: use the notebooks

### 9. Add notebook packages

```sh
uv add --dev ipykernel jupyterlab
uv add matplotlib scikit-learn
```

### 10. Select the environment in VS Code

1. Open the whole `demo_1` folder.
2. Run **Python: Select Interpreter** from the Command Palette and select the root `.venv`.
3. Open a notebook in `notebooks/fr/` (French) or `notebooks/en/` (English).
4. Use **Select Kernel → Python Environments** and select that same `.venv`.

In a notebook cell, verify:

```python
import sys
import numpy as np
import pandas as pd

print(sys.executable)
assert np.mean([1, 2, 3]) == 2
assert pd.Series([1, 2, 3]).sum() == 6
```

The interpreter should be inside `demo_1/.venv`. If imports fail, check the selected kernel and restart it.

### 11. Browser alternative: JupyterLab

From `demo_1`:

```sh
uv run jupyter lab
```

Open a notebook under `notebooks/fr/` (French) or `notebooks/en/` (English) and select the project's Python kernel. Stop the server with `Ctrl+C`.

### 12. Keep the project files

Add these lines to `demo_1/.gitignore`:

```gitignore
.venv/
__pycache__/
.ipynb_checkpoints/
.env
```

Commit scripts, notebooks, `pyproject.toml`, `uv.lock`, and `.gitignore`. Keep the manual snapshot for comparison.

## Returning later

From `demo_1`:

```sh
uv sync --locked
uv run python/check_environment.py
```

Then open your notebook and select the root `.venv` kernel. Use `uv add` for new packages; do not initialize the project again.

Reference: [Python command-line options](https://docs.python.org/3/using/cmdline.html#interface-options) · [uv project creation](https://docs.astral.sh/uv/concepts/projects/init/) · [uv with Jupyter](https://docs.astral.sh/uv/guides/integration/jupyter/)
