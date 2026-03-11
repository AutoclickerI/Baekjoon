import math

class node:
    def __init__(self,gcd,sum):
        self.gcd=gcd
        self.sum=sum

def merge(L,R):
    if L==None:
        return R
    if R==None:
        return L
    return node(math.gcd(L.gcd,R.gcd),L.sum+R.sum)

def update(i,v):
    i+=N
    tree[i]=node(*[tree[i].sum+v]*2)
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
    
[N],A,_,*Q=[[*map(int,i.split())]for i in open(0)]
N+=1
tree=[0]*N
p=0
for v in A+[0]:
    tree+=node(v-p,v-p),
    p=v
for i in range(N-1,0,-1):
    tree[i]=merge(tree[i<<1],tree[i<<1|1])

for T,A,B in Q:
    if T:
        update(A-1,T)
        update(B,-T)
    else:
        if A==B:
            print(getval(0,A).sum)
        else:
            v=getval(0,A).sum
            g=getval(A,B).gcd
            print(math.gcd(v,g))