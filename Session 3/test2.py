#list (array)

#create:
menu =[
    "Mi Tom",
    "Pho",
    "Salad",
]
# print (*menu, sep=", ")


#them phan tu vao list:

menu.append("Banh Muot")
print((*menu), sep=', ')
print(len(menu))

# first_item = menu[-1]
# print(first_item)

# for i in range (len(menu)):
#     # print((i+1),'. ',menu[i], sep='') #sep='' dùng để loại bỏ dấu cách giữa các phần tử = cách chèn xâu rỗng
#     print("{0}. {1}".format(i, menu[i])) #string formatting: i sẽ vào vị trí 0; menu[i] vào vị trí 1

# print("**********************")
# for index, item in enumerate(menu):
#     print("{0}. {1}".format(index+1, item))

# print("**********************")
# for item in menu:
#     print(item)

#update menu
menu [2] = "cua"
print(*menu, sep=', ')