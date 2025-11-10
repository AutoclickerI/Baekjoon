R,C,K=map(int,input().split())
b=[input()for _ in[0]*R]
v=[C*[0]for _ in[0]*R]
ans=0
def backtracking(y,x,c):
    global ans
    if(y,x)==(0,C-1):
        ans+=c==K
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<R and 0<=nx<C and b[ny][nx]<'T'and v[ny][nx]<1:
            v[ny][nx]=1
            backtracking(ny,nx,c+1)
            v[ny][nx]=0
v[-1][0]=1
backtracking(R-1,0,1)
print(ans)