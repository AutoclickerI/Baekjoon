import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())
edges=[[]for _ in[0]*-~N]
for _ in[0]*M:
    a,b,c=map(int,input().split())
    edges[a]+=(b,c),

from heapq import*
v=[float('inf')]*-~N
hqs=[[]for _ in[0]*-~N]
hqs[1]+=0,

l=[(0,1)]
for c,n in l:
    if v[n]<c:
        continue
    for e,d in edges[n]:
        nc=c+d
        if nc<v[e]:
            heappush(hqs[e],-nc)
            while K<=len(hqs[e]):
                v[e]=min(v[e],-heappop(hqs[e]))
            l+=(nc,e),
for i in range(1,N+1):
    while K<=len(hqs[i]):
        v[i]=min(v[i],-heappop(hqs[i]))
    print(-(float('inf')==v[i])or v[i])