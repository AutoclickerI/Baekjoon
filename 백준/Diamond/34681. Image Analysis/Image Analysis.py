import math

[n,p,q],[W,H],*l=[[*map(int,i.split())]for i in open(0)]
P,l=l[:p],l[p:]

Y=[0]*(n+W+2);CX=[0]*(n+W+2)
X=[0]*(n+H+3);CY=[0]*(n+H+3)
ix={}
for x,y,c in P:
    Y[x]=y;X[y]=x
    CX[x]=CY[y]=ix[c]=ix.get(c,len(ix))

blk=math.isqrt(4*(n-W)*(n-H)//q)+1

cnt=[0]*len(ix)
G=[0]*(p+1)

def push(c):
    k=cnt[c];G[k]+=1;cnt[c]=k+1

def pop(c):
    k=cnt[c]-1;cnt[c]=k;G[k]-=1

px=1
py=n+1
d={}
for L,D,A,B in sorted(l,key=lambda i:(i[0]//blk,i[1])):
    while px<L:
        if py<=Y[px]<=py+H:pop(CX[px])
        if py<=Y[px+W+1]<=py+H:push(CX[px+W+1])
        px+=1
    while L<px:
        px-=1
        if py<=Y[px]<=py+H:push(CX[px])
        if py<=Y[px+W+1]<=py+H:pop(CX[px+W+1])
    while py<D:
        if px<=X[py]<=px+W:pop(CY[py])
        if px<=X[py+H+1]<=px+W:push(CY[py+H+1])
        py+=1
    while D<py:
        py-=1
        if px<=X[py]<=px+W:push(CY[py])
        if px<=X[py+H+1]<=px+W:pop(CY[py+H+1])
    d[L,D,A,B]=G[A-1]-G[B]

for L,D,A,B in l:print(d[L,D,A,B])