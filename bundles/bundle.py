from bundles.bundlelist import load, save
from prettytable import PrettyTable
from texttable import Texttable
import re

bundles = load()
i=0
n=len(bundles)

key = ['id','articles','expiry']

def table_create(bundles):
    table = PrettyTable()
    table.field_names = ["ID", "Valid Until (inclusive)", "Article", "New price" ]
    z=0
    for bundle in bundles:
        z+=1
        table.add_row([bundle['id'], bundle['expiry'], bundle['articles'][0]['title'], bundle['articles'][0]['price']])
        n_articles = len(bundle['articles'])
        for i in range(n_articles-1):
            table.add_row(['', '', bundle['articles'][i+1]['title'], bundle['articles'][i+1]['price']])
        if(z<(n)):
            table.add_row(['', '', '', ''])
            table.add_row(['*','*','*','*'])
            table.add_row(['','','',''])
    return table

def sort():
    table = table_create(bundles)
    print(table)


'''
def length_list():
    max='1'
    for i in range(3):
        max = len(str(bundles[0][key[i]]))
        for j in range(n-1):
            if (max < len(str(bundles[j + 1][key[i]]))):
                max = len(str(bundles[j + 1][key[i]]))
        length[i]=max

#RESPONSIVE TABLE
def list(bundleslist):
    length_list()
    print('\nID', end="")
    for i in range(length[0]+1):
        print(' ', end="")
    print('Articles', end="")
    for i in range(length[1]+1):
        print(' ', end="")
    print('Expiry date', end="\n")
    for bundle in bundleslist:
        #if(type=='a' or bundles['expiy']== False ):
        print(bundle['id'], end="")
        for i in range(length[0]+3-len(str(bundle['id']))):
            print(' ',end="")
        spacing=0
        for article in bundle['articles']:
            print(article['id'], end=" ")
            spacing+=len(article['id'])
        for i in range(spacing): #length[1]+9-len(str(article['id']))
            print(' ',end="")
        print(bundle['expiry'], end="\n")
    #else: pass

list(bundles)
'''