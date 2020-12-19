from bundles.bundlelist import load, save
from prettytable import PrettyTable
from beautifultable import BeautifulTable
import re

bundles = load()
#i=0
n=len(bundles)

key = ['id','articles','expiry']

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

def table_create(bundles):
    table = BeautifulTable()
    for bundle in bundles:
        table.rows.append([bundle['id'], bundle['expiry'], print_articles(bundle), print_prices(bundle)])
    table.columns.header = ["ID", "Valid until\n(inclusive)", "Articles", "New Prices"]
    return table

def sort():
    table = table_create(bundles)
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