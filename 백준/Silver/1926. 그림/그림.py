import sys
sys.setrecursionlimit(9**9)
from collections import*
def DFS(y,x):
    f=1
    v[y][x]=0
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        if M>x+dx>=0<=y+dy<N and v[y+dy][x+dx]:
            v[y+dy][x+dx]=0
            f+=DFS(y+dy,x+dx)
    return f
N,M=map(int,input().split())
v=eval('[*map(int,input()[::2])],'*N)
c=[0]
for i in range(N):
    for j in range(M):
        if v[i][j]:
            c+=DFS(i,j),
print(len(c)-1,max(c))