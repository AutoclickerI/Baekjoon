a = list(range(1, 10001))
b = []
def d(n):
    return n + sum(list(map(int, list(str(n)))))
for i in a:
    if d(i) in b:
        pass
    else:
        b.append(d(i))
for i in a:
    if i in b:
        pass
    else:
        print(i)