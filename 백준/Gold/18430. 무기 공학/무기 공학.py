[N,M],*b=[[*map(int,i.split())]for i in open(0)]
v=[M*[0]for _ in[0]*N]

def check(y,x,d):
    for dy,dx in d:
        ny,nx=y+dy,x+dx
        if not(0<=ny<N and 0<=nx<M and v[ny][nx]<1):
            return 0
    return 1
r=0
def backtrack(n,c):
    global r
    if n==N*M:
        r=max(r,c)
        return
    y,x=n//M,n%M
    if v[y][x]:
        backtrack(n+1,c)
        return
    for d in[(0,1),(1,0)],[(0,1),(-1,0)],[(0,-1),(1,0)],[(0,-1),(-1,0)]:
        if check(y,x,d):
            nc=c+b[y][x]*2
            v[y][x]=1
            for dy,dx in d:
                ny,nx=y+dy,x+dx
                nc+=b[ny][nx]
                v[ny][nx]=1
            backtrack(n+1,nc)
            v[y][x]=0
            for dy,dx in d:
                ny,nx=y+dy,x+dx
                v[ny][nx]=0
    backtrack(n+1,c)
backtrack(0,0)
print(r)