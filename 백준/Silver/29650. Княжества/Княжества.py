from collections import deque

d = {'M':[]}
e = {'M':1}
def f(x,n):
    q = deque([x])
    while q:
        u = q.popleft()
        if e[u]: 
            if n<1: return u
            n -= 1
        q+=d[u]
    return '-'
for i in[*open(0)][1:]:
    x,*y = i.split()
    if x=='-': e[y[0]] = 0
    elif x=='+':
        d[y[0]] += y[1],
        d[y[1]] = []
        e[y[1]] = 1
    else: print(f('M',int(y[0])-1))