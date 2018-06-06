abbdict = {
    'hc': 'Học',
    'ng': 'Người',
    'stt': 'Status',
    'lm': 'Lắm'
}

while True:

    for key in abbdict:
        print(key, end='\t') #\t = tab: cach nhau 1 tab
    print()

    abb = input("Enter an abbreviation: ")

    if abb in abbdict:
        print("Translation: ", abbdict[abb])
    else: 
        print ("not found")
        update = input("Do you want to contribute? (Y/N): ").lower()

        if update == "y":
            definition = input ("Add definition: ")
            abbdict[abb] = definition
            print(abbdict)
        
        else:
            print("Bye")
            break
    print("**************************")
