s = input("Nhap day so: ")

words = s.strip().split(" ")

number = []

for item in words:
    number.append(int(item)) # chuyển str trong words[] thành int, thêm vào number[]

print (number)

is_sorted = True

for i in range (len(number)-1):
    if number[i] > number[i+1]:
        is_sorted = False
        break

if is_sorted:
    print("Da sap xep")
else: print ("Chua sap xep")


