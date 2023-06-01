a = []
for i in range(int(input())):
    a.append(list(map(int, input().split())))
for b in sorted(a, key = lambda x : (x[1], x[0])):
    print(f'{b[0]} {b[1]}')