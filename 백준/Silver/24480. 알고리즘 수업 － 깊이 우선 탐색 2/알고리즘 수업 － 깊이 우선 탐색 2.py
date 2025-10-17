import sys
sys.setrecursionlimit(2*10**5)

N,M,R=map(int,input().split())

edges=[[]for _ in[0]*-~N]
for _ in[0]*M:
    s,e=map(int,input().split())
    edges[s]+=-e,
    edges[e]+=-s,
v=[0]*-~N

cnt=0

def DFS(n):
    global cnt
    cnt+=1
    v[n]=cnt
    for e in sorted(edges[n]):
        v[-e]or DFS(-e)

DFS(R)
print(*v[1:])