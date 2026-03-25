def nhan_an_do(a, b):
    ket_qua = 0

    dau = 1 if (a >= 0 and b >= 0) or (a < 0 and b < 0) else -1
    a = abs(a)
    b = abs(b)

    while b > 0:
        if b % 2 != 0:
            ket_qua = ket_qua + a
        a = a * 2
        b = b // 2

    return ket_qua * dau


m = int(input("Nhập a: "))
n = int(input("Nhập b: "))

print("Kết quả:", nhan_an_do(m, n))