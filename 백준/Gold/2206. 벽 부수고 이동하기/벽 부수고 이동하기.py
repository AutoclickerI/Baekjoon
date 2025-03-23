N,M=map(int,input().split())

b=[input()for _ in[0]*N]

c0=[M*[9**9]for _ in[0]*N]
c1=[M*[9**9]for _ in[0]*N]

from heapq import*

c0[0][0]=1

hq0=[[1,0,0]] #cost,y,x
hq1=[]

while hq0:
    c,y,x=heappop(hq0)
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny=y+dy;nx=x+dx
        if 0<=ny<N and 0<=nx<M:
            if b[ny][nx]=='0'and c+1<c0[ny][nx]:
                c0[ny][nx]=c+1
                heappush(hq0,(c+1,ny,nx))
            if b[ny][nx]=='1'and c+1<c1[ny][nx]:
                c1[ny][nx]=c+1
                heappush(hq1,(c+1,ny,nx))
while hq1:
    c,y,x=heappop(hq1)
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny=y+dy;nx=x+dx
        if 0<=ny<N and 0<=nx<M:
            if b[ny][nx]=='0'and c+1<c1[ny][nx]:
                c1[ny][nx]=c+1
                heappush(hq1,(c+1,ny,nx))
m=min(c0[-1][-1],c1[-1][-1])

print([-1,m][m<9**9])