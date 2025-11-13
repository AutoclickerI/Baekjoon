N=int(input())
b=[[*input()[::2]]for _ in[0]*N]

l=[(y,x)for y in range(N)for x in range(N)if b[y][x]=='X']

def move(y,x,dy,dx):
    if 0<=y<N and 0<=x<N and b[y][x]!='O':
        if b[y][x]=='S':
            return 0
        return move(y+dy,x+dx,dy,dx)
    return 1

def check():
    for y in range(N):
        for x in range(N):
            if b[y][x]=='T':
                for dy,dx in(-1,0),(0,1),(1,0),(0,-1):
                    if move(y,x,dy,dx)<1:
                        return 0
    return 1

from itertools import*

for(y1,x1),(y2,x2),(y3,x3)in combinations(l,3):
    b[y1][x1]=b[y2][x2]=b[y3][x3]='O'
    if check():
        exit(print('YES'))
    b[y1][x1]=b[y2][x2]=b[y3][x3]='X'
print('NO')