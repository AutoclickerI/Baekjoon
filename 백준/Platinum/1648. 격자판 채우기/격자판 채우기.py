def zero_pos(n):
    r=0
    while n&1:
        n>>=1
        r+=1
    return r

def pack(y,x):
    return 1<<y*M+x

N,M=map(int,input().split())
from heapq import*
hq=[0]
v={0:1}
while hq:
    n=heappop(hq)
    ix=zero_pos(n)
    y,x=ix//M,ix%M
    for dy,dx in(1,0),(0,1):
        ny,nx=y+dy,x+dx
        p=pack(y,x)|pack(ny,nx)
        if 0<=ny<N and 0<=nx<M and n&p<1:
            if n|p not in v:
                v[n|p]=0
                heappush(hq,n|p)
            v[n|p]=(v[n|p]+v[n])%9901

print(v.get(2**(N*M)-1,0))