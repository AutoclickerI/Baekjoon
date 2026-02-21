class node:
    def __init__(self,l='L',r='L',len=1,lmax=1,rmax=1,sum=1,max=1):
        self.l=l
        self.r=r
        self.len=len
        self.lmax=lmax
        self.rmax=rmax
        self.sum=sum
        self.max=max

def merge(L,R):
    if L==None:
        return R
    if R==None:
        return L
    return node(L.l,R.r,L.len+R.len,max((L.sum+R.lmax)*(L.sum and L.r!=R.l),L.lmax),max((R.sum+L.rmax)*(R.sum and L.r!=R.l),R.rmax),(L.sum+R.sum)*(L.r!=R.l and L.sum==L.len and R.sum==R.len),max(L.max,R.max,(L.rmax+R.lmax)*(L.r!=R.l)))

def update(i):
    i+=N
    v='RL'[tree[i].l=='R']
    tree[i]=node(v,v)
    while 1<i:
        i>>=1
        tree[i]=merge(tree[i*2],tree[i*2|1])

def getval(l,r):
    l+=N
    r+=N
    right=left=None
    while l<r:
        if l%2:
            if left==None:
                left=tree[l]
            else:
                left=merge(left,tree[l])
            l+=1
        if r%2:
            r-=1
            if right==None:
                right=tree[r]
            else:
                right=merge(tree[r],right)
        l>>=1
        r>>=1
    return merge(left,right)
    
N,Q,*l=map(int,open(0).read().split())

tree=[0]*2*N
for i in range(N):
    tree[i+N]=node()

for i in range(N-1,0,-1):
    tree[i]=merge(tree[i*2],tree[i*2|1])

for i in l:
    update(i-1)
    print(getval(0,N).max)