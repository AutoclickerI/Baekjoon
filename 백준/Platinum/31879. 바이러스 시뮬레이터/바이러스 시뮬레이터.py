import sys
input=sys.stdin.readline

class node:
    def __init__(self,midx,max,lcnt,lsum,rcnt,rsum,sum,cnt):
        self.midx=midx
        self.max=max
        self.lcnt=lcnt
        self.lsum=lsum
        self.rcnt=rcnt
        self.rsum=rsum
        self.sum=sum
        self.cnt=cnt

def merge(L,R):
    if L==None:
        return R
    if R==None:
        return L
    return node(R.midx if L.max<R.max else L.midx,
                max(L.max,R.max),
                L.lcnt+R.lcnt*(L.lcnt==L.cnt),
                L.lsum+R.lsum*(L.lcnt==L.cnt),
                R.rcnt+L.rcnt*(R.rcnt==R.cnt),
                R.rsum+L.rsum*(R.rcnt==R.cnt),
                max(L.sum,R.sum,L.rsum+R.lsum),
                L.cnt+R.cnt)

def update(i,v):
    i+=N
    v+=tree[i].sum
    tree[i]=node(i-N,v,0<v,v,0<v,v,v,1)
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
    
[N,Q],A,*l=[map(int,i.split())for i in open(0)]
tree=[0]*N
for i,v in enumerate(A):
    tree+=node(i,v,1,v,1,v,v,1),
for i in range(N-1,0,-1):
    tree[i]=merge(tree[i<<1],tree[i<<1|1])

for q,i,j in l:
    i-=1
    if q<2:
        while j and getval(i,N).max:
            v=getval(i,i+1).max
            if v<=j:
                update(i,-v)
                i=getval(i,N).midx
                j-=v
            else:
                update(i,-j)
                break            
    elif q<3:
        update(i,j)
    else:
        print(getval(i,j).sum)