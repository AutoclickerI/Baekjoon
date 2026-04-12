[N,M],*b=[[*map(int,i.split())]for i in open(0)]

v=[M*[0]for _ in[0]*N]
d={}
cnt=0

for y in range(N):
    for x in range(M):
        if v[y][x]<1 and b[y][x]:
            cnt+=1
            v[y][x]=cnt
            d[cnt]=1
            l=[(y,x)]
            for cy,cx in l:
                for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                    ny,nx=cy+dy,cx+dx
                    if 0<=ny<N and 0<=nx<M and v[ny][nx]<1 and b[ny][nx]:
                        v[ny][nx]=cnt
                        l+=(ny,nx),
                        d[cnt]+=1

s=set()
for y in range(N):
    for x in range(M):
        if v[y][x]<1:
            l=[]
            for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                ny,nx=y+dy,x+dx
                if 0<=ny<N and 0<=nx<M and v[ny][nx]:
                    l+=v[ny][nx],
            s|={(*sorted({*l}),)}

m=1
for i in range(1,cnt+1):
    m=max(m,d[i]+1)
for sl in s:
    m=max(m,sum(d[i]for i in sl)+1)
print(min(m,N*M))