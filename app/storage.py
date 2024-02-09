import json
from pathlib import Path

DATA_FILE = Path("data/tasks.json")

def load_tasks():

    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    else:
        return []

def save_tasks(tasks):
    
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
