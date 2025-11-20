[N],*b=[[*map(int,i.split())]for i in open(0)]

mv=float('inf')
from itertools import*

for i in combinations(range(N*N),3):
    s=set()
    r=0
    for v in i:
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1),(0,0):
            ny,nx=v//N+dy,v%N+dx
            if 0<=ny<N and 0<=nx<N:
                r+=b[ny][nx]
                s|={(ny,nx)}
    if len(s)==15:
        mv=min(mv,r)
print(mv)