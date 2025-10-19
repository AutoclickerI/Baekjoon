N,M=map(int,input().split())
b=[input()[::2]for _ in[0]*N]

v=[M*[0]for _ in[0]*N]

def DFS(y,x,c):
    v[y][x]=c
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<M and v[ny][nx]<1 and'0'<b[ny][nx]:
            DFS(ny,nx,c)

def travel(y,x,dy,dx,c):
    if y<N and x<M:
        if v[y][x]==0:
            d,c=travel(y+dy,x+dx,dy,dx,c)
            return c and d+1,c
        if v[y][x]!=c:
            return 0,v[y][x]
    return 0,0

c=0
for y in range(N):
    for x in range(M):
        if v[y][x]<1 and'0'<b[y][x]:
            c+=1
            DFS(y,x,c)

edges=[]

for y in range(N):
    for x in range(M):
        if v[y][x]:
            for dy,dx in(1,0),(0,1):
                d,e=travel(y+dy,x+dx,dy,dx,v[y][x])
                if e and 1<d:
                    edges+=(d,e-1,v[y][x]-1),
edges.sort()

*p,=range(c)

def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]
ans=0
con=0
for v,s,e in edges:
    s,e=sorted([find(s),find(e)])
    if s-e:
        p[e]=s
        ans+=v
        con+=1
if con==c-1:
    print(ans)
else:
    print(-1)