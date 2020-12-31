from beautifultable import BeautifulTable
from receipts.receiptlist import load

receipts = load()

'''
def length_list(books):
    max='1'
    length=[]
    n=len(books)
    for i in range(9):
        max = len(str(books[0][key[i]]))
        for j in range(n-1):
            if (max < len(str(books[j + 1][key[i]]))):
                max = len(str(books[j + 1][key[i]]))
        length[i]=max
    return length
'''

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
            if (receipt['articles'][i + 1] != None): string += '\n'
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
            if (receipt['articles'][i + 1] != None): string += '\n'
        except IndexError: break
        i += 1
    return string

def print_table(receipt):
    table = BeautifulTable()
    table.maxwidth=300
    table.rows.append([receipt['id'], receipt['seller'], receipt['date_time'], print_articles(receipt), print_prices(receipt), receipt['total']])
    table.columns.header = ["ID", "Seller", "Time", "Articles", "New Prices", "Total"]
    print(table)

def print_table_account(receipts):
    table = BeautifulTable()
    table.maxwidth = 300
    for receipt in receipts:
        table.rows.append([print_articles(receipt), print_prices(receipt), receipt['total']])
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
    print(booklist)

all_books()

def all_bundles():
    #make an array including all books sold through bundles in receipt database
    pass

def filter_books(books, key):
    #pass booklist from all_books and filter by chosen filter key, send ret_val to print_accounting_table
    pass

def print_accounting_table(books):
    #print table
    pass


def account():
    while True:
        print('\nSell:')
        print('1. All transactions')
        print('2. All books sold through bundles')
        print('3. All books sold by a specific author')
        print('4. All books sold by a specific publisher')
        print('5. All books sold by a specific genre')
        print('6. Exit to main menu (empty the cart)')
        option = input('Select an option:')
        if (option == '1'):
            if(print_table_account(receipts)==True):
                print('Shopping cart successfully updated:')
        elif (option == '2'):
            if (sell_bundle() == True):
                print('Shopping cart successfully updated:')
        elif (option == '3'):
            pass
        elif (option == '4'):
            if (sell_complete() == False):
                return False
        elif (option == '5'):
            return False
        elif (option == '6'):
            return False
        else:
            print('Invalid option, try again...')