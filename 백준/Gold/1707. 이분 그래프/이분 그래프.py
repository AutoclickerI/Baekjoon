import sys
sys.setrecursionlimit(9**9)
input=sys.stdin.readline

def DFS(n,p):
    f=1
    visited[n]=p+1
    for e in edges[n]:
        if visited[e]<1:
            f&=DFS(e,p^1)
        elif visited[e]==p+1:
            f=0
    return f
for K in[0]*int(input()):
    V,E=map(int,input().split())
    edges=[[]for _ in[0]*V]
    for _ in[0]*E:
        s,e=map(int,input().split())
        edges[s-1]+=e-1,
        edges[e-1]+=s-1,
    visited=[0]*V
    f=1
    for i in range(V):
        if visited[i]<1:
            f&=DFS(i,0)
    if f:
        print('YES')
    else:
        print('NO')