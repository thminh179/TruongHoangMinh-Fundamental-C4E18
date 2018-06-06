bacteria = int (input("How many B bacterias are there? "))

time = int (input("How much time in minutes will we wait? "))

if time % 2 != 0:
    time = time - 1

replicate = bacteria * time

print ("After {0} minutes, we whould have {1} bacterias".format(time, replicate))