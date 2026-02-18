N,M,K=map(int,input().split())
b=[input()for _ in[0]*N]
c,*s=input()
v=[[j==c for j in i]for i in b]
for c in s:
    t=[M*[0]for _ in[0]*N]
    for y in range(N):
        for x in range(M):
            for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                for k in range(K):
                    ny,nx=y-~k*dy,x-~k*dx
                    if 0<=ny<N and 0<=nx<M and c==b[ny][nx]:
                        t[ny][nx]+=v[y][x]
    v=t
print(sum(sum(i)for i in v))