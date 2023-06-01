a = {}
for i in range(int(input())):
    n = input()
    if len(n) in a:
        a[len(n)].append(n)
    else:
        a[len(n)] = [n]
b = list(a.keys())
b.sort()
for c in b:
    a[c] = list(set(a[c]))
    a[c].sort()
    print('\n'.join(a[c]))