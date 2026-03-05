class node:
    def __init__(self,lmax,rmax,max,sum):
        self.lmax=lmax
        self.rmax=rmax
        self.max=max
        self.sum=sum

def merge(L,R):
    if L==None:
        return R
    if R==None:
        return L
    return node(max(L.lmax,L.sum+R.lmax),max(R.rmax,R.sum+L.rmax),max(L.max,R.max,L.rmax+R.lmax),L.sum+R.sum)

def update(i,v):
    i+=N
    tree[i]=node(*[tree[i].sum+v]*4)
    while i:=i>>1:
        tree[i]=merge(tree[i<<1],tree[i<<1|1])

def getval(l,r):
    l+=N
    r+=N
    right=left=None
    while l<r:
        if l%2:
            left=merge(left,tree[l])
            l+=1
        if r%2:
            r-=1
            right=merge(tree[r],right)
        l>>=1
        r>>=1
    return merge(left,right)
    
N,*l=map(int,open(0).read().split())

tree=[0]*N+[node(*[i]*4)for i in l]

for i in range(N-1,0,-1):
    tree[i]=merge(tree[i<<1],tree[i<<1|1])

for i in range(N):
    update(i,10**18)
    print(getval(0,N).max-10**18)
    update(i,-10**18)