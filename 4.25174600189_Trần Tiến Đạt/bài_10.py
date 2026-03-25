#in số nguyên tố từ 1->n
n = int(input("Nhập n: "))

for x in range(2, n+1):
    la_so_nguyen_to = True
    for i in range(2, x):
        if x % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        print(x, end=" ")

#in số hoàn hảo từ 1->n
n = int(input("Nhập n: "))

for x in range(1, n+1):
    tong = 0
    for i in range(1, x):
        if x % i == 0:
            tong = tong + i
    if tong == x:
        print(x, end=" ")