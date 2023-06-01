while True:
    a = input().split(' ')
    if a[0] == a[1]:
        if a[1] == '0':
            break
    print(int(a[0]) + int(a[1]))