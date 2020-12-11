test.py - used for testing specific parts of the code
notes.txt - some important notes acquired throughout writing this code


MODULES

main.py (main)

books=>boolist.py (load, save) // load() :: loads all books from database=>books.json // save() :: self-explanatory(s/e)
     =>book.py (length_list, show_list, sort, search, register, edit) // length_list() :: returns a list in which every element shows the value of the longest string for that key //
     // show_list() :: prints a table of all the books from database=>books.json // register() :: adds a book to database=>books.json // sort(),search(),edit() :: (s/e)

users=>userlist.py (load, save) // load() :: loads all users from database=>users.json // save() :: self-explanatory(s/e)
     =>user.py (login, register, length_list, show_list) // register() :: adds a user to database=>users.json // login(),length_list(),show_list() :: (s/e)
