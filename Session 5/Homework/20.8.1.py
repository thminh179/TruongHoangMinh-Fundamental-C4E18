word = input ("Enter a word: ").lower() 

count ={}

for letter in word:
    count[letter] = count.get(letter, 0) +1

for k, v in count.items():
    print (k, v)

