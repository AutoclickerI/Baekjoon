import sys
#input=sys.stdin.readline

N=int(input())

v=[[*map(int,input().split())]for _ in[0]*N]

mv=max([*zip(*v)][0])

idxs=[[]for _ in[0]*(mv+2)]

for idx,(i,t)in enumerate(v,1):
    idxs[i]+=idx,

edges=[[]for _ in[0]*-~N]
deg=[0]*-~N
c=[0]*-~N
x=[0]*-~N

for idx,(i,t)in enumerate(v,1):
    for e in idxs[i+1]:
        edges[idx]+=e,
        deg[e]+=1
    c[idx]=t

from collections import deque

dq=deque()

for i in idxs[1]:dq+=i,;x[i]=c[i]

while dq:
    n=dq.popleft()
    for e in edges[n]:
        x[e]=max(x[e],(e-n)**2+x[n]+c[e])
        deg[e]-=1
        if deg[e]<1:
            dq+=e,
print(max(x))