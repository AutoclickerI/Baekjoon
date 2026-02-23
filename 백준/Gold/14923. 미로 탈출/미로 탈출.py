[N,M],[Hy,Hx],[Ey,Ex],*b=[[*map(int,i.split())]for i in open(0)]
v=[[2*[1e9]for _ in[0]*M]for _ in[0]*N]
Hy-=1
Hx-=1
Ey-=1
Ex-=1
v[Hy][Hx][0]=0
l=[(Hy,Hx,0,0)]
for y,x,c,f in l:
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<M and c+1<v[ny][nx][f]:
            if b[ny][nx]==0:
                v[ny][nx][f]=c+1
                l+=(ny,nx,c+1,f),
            if f==0 and c+1<v[ny][nx][1]:
                v[ny][nx][1]=c+1
                l+=(ny,nx,c+1,1),
v=min(v[Ey][Ex])
print(-(v==1e9)or v)