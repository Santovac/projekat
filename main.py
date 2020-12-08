from users.user import login

def meni_administrator():
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
        print('10. Exit.')
        option = int(input('Pick an option:'))
        if(option==1):
            pass
        else: print('Invalid option, try again')



def main():

    for i in range(4):
        if(i==3):
            print('Too many unsuccessful login attempts. Program shutting down...')
            return 0
        user = login()
        if(user!=False):
            print('Login successful. Account type:', user['type'])
            if(user['type']=='Administrator'):
                meni_administrator()
            if (user['type'] == 'Manager'):
                pass
            if (user['type'] == 'Seller'):
                pass
        elif(user==False and i<2): print('Login unsuccessful, try again.')







main()