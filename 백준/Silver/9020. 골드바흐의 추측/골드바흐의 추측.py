def l(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
for i in range(int(input())):
    n = int(int(input())/2)
    a = 0
    while True:
        if l(n - a) == True and l(n + a) == True:
            break
        a += 1
    print(f'{n - a} {n + a}')