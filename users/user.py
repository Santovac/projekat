from users.userlist import load, save

users = load()
n=len(users)

def login():

    print('\n-Login-')
    username = input('Username:')
    password = input('Password:')
    #print(users) debug
    for user in users:
        if((user['username']==username) and (user['password']==password)):
            return user
    return False

def register():
    username = input("\nUsername (input 'back' to return to the main menu):")
    for user in users:
        if(user['username']==username):
             print('Username taken, try again...')
             register()
        elif(username=='back'):
            return False
    password = input('Password:')
    name = input('Name:')
    lastname = input('Lastname:')
    type = input('Type (m/s):')
    new_user = {
        "username": "",
        "password": "",
        "name": "",
        "lastname": ""
    }
    #print('new users:', new_user)
    new_user['username']= username
    new_user['password'] = password
    new_user['name'] = name
    new_user['lastname'] = lastname
    if(type=='m'): new_user['type'] = 'Manager'
    else: new_user['type']= 'Seller'
    users.append(new_user)
    save(users)
    print('%s has been added to the user database as a %s' %(new_user['username'], new_user['type']))
    return False
