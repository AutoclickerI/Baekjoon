import sys
input=sys.stdin.readline

N,M=map(int,input().split())

edges=[[]for _ in[0]*-~N]
cost=[float('inf')]*-~N

for _ in[0]*M:
    u,v,c=map(int,input().split())
    edges[u]+=(v,c),
    edges[v]+=(u,c),

v=[0]*-~N
vc=[0]*-~N

vc[1]=1

from collections import*

dq=deque([(1,0,1)])

while dq:
    n,c,s=dq.popleft()
    if cost[n]<c:
        continue
    for e,q in edges[n]:
        if c<cost[e]:
            if c+1==cost[e]:
                v[e]+=v[n]+q*vc[n]
                vc[e]+=vc[n]
            else:
                v[e]=v[n]+q*vc[n]
                cost[e]=c+1
                vc[e]=vc[n]
                dq+=(e,c+1,n),

for i,j in zip(v[2:],vc[2:]):
    print(i*pow(j,-1,998244353)%998244353)