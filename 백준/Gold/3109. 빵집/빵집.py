R,C=map(int,input().split())
b=[input()for _ in[0]*R]
v=[C*[0]for _ in[0]*R]
ans=[0]
def DFS(y,x):
    v[y][x]=1
    if x==C-1:
        ans[0]+=1
        return 1
    for dy in-1,0,1:
        ny=y+dy
        if 0<=ny<R and v[ny][x+1]<1 and b[ny][x+1]=='.':
            if DFS(ny,x+1):
                return 1
for i in range(R):
    DFS(i,0)
print(*ans)