prime = int(input("Enter a number:"))

is_prime = True

for i in range (2, prime):
    if(prime % i == 0):
        is_prime = False
        break
    
if is_prime == True:
    print ("{0} is a prime number".format(prime))
else:
    print("{0} is not a prime number".format(prime))



    
