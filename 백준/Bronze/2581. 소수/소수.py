a = int(input())
b = int(input())
c = []
def l(n):
    if n == 1:
        return 0
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return n
for i in range(a, b + 1):
    if l(i) != 0:
        c.append(l(i))
try:
    d = c[0]
    print(sum(c))
    print(d)
except:
    print(-1)