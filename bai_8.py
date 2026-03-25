i = 2
while i <= 1000:
    j = 2
    la_snt = 1

    while j * j <= i:
        if i % j == 0:
            la_snt = 0
            break
        j = j + 1

    if la_snt == 1:
        print(i, end=" ")
    i = i + 1