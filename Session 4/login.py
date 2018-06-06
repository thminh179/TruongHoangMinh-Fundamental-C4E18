# username == "minh"
# password == "123"

# attempt = 0

# username = input ("Username: ")

# while username == "minh":

#     password = input("Password: ")

#     if password == "123":
#         print ("welcome")
#         break

#     else:
#         attempt += 1
#         if attempt == 3:
#             print ("locked")
#             break

#correction by TA:

count = 0

while True:

    username = input("Username: ")
    if username == "c4e":
        password = input("Password: ")
        if password == "codethechange":
            print("welcome")
            break
        else:
            print("Password incorrect")
    else: print ("incorrect username") 

    count += 1
    if count == 3:
        print ("failed to login 3 times. Go away")
        break       


 
