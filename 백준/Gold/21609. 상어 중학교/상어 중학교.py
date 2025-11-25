[N,M],*b=[[*map(int,i.split())]for i in open(0)]

def BFS(y,x,fill):
    v[y][x]=cnt
    cmp=b[y][x]
    l=[(y,x)]
    r=1
    rr=0
    for y,x in l:
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<N and v[ny][nx]<cnt and(b[ny][nx]in[0,cmp]):
                v[ny][nx]=cnt
                l+=(ny,nx),
                r+=1
                rr+=b[ny][nx]<1
    if fill:
        for y,x in l:b[y][x]=-2
    return r,rr

def fall():
    for x in range(N):
        for y in range(N)[::-1]:
            if b[y][x]!=-1:
                while y+1<N and b[y+1][x]==-2:
                    b[y+1][x]=b[y][x]
                    b[y][x]=-2
                    y+=1

def debug(n):
    for i in b:print(*i)
    print('-'*20,n)

ans=0
while 1:
    cnt=0
    v=[N*[0]for _ in[0]*N]
    pos=[]
    for y in range(N):
        for x in range(N):
            if 0<b[y][x] and v[y][x]<1:
                cnt+=1
                r,rr=BFS(y,x,0)
                if 1<r:
                    pos+=(r,rr,y,x),
    if[]==pos:
        break
    v=[N*[0]for _ in[0]*N]
    r,_,y,x=max(pos)
    BFS(y,x,1)
    ans+=r*r
    fall()
    b=[[*i]for i in zip(*[i[::-1]for i in b])]
    fall()
print(ans)