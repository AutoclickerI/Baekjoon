import sys
sys.setrecursionlimit(9999)

N,L,R=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*N]

def DFS(y,x):
    v[y][x]=1
    ret=[(y,x)]
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        (p,q),(r,s)=sorted([(y,x),(ny,nx)])
        if 0<=ny<N and 0<=nx<N and v[ny][nx]<1 and(p,q,r,s)in e:
            ret+=DFS(ny,nx)
    return ret
cnt=0
while 1:
    e=set()
    for y in range(N):
        for x in range(N):
            for dy,dx in(1,0),(0,1):
                ny,nx=y+dy,x+dx
                if ny<N and nx<N and L<=abs(b[y][x]-b[ny][nx])<=R:
                    e|={(y,x,ny,nx)}
    if not e:
        break
    v=[N*[0]for _ in[0]*N]
    for y in range(N):
        for x in range(N):
            if v[y][x]<1:
                q=DFS(y,x)
                s=0
                for ny,nx in q:
                    s+=b[ny][nx]
                s//=len(q)
                for ny,nx in q:
                    b[ny][nx]=s
    cnt+=1
print(cnt)