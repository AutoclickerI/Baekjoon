N,M=map(int,input().split())
b=[input()for _ in[0]*N]

def getn(y,x,dy,dx):
    if dx==dy==0:dx=1e9
    global l
    s=''
    while 0<=y<N and 0<=x<M:
        s+=b[y][x];y+=dy;x+=dx
        n=int(s)
        if math.isqrt(n)**2==n:
            l=max(l,n)

import math
l=-1
for y in range(N):
    for x in range(M):
        for dy in range(1-N,N):
            for dx in range(1-M,M):
                getn(y,x,dy,dx)
print(l)