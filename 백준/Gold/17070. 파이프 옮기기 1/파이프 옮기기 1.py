n=int(input())

b=[input()[::2]for _ in[0]*n]

v=[[3*[0]for _ in[0]*n]for _ in[0]*n] # -\|

v[0][1][0]=1

def check(y,x,t):
    if t==0:
        return x+1<n and b[y][x+1]=='0'
    if t==1:
        return x+1<n>y+1 and all(b[y+dy][x+dx]=='0'for dy,dx in((1,0),(0,1),(1,1)))
    return y+1<n and b[y+1][x]=='0'

def act(y,x,t,orig):
    global dq
    ad=v[y][x][orig]
    if ad<1:
        return
    if t==0:
        dq+=(y,x+1,0),
        v[y][x+1][0]+=ad
    if t==1:
        dq+=(y+1,x+1,1),
        v[y+1][x+1][1]+=ad
    if t==2:
        dq+=(y+1,x,2),
        v[y+1][x][2]+=ad

from collections import deque

dq=deque([[0,1,0]])

while dq:
    y,x,t=dq.popleft()
    if y==x==n-1:
        continue
    if t==0:
        if check(y,x,0):
            act(y,x,0,t)
        if check(y,x,1):
            act(y,x,1,t)
    if t==1:
        if check(y,x,0):
            act(y,x,0,t)
        if check(y,x,1):
            act(y,x,1,t)
        if check(y,x,2):
            act(y,x,2,t)
    if t==2:
        if check(y,x,1):
            act(y,x,1,t)
        if check(y,x,2):
            act(y,x,2,t)
    v[y][x][t]=0

print(sum(v[-1][-1]))