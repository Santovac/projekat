from books.booklist import load, save
from bundles import bundle
from datetime import date, datetime
from users import user
from receipts import receiptlist
from receipts import receipt as mreceipt
import re

type='neutral'

def permissions(rights):
    global type
    type=rights

bundles=bundle.load()
books = load()
n=len(books)

length = [1,1,1,1,1,1,1,1,1]
cart = []
total = 0.0
key = ['id','title','author','isbn','publisher','year','price','genre','pages']

def length_list(books):
    max='1'
    n=len(books)
    for i in range(9):
        max = len(str(books[0][key[i]]))
        for j in range(n-1):
            if (max < len(str(books[j + 1][key[i]]))):
                max = len(str(books[j + 1][key[i]]))
        length[i]=max
    return length

#RESPONSIVE TABLE
def list(booklist):
    length = length_list(booklist)
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
    print('')
    for book in booklist:
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
            books.sort(key=lambda books:books.get('title'))
        elif(sorter=='d'):
            books.sort(key=lambda books:books.get('title'), reverse=True)
        else:
            print("Invalid option selected, ascending mode selected by default.")
            books.sort(key=lambda books:books.get('title'))

    elif (sorter == 'genre'):
        sorter = input('Ascending or desceding(a/d)?')
        if (sorter == 'a'):
            books.sort(key=lambda books:books.get('genre'))
        elif (sorter == 'd'):
            books.sort(key=lambda books:books.get('genre'), reverse=True)
        else:
            print("Invalid option selected, ascending mode selected by default.")
            books.sort(key=lambda books:books.get('genre'))

    elif (sorter == 'author'):
        sorter = input('Ascending or desceding(a/d)?')
        if (sorter == 'a'): books.sort(key=lambda books:books.get('author'))
        elif (sorter == 'd'): books.sort(key=lambda books:books.get('author'), reverse=True)
        else:
            print("Invalid option selected, ascending mode selected by default.")
            books.sort(key=lambda books:books.get('author'))

    elif (sorter == 'publisher'):
        sorter = input('Ascending or desceding(a/d)?')
        if (sorter == 'a'):
            books.sort(key=lambda books:books.get('publisher'))
        elif (sorter == 'd'):
            books.sort(key=lambda books:books.get('publisher'), reverse=True)
        else:
            print("Invalid option selected, ascending mode selected by default.")
            books.sort(key=lambda books:books.get('publisher'))

    elif (sorter == 'price'):
        sorter = input('Ascending or desceding(a/d)?')
        if (sorter == 'a'):
            books.sort(key=lambda books:books.get('price'))
        elif (sorter == 'd'):
            books.sort(key=lambda books:books.get('price'), reverse=True)
        else:
            print("Invalid option selected, ascending mode selected by default.")
            books.sort(key=lambda books:books.get('price'))
    list(books)

def find(term):
    for book in books:
        result = re.search(term.lower(), str(book['id']).lower())
        if(result!=None):
            return book
    return None

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
        if(notes!=[]): list(notes)
        else: print('No results found.')
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
        if(notes!=[]):
            list(notes)
        else: print('No results found.')
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
    while True:
        try:
            year = int(input('Year:'))
            break
        except ValueError: print('Invalid input, try again...')
    while True:
        try:
            price = float(input('Price:'))
            break
        except ValueError: print('Invalid input, try again...')
    genre = input('Genre:')
    while True:
        try:
            pages = int(input('Pages:'))
            break
        except ValueError: print('Invalid input, try again...')
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
    print('\nBook will be added to the database:')
    new_books = [new_book]
    list(new_books)
    while True:
        print('\nDo you wish to proceed?\n1. Yes\n2. Cancel')
        option = input('Input:')
        if (option == '1'):
            books.append(new_book)
            break
        elif (option == '2'):
            return False
        else:
            print('Invalid option selected, try again...')
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
        year = int(input('Overwrite year (blank string or incorrect input will not overwrite this information):'))
    except ValueError:
        year = books[i]['year']
    try:
        price = float(input('Overwrite price (blank string or incorrect input will not overwrite this information):'))
    except ValueError:
        price = books[i]['price']
    genre = input('Overwrite genre (blank string will not overwrite this information):')
    if (genre == ''):
        genre = books[i]['genre']
    try:
        pages = int(input('Overwrite pages (blank string or incorrect input will not overwrite this information):'))
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

def sell_book():
    global cart
    z = -1
    i = 0
    while True:
        id = input("\nID (input 'back' to return to the shopping menu):")
        if (id == 'back'):
            return False
        elif (id != ''):
            result = re.search(' ', id)
            if (result == None):
                break
            else:
                print("ID cannot contain spaces, try again...")
                if (sell_book() == False):
                    return False
        else:
            print("ID cannot be blank, try again...")
            if (sell_book() == False):
                return False
            else: return True
    for book in books:
        if (book['id'] == id and book['erased']==False):
            print('Book found.')
            z = i
            break
        i += 1
    if (z == -1):
        print('Book not found, try again...')
        if (sell_book() == False ):
            return False
        else: return True
    cart_item=[]
    while True:
        q=-1
        try:
            q = int(input('Quantity:'))
        except ValueError: pass
        if(q>0): break
        else: print('Invalid input, try again...')
    print('Item(s) will be added to the cart:')
    for i in range(q):
        cart_item+= [books[z]]
    list(cart_item)
    while True:
        print('\nDo you wish to proceed?\n1. Yes\n2. Cancel')
        option = input('Input:')
        if (option == '1'):
            cart[0]["articles"] += cart_item
            return True
        elif (option == '2'):
            return False
        else:
            print('Invalid option selected, try again...')

def sell_bundle():
    global cart
    z = -1
    i = 0
    while True:
        id = input("\nID (input 'back' to return to the shopping menu):")
        if (id == 'back'):
            return False
        elif (id != ''):
            result = re.search(' ', id)
            i=0
            for bundle in bundles:
                if (str(bundle['id']) == id and bundle['expiry'] > str(date.today())):
                    print('Bundle found.')
                    z = i
                    break
                i += 1
        if (z == -1):
            print('Bundle not found or expired, try again...')
        if(z!=-1): break
    cart_item=[]
    print('Item(s) will be added to the cart:')
    n=len(bundles[z]['articles'])
    for i in range(n):
        cart_item+= [bundles[z]['articles'][i]]
    list(cart_item)
    while True:
        print('\nDo you wish to proceed?\n1. Yes\n2. Cancel')
        option = input('Input:')
        if (option == '1'):
            cart[0]["bundle_books"]+= cart_item
            return True
        elif (option == '2'):
            return False
        else:
            print('Invalid option selected, try again...')

def receipt_create():
    global total
    receipt = {
        "id": 0,
        "seller": "S",
        "date_time": "2020-12-24T18:16:25.925653",
        "articles": [
            {
                "id": "N/A",
                "title": "N/A",
                "author": "N/A",
                "isbn": "N/A",
                "publisher": "N/A",
                "year": 2020,
                "price": 0.0,
                "genre": "N/A",
                "pages": 0,
                "erased": False
            }
        ],
        "bundle_books": [
            {
                "id": "N/A",
                "title": "N/A",
                "author": "N/A",
                "isbn": "N/A",
                "publisher": "N/A",
                "year": 2020,
                "price": 0.0,
                "genre": "N/A",
                "pages": 0,
                "erased": False
            }
        ],
        "total": 0.0
    }
    old_receipts = receiptlist.load()
    z=0
    for receipt in old_receipts:
        z+=1
    receipt['id'] = z
    receipt['seller'] = user.get_username()
    receipt['date_time'] = datetime.now().isoformat()
    receipt['articles'] = cart[0]['articles']
    receipt['bundles'] = cart[0]['bundle_books']
    receipt['total'] = total
    return receipt

def sell_complete():
    receipts = receiptlist.load()
    receipt = receipt_create()
    try:
        print('\nFollowing book(s) will be sold:')
        list(cart[0]["articles"])
    except IndexError: pass
    try:
        print('\nFollowing bundle(s) will be sold:')
        list(cart[0]["bundle_books"])
    except IndexError: pass
    while True:
        print('\nDo you wish to proceed?\n1. Yes\n2. Cancel')
        option = input('Input:')
        if (option == '1'):
            if(total!=0): receipts.append(receipt)
            break
        elif (option == '2'):
            return True
        else:
            print('Invalid option selected, try again...')
    receiptlist.save(receipts)
    if(total!=0):
        print('Books have been sold. Receipt:')
        mreceipt.print_table(receipt)
    else: print('Cart was empty, no books were sold.')
    return False

def sell_menu():
    global cart
    global total
    while True:
        total = 0.0
        for item in cart[0]["articles"]:
            total += item["price"]
        for item in cart[0]["bundle_books"]:
            total += item["price"]
        print('\nSell:')
        print('1. Books')
        print('2. Bundles')
        print('3. Show cart')
        print('4. Complete transaction')
        print('5. Exit to main menu (empty the cart)')
        option = input('Select an option:')
        if (option == '1'):
            if(sell_book()==True):
                print('Shopping cart successfully updated:')
            else:
                print('Shopping cart was not updated:')
                if(sell_menu()==False):
                    return False
        elif (option == '2'):
            if (sell_bundle() == True):
                print('Shopping cart successfully updated:')
            else:
                print('Shopping cart was not updated:')
                if (sell_menu() == False):
                    return False
        elif (option == '3'):
            try:
                list(cart[0]["articles"])
            except IndexError: pass
            try:
                list(cart[0]["bundle_books"])
            except IndexError: pass
            print('\nTotal:', total)
        elif (option == '4'):
            if (sell_complete() == True): pass
            else: return False
        elif (option == '5'):
            return False
        else:
            print('Invalid option, try again...')

def sell():
    global cart
    cart_keys = {
        "articles": [],
        "bundle_books": []
    }
    cart=[cart_keys]
    if(sell_menu()==False): return False