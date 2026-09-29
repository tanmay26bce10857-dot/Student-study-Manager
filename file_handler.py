import json
import os

folder = "data"

def load(file):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, file)

    if not os.path.exists(path):
        return []

    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return []

def save(file, data):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, file)

    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except:
        return False