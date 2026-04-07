N,M,K=map(int,input().split())
b=[input()for _ in[0]*N]

d={}

def DFS(y,x,depth,s):
    d[s]=d.get(s,0)+1
    if depth==5:return
    for dy in-1,0,1:
        for dx in-1,0,1:
            if dy==dx==0:
                continue
            ny,nx=(y+dy)%N,(x+dx)%M
            DFS(ny,nx,depth+1,s+b[ny][nx])

for y in range(N):
    for x in range(M):
        DFS(y,x,1,b[y][x])

for _ in[0]*K:
    print(d.get(input(),0))