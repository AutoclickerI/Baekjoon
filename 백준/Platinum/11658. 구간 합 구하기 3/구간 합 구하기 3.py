import sys
input=sys.stdin.readline

N,M=map(int,input().split())
tree=[2*N*[0]for _ in[0]*N]
for _ in[0]*N:
    tree+=[0]*N+[*map(int,input().split())],

for i in range(N,2*N):
    for j in range(N)[::-1]:
        tree[i][j]=tree[i][j*2]+tree[i][j*2|1]

for i in range(2*N):
    for j in range(N)[::-1]:
        tree[j][i]=tree[j*2][i]+tree[j*2|1][i]

def update(y,x,v):
    y+=N
    x+=N
    tree[y][x]=v
    while y:
        tx=x
        while tx:=tx>>1:
            tree[y][tx]=tree[y][tx*2]+tree[y][tx*2|1]
        y>>=1
        tree[y][x]=tree[y*2][x]+tree[y*2|1][x]

def getval(arr,l,r):
    l+=N
    r+=N
    ret=0
    while l<r:
        if l%2:
            ret+=arr[l]
            l+=1
        if r%2:
            r-=1
            ret+=arr[r]
        l>>=1
        r>>=1
    return ret

def getval2d(yl,yr,xl,xr):
    yl+=N
    yr+=N
    ret=0
    while yl<yr:
        if yl%2:
            ret+=getval(tree[yl],xl,xr)
            yl+=1
        if yr%2:
            yr-=1
            ret+=getval(tree[yr],xl,xr)
        yl>>=1
        yr>>=1
    return ret

for _ in[0]*M:
    q,*l=map(int,input().split())
    if q:
        y1,x1,y2,x2=l
        print(getval2d(y1-1,y2,x1-1,x2))
    else:
        y,x,c=l
        update(y-1,x-1,c)