a = []
for i in range(9):
    a.append(int(input()))
b = a.copy()
b.sort()
print(b[-1])
print(a.index(b[-1]) + 1)