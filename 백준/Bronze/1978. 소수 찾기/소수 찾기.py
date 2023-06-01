input()
b = list(map(int, input().split()))
c = 0
def i(n):
    if n == 1:
        return 0
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1
for d in b:
    c += i(d)
print(c)