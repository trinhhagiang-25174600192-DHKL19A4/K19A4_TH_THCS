n = int(input("Nhập n: "))
if n < 2:
    print("Không phải snt")
else:
    i = 2
    la_snt = 1
    while i <= n - 1:
        if n % i == 0:
            la_snt = 0
            break
        i = i + 1
    if la_snt == 1:
        print("Là snt")
    else:
        print("Không phải snt")