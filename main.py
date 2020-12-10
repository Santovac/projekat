from users.user import login
from books.book import list, search

def menu_administrator():
    while True:
        print('\n1. List all books')
        print('2. Search books')
        print('3. List all deals')
        print('4. Search deals')
        print('5. Register a user')
        print('6. List all users')
        print('7. Add a book')
        print('8. Edit a book')
        print('9. Erase a book (Logical deletion)')
        print('10. Logout')
        print('11. Exit.')
        option = int(input('Pick an option:'))
        if(option == 1):
            if(list()==False):
                menu_administrator()
        elif(option == 2):
            if(search()==False):
                menu_administrator()
        elif (option == 3):
            print('WIP')
            menu_administrator()
        elif (option == 4):
            print('WIP')
            menu_administrator()
        elif (option == 5):
            print('WIP')
            menu_administrator()
        elif (option == 6):
            print('WIP')
            menu_administrator()
        elif (option == 7):
            print('WIP')
            menu_administrator()
        elif (option == 8):
            print('WIP')
            menu_administrator()
        elif (option == 9):
            print('WIP')
            menu_administrator()
        elif(option == 10):
            main()
        elif(option == 11):
            exit()

        else: print('Invalid option, try again...')



def main():
    for i in range(4):
        if(i==3):
            print('Too many unsuccessful login attempts. Program shutting down...')
            return 0
        user = login()
        print(user)
        if(user!=False):
            print('Login successful. Account type:', user['type'])
            if(user['type']=='Administrator'):
                menu_administrator()
            if (user['type'] == 'Manager'):
                pass
            if (user['type'] == 'Seller'):
                pass
        elif(user==False and i<2): print('Login unsuccessful, try again.')

main()