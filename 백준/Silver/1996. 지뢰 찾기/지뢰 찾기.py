N=int(input())
b=[input()for _ in[0]*N]
r=[N*[0]for _ in[0]*N]

for y in range(N):
    for x in range(N):
        if b[y][x]!='.':
            for dy in-1,0,1:
                for dx in-1,0,1:
                    ny,nx=y+dy,x+dx
                    if 0<=ny<N and 0<=nx<N:
                        r[ny][nx]+=int(b[y][x])
for y in range(N):
    for x in range(N):
        if 9<r[y][x]:
            r[y][x]='M'
        if b[y][x]!='.':
            r[y][x]='*'
for i in r:print(*i,sep='')