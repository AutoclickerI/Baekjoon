import sys
sys.setrecursionlimit(2*10**5)

[N],*l=[map(int,i.split())for i in open(0)]
edges=[[]for _ in[0]*-~N]

for s,e in l:
    edges[s]+=e,
    edges[e]+=s,

v=[0]*-~N
r=0
def DFS(n,depth):
    global r
    v[n]=1
    f=1
    for e in edges[n]:
        if v[e]<1:
            f=0
            DFS(e,depth+1)
    if f:
        r+=depth

DFS(1,0)

print('NYoe s'[r%2::2])