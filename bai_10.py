# Số nguyên tố
n = int(input("Nhập n: "))
i = 2
while i <= n:
    j = 2
    la_snt = 1
    while j * j <= i:
        if i % j == 0:
            la_snt = 0
            break
        j = j + 1
    if la_snt == 1:
        print(i, end="\n")
    i = i + 1
# Số hoàn hảo
n = int(input("Nhập n: "))
i = 1
while i <= n:
    tong = 0
    j = 1
    while j < i:
        if i % j == 0:
            tong = tong + j
        j = j + 1
    if tong == i:
        print("Số hoàn hảo là:",i, end="\n")
    i = i + 1
