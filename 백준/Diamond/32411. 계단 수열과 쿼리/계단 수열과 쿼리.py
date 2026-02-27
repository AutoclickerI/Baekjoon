import sys
input=sys.stdin.readline

class node:
    def __init__(self,lmax,lv,rmax,rv,max,len):
        self.lmax=lmax
        self.lv=lv
        self.rmax=rmax
        self.rv=rv
        self.max=max
        self.len=len

def merge(L,R):
    if L==None:
        return R
    if R==None:
        return L
    lmax=L.lmax[:]
    for i in range(10):
        if lmax[i]==L.len and i+1==abs(L.rv-R.lv):
            lmax[i]+=R.lmax[i]
    rmax=R.rmax[:]
    for i in range(10):
        if rmax[i]==R.len and i+1==abs(R.lv-L.rv):
            rmax[i]+=L.rmax[i]
    *m,=map(max,L.max,R.max)
    for i in range(10):
        if i+1==abs(R.lv-L.rv):
            m[i]=max(m[i],L.rmax[i]+R.lmax[i])
    return node(lmax,L.lv,rmax,R.rv,m,L.len+R.len)


N,Q=map(int,input().split())
*l,=map(int,input().split())
tree=[0]*4*N
lazy=[0]*4*N

def build(s,e,i=1):
    if e-s<2:
        v=l[s]
        tree[i]=node([1]*10,v,[1]*10,v,[1]*10,1)
        return tree[i]
    m=s+e>>1
    tree[i]=merge(build(s,m,i<<1),build(m,e,i<<1|1))
    return tree[i]    

def propagate(s,e,i=1):
    if lazy[i]:
        if 1<e-s:
            lazy[i<<1]+=lazy[i]
            tree[i<<1].lv+=lazy[i]
            tree[i<<1].rv+=lazy[i]
            tree[i<<1|1].lv+=lazy[i]
            tree[i<<1|1].rv+=lazy[i]
            lazy[i<<1|1]+=lazy[i]
        lazy[i]=0

def update_lazy(s,e,l,r,v,i=1):
    if e<=l or r<=s:
        propagate(s,e,i)
        return tree[i]
    if l<=s and e<=r:
        lazy[i]+=v
        tree[i].rv+=v
        tree[i].lv+=v
        return tree[i]
    propagate(s,e,i)
    m=s+e>>1
    tree[i]=merge(update_lazy(s,m,l,r,v,i<<1),update_lazy(m,e,l,r,v,i<<1|1))
    return tree[i]

def get_val(s,e,l,r,i=1):
    propagate(s,e,i)
    if e<=l or r<=s:
        return None
    if l<=s and e<=r:
        return tree[i]
    m=s+e>>1
    return merge(get_val(s,m,l,r,i<<1),get_val(m,e,l,r,i<<1|1))

build(0,N)

for _ in[0]*Q:
    q,i,j,k=map(int,input().split())
    if q<2:
        update_lazy(0,N,i-1,j,k)
    else:
        print(get_val(0,N,i-1,j).max[k-1])