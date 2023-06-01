n = int(input())
if n < 100:
    print(n)
else:
    num = 99
    for i in range(100, n + 1):
        a = list(map(int, list(str(i))))
        if a[0] - a[1] == a[1] - a[2]:
            num += 1
    print(num)