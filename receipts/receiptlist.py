import json

path = './database/receipts.json'

def load():
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def save(receipts_new):
    with open(path, "w", encoding='utf-8') as f:
        json.dump(receipts_new, f, ensure_ascii=False, indent=4)