import sys
sys.setrecursionlimit(9**9)

[N],p,*l=[[*map(int,i.split())]for i in open(0)]
edges=[[]for _ in[0]*N]
for s,e in l:
    edges[s-1]+=e-1,
    edges[e-1]+=s-1,

v=[0]*N
o=v[:]
z=v[:]

def DFS(n):
    v[n]=1
    o[n]=p[n]
    q=float('inf')
    for e in edges[n]:
        if v[e]<1:
            DFS(e)
            z[n]+=max(z[e],o[e])
            o[n]+=z[e]

DFS(0)
print(max(o[0],z[0]))