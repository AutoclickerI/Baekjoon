a = []
for i in range(int(input())):
    a.append(list(map(int, input().split())))
for b in a:
    n = 1
    for i in range(len(a)):
        if b[0]<a[i][0] and b[1]<a[i][1]:
            n += 1
    print(n, end=' ')