import sys
sys.setrecursionlimit(9**9)

[N,W],*l=[map(int,i.split())for i in open(0)]

edges=[[]for _ in[0]*-~N]

for s,e in l:
    edges[s]+=e,
    edges[e]+=s,

v=[0]*-~N
r=0
def DFS(n):
    global r
    f=1
    v[n]=1
    for e in edges[n]:
        if v[e]<1:
            DFS(e)
            f=0
    r+=f

DFS(1)
print(W/r)