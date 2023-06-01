a = list(map(int, input().split()))
def l(n):
    if n == 1:
        return 0
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return n
for i in range(a[0], a[1] + 1):
    if l(i) != 0:
        print(l(i))