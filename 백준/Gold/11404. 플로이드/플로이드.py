import sys
input=sys.stdin.readline

N=int(input())

b=[[9**9*(i!=j)for i in range(N)]for j in range(N)]

for _ in[0]*int(input()):
    s,e,c=map(int,input().split())
    b[s-1][e-1]=min(b[s-1][e-1],c)

for m in range(N):
    for s in range(N):
        for e in range(N):
            b[s][e]=min(b[s][e],b[s][m]+b[m][e])

for y in range(N):
    for x in range(N):
        if b[y][x]==9**9:b[y][x]=0

for i in b:print(*i)