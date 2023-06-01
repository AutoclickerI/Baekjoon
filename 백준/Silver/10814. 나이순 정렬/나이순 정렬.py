a = []
for i in range(int(input())):
    a.append(input().split())
b = list(set([int(a[i][0]) for i in range(len(a))]))
b.sort()
for i in b:
    for j in range(len(a)):
        if int(a[j][0]) == i:
            print(' '.join(a[j]))