[N,K],*q=[map(int,i.split())for i in open(0)]

v=[N*[0]for _ in[0]*N]
cnt=0
l=[]
for s,e in q:
    cnt+=1
    v[s-1][e-1]=cnt
    l+=(0,cnt,s-1,e-1),

*p,=range(cnt+1)

def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a,b=sorted([find(a),find(b)])
    if a!=b:
        p[b]=a
        return 1
    return 0

for c,f,y,x in l:
    for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<N and v[ny][nx]:
            K-=merge(f,v[ny][nx])

if K<2:
    exit(print(0))

for c,f,y,x in l:
    for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<N and v[ny][nx]<1:
            v[ny][nx]=f
            for ddy,ddx in(-1,0),(1,0),(0,1),(0,-1):
                nny,nnx=ny+ddy,nx+ddx
                if 0<=nny<N and 0<=nnx<N and v[nny][nnx]:
                    K-=merge(v[nny][nnx],v[ny][nx])
            l+=(c+1,f,ny,nx),
    if K<2:
        print(c+1)
        break