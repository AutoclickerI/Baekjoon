W,H=map(int,input().split())
# - ㄴ | ㄱ
b=[[[0,0,0,0]for _ in[0]*W]for _ in[0]*H]
for y in range(H):
    b[y][0]=0,0,1,0
for x in range(W):
    b[0][x]=1,0,0,0
for y in range(1,H):
    for x in range(1,W):
        b[y][x]=sum(b[y][x-1][:2]),b[y][x-1][2],sum(b[y-1][x][2:]),b[y-1][x][0]

print(sum(b[-1][-1])%100000)