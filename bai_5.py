n = int(input("Nhập n: "))
dao = 0
while n > 0:
    so_du = n % 10
    dao = dao * 10 + so_du
    n = n // 10

print("Kết quả:",dao)