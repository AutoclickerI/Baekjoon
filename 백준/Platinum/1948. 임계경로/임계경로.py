import sys
input=sys.stdin.readline
sys.setrecursionlimit(2*10**5)

N=int(input())

edges=[[]for _ in[0]*-~N]
deg=[0]*-~N
c={}
cnt={}
v=[0]*-~N
backedges=[[]for _ in[0]*-~N]

for _ in[0]*int(input()):
    s,e,m=map(int,input().split())
    if(s,e)not in c:
        edges[s]+=e,
        deg[e]+=1
    if c.get((s,e),0)==m:
        cnt[s,e]=cnt.get((s,e),0)+1
    if c.get((s,e),0)<m:
        c[s,e]=m
        cnt[s,e]=1

S,E=map(int,input().split())

from collections import deque

dq=deque([S])
v[S]=0

while dq:
    n=dq.popleft()
    for e in edges[n]:
        deg[e]-=1
        nv=v[n]+c[n,e]
        if nv==v[e]:
            backedges[e]+=n,
        if v[e]<nv:
            v[e]=nv
            backedges[e]=[n]
        if deg[e]<1:
            dq+=e,

print(v[E])
ans=0
vi=[0]*-~N
def DFS(n):
    global ans
    for e in backedges[n]:
        ans+=1
        if vi[e]<1:
            vi[e]=1
            DFS(e)
DFS(E)
print(ans)