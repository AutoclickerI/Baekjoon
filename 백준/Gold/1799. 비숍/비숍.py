n=int(input())
l=[[*map(int,input().split())]for _ in[0]*n]
V1=[(i,j)for i in range(n)for j in range(n)if l[i][j]==1 and (i+j)%2]
V2=[(i,j)for i in range(n)for j in range(n)if l[i][j]==1 and (i+j)%2-1]
m=[0]
n=[n]
def find(x,y):
    if l[x][y]==1:return 1
    for p,q in[(1,1),(1,-1),(-1,1),(-1,-1)]:
        z,a=x,y
        z+=p;a+=q
        while min(z,a)>=0 and max(z,a)<=n[0]-1:
            if l[z][a]==2:
                return 0
            z+=p;a+=q
    return 1
def DFS(N,M):
    if N==len(V1):m[0]=max(m[0],M);return
    for i in range(2,0,-1):
        P,Q=V1[N]
        l[P][Q]=i
        if find(P,Q):
            DFS(N+1,M+i-1)
DFS(0,0)
ans=m[0]
m=[0]
def DFS(N,M):
    if N==len(V2):m[0]=max(m[0],M);return
    for i in range(2,0,-1):
        P,Q=V2[N]
        l[P][Q]=i
        if find(P,Q):
            DFS(N+1,M+i-1)
DFS(0,0)
print(ans+m[0])