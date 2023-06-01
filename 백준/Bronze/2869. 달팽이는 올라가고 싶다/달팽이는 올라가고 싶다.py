a = list(map(int, input().split()))
b = a[2] // (a[0] - a[1]) - 1 - a[1]
c = a[2] - b * (a[0] - a[1])
while True:
    b += 1
    c -= a[0]
    if c < 1:
        break
    c += a[1]
print(b)