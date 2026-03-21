N,D,*l=map(int,open(0).read().split())

tree=[-float('inf')]*2*N

def update(i,v):
    i+=N
    tree[i]=v
    while i:=i>>1:
        tree[i]=max(tree[i<<1],tree[i<<1|1])

def getval(l,r):
    l+=N
    r+=N
    ret=-float('inf')
    while l<r:
        if l&1:
            ret=max(ret,tree[l])
            l+=1
        if r&1:
            r-=1
            ret=max(ret,tree[r])
        l>>=1
        r>>=1
    return ret

for i,v in enumerate(l):
    update(i,max(0,getval(max(i-D,0),i))+v)
print(getval(0,N))