n=int(input())
b=[input()for _ in[0]*n]

v=[n*[0]for _ in[0]*n]

from collections import deque

dq=deque([(0,0,0)])

while dq:
    c,y,x=dq.popleft()
    if y==x==n-1:break
    for dy,dx in(-1,0),(0,1),(1,0),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<n and 0<=nx<n and v[ny][nx]<1:
            v[ny][nx]=1
            if'0'<b[ny][nx]:
                dq.appendleft((c,ny,nx))
            else:
                dq+=(c+1,ny,nx),

print(c)