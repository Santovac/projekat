import json

path = './database/users.json'

def load():
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def save(users_new):
    with open(path, "w") as f:
        json.dump(users_new, f)