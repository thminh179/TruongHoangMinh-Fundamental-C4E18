flock = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Minh and these are my sheeps' size", flock)

maxsize = max(flock)
print("Now my biggest sheep has size", maxsize, ",let's shear it")

sheer = flock.index(maxsize)
flock [sheer] = 8
print ("After shearing, here is my flock", flock )

total = 0

for i in range (3):
    for j in range (len(flock)):
        flock[j]+=50
        if i == 2:
            total += flock[j]
    print ("Month",i+1,":")
    print ("One month has passed, now here is my flock: \n",flock)
    while i < 2:
        maxsize = max(flock)
        sheer = flock.index(maxsize)
        flock[sheer]=8
        print ("Now my biggest sheep size", maxsize,"let's shear it")
        print ("After shearing here is my flock: ", flock)
        break

print ("my flock size in total:", total)
print (" I would get: ", 2*total)

