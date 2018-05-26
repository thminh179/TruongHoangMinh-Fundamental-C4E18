n = int (input("Input a number:"))

m = range (1,n+1)
for i in range (1,n+1):
    for j in range (1,n+1):        
        print( m[j-1]*i ,' ', end=" ")
    print()