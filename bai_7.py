chon = -1
while chon != 0:
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    chon = int(input("Nhập lựa chọn: "))

    if chon == 0:
        break

    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))

    if chon == 1:
        print("Kết quả:",a + b)
    elif chon == 2:
        print("Kết quả:",a - b)
    elif chon == 3:
        print("Kết quả:",a * b)
    elif chon == 4:
        if b != 0:
            print("Kết quả:",a / b)
        else:
            print("Không chia được")
    else:
        print("Lựa chọn không hợp lệ!")