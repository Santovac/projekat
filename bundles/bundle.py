from bundles.bundlelist import load, save
from datetime import date
from beautifultable import BeautifulTable
from books import book
import re

bundles = load()
n=len(bundles)

key = ['title','author','genre']

def print_articles(bundle):
    string=''
    i=0
    for article in bundle["articles"]:
        string+=article["title"]
        try:
            if(bundle["articles"][i+1]!=None):
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
    table.maxwidth=300
    for bundle in bundles:
        if(bundle['expiry']>str(date.today()) or show_valid == False):
            table.rows.append([bundle["id"], bundle["expiry"], print_articles(bundle), print_prices(bundle)])
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
    show_valid = False
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
        table = table_create(notes, show_valid)
        print(table)
        search()
    elif (option == '5'):
        return False
    else:
        print('Invalid option, try again...')
        if (search() == False): return False


def register():
    new_bundle = {
        "id": "350497",
        "articles": [{
            "id": "350256",
            "title": "Gde kad",
            "author": "Aleksandar Vedenski",
            "isbn": "9788660400194",
            "publisher": "Logos",
            "year": 2020,
            "price": 1320.0,
            "genre": "Poezija",
            "pages": 447,
            "erased": False
        }],
        "expiry": "2020-1-1"
    }
    for bundle in bundles:
        id = bundle['id']
    id+=1
    new_bundle['id']= id
    bundle_books = []
    while True:
        prompt = 0
        breaker=0
        id = input("Book ID (input 'back' to return to the main menu):")
        if(book.find(id)!=None and id!=''):
            book1 = book.find(id)
            print('Book found.')
            prompt=1
            print('Book will be added to the bundle:')
            books = [book1]
            book.permissions('a')
            book.list(books)
            book.permissions('m')
            while True:
                print('\nDo you wish to proceed?\n1. Yes\n2. Cancel')
                option = input('Input:')
                if (option == '1'):
                    while True:
                        try:
                            price = float(input('New price for the book:'))
                            book1['price'] = price
                            break
                        except ValueError: print('Invalid input, try again...')
                    bundle_books.append(book1)
                    break
                elif (option == '2'):
                    prompt=0
                    id='a'
                    break
                else:
                    print('Invalid option selected, try again...')
        elif(id=='back'): return False
        else: print('Invalid id, try again...')
        if(prompt==1):
            while True:
                print('\nDo you wish to add another book to the bundle?\n1. Yes\n2. No')
                option = input('Input:')
                if (option == '1'):
                    break
                elif (option == '2'):
                    breaker=1
                    break
                else:
                    print('Invalid option selected, try again...')
            if(breaker==1 and bundle_books!=[]): break
    new_bundle['articles']=bundle_books

    while True:
        try:
            year = int(input('Expiry date year:'))
            expiry = date(year, 1, 1)
            break
        except ValueError: print('Invalid input, try again...')
    while True:
        try:
            month = int(input('Month:'))
            expiry = date(year, month, 1)
            break
        except ValueError: print('Invalid input, try again...')
    while True:
        try:
            day = int(input('Day:'))
            expiry = date(year, month, day)
            break
        except ValueError: print('Invalid input, try again...')
    new_bundle['expiry']= str(expiry)
    print('\nBundle will be added to the database:')
    new_bundles = [new_bundle]
    show_valid = False
    table = table_create(new_bundles, show_valid)
    print(table)
    while True:
        print('\nDo you wish to proceed?\n1. Yes\n2. Cancel')
        option = input('Input:')
        if (option == '1'):
            bundles.append(new_bundle)
            break
        elif (option == '2'):
            return False
        else:
            print('Invalid option selected, try again...')
    save(bundles)
    print('Bundle has been added to the database. Bundle ID=[%s]' %(new_bundle['id']))
    return False