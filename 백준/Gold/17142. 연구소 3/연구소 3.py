N,M=map(int,input().split())

b=[input()[::2]for _ in[0]*N]

viruses=[]

zeros=0

for y in range(N):
    for x in range(N):
        if b[y][x]=='2':
            viruses+=(y,x),
        if b[y][x]=='0':
            zeros+=1

from itertools import*

m=[]

def BFS():
    o=[[*i]for i in b]
    v=[(0,*i)for i in subset]
    cnt=0
    for i,y,x in v:
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<N and o[ny][nx]not in'13':
                cnt+=o[ny][nx]=='0'
                if cnt==zeros:
                    return i+1
                o[ny][nx]='3'
                v+=(i+1,ny,nx),

for subset in combinations(viruses,M):
    v=BFS()
    if v:
        m+=v,
print(zeros and min(m or[-1]))