import sys
sys.setrecursionlimit(10**5)

N=7

edges=[[3,6],[0],[3,4],[],[],[],[]]
deg=[1,0,0,2,1,0,1]

while 1:
    s=int(input())-1
    e=int(input())-1
    if s==e==-1:
        break
    edges[s]+=e,
    deg[e]+=1

from heapq import*

hq=[]

for i in range(N):
    if deg[i]<1:
        heappush(hq,i)

a=[]

while hq:
    n=heappop(hq)
    a+=n+1,
    for e in edges[n]:
        deg[e]-=1
        if deg[e]<1:
            heappush(hq,e)

if len(a)!=N:
    print('Cannot complete these tasks. Going to bed.')
else:
    print(*a)