import sys
sys.setrecursionlimit(2*10**5)

input=sys.stdin.readline

N=int(input())

edge=[[]for _ in[0]*-~N]

for _ in[0]*~-N:
    s,*l=map(int,input().split())
    for i,j in zip(*[iter(l)]*2):
        edge[s]+=(i,j),
        edge[i]+=(s,j),

visited=[0]*-~N
def DFS(v,c):
    visited[v]=1
    mc=c
    mv=v
    for e,nc in edge[v]:
        if visited[e]<1:
            f_v,f_c=DFS(e,nc+c)
            if mc<f_c:
                mv=f_v
                mc=f_c
    return mv,mc

mv,_=DFS(1,0)
visited=[0]*-~N

print(DFS(mv,0)[1])