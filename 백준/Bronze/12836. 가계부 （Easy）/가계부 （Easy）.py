import sys
input = sys.stdin.read

def update(tree, i, x, N):
    while i <= N:
        tree[i] += x
        i += i & -i

def query(tree, i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= i & -i
    return res

data = input().split()
N, Q = map(int, data[:2])
tree = [0] * (N + 1)

idx = 2
out = []

for _ in range(Q):
    t = int(data[idx])
    if t == 1:
        p = int(data[idx + 1])
        x = int(data[idx + 2])
        update(tree, p, x, N)
        idx += 3
    else:
        p = int(data[idx + 1])
        q = int(data[idx + 2])
        out.append(str(query(tree, q) - query(tree, p - 1)))
        idx += 3

print('\n'.join(out))
