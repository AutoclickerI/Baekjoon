def a(n):
    if n == 1:
        return ['1 3']
    return b(n-1) + ['1 3'] + d(n-1)
def b(n):
    if n == 1:
        return ['1 2']
    return a(n-1) + ['1 2'] + f(n-1)
def c(n):
    if n == 1:
        return ['2 1']
    return d(n-1) + ['2 1'] + e(n-1)
def d(n):
    if n == 1:
        return ['2 3']
    return c(n-1) + ['2 3'] + a(n-1)
def e(n):
    if n == 1:
        return ['3 1']
    return f(n-1) + ['3 1'] + c(n-1)
def f(n):
    if n == 1:
        return ['3 2']
    return e(n-1) + ['3 2'] + b(n-1)
n = int(input())
print(2**n-1)
for h in a(n):
    print(h)