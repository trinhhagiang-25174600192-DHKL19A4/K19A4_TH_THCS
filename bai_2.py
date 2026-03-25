m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
if m < n:
    X = m
    m = n
    n = X
while m != n:
    r = m - n
    if r > n:
        m = r
    else:
        m = n
        n = r

print("UCLN của m và n là:",m)