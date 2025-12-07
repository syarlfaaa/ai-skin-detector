import json
import os
from config import USERS_FILE

def load_users():
    """Load user data dari file JSON"""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    """Save user data ke file JSON"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)