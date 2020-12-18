from bundles.bundlelist import load, save
from prettytable import PrettyTable
import re

bundles = load()
#i=0
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