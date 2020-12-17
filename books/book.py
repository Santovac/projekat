from books.booklist import load, save
import re

type='neutral'

def permissions(rights):
    global type
    type=rights

books = load()
i=0
n=len(books)

length = [1,1,1,1,1,1,1,1,1]

key = ['id','title','author','isbn','publisher','year','price','genre','pages']

lista=[0,1,2,3,4,5,6,7,8]

def length_list():
    max='1'
    for i in range(9):
        max = len(str(books[0][key[i]]))
        for j in range(n-1):
            if (max < len(str(books[j + 1][key[i]]))):
                max = len(str(books[j + 1][key[i]]))
        length[i]=max

#RESPONSIVE TABLE
def list(bookslist):
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
    print('Pages', end="\n")
    for book in bookslist:
        if(type=='a' or book['erased']== False ):
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
            print(book['genre'], end="")
            for i in range(length[7]+6-len(str(book['genre']))):
                print(' ',end="")
            print(book['pages'], end="\n")
        else: pass

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

def sort():
    while True:
        print('\nSort by:')
        print('1. Title')
        print('2. Genre')
        print('3. Author')
        print('4. Publisher')
        print('5. Price')
        print('6. Back')
        option = input('Select an option:')
        if (option == '1'):
            sorter='title'
            break
        elif (option == '2'):
            sorter = 'genre'
            break
        elif (option == '3'):
            sorter = 'author'
            break
        elif (option == '4'):
            sorter = 'publisher'
            break
        elif (option == '5'):
            sorter = 'price'
            break
        elif (option=='6'):
            return False
        else: print('Invalid option, try again...')

    if(sorter=='title'):
        sorter=input('Ascending or desceding(a/d)?')
        if(sorter=='a'):
            books.sort(key=get_title)
        elif(sorter=='d'):
            books.sort(key=get_title, reverse=True)
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
    list(books)



def search():

    print('\nSearch by:')
    print('1. ID')
    print('2. Title')
    print('3. Author')
    print('4. Genre')
    print('5. Publisher')
    print('6. Price range')
    print('7. Back')
    option = input('Select an option:')
    if(option=='1' or option=='2' or option=='3' or option=='4' or option=='5'):
        term = input('Search:')
        notes=[]
        for book in books:
            if   (option == '1'): i = 0
            elif (option == '2'): i = 1
            elif (option == '3'): i = 2
            elif (option == '4'): i = 7
            elif (option == '5'): i = 4
            result = re.search(term.lower(), str(book[key[i]]).lower())
            if (result != None):
                notes.append(book)
        list(notes)
        search()
    elif(option == '6'):
        notes = []
        while True:
            try:
                term = int(input('\nMinimum price:'))
                break
            except ValueError: print('Please input whole numbers only...')

        while True:
            try:
                term2 = int(input('Maximum price:'))
                break
            except ValueError: print('Please input whole numbers only...')
        for book in books:
            if(term <= book['price'] and term2 >= book['price']):
                notes.append(book)
        list(notes)
        search()
    elif(option == '7'):
        return False
    else:
        print('Invalid option, try again...')
        if(search()==False): return False

def register():
    while True:
        id = input("\nID (input 'back' to return to the main menu):")
        if(id!=''):
            result = re.search(' ', id)
            if(result==None):
                break
            else:
                print("ID cannot contain spaces, try again...")
                if(register()==False):
                    return False
        else:
            print("ID cannot be blank, try again...")
            if(register()==False):
                return False
    for book in books:
        if(book['id']==id):
            print('Book with the same ID already exists, try again...')
            if(register()==False):
                return False
        elif(id=='back'):
            return False
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


def edit():
    validator = 0
    id = input("\nID (input 'back' to return to the main menu):")
    i=0
    for book in books:
        if(book['id']==id):
            validator = 1
            print('Book found.')
            break
        elif(id=='back'):
            return False
        i+=1
    if(validator==0):
        print('Invalid ID, try again...')
        if(edit()==False):
            return False
    old_book = {
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
    old_book=books[i]
    z=i
    old_books = [old_book]
    list(old_books)

    title = input('\nOverwrite title (blank string will not overwrite this information):')
    if(title==''):
        title=books[i]['title']
    author = input('Overwrite author (blank string will not overwrite this information):')
    if (author == ''):
        author = books[i]['author']
    isbn = input('Overwrite ISBN (blank string will not overwrite this information):')
    if (isbn == ''):
        isbn = books[i]['isbn']
    publisher = input('Overwrite publisher (blank string will not overwrite this information):')
    if (publisher == ''):
        publisher = books[i]['publisher']
    try:
        year = int(input('Overwrite year (blank string will not overwrite this information):'))
    except ValueError:
        year = books[i]['year']
    try:
        price = float(input('Overwrite price (blank string will not overwrite this information):'))
    except ValueError:
        price = books[i]['price']
    genre = input('Overwrite genre (blank string will not overwrite this information):')
    if (genre == ''):
        genre = books[i]['genre']
    try:
        pages = int(input('Overwrite pages (blank string will not overwrite this information):'))
    except ValueError:
        pages = books[i]['pages']
    erased=books[i]['erased']
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
    new_book['erased'] = erased

    old_books = [books[z],new_book]
    print('\nOverwriting top with bottom:')
    list(old_books)
    while True:
        print('\nDo you wish to proceed?\n1. Yes\n2. Cancel')
        option = input('Input:')
        if(option=='1'):
            books[z]=new_book
            break
        elif(option=='2'): return False
        else: print('Invalid option selected, try again...')

    save(books)
    print('%s has been edited in the book database. Book ID=[%s]' %(new_book['title'], new_book['id']))
    return False


def erase():
    z=-1
    i=0
    while True:
        id = input("\nID (input 'back' to return to the main menu):")
        if(id=='back'):
            return False
        elif(id!=''):
            result = re.search(' ', id)
            if(result==None):
                break
            else:
                print("ID cannot contain spaces, try again...")
                if(erase()==False):
                    return False
        else:
            print("ID cannot be blank, try again...")
            if(erase()==False):
                return False
    for book in books:
        if(book['id']==id):
            print('Book found.')
            z=i
            break
        i+= 1
    if(z==-1):
        print('Book not found, try again...')
        if(erase()==False):
            return False
    deleted_books = [books[z]]
    print('\nBook will be erased:')
    list(deleted_books)
    while True:
        print('\nDo you wish to proceed?\n1. Yes\n2. Cancel')
        option = input('Input:')
        if (option == '1'):
            del_book = books[z]
            del_book['erased'] = True
            break
        elif (option == '2'):
            return False
        else:
            print('Invalid option selected, try again...')

    save(books)

    print('%s has been erased in the book database. Book ID=[%s]' % (del_book['title'], del_book['id']))
    return False
