def a(n):
    for i in range(1, n + 1):
        b = list(map(int, list(str(i))))
        if n == i + sum(b):
            return i
    return 0
print(a(int(input())))