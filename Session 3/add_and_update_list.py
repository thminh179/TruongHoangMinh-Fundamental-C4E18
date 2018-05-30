hobby=["car", "tech", "grill"]

# #add
# add = input("Name one thing you want to add. ")

# hobby.append(add)

# print("here are your favorite things so far:", end='')
# print((*hobby), sep=', ')

# #update
for index, item in enumerate(hobby):
    print("{0}. {1}".format(index+1, item))

position = int (input("Which position do you want to update?"))
new = input("What is your new favorite thing?")

hobby[position-1] = new
for index, item in enumerate(hobby):
    print("{0}. {1}".format(index+1, item))


