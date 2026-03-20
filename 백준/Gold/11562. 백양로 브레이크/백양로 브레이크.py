import sys
input=sys.stdin.readline

n,m=map(int,input().split())
n+=1
d=[n*[float('inf')]for _ in[0]*n]
for i in range(n):d[i][i]=0

for _ in[0]*m:
    u,v,b=map(int,input().split())
    if b:
        d[u][v]=d[v][u]=0
    else:
        d[u][v]=0
        d[v][u]=1

for m in range(n):
    for s in range(n):
        for e in range(n):
            d[s][e]=min(d[s][e],d[s][m]+d[m][e])

for _ in[0]*int(input()):
    s,e=map(int,input().split())
    print(d[s][e])