class node:
    def __init__(self,max,min,sum,ls,rs,lsM,rsM,lsm,rsm,lsmM,rsmM,m):
        self.max=max
        self.min=min
        self.sum=sum
        
        self.ls=ls # sum
        self.rs=rs
        
        self.lsM=lsM # sum + max
        self.rsM=rsM
        
        self.lsm=lsm # sum - min
        self.rsm=rsm
        
        self.lsmM=lsmM # sum - min + max
        self.rsmM=rsmM
        
        self.m=m

def merge(L,R):
    if L==None:
        return R
    if R==None:
        return L
    return node(max(L.max,R.max),
                min(L.min,R.min),
                L.sum+R.sum,
                max(L.ls,L.sum+R.ls),
                max(R.rs,R.sum+L.rs),
                max(L.lsM,L.sum+L.max+R.ls,L.sum+R.lsM),
                max(R.rsM,R.sum+R.max+L.rs,R.sum+L.rsM),
                max(L.lsm,L.sum-L.min+R.ls,L.sum+R.lsm),
                max(R.rsm,R.sum-R.min+L.rs,R.sum+L.rsm),
                max(L.lsmM,L.sum-L.min+L.max+R.ls,L.sum-L.min+R.lsM,L.sum+L.max+R.lsm,L.sum+R.lsmM),
                max(R.rsmM,R.sum-R.min+R.max+L.rs,R.sum-R.min+L.rsM,R.sum+R.max+L.rsm,R.sum+L.rsmM),
                max(L.m,R.m,L.rsmM+R.ls,L.rsm+R.lsM,L.rsM+R.lsm,L.rs+R.lsmM))

def update(i,v):
    i+=N
    tree[i]=node(v,v,v,v,v,2*v,2*v,0,0,v,v,v)
    while i:=i>>1:
        tree[i]=merge(tree[i<<1],tree[i<<1|1])

def getval(l,r):
    l+=N
    r+=N
    left=right=None
    while l<r:
        if l&1:
            left=merge(left,tree[l])
            l+=1
        if r&1:
            r-=1
            right=merge(tree[r],right)
        l>>=1
        r>>=1
    return merge(left,right)

[N,Q],A,*l=[[*map(int,i.split())]for i in open(0)]

tree=[0]*2*N

for i,v in enumerate(A,N):
    tree[i]=node(v,v,v,v,v,2*v,2*v,0,0,v,v,v)

for i in range(N-1,0,-1):
    tree[i]=merge(tree[i<<1],tree[i<<1|1])

for q,i,j in l:
    if q<2:
        update(i-1,j)
    else:
        print(getval(i-1,j).m)