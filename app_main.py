from users import user
from books import book
from bundles import bundle

def menu_administrator():
    while True:
        type = 'a'
        book.permissions(type)
        print('\n1. List all books')
        print('2. Search books')
        print('3. List all bundles')
        print('4. Search bundles')
        print('5. Register a user')
        print('6. List all users')
        print('7. Add a book')
        print('8. Edit a book')
        print('9. Erase a book (Logical deletion)')
        print('10. Logout')
        print('11. Exit.')
        option = input('Select an option:')
        if(option == '1'):
            if(book.sort()==False):
                menu_administrator()
        elif(option == '2'):
            if(book.search()==False):
                menu_administrator()
        elif (option == '3'):
            if (bundle.sort() == False):
                menu_administrator()
        elif (option == '4'):
            print('WIP')
            menu_administrator()
        elif (option == '5'):
            if(user.admin_register()==False):
                menu_administrator()
        elif (option == '6'):
            if(user.sort()==False):
                menu_administrator()
        elif (option == '7'):
            if(book.register()==False):
                menu_administrator()
        elif (option == '8'):
            if(book.edit()==False):
                menu_administrator()
            menu_administrator()
        elif (option == '9'):
            if(book.erase()==False):
                menu_administrator()
        elif(option == '10'):
            main()
        elif(option == '11'):
            exit()

        else: print('Invalid option, try again...')


def menu_manager():
    while True:
        type = 'm'
        book.permissions(type)
        print('\n1. List all books')
        print('2. Search books')
        print('3. List all bundles')
        print('4. Search bundles')
        print('5. Register a user')
        print('6. List all users')
        print('7. Add a bundle')
        print('8. Account (financial record)')
        print('9. Logout')
        print('10. Exit.')
        option = input('Select an option:')
        if(option == '1'):
            if(book.sort()==False):
                menu_manager()
        elif(option == '2'):
            if(book.search()==False):
                menu_manager()
        elif (option == '3'):
            print('WIP')
            menu_manager()
        elif (option == '4'):
            print('WIP')
            menu_manager()
        elif (option == '5'):
            if(user.manager_register()==False):
                menu_manager()
        elif (option == '6'):
            if(user.sort()==False):
                menu_manager()
        elif (option == '7'):
            print('WIP')
            menu_manager()
        elif (option == '8'):
            print('WIP')
            menu_manager()
        elif(option == '9'):
            main()
        elif(option == '10'):
            exit()

        else: print('Invalid option, try again...')


def menu_seller():
    while True:
        type = 's'
        book.permissions(type)
        print('\n1. List all books')
        print('2. Search books')
        print('3. List all bundles')
        print('4. Search bundles')
        print('5. Sell a book')
        print('6. Add a book')
        print('7. Edit a book')
        print('8. Erase a book (Logical deletion)')
        print('9. Logout')
        print('10. Exit.')
        option = input('Select an option:')
        if(option == '1'):
            if(book.sort()==False):
                menu_seller()
        elif(option == '2'):
            if(book.search()==False):
                menu_seller()
        elif (option == '3'):
            print('WIP')
            menu_seller()
        elif (option == '4'):
            print('WIP')
            menu_seller()
        elif (option == '5'):
            print('WIP')
            menu_seller()
        elif (option == '6'):
            if(book.register()==False):
                menu_seller()
        elif (option == '7'):
            if(book.edit()==False):
                menu_seller()
        elif (option == '8'):
            if(book.erase()==False):
                menu_seller()
        elif(option == '9'):
            main()
        elif(option == '10'):
            exit()

        else: print('Invalid option, try again...')



def main():
    for i in range(4):
        if(i==3):
            print('Too many unsuccessful login attempts. Program shutting down...')
            exit()
        user1 = user.login()
        #print(user)
        if(user1!=False):
            print('Login successful. Account type:', user1['type'])
            if(user1['type']=='Administrator'):
                menu_administrator()
            if (user1['type'] == 'Manager'):
                menu_manager()
            if (user1['type'] == 'Seller'):
                menu_seller()
        elif(user1==False and i<2): print('Login unsuccessful, try again.')

main()