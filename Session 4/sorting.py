#sắp xếp dãy số
#idea
# trích giá trị min từ list, thêm vào 1 list mới
# xóa giá trị min cũ trong list cũ
# lặp

initial = [-5, 10, 4, 7]

sort = []

while True:
    smallest = min(initial)
    sort.append(smallest)
    initial.remove(smallest)

    if len(initial) == 0:
        break

print (*sort)



 