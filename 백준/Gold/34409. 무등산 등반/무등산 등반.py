N,M=map(int,input().split())
x,y=map(int,input().split())
a,b,c=map(int,input().split())
v=[[*map(int,input().split())]for _ in[0]*N]

from heapq import*
h=[M*[1e9]for _ in[0]*N]
hq=[(0,x-1,y-1)]
h[x-1][y-1]=0

m=0

for y in range(N):
    for x in range(M):
        if m<v[y][x]:
            m=v[y][x]
            e=y,x

while hq:
    cost,y,x=heappop(hq)
    if h[y][x]<cost:
        continue
    if(y,x)==e:
        break
    for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<M:
            dv=v[ny][nx]-v[y][x]
            if dv==0:
                if h[y][x]+1<h[ny][nx]:
                    h[ny][nx]=h[y][x]+1
                    heappush(hq,(h[ny][nx],ny,nx))
            if 0<dv<=c:
                if h[y][x]+a*dv<h[ny][nx]:
                    h[ny][nx]=h[y][x]+a*dv
                    heappush(hq,(h[ny][nx],ny,nx))
            if -c<=dv<0:
                if h[y][x]-b*dv<h[ny][nx]:
                    h[ny][nx]=h[y][x]-b*dv
                    heappush(hq,(h[ny][nx],ny,nx))
else:
    exit(print(-1))
print(cost)