input()
a = list(map(int, input().split()))
b = list(set(a))
b.sort()
c = {b[i] : i for i in range(0, len(b))}
for i in a:
    print(c[i], end = ' ')