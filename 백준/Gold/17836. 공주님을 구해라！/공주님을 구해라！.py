[N,M,T],*b=[[*map(int,i.split())]for i in open(0)]

v=[[2*[0]for _ in[0]*M]for _ in[0]*N]

v[0][0][0]=0

l=[(0,0,0,0)]

for t,u,y,x in l:
    if(y,x)==(N-1,M-1):
        if t<=T:
            print(t)
            exit()
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<M:
            nu=u|(b[ny][nx]==2)
            if v[ny][nx][nu]<1 and(nu or b[ny][nx]<1):
                v[ny][nx][nu]=1
                l+=(t+1,nu,ny,nx),
print('Fail')