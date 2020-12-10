from users.userlist import load, save
import re,getpass

users = load()
n=len(users)

def login():

    print("\n/Project BOOKS by Santovac Stefan/")
    print('\n-Login-')
    username = input('Username:')
    password = getpass.getpass('Password:')
    #print(users) debug
    for user in users:
        if((user['username']==username) and (user['password']==password)):
            return user
    return False

def register():
    while True:
        username = input("\nUsername (input 'back' to return to the main menu):")
        result = re.search(' ', username)
        if (result != None): print('No spaces allowed, try again...')
        elif(username == ''): print('Username cannot be an empty string, try again...')
        else: break
    for user in users:
        if(user['username']==username):
             print('Username taken, try again...')
             if(register()==False):
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
    users.append(new_user)
    save(users)
    print('%s has been added to the user database. Account type=[%s]' %(new_user['username'], new_user['type']))
    return False

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
def show_list():
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