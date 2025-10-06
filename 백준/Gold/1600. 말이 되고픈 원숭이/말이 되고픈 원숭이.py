[K],[W,H],*b=[[*map(int,i.split())]for i in open(0)]

v=[[-~K*[0]for _ in[0]*W]for _ in[0]*H]

v[0][0][0]=1

l=[(0,0,0,0)] #cnt, K, y, x

for c,k,y,x in l:
    if(y,x)==(H-1,W-1):
        exit(print(c))
    if k<K:
        for dy,dx in(-2,1),(-2,-1),(-1,2),(-1,-2),(2,1),(2,-1),(1,2),(1,-2):
            ny,nx=y+dy,x+dx
            if 0<=ny<H and 0<=nx<W and b[ny][nx]<1 and v[ny][nx][k+1]<1:
                v[ny][nx][k+1]=1
                l+=(c+1,k+1,ny,nx),
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<H and 0<=nx<W and b[ny][nx]<1 and v[ny][nx][k]<1:
            v[ny][nx][k]=1
            l+=(c+1,k,ny,nx),
print(-1)