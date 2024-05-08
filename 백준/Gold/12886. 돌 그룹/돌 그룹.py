d={}
from collections import deque

dq=deque([(*sorted(map(int,input().split())),)])

while dq:
    p,q,r=dq.popleft()
    if p==q==r:
        exit(print(1))
    for p,q,r in map(sorted,[[p*2,q-p,r],[p*2,q,r-p],[p,q*2,r-q]]):
        if(p,q,r)not in d:
            d[p,q,r]=1
            dq.append((p,q,r))
print(0)