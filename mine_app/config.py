# mine_app/config.py

"""
⚙️ Mine App Configuration File
All global settings, constants, and configs live here.
"""

import os

# 🔹 App Metadata
APP_NAME = "Mine App"
APP_VERSION = "1.0.0"
DEBUG = True  # Set to False in production

# 🔹 Default Settings
DEFAULT_LANGUAGE = "en"
DEFAULT_CURRENCY = "USD"

# 🔹 Environment Variables (safe fallback values)
SECRET_KEY = os.getenv("MINE_APP_SECRET_KEY", "change_this_secret")
DATABASE_URL = os.getenv("MINE_APP_DATABASE_URL", "sqlite:///mine_app.db")

# 🔹 Utility function for config check
def show_config():
    """Print the current app configuration."""
    print(f"🔧 {APP_NAME} (v{APP_VERSION})")
    print(f"   Debug Mode: {DEBUG}")
    print(f"   Default Language: {DEFAULT_LANGUAGE}")
    print(f"   Default Currency: {DEFAULT_CURRENCY}")
    print(f"   Database URL: {DATABASE_URL}")
