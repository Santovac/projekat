from bundles.bundlelist import load, save
from datetime import date
from beautifultable import BeautifulTable
import re

bundles = load()
#i=0
n=len(bundles)

key = ['title','author','genre']

def print_articles(bundle):
    string=''
    i=0
    for article in bundle['articles']:
        string+=article['title']
        try:
            if(bundle['articles'][i+1]!=None):
                string+='\n'
        except IndexError: break
        i+=1
    return string

def print_prices(bundle):
    string = ''
    i = 0
    for article in bundle['articles']:
        string += str(article['price'])
        try:
            if (bundle['articles'][i + 1] != None):
                string += '\n'
        except IndexError:
            break
        i += 1
    return string

def table_create(bundles, show_valid):
    table = BeautifulTable()
    for bundle in bundles:
        if(bundle['expiry']>str(date.today()) or show_valid == False):
            table.rows.append([bundle['id'], bundle['expiry'], print_articles(bundle), print_prices(bundle)])
    table.columns.header = ["ID", "Valid until\n(inclusive)", "Articles", "New Prices"]
    return table

def sort():
    show_valid = True
    table = table_create(bundles, show_valid)
    while True:
        print('\nSort by:')
        print('1. ID')
        print('2. Expiry date')
        print('3. Back')
        option = input('Select an option:')
        if (option == '1'):
            table.rows.sort("ID")
            break
        elif (option == '2'):
            table.rows.sort("Valid until\n(inclusive)")
            break
        elif (option=='3'):
            return False
        else: print('Invalid option, try again...')
    print(table)

def search():
    print('\nSearch by:')
    print('1. ID')
    print('2. Title')
    print('3. Author')
    print('4. Genre')
    print('5. Back')
    option = input('Select an option:')
    if (option == '2' or option == '3' or option == '4'):
        term = input('Search:')
        notes = []
        for bundle in bundles:
            if (option == '2'):
                i = 0
            elif (option == '3'):
                i = 1
            elif (option == '4'):
                i = 2
            for article in bundle['articles']:
                result = re.search(term.lower(), str(article[key[i]]).lower())
                if (result != None):
                    notes.append(bundle)
                    break
        show_valid = False
        table = table_create(notes, show_valid)
        print(table)
        search()
    elif (option == '1'):
        notes = []
        while True:
            try:
                term = int(input('\nSearch:'))
                break
            except ValueError:
                print('Please input whole numbers only...')
        for bundle in bundles:
            result = re.search(str(term).lower(), str(bundle['id']).lower())
            if (result!=None):
                notes.append(bundle)
        table = table_create(notes)
        print(table)
        search()
    elif (option == '5'):
        return False
    else:
        print('Invalid option, try again...')
        if (search() == False): return False


def register():
    for bundle in bundles:
        id = bundle['id']
    id+=1
    title = input('Title:')
    author = input('Author:')
    isbn = input('ISBN:')
    publisher = input('Publisher:')
    year = int(input('Year:'))
    price = float(input('Price:'))
    genre = input('Genre:')
    pages = int(input('Pages:'))
    new_book = {
        "id": "350497",
        "title": "Medvedgrad",
        "author": "Fredrik Bakman",
        "isbn": "9788652139743",
        "publisher": "Laguna",
        "year": 2016,
        "price": 899.00,
        "genre": "Roman",
        "pages": 447,
        "erased": False
    }
    new_book['id']= id
    new_book['title'] = title
    new_book['author'] = author
    new_book['isbn'] = isbn
    new_book['publisher']= publisher
    new_book['year'] = year
    new_book['price'] = price
    new_book['genre'] = genre
    new_book['pages']= pages
    new_book['erased']= False

    books.append(new_book)
    save(books)
    print('%s has been added to the book database. Book ID=[%s]' %(new_book['title'], new_book['id']))
    return False