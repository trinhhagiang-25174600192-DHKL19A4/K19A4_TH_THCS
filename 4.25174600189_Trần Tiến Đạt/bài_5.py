n = int(input("Nhập số: "))

dao = 0
while n != 0:
    du = n % 10
    dao = dao * 10 + du
    n = n // 10

print("Số đảo:", dao)