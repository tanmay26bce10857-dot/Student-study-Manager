import json
import os


DATA_FOLDER = "data"


def ensure_data_folder():
    """Create the data folder if it does not already exist."""
    os.makedirs(DATA_FOLDER, exist_ok=True)


def load_data(filename):
    """Load data from a JSON file."""
    ensure_data_folder()

    file_path = os.path.join(DATA_FOLDER, filename)

    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    ensure_data_folder()

    file_path = os.path.join(DATA_FOLDER, filename)

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return True
    except OSError:
        return False