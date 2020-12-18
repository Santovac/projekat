import json

path = './database/bundles.json'

def load():
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def save(bundles_new):
    with open(path, "w", encoding='utf-8') as f:
        json.dump(bundles_new, f, ensure_ascii=False, indent=4)

load()