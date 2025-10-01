def step():
    l=[(0,0)]
    v=[M*[1]for _ in[0]*N]
    for y,x in l:
        for dy,dx in(-1,0),(0,1),(0,-1),(1,0):
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<M and v[ny][nx]:
                v[ny][nx]=0
                if b[ny][nx]<1:
                    l+=(ny,nx),
    for y in range(N):
        for x in range(M):
            b[y][x]*=v[y][x]

N,M=map(int,input().split())
b=[[*map(int,input()[::2])]for _ in[0]*N]
cnt=1e9
v=0
while cnt:
    v+=1
    p=cnt
    cnt=sum(sum(b,[]))
    step()
    
print(v-1,p)