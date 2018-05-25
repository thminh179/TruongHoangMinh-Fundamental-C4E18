#drawing a maze
from turtle import *

speed (-1)
color ("green")

# for i in range (10, 300, 5):
#     forward(i)
#     left(90)

# or

length = 5

for i in range (40):
    forward (length)
    left (90)

    length = length + 5 # ~ length += 5
    

mainloop()


