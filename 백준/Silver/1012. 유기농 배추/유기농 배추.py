import sys
sys.setrecursionlimit(9**9)
for _ in[0]*int(input()):
    n,q,r=map(int,input().split())
    l=[[0]*n for _ in[0]*q]
    visited=[0]*n*q
    num=1
    update=0
    for _ in[0]*r:P,Q=map(int,input().split());l[Q][P]=1
    def DFS(y,x):
        global update
        if visited[y*n+x] or l[y][x]==0:return
        visited[y*n+x]=num
        for i,j in[[-1,0],[1,0],[0,1],[0,-1]]:
            DFS(max(0,min(y+i,q-1)),max(0,min(x+j,n-1)))
        update=1
    for x in range(n):
        for y in range(q):
            DFS(y,x)
            num+=update
            update=0
    print(num-1)