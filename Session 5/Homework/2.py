number = [1, 6 ,8, 1, 2, 1, 5, 6]

#with count()
# n = int(input("Enter a number: "))

# count = number.count(n)

# print ("{0} appears {1} time(s) in my list".format(n, count))

#without count()
n = int(input("Enter a number: "))
count = 0
for i in number:
    if (i == n):
        count += 1

print ("{0} appears {1} time(s) in my list".format(n, count))
