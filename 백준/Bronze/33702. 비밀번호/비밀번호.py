K=int(input())-1

v=[3*[0]for _ in[0]*3]
a=[0]

def DFS(y,x,depth):
    if depth==9:
        a[0]+=1
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny=y+dy;nx=x+dx
        if 0<=ny<3 and 0<=nx<3 and v[ny][nx]<1:
            v[ny][nx]=1
            DFS(ny,nx,depth+1)
            v[ny][nx]=0

v[K//3][K%3]=1
DFS(K//3,K%3,1)

print(a[0])