def f(n):
    if n == -1:
        return 1
    return int((1/5**0.5)*(((1+5**0.5)/2)**n - ((1-5**0.5)/2)**n))
for i in range(int(input())):
    n = int(input())
    print(f'{f(n - 1)} {f(n)}')