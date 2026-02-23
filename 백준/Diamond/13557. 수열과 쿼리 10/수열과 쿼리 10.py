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
    
[N],A,_,*l=[map(int,i.split())for i in open(0)]

tree=[0]*N+[node(*[i]*4)for i in A]

for i in range(N-1,0,-1):
    tree[i]=merge(tree[i<<1],tree[i<<1|1])

for x1,y1,x2,y2 in l:
    update(y1-1,10**18)
    update(x2-1,10**18)
    r=[getval(x1-1,y2).max-10**18*2]
    update(y1-1,-10**18)
    update(x2-1,-10**18)
    if x2<y1:
        r+=getval(x2,y1).max,
        update(y1-1,10**18)
        r+=getval(x1-1,y2).max-10**18,
        update(y1-1,-10**18)
        update(x2-1,10**18)
        r+=getval(x1-1,y2).max-10**18,
        update(x2-1,-10**18)
    print(max(r))