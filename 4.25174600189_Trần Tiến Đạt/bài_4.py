n = int(input("Nhập số lượng: "))

for i in range(n):
    x = int(input("Nhập số: "))
    if x < 0:
        print("Nếu gặp số âm, kết thúc!")
        break