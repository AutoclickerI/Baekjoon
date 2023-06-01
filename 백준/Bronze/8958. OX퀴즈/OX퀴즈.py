for i in range(int(input())):
    a = input()
    b = 1
    c = 0
    for j in range(len(a)):
        if a[j] == 'O':
            c += b
            b += 1
        else:
            b = 1
    print(c)
            