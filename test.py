''' sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]
0000
# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n') '''


'''
import json

path = 'database/books.json'

with open(path, encoding='utf-8') as f:
    books = json.load(f)
    max=len(str(books[0]['title']))
    for i in range(3):
        if(len(str(books[i]['title']))<len(str(books[i+1]['title']))):
            max=len(str(books[i+1]['title']))
        print(books[i]['title'])
    print(max)'''

'''from books.booklist import load, save

books = load()
i=0
n=0
#print(books[i]['title'])
while True:
    if(books[i+2]==None):
        break
    i+=1
    n+=1
n = len(books)
print('n=',n)'''

'''import re

result = re.search('penis', 'TP Tutorials Point TP')
if(result!=None):
    print(result.group(0))
elif(result==None):
    print('bula')'''

'''txt = "Hello my FRIENDS"

x = txt.lower()

print(x) '''