a = list(map(int, input().split()))
b = []
for i in range(a[0]):
    b.append(input())
def q(b):
    c = [0, 0]
    F1 = 'B'
    for i in range(8):
        F = F1
        if F == 'B':
            F1 = 'W'
        else:
            F1 = 'B'
        for j in range(8):
            if F == 'B':
                F = 'W'
                if b[i][j] == F:
                    c[0] += 1
            else:
                F = 'B'
                if b[i][j] == F:
                    c[0] += 1
    F1 = 'W'
    for i in range(8):
        F = F1
        if F == 'B':
            F1 = 'W'
        else:
            F1 = 'B'
        for j in range(8):
            if F == 'B':
                F = 'W'
                if b[i][j] == F:
                    c[1] += 1
            else:
                F = 'B'
                if b[i][j] == F:
                    c[1] += 1
    c.sort()
    return c[0]
c = []
for i in range(a[0] - 7):
    for j in range(a[1] - 7):
        d = b.copy()
        d = d[i:i + 8]
        for k in range(len(d)):
            d[k] = d[k][j:j + 8]
        c.append(q(d))
c.sort()
print(c[0])