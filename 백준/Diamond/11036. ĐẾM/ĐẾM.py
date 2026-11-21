import sys
input=sys.stdin.readline

N,M,Q=map(int,input().split())
tree,ytree,xtree,yxtree=[[[0]*2*M for _ in[0]*2*N]for _ in[0]*4]

def update(tree,y,x,v):
    y+=N
    x+=M
    while y:
        tx=x
        while tx:
            tree[y][tx]+=v
            tx>>=1
        y>>=1

def getval(arr,l,r):
    l+=M
    r+=M
    ret=0
    while l<r:
        if l&1:
            ret+=arr[l]
            l+=1
        if r&1:
            r-=1
            ret+=arr[r]
        l>>=1
        r>>=1
    return ret

def getval2d(tree,yl,yr,xl,xr):
    yl+=N
    yr+=N
    ret=0
    while yl<yr:
        if yl&1:
            ret+=getval(tree[yl],xl,xr)
            yl+=1
        if yr&1:
            yr-=1
            ret+=getval(tree[yr],xl,xr)
        yl>>=1
        yr>>=1
    return ret

def add(y,x,v):
    if y<N and x<M:
        update(tree,y,x,v)
        update(ytree,y,x,v*y)
        update(xtree,y,x,v*x)
        update(yxtree,y,x,v*y*x)

def prefix(y,x):
    return y*x*getval2d(tree,0,y,0,x)-x*getval2d(ytree,0,y,0,x)-y*getval2d(xtree,0,y,0,x)+getval2d(yxtree,0,y,0,x)

for _ in[0]*Q:
    q,*l=map(int,input().split())
    if q<2:
        y1,x1,y2,x2,v=l
        add(y1-1,x1-1,v)
        add(y1-1,x2,-v)
        add(y2,x1-1,-v)
        add(y2,x2,v)
    else:
        y1,x1,y2,x2=l
        print(prefix(y2,x2)-prefix(y1-1,x2)-prefix(y2,x1-1)+prefix(y1-1,x1-1))