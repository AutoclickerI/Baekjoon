import sys
sys.setrecursionlimit(9**9)
from collections import*
def DFS(y,x):
    f=v[y][x]
    v[y][x]=0
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        if M>x+dx>=0<=y+dy<N and v[y+dy][x+dx]:
            v[y+dy][x+dx]=0
            f=1
            DFS(y+dy,x+dx)
    return f
for _ in[0]*int(input()):
    N,M=map(int,input().split())
    v=eval('[1]*M,'*N)
    for i in range(N):
        for j,k in enumerate(input()):
            v[i][j]=k<'.'
    print(sum(DFS(i,j)for i in range(N)for j in range(M)if v[i][j]))