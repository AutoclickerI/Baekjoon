from itertools import*
m=0
N=int(input())
l=[[*input()]for _ in[0]*N]

for y in range(N):
    for x in range(N):
        for dy,dx in(1,0),(0,1):
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<N and l[y][x]!=l[ny][nx]:
                l[y][x],l[ny][nx]=l[ny][nx],l[y][x]
                for i in*l,*zip(*l):
                    m=max(m,*[sum(1 for _ in j)for _,j in groupby(i)])
                l[y][x],l[ny][nx]=l[ny][nx],l[y][x]
print(m)