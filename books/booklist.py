import json

path = './database/books.json'

def load():
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def save(books_new):
    with open(path, "w") as f:
        json.dump(books_new, f)

