class node:
    def __init__(self,sum,cnt):
        self.sum=sum
        self.cnt=cnt

def merge(L,R):
    if L is None:
        return R
    if R is None:
        return L
    return node(L.sum+R.sum,L.cnt+R.cnt)

def update(i,v):
    i+=N
    tree[i]=merge(tree[i],node(v,1))
    while i:=i>>1:
        tree[i]=merge(tree[i<<1],tree[i<<1|1])

def getval(l,r):
    if l>=r:
        return node(0,0)
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
    return merge(left,right)or node(0,0)

_,i,*l=map(int,open(0))
N=200001
tree=[node(0,0)]*2*N

r=1
update(i,i)
for i in l:
    left=getval(0,i)
    right=getval(i+1,N)
    r*=right.sum-right.cnt*i+left.cnt*i-left.sum
    r%=10**9+7
    update(i,i)
print(r)