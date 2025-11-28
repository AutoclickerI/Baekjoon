N,M=map(int,input().split())
b=[input()for _ in[0]*N]
l=[(0,i)for i in range(M)if b[0][i]<'1']
v=[M*[1]for _ in[0]*N]
for y,x in l:
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<M and v[ny][nx] and b[ny][nx]<'1':
            v[ny][nx]=0
            l+=(ny,nx),
print('YNEOS'[all(v[-1])::2])