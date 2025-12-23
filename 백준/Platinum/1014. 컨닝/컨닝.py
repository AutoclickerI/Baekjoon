def DFS(n):
    v[n]=1
    for ep in o[n]:
        if e.get(ep)==None or v.get(e[ep],0)<1 and DFS(e[ep]):
            e[ep]=n
            return 1
    return 0

for T in[0]*int(input()):
    N,M=map(int,input().split())
    b=[input()for _ in[0]*N]
    o={}
    e={}
    for y in range(N):
        for x in range(M):
            for dy,dx in(-1,-1),(-1,1),(0,-1),(0,1):
                ny,nx=y+dy,x+dx
                if 0<=ny<N and 0<=nx<M and b[y][x]==b[ny][nx]=='.':
                    if x%2<1:
                        o[y,x]=o.get((y,x),[])
                        o[y,x]+=(ny,nx),
                    else:
                        o[ny,nx]=o.get((ny,nx),[])
                        o[ny,nx]+=(y,x),
    a=0
    for i in o:
        v={}
        a+=DFS(i)
    print(sum(i.count('.')for i in b)-a)