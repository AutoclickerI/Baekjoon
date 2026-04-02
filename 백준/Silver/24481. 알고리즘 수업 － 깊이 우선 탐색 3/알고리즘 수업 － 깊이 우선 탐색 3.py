import sys
sys.setrecursionlimit(2*10**5)

[N,M,R],*l=[map(int,i.split())for i in open(0)]

edges=[[]for _ in[0]*-~N]

for u,v in l:
    edges[u]+=v,
    edges[v]+=u,

v=[-1]*-~N

def DFS(n,d):
    v[n]=d
    for e in sorted(edges[n]):
        if v[e]<0:
            DFS(e,d+1)

DFS(R,0)

print(*v[1:])