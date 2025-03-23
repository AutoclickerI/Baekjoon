import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

N,M=map(int,input().split())

edges=[[]for _ in[0]*-~N]

v=[0]*-~N

for _ in[0]*M:
    s,e=map(int,input().split())
    edges[s]+=e,

a=[]
def DFS(n):
    for i in edges[n]:
        if v[i]<1:
            v[i]=1
            DFS(i)
    a.append(n)

for i in range(1,N+1):
    if v[i]<1:
        v[i]=1
        DFS(i)

print(*a[::-1])