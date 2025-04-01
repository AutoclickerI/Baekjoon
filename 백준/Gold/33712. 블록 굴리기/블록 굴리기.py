N,M,Ko=map(int,input().split())
board=[[*map(int,input().split())]for _ in[0]*N]

from collections import deque

dq=deque() # K, type(1(.),2(|),4(_)), y, x

for y in range(N):
    for x in range(M):
        if board[y][x]==2:
            ty,tx=y,x
            dq+=(0,1,y,x),

def possible(*l):
    for y,x in l:
        if y<0 or N<=y or x<0 or M<=x or board[y][x]==0:
            return 0
    return 1

pK=-1
while dq and dq[0][0]<Ko:
    K,t,y,x=dq.popleft()
    if pK!=K:
        visited=[M*[0]for _ in[0]*N]
        pK=K
    if t==1:
        for dy,dx,nt in(-1,0,2),(1,0,2),(0,-1,4),(0,1,4):
            if possible((y+dy*2,x+dx*2),(y+dy,x+dx)):
                vy,vx=min((y+dy*2,x+dx*2),(y+dy,x+dx))
                if not visited[vy][vx]&nt:
                    visited[vy][vx]|=nt
                    dq+=(K+1,nt,vy,vx),
    elif t==2:
        for dx in-1,1:
            vx=x+dx
            if possible((y,vx),(y+1,vx)):
                if not visited[y][vx]&t:
                    visited[y][vx]|=t
                    dq+=(K+1,t,y,vx),
        for dy in-1,2:
            vy=y+dy
            nt=1
            if possible((vy,x)):
                if not visited[vy][x]&nt:
                    visited[vy][x]|=nt
                    dq+=(K+1,nt,vy,x),
    elif t==4:
        for dy in-1,1:
            vy=y+dy
            if possible((vy,x),(vy,x+1)):
                if not visited[vy][x]&t:
                    visited[vy][x]|=t
                    dq+=(K+1,t,vy,x),
        for dx in-1,2:
            vx=x+dx
            nt=1
            if possible((y,vx)):
                if not visited[y][vx]&nt:
                    visited[y][vx]|=nt
                    dq+=(K+1,nt,y,vx),
visited[ty][tx]=0
print(0 if(K!=Ko-1)else sum(sum(j&1 for j in i)for i in visited))