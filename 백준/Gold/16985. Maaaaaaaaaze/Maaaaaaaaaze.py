def BFS(arr):
    v=[[5*[float('inf')]for _ in[0]*5]for _ in[0]*5]
    l=[(0,0,0,0)]*arr[0][0][0]
    for z,y,x,c in l:
        for dz,dy,dx in(-1,0,0),(1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1):
            nz,ny,nx=z+dz,y+dy,x+dx
            if 0<=min(nz,ny,nx)<=max(nz,ny,nx)<5 and c+1<v[nz][ny][nx] and arr[nz][ny][nx]:
                v[nz][ny][nx]=c+1
                l+=(nz,ny,nx,c+1),
    return v[-1][-1][-1]

b=[[[*map(int,input().split())]for _ in[0]*5]for _ in[0]*5]
from itertools import*

mv=float('inf')
for bb in permutations(b):
    for r in product(range(4),repeat=5):
        arr=[*bb]
        for i,rot in enumerate(r):
            for _ in[0]*rot:
                arr[i]=[i[::-1]for i in zip(*arr[i])]
        mv=min(mv,BFS(arr))

print(-(mv==float('inf'))or mv)