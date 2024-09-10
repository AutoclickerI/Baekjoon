import sys
sys.setrecursionlimit(2*10**5)
input=sys.stdin.readline
N,Q=map(int,input().split())
edges=[[]for _ in[0]*-~N]
for _ in[0]*~-N:
    u,v=map(int,input().split())
    edges[u]+=v,
    edges[v]+=u,
*S,=map(int,input().split())
parent=[0]*-~N
decendent=[[]for _ in[0]*-~N]
visited=[0]*-~N
def DFS(n):
    visited[n]=1
    for i in edges[n]:
        if not visited[i]:
            decendent[n]+=i,
            parent[i]=n
            DFS(i)
DFS(1)
def water(n,w):
    absorb=min(w,S[n-1])
    w-=absorb
    S[n-1]+=absorb
    if decendent[n] and (downstream:=w//len(decendent[n])):
        for i in decendent[n]:
            water(i,downstream)
for _ in[0]*Q:
    q,*l=map(int,input().split())
    if q==2:
        print(S[l[0]-1])
    else:
        water(l[0],l[1])