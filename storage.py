import json
from pathlib import Path

DATA_FILE = Path("transactions.json")

def load_transactions():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_transactions(transactions):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(transactions, file, indent=4)