#idea:
#nhập vào 1 số từ 0->100, máy đoán số đó
# chia đôi (0,100), nếu số đó lớn hơn TB thì dịch giá trị min = TB, nhỏ hơn TB thì dịch giá trị max = TB
# lặp lại đến khi tìm ra số 

print("Guess your number game")
print("Now think of a number from 0-100, then press Enter ")
input() #enter để tiếp tục

print("""
All you have to do is to answer my guess
'c' if my guess is Correct
's' if my guess is Smaller
'l' if my guess is larger
""") #3 dấu nháy để print xuống dòng các line

low = 0
high = 101

while True:
    mid = (low+high) // 2

    ans = input ("Is {0} your number: ".format(mid)).lower()

    if ans == 'c':
        print("I knew it!")
        break

    elif ans == 's':
        low = mid
    elif ans == 'l':
        high = mid



