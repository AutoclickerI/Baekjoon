import sys
sys.setrecursionlimit(2*10**5)

[N,M,R],*l=[map(int,i.split())for i in open(0)]

v=[0]*N
edges=[[]for _ in[0]*N]
for s,e in l:
    edges[s-1]+=e-1,
    edges[e-1]+=s-1,

c=1
def DFS(n):
    global c
    v[n]=c
    c+=1
    for e in sorted(edges[n]):
        if v[e]<1:
            DFS(e)

DFS(R-1)
print(*v)