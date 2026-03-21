[Q],*l=[map(int,i.split())for i in open(0)]

N=2097152
tree=[0]*2*N

def update(i,v):
    i+=N
    tree[i]+=v
    while i:=i>>1:
        tree[i]=tree[i<<1]+tree[i<<1|1]

def getval(l,r):
    l+=N
    r+=N
    ret=0
    while l<r:
        if l&1:
            ret+=tree[l]
            l+=1
        if r&1:
            r-=1
            ret+=tree[r]
        l>>=1
        r>>=1
    return ret

for q,v in l:
    if q<2:
        update(v,1)
    else:
        s=0
        e=N
        while 1<e-s:
            m=s+e>>1
            if getval(0,m+1)<v:
                s=m
            else:
                e=m
        print(e)
        update(e,-1)