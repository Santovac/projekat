from beautifultable import BeautifulTable
from receipts.receiptlist import load
import re

receipts = load()

def print_articles(receipt):
    string=''
    i=0
    for article in receipt['articles']:
        string+=article['title']
        try:
            if(receipt['articles'][i+1]!=None): string+='\n'
        except IndexError: break
        i+=1
    if (receipt['articles'] != []): string += '\n'
    i = 0
    for article in receipt['bundles']:
        string += article['title']
        try:
            if (receipt['bundles'][i + 1] != None): string += '\n'
        except IndexError: break
        i += 1
    return string

def print_prices(receipt):
    string = ''
    i = 0
    for article in receipt['articles']:
        string += str(article['price'])
        try:
            if (receipt['articles'][i + 1] != None): string+='\n'
        except IndexError: break
        i += 1
    if(receipt['bundles']!=[]): string+='\n'
    i = 0
    for article in receipt['bundles']:
        string += str(article['price'])
        try:
            if (receipt['bundles'][i + 1] != None): string += '\n'
        except IndexError: break
        i += 1
    return string

def print_table(receipt):
    table = BeautifulTable()
    table.maxwidth=300
    table.rows.append([receipt['id'], receipt['seller'], receipt['date_time'], print_articles(receipt), print_prices(receipt), receipt['total']])
    table.columns.header = ["ID", "Seller", "Time", "Articles", "New Prices", "Total"]
    print(table)



def all_books():
    #make an array including all books in receipt database
    booklist=[]
    receipts=load()
    for receipt in receipts:
        if(receipt['articles']!=[]):
            for article in receipt['articles']:
                booklist.append(article)
        if(receipt['bundles']!=[]):
            for article in receipt['bundles']:
                booklist.append(article)
    return booklist

def all_bundles():
    # make an array including all books sold through bundles in receipt database
    booklist = []
    receipts = load()
    for receipt in receipts:
        if (receipt['bundles'] != []):
            for article in receipt['bundles']:
                booklist.append(article)
    return booklist

def filter_books(books, key):
    #pass booklist from all_books and filter by chosen filter key, send ret_val to print_accounting_table
    filtered_books=[]
    term = input('Search:')
    for book in books:
        result = re.search(term.lower(), str(book[key]).lower())
        if(result!=None):
            filtered_books.append(book)
    print_table_account(filtered_books)

def print_table_account(books):
    table = BeautifulTable()
    table.maxwidth = 300
    current_books=[]
    for current_book in books:
        quantity=0
        book_earnings=0
        for book in books:
            if(current_book['title']==book['title']):
                quantity+=1
                book_earnings+=book['price']
        if(current_book not in current_books):  
            table.rows.append([current_book['title'], quantity, book_earnings])
            current_books.append(current_book)
    table.columns.header = ["Title", "Quantity sold", "Total earnings for the book"]
    print(table)

def account():
    while True:
        books=all_books()
        bundles=all_bundles()
        print('\nShow:')
        print('1. All transactions')
        print('2. All books sold through bundles')
        print('3. All books sold by a specific author')
        print('4. All books sold by a specific publisher')
        print('5. All books sold by a specific genre')
        print('6. Back')
        option = input('Select an option:')
        if (option == '1'):
            print_table_account(books)
        elif (option == '2'):
            print_table_account(bundles)
        elif (option == '3'):
            filter_books(books, 'author')
        elif (option == '4'):
            filter_books(books, 'publisher')
        elif (option == '5'):
            filter_books(books, 'genre')
        elif (option == '6'):
            return False
        else:
            print('Invalid option, try again...')