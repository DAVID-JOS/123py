# mine_app/utils.py

"""
⚙️ Utility functions for Mine App
These are helper functions that can be used across the app.
"""

import datetime
import random

def get_timestamp():
    """Return the current timestamp as a string."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_user_id(prefix="USR"):
    """Generate a random user ID with a prefix."""
    unique_number = random.randint(1000, 9999)
    return f"{prefix}{unique_number}"

def log_event(message):
    """Log an event with timestamp."""
    print(f"[{get_timestamp()}] {message}")
