"""Delete only the project root's .venv. Run with base Python after deactivate."""

import os
from pathlib import Path
import shutil
import stat
import sys

environment = Path(__file__).resolve().parents[1] / ".venv"

if sys.prefix != sys.base_prefix or os.environ.get("VIRTUAL_ENV"):
    raise SystemExit(
        "Deactivate first, then run with base Python: "
        "python3 python/reset_environment.py (macOS/Linux) or "
        "py -3 python/reset_environment.py (Windows), from the project root."
    )

if environment.is_symlink() or (
    os.name == "nt" and environment.exists()
    and environment.lstat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT
):
    raise SystemExit("Refusing to delete a linked .venv. Use a fresh starter copy.")

if not environment.exists():
    raise SystemExit("No .venv in the project root. Nothing to delete.")

if not (environment / "pyvenv.cfg").is_file():
    raise SystemExit("Refusing to delete .venv: no pyvenv.cfg environment marker.")

print("Deleting:", environment)
try:
    shutil.rmtree(environment)
except PermissionError as error:
    raise SystemExit(
        "Close programs using this environment, then retry with base Python."
    ) from error

print("Removed .venv. Your code and dependency records are still here.")
