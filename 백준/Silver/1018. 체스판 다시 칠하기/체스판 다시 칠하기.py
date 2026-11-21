a = list(map(int, input().split()))
b = []
for i in range(a[0]):
    b.append(input())
def q(b):
    c = [0, 0]
    d = ['BWBWBWBW', 'WBWBWBWB']
    for i in range(8):
        for j in range(8):
            if b[i][j] == d[i%2][j]:
                c[0] += 1
    for i in range(8):
        for j in range(8):
            if b[i][j] == d[(i+1)%2][j]:
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