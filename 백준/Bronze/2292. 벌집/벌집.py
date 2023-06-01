a = int(input()) - 2
if a == -1:
    print(1)
else:
    a = a // 6
    b = 0
    c = 2
    d = 2
    while a > b:
        b += d
        d += 1
        c += 1
    print(c)