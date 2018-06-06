a = 1
b = 1
n = 0
for i in range(4):
    n = a + b
    a = b
    b = n
    
    print("Month {0}: {1} pair(s) of rabbit".format(n-1, n))

#please suggest if there is a better way to generate fibonnaci sequence and of course there is :)
