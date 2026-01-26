[N],*b=[[*map(int,i.split())]for i in open(0)]

t=[[201*[-1e9]for _ in[0]*N]for _ in[0]*N]

hq=[(-b[0][0],b[0][0],0,0)] #min,max,y,x

from heapq import*

while hq:
    mv,Mv,y,x=heappop(hq)
    if -mv<t[y][x][Mv]:
        continue
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<N:
            nmv=min(-mv,b[ny][nx])
            nMv=max(Mv,b[ny][nx])
            if t[ny][nx][nMv]<nmv:
                t[ny][nx][nMv]=nmv
                heappush(hq,(-nmv,nMv,ny,nx))
vv=t[-1][-1]
mv=1e9
for i in range(201):
    mv=min(mv,i-vv[i])
print(mv)