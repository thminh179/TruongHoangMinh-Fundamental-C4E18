store = ["T-shirt", "Sweater"]

nhap = input("Welcome to our shop, what do you want (C, R, U, D)? ").lower()

if nhap == 'c':
    add = input("Enter new item")
    store.append(add)
    print ("Enter new item:", end='')
    print ("Our items:", *store, sep=', ')

if nhap == 'r':
    print ("Enter new item:", end='')
    print ("Our items:",*store, sep=', ')

if nhap == 'u':
    pos = int( input("Update position? "))
    new = input("New item?")
    store[pos-1] = new
    print ("Our items:",*store, sep=', ') 

if nhap == 'd':
   delete = int (input ("Delete position"))
   del store[delete-1]
   print ("Our items:",*store, sep=', ')