from users.userlist import load, save

def login():

    users = load()
    username = input('Username:')
    password = input('Password:')
    #print(users) debug
    for user in users:
        if((user['username']==username) and (user['password']==password)):
            return user
    return False

