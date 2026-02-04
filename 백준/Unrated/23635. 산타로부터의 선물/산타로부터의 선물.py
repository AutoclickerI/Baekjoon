K,N,*A=map(int,open(0).read().split())
P=[0]
s = 0
for i in A:P+=P[-1]+i,
S = P[N]

INF = N + 5

lb = [INF] * (S + 2)
for i in range(N + 1):
    lb[P[i]] = i

for x in range(S - 1, -1, -1):
    if lb[x] > lb[x + 1]:
        lb[x] = lb[x + 1]

ans = 10**30

for m in range(1, S + 1):
    pos = 0
    ok = True
    for _ in range(K):
        target = P[pos] + m
        if target > S:
            ok = False
            break
        pos = lb[target]
        if pos >= INF:
            ok = False
            break
    if not ok:
        continue

    total = P[pos]
    cand = total - K * m
    if cand < ans:
        ans = cand

print(ans)