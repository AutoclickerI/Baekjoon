a = []
for i in range(int(input())):
    a.append(list(map(int, input().split())))
for b in sorted(a):
    print(f'{b[0]} {b[1]}')
