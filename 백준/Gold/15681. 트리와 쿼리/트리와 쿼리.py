import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N,R,Q=map(int,input().split())

edges=[[]for _ in[0]*-~N]

for _ in[0]*~-N:
    u,v=map(int,input().split())
    edges[u]+=v,
    edges[v]+=u,

v=[0]*-~N

def DFS(n):
    c=1
    v[n]=1
    for ne in edges[n]:
        if v[ne]<1:
            c+=DFS(ne)
    v[n]=c
    return c

DFS(R)

for _ in[0]*Q:
    print(v[int(input())])