from beautifultable import BeautifulTable

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
            if(receipt['articles'][i+1]!=None):
                string+='\n'
        except IndexError: break
        i+=1
    return string

def print_prices(receipt):
    string = ''
    i = 0
    for article in receipt['articles']:
        string += str(article['price'])
        try:
            if (receipt['articles'][i + 1] != None):
                string += '\n'
        except IndexError:
            break
        i += 1
    return string

def print_table(receipt):

    table = BeautifulTable()
    table.maxwidth=300
    table.rows.append([receipt['id'], receipt['seller'], receipt['date_time'], print_articles(receipt), print_prices(receipt), receipt['total']])
    table.columns.header = ["ID", "Seller", "Time", "Articles", "New Prices", "Total"]
    print(table)