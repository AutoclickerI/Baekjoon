class node:
    def __init__(self,lmax=0,rmax=0,max=0,lmin=0,rmin=0,min=0,sum=0):
        self.lmax=lmax
        self.rmax=rmax
        self.max=max
        self.lmin=lmin
        self.rmin=rmin
        self.min=min
        self.sum=sum

def merge(L,R):
    if L==None:
        return R
    if R==None:
        return L
    return node(max(L.lmax,L.sum+R.lmax),max(R.rmax,R.sum+L.rmax),max(L.max,R.max,L.rmax+R.lmax),min(L.lmin,L.sum+R.lmin),min(R.rmin,R.sum+L.rmin),min(L.min,R.min,L.rmin+R.lmin),L.sum+R.sum)

def update(i,v):
    i+=N
    tree[i]=node(*[v+tree[i].sum]*7)
    while 1<i:
        i//=2
        tree[i]=merge(tree[i*2],tree[i*2|1])

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
    
[N,Q],*l=[map(int,i.split())for i in open(0)]

tree=[node()]*2*N

for q,*v in l:
    if q-1:
        v=getval(0,N)
        print(max([v.sum-v.min,v.max][v.min==v.sum:]))
    else:
        i,j=v
        update(i-1,j)