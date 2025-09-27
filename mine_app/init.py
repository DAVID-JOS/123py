# mine_app/__init__.py

"""
🚀 mine_app package
This initializes the Mine App package and makes it importable.
"""

# Import the main entry point so users can call mine_app.run_app()
from .main import run_app

# Optional: define what gets imported with `from mine_app import *`
__all__ = ["run_app"]
