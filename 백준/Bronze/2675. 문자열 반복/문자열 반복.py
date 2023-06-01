for i in range(int(input())):
    b = input().split(' ')
    c = ''
    for j in range(len(b[1])):
        c += int(b[0]) * b[1][j]
    print(c)