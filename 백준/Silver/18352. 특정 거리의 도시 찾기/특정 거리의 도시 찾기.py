import sys
input=sys.stdin.readline
N,M,K,X=map(int,input().split())
edges=[[]for _ in[0]*-~N]
for _ in[0]*M:
    s,e=map(int,input().split())
    edges[s]+=e,
from collections import deque
dq=deque([[0,X]])
v=[0]*-~N
a=[]
while dq:
    c,s=dq.popleft()
    if v[s]:
        continue
    v[s]=1
    if c==K:
        a+=s,
    elif c<K:
        for e in edges[s]:
            dq+=(c+1,e),
print(*sorted(a)or[-1])