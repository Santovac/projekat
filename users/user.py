from users.userlist import load, save
import re, getpass

users = load()
n=len(users)
username=''

def login():
    global username
    print("\n/Project BOOKS by Santovac Stefan/\nCoded for 1920x1080 resolution at 100% font size\nInput 'exit()' as username to exit the program.")
    print('\n-Login-')
    username = input('Username:')
    if(username=='exit()'):
        exit()
    password = getpass.getpass('Password:')
    #print(users) debug
    for user in users:
        if((user['username']==username) and (user['password']==password)):
            username=user['username']
            return user
    return False

def get_username():
    return username

length = [1,1,1,1,1]

key = ['username','password','name','lastname','type']

def length_list():
    max='1'
    for i in range(5):
        max = len(str(users[0][key[i]]))
        for j in range(n-1):
            if (max < len(str(users[j + 1][key[i]]))):
                max = len(str(users[j + 1][key[i]]))
        length[i]=max

#RESPONSIVE TABLE
def list(users):
    length_list()
    print('\nUsername', end="")
    for i in range(length[0]+1):
        print(' ', end="")
    print('Password', end="")
    for i in range(length[1]+1):
        print(' ', end="")
    print('Name', end="")
    for i in range(length[2]+1):
        print(' ', end="")
    print('Lastname', end="")
    for i in range(length[3]+1):
        print(' ', end="")
    print('Type', end="")
    for i in range(length[4]+1):
        print(' ', end="")
    print('\n')
    for user in users:
        print(user['username'], end="")
        for i in range(length[0]+9-len(str(user['username']))):
            print(' ',end="")
        print('*****', end="")
        for i in range(length[1]+4):
            print(' ',end="")
        print(user['name'], end="")
        for i in range(length[2]+5-len(str(user['name']))):
            print(' ',end="")
        print(user['lastname'], end="")
        for i in range(length[3]+9-len(str(user['lastname']))):
            print(' ',end="")
        print(user['type'], end="\n")
        i+=1


def sort():
    while True:
        print('\nSort by:')
        print('1. Name')
        print('2. Lastname')
        print('3. Type')
        print('4. Back')
        option = input('Select an option:')
        if (option == '1'):
            sorter='name'
            break
        elif (option == '2'):
            sorter = 'lastname'
            break
        elif (option == '3'):
            sorter = 'type'
            break
        elif (option=='4'):
            return False
        else: print('Invalid option, try again...')

    if(sorter=='name'):
        sorter=input('Ascending or desceding(a/d)?')
        if(sorter=='a'):
            users.sort(key=lambda users:users.get('name'))
        elif(sorter=='d'):
            users.sort(key=lambda users:users.get('name'), reverse=True)
        else:
            print("Invalid option selected, ascending mode selected by default.")
            users.sort(key=lambda users:users.get('name'))

    elif (sorter == 'lastname'):
        sorter = input('Ascending or desceding(a/d)?')
        if (sorter == 'a'):
            users.sort(key=lambda users:users.get('lastname'))
        elif (sorter == 'd'):
            users.sort(key=lambda users:users.get('lastname'), reverse=True)
        else:
            print("Invalid option selected, ascending mode selected by default.")
            users.sort(key=lambda users:users.get('lastname'))

    elif (sorter == 'type'):
        sorter = input('Ascending or desceding(a/d)?')
        if (sorter == 'a'):
            users.sort(key=lambda users:users.get('type'))
        elif (sorter == 'd'):
            users.sort(key=lambda users:users.get('type'), reverse=True)
        else:
            print("Invalid option selected, ascending mode selected by default.")
            users.sort(key=lambda users:users.get('type'))
    list(users)

def list_one(users):
    length_list()
    print('\nUsername', end="")
    for i in range(length[0]+1):
        print(' ', end="")
    print('Password', end="")
    for i in range(length[1]+1):
        print(' ', end="")
    print('Name', end="")
    for i in range(length[2]+1):
        print(' ', end="")
    print('Lastname', end="")
    for i in range(length[3]+1):
        print(' ', end="")
    print('Type', end="")
    for i in range(length[4]+1):
        print(' ', end="")
    print('\n')
    for user in users:
        print(user['username'], end="")
        for i in range(length[0]+9-len(str(user['username']))):
            print(' ',end="")
        print(user['password'], end="")
        for i in range(length[1]+9-len(str(user['password']))):
            print(' ',end="")
        print(user['name'], end="")
        for i in range(length[2]+5-len(str(user['name']))):
            print(' ',end="")
        print(user['lastname'], end="")
        for i in range(length[3]+9-len(str(user['lastname']))):
            print(' ',end="")
        print(user['type'], end="\n")
        i+=1


def admin_register():
    while True:
        username = input("\nUsername (input 'back' to return to the main menu):")
        result = re.search(' ', username)
        if (result != None): print('No spaces allowed, try again...')
        elif(username == ''): print('Username cannot be an empty string, try again...')
        else: break
    for user in users:
        if(user['username']==username):
             print('Username taken, try again...')
             if(admin_register()==False):
                 return False
        if(username=='back'):
            return False
    while True:
        password = getpass.getpass('Password:')
        result = re.search(' ', password)
        if (result != None): print('No spaces allowed, try again...')
        elif (password == ''):
            print('Password cannot be an empty string, try again...')
        else:
            break
    name = input('Name:')
    lastname = input('Lastname:')
    while True:
        type = input('Account type manager or seller (m/s):')
        if(type!='m' and type!='s'): print('Invalid type, try again...')
        else: break

    new_user = {
        "username": "",
        "password": "",
        "name": "",
        "lastname": ""
    }
    new_user['username']= username
    new_user['password'] = password
    new_user['name'] = name
    new_user['lastname'] = lastname
    if(type=='m'): new_user['type'] = 'Manager'
    else: new_user['type']= 'Seller'
    print('\nUser will be added to the database:')
    new_users = [new_user]
    list_one(new_users)
    while True:
        print('\nDo you wish to proceed?\n1. Yes\n2. Cancel')
        option=input('Input:')
        if(option=='1'):
            users.append(new_user)
            break
        elif(option=='2'): return False
        else: print('Invalid option selected, try again...')
    save(users)
    print('\n%s has been added to the user database. Account type=[%s]' %(new_user['username'], new_user['type']))
    return False


def manager_register():
    while True:
        username = input("\nUsername (input 'back' to return to the main menu):")
        result = re.search(' ', username)
        if (result != None): print('No spaces allowed, try again...')
        elif(username == ''): print('Username cannot be an empty string, try again...')
        else: break
    for user in users:
        if(user['username']==username):
             print('Username taken, try again...')
             if(manager_register()==False):
                 return False
        if(username=='back'):
            return False
    while True:
        password = getpass.getpass('Password:')
        result = re.search(' ', password)
        if (result != None): print('No spaces allowed, try again...')
        elif (password == ''):
            print('Password cannot be an empty string, try again...')
        else:
            break
    name = input('Name:')
    lastname = input('Lastname:')

    new_user = {
        "username": "",
        "password": "",
        "name": "",
        "lastname": ""
    }
    new_user['username'] = username
    new_user['password'] = password
    new_user['name'] = name
    new_user['lastname'] = lastname
    new_user['type'] = 'Seller'
    print('\nUser will be added to the database:')
    new_users = [new_user]
    list_one(new_users)
    while True:
        print('\nDo you wish to proceed?\n1. Yes\n2. Cancel')
        option = input('Input:')
        if (option == '1'):
            users.append(new_user)
            break
        elif (option == '2'):
            return False
        else:
            print('Invalid option selected, try again...')
    save(users)
    print('\n%s has been added to the user database. Account type=[%s]' % (new_user['username'], new_user['type']))
    return False