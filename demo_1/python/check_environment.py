"""Run using the project root's .venv. See README.md."""

import sys
from pathlib import Path

print("Python version:", sys.version.split()[0])
print("Interpreter:", sys.executable)
print("Environment:", sys.prefix)
print("Working directory:", Path.cwd())

expected_environment = Path(__file__).resolve().parents[1] / ".venv"
if sys.prefix == sys.base_prefix or Path(sys.prefix).resolve() != expected_environment.resolve():
    raise SystemExit(
        "Wrong environment. In the manual phase, activate this project's .venv "
        "or name its Python directly.\n"
        "From the project root after uv setup, run: uv run python/check_environment.py"
    )

try:
    import numpy as np
    import pandas as pd
except ModuleNotFoundError as error:
    raise SystemExit(
        f"Missing import: {error.name}. In the manual phase, use the activated "
        "venv: python -m pip install numpy pandas\n"
        "In the uv phase, run: uv add numpy pandas"
    ) from error

print("NumPy version:", np.__version__)
print("pandas version:", pd.__version__)
print("NumPy location:", np.__file__)

values = np.array([1, 2, 3])
table = pd.DataFrame({"value": values})
assert np.isclose(values.mean(), 2.0)
assert table["value"].sum() == 6
print("PASS: this project's environment and imports work.")
