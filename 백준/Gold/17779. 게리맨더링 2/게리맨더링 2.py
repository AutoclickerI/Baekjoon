[N],*b=[[*map(int,i.split())]for i in open(0)]

def getarr(x,y,d1,d2):
    ret=[0]*5
    for r in range(1,N+1):
        for c in range(1,N+1):
            if 1<=r<x+d1 and 1<=c<=y and r+c<x+y:
                ret[0]+=b[r-1][c-1]
            elif 1<=r<=x+d2 and y<c<=N and y-x<c-r:
                ret[1]+=b[r-1][c-1]
            elif x+d1<=r<=N and 1<=c<y-d1+d2 and c-r<y-x-2*d1:
                ret[2]+=b[r-1][c-1]
            elif x+d2<r<=N and y-d1+d2<=c<=N and x+y+2*d2<r+c:
                ret[3]+=b[r-1][c-1]
            else:
                ret[4]+=b[r-1][c-1]
    return max(ret)-min(ret)

def paint(x,y,d1,d2):
    v=[N*[0]for _ in[0]*N]
    for r in range(1,N+1):
        for c in range(1,N+1):
            if 1<=r<x+d1 and 1<=c<=y and r+c<x+y:
                v[r-1][c-1]=1
            elif 1<=r<=x+d2 and y<c<=N and y-x<c-r:
                v[r-1][c-1]=2
            elif x+d1<=r<=N and 1<=c<y-d1+d2 and c-r<y-x-2*d1:
                v[r-1][c-1]=3
            elif x+d2<r<=N and y-d1+d2<=c<=N and x+y+2*d2<r+c:
                v[r-1][c-1]=4
            else:
                v[r-1][c-1]=5
    for i in v:print(*i)


m=float('inf')

for x in range(1,N+1):
    for y in range(1,N+1):
        for d1 in range(1,N+1):
            for d2 in range(1,N+1):
                if 1<=x<x+d1+d2<=N and 1<=y-d1<y<y+d2<=N:
                    m=min(m,getarr(x,y,d1,d2))

print(m)