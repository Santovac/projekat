from books.booklist import load, save
import re

books = load()
i=0
n=len(books)

length = [1,1,1,1,1,1,1,1]

key = ['id','title','author','isbn','publisher','year','price','genre']

def length_list():
    max='1'
    for i in range(8):
        max = len(str(books[0][key[i]]))
        for j in range(n-1):
            if (max < len(str(books[j + 1][key[i]]))):
                max = len(str(books[j + 1][key[i]]))
        length[i]=max

def show_list(books):
    length_list()
    print('\nID', end="")
    for i in range(length[0]+1):
        print(' ', end="")
    print('Title', end="")
    for i in range(length[1]+1):
        print(' ', end="")
    print('Author', end="")
    for i in range(length[2]+1):
        print(' ', end="")
    print('ISBN', end="")
    for i in range(length[3]+1):
        print(' ', end="")
    print('Publisher', end="")
    for i in range(length[4]+1):
        print(' ', end="")
    print('Year', end="")
    for i in range(length[5]+1):
        print(' ', end="")
    print('Price', end="")
    for i in range(length[6]+1):
        print(' ', end="")
    print('Genre', end="")
    for i in range(length[7]+1):
        print(' ', end="")
    print('\n')
    for book in books:
        print(book['id'], end="")
        for i in range(length[0]+3-len(str(book['id']))):
            print(' ',end="")
        print(book['title'], end="")
        for i in range(length[1]+6-len(str(book['title']))):
            print(' ',end="")
        print(book['author'], end="")
        for i in range(length[2]+7-len(str(book['author']))):
            print(' ',end="")
        print(book['isbn'], end="")
        for i in range(length[3]+5-len(str(book['isbn']))):
            print(' ',end="")
        print(book['publisher'], end="")
        for i in range(length[4]+10-len(str(book['publisher']))):
            print(' ',end="")
        print(book['year'], end="")
        for i in range(length[5]+5-len(str(book['year']))):
            print(' ',end="")
        print(book['price'], end="")
        for i in range(length[6]+6-len(str(book['price']))):
            print(' ',end="")
        print(book['genre'], end="\n")
        i+=1

def get_title(books):
    return books.get('title')
def get_genre(books):
    return books.get('genre')
def get_author(books):
    return books.get('author')
def get_publisher(books):
    return books.get('publisher')
def get_price(books):
    return books.get('price')

def list():
    while True:
        print('\nSort by:')
        print('1. Title')
        print('2. Genre')
        print('3. Author')
        print('4. Publisher')
        print('5. Price')
        print('6. Back')
        option = int(input('Pick an option:'))
        if (option == 1):
            sorter='title'
            break
        elif (option == 2):
            sorter = 'genre'
            break
        elif (option == 3):
            sorter = 'author'
            break
        elif (option == 4):
            sorter = 'publisher'
            break
        elif (option == 5):
            sorter = 'price'
            break
        elif (option==6):
            return False
        else: print('Invalid option, try again...')

    if(sorter=='title'):
        sorter=input('Ascending or desceding(a/d)?')
        if(sorter=='a'): books.sort(key=get_title)
        elif(sorter=='d'): books.sort(key=get_title, reverse=True)
        else:
            print("Invalid option selected, ascending mode selected by default.")
            books.sort(key=get_title)

    elif (sorter == 'genre'):
        sorter = input('Ascending or desceding(a/d)?')
        if (sorter == 'a'): books.sort(key=get_genre)
        elif (sorter == 'd'): books.sort(key=get_genre, reverse=True)
        else:
            print("Invalid option selected, ascending mode selected by default.")
            books.sort(key=get_genre)
    elif (sorter == 'author'):
        sorter = input('Ascending or desceding(a/d)?')
        if (sorter == 'a'): books.sort(key=get_author)
        elif (sorter == 'd'): books.sort(key=get_author, reverse=True)
        else:
            print("Invalid option selected, ascending mode selected by default.")
            books.sort(key=get_author)
    elif (sorter == 'publisher'):
        sorter = input('Ascending or desceding(a/d)?')
        if (sorter == 'a'):
            books.sort(key=get_publisher)
        elif (sorter == 'd'):
            books.sort(key=get_publisher, reverse=True)
        else:
            print("Invalid option selected, ascending mode selected by default.")
            books.sort(key=get_publisher)
    elif (sorter == 'price'):
        sorter = input('Ascending or desceding(a/d)?')
        if (sorter == 'a'):
            books.sort(key=get_price)
        elif (sorter == 'd'):
            books.sort(key=get_price, reverse=True)
        else:
            print("Invalid option selected, ascending mode selected by default.")
            books.sort(key=get_price)
    show_list(books)



def search():

    print('\nSearch by:')
    print('1. ID')
    print('2. Title')
    print('3. Author')
    print('4. Genre')
    print('5. Publisher')
    print('6. Price range')
    print('7. Back')
    option = int(input('Pick an option:'))
    if(option==1 or option==2 or option==3 or option==4 or option==5):
        term = input('Search:')
        notes=[]
        for book in books:
            if   (option == 1): i = 0
            elif (option == 2): i = 1
            elif (option == 3): i = 2
            elif (option == 4): i = 7
            elif (option == 5): i = 4
            result = re.search(term.lower(), str(book[key[i]]).lower())
            if (result != None):
                notes.append(book)
        show_list(notes)
        search()
    elif(option == 6):
        notes = []
        term = int(input('Minimum price:'))
        term2 = int(input('Maximum price:'))
        for book in books:
            if(term <= book['price'] and term2 >= book['price']):
                notes.append(book)
        show_list(notes)
        search()
    elif(option == 7):
        return False
    else: print('Invalid option, try again...')
