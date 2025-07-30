N=int(input())
a=set()
for _ in[0]*int(input()):
    y,x=map(int,input().split())
    a|={(y,x)}
l=[input().split()for _ in[0]*int(input())][::-1]
T=0
d=1
from collections import deque

dq=deque([(1,1)])

while 1:
    y,x=dq[-1]
    if l and l[-1][0]==str(T):
        _,v=l.pop()
        if v=='L':
            d-=1
        else:
            d+=1
    T+=1
    dy,dx=((-1,0),(0,1),(1,0),(0,-1))[d%4]
    ny,nx=y+dy,x+dx
    if not(0<ny<=N and 0<nx<=N)or(ny,nx)in dq:
        break
    dq+=(ny,nx),
    if(ny,nx)in a:
        a-={(ny,nx)}
    else:
        dq.popleft()
print(T)