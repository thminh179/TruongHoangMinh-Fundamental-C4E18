# nhập vào số cạnh, vẽ là hình có số cạnh tương ứng
from turtle import *

canh = int (input("Nhap so canh:"))

speed(-1)
shape("turtle")
color("green")

for i in range (canh):
    forward(50)
    left(360/canh)

mainloop()