a = [[], []]
for i in range(3):
    b = input().split()
    a[0].append(b[0])
    a[1].append(b[1])
for i in range(2):
    a[i].sort()
    if a[i][1] == a[i][0]:
        a[i] = a[i][2]
    else:
        a[i] = a[i][0]
print(f'{a[0]} {a[1]}')