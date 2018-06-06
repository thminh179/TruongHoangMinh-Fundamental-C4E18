#dictionary: {} bao gom cac cap key - value

person = {
    #"key": value
    "name": "Quy",
    "age": 20,
    "hobby": ["manga", "code"]
}

print (person)

#truy van 1 gia tri (value) trong dictionary
name = person['name']
# print(name)

#them 1 key vao dictionary
person['length'] = 20 #cu phap: <dictionary>['<key>'] = <value>
# print(person)

#update
person['length'] = 10
# print(person)

#delete
del person['length']

#kiem tra xem 1 key co trong phan tu hay khong: if <key> in <dict> 
# key = 'length'
# if key in person:
#     print(person[key])
# else: print ('not found')

#xuat cac key, value trong dictionary
for k in person:
    print (k, person[k])

## or
for k, v in person.items():
    print (k, v)  

#duyet va xuat rieng cac value: .values()
for v in person.values():
    print(v)

  

