"""Tests module init file."""
import os
import sys
import pathlib
script_dir = pathlib.Path(
    os.path.abspath(__file__), "..", "..", "linkedlist"
).resolve()
sys.path.append(str(script_dir))
