N,M=map(int,input().split())

edges=[[]for _ in[0]*-~N]
edges_r=[[]for _ in[0]*-~N]
deg=[0]*-~N
deg_r=deg[:]
c=[0]*-~N
c_r=c[:]
db=[]

for _ in[0]*M:
    s,e=l=sorted(map(int,input().split()))
    db+=l,
    edges[s]+=e,
    edges_r[e]+=s,
    deg[e]+=1
    deg_r[s]+=1

from collections import deque

dq=deque()

for i in range(1,N+1):
    if deg[i]<1:dq+=i,;c[i]=1

while dq:
    n=dq.popleft()
    for e in edges[n]:
        c[e]+=c[n]
        deg[e]-=1
        if deg[e]<1:
            dq+=e,

for i in range(1,N+1):
    if deg_r[i]<1:dq+=i,;c_r[i]=1

while dq:
    n=dq.popleft()
    for e in edges_r[n]:
        c_r[e]+=c_r[n]
        deg_r[e]-=1
        if deg_r[e]<1:
            dq+=e,

mv=0

for s,e in db:
    mv=max(mv,c[s]*c_r[e])

print(mv)