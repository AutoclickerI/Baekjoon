import sys
sys.setrecursionlimit(9**9)
input=sys.stdin.readline

N=int(input())

edges=[[]for _ in[0]*-~N]
v=[0]*-~N
d=[[0,1]for _ in[0]*-~N]

for _ in[0]*~-N:
    s,e=map(int,input().split())
    edges[s]+=e,
    edges[e]+=s,

def DFS(n):
    v[n]=1
    for e in edges[n]:
        if v[e]<1:
            DFS(e)
            d[n][0]+=d[e][1]
            d[n][1]+=min(d[e])
            

DFS(1)
print(min(d[1]))