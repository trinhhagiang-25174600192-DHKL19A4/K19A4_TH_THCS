n = int(input("Nhập n: "))

if n < 2:
    print("Không phải là số nguyên tố")
else:
    la_snt = True
    for i in range(2, n):
        if n % i == 0:
            la_snt = False
            break

    if la_snt:
        print("Là số nguyên tố")
    else:
        print("Không phải là số nguyên tố")