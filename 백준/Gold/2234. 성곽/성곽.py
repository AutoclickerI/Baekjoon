[N,M],*b=[[*map(int,i.split())]for i in open(0)]
w=set()
for y in range(M):
    for x in range(N):
        for m,dy,dx in(1,0,-1),(2,-1,0),(4,0,1),(8,1,0):
            ny,nx=y+dy,x+dx
            if b[y][x]&m and 0<=ny<M and 0<=nx<N:
                s,e=sorted([(y,x),(ny,nx)])
                w.add((s,e))
v=[N*[0]for _ in[0]*M]
cnt=0
def BFS(y,x):
    l=[(y,x)]
    v[y][x]=cnt
    for y,x in l:
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            s,e=sorted([(y,x),(ny,nx)])
            if 0<=ny<M and 0<=nx<N and v[ny][nx]<1 and (s,e)not in w:
                v[ny][nx]=cnt
                l+=(ny,nx),
    return len(l)
d={}
for y in range(M):
    for x in range(N):
        if v[y][x]<1:
            cnt+=1
            d[cnt]=BFS(y,x)
mr=mv=max(d.values())
for y in range(M):
    for x in range(N):
        for dy,dx in(1,0),(0,1):
            ny,nx=y+dy,x+dx
            if ny<M and nx<N and v[ny][nx]!=v[y][x]:
                mv=max(mv,d[v[ny][nx]]+d[v[y][x]])
print(cnt,mr,mv)