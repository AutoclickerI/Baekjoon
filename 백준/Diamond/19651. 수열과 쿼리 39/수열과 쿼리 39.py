import sys
input=sys.stdin.readline

class node:
    def __init__(self,lmax,lv,ls,rmax,rv,rs,max,len):
        self.lmax=lmax
        self.lv=lv
        self.ls=ls
        self.rmax=rmax
        self.rv=rv
        self.rs=rs
        self.max=max
        self.len=len

def merge(L,R):
    if L==None:
        return R
    if R==None:
        return L
    lmax=L.lmax
    ls=L.ls
    if L.lmax==L.len and (ls==None or ls==R.lv-L.rv):
        ls=R.lv-L.rv
        lmax+=(ls!=R.ls)or R.lmax
    rmax=R.rmax
    rs=R.rs
    if R.rmax==R.len and (rs==None or rs==L.rv-R.lv):
        rs=L.rv-R.lv
        rmax+=(L.rs!=rs)or L.rmax
    m=max(L.max,R.max,R.lmax+(R.lv-L.rv==R.ls),L.rmax+(L.rv-R.lv==L.rs))
    if L.rs==None and R.ls==None:
        m=2
    elif L.rs!=None and R.ls!=None and-L.rs==R.ls and R.lv-L.rv==R.ls:
        m=max(m,L.rmax+R.lmax)
    
    return node(lmax,L.lv,ls,rmax,R.rv,rs,m,L.len+R.len)


N=int(input())
*l,=map(int,input().split())
tree=[0]*4*N
lazy=[[0,0]for _ in[0]*4*N]

def build(s,e,i=1):
    if e-s<2:
        v=l[s]
        tree[i]=node(1,v,None,1,v,None,1,1)
        return tree[i]
    m=s+e>>1
    tree[i]=merge(build(s,m,i<<1),build(m,e,i<<1|1))
    return tree[i]    

def propagate(s,e,i=1):
    if lazy[i]!=[0,0]:
        if 1<e-s:
            m=e-s>>1
            lazy[i<<1][0]+=lazy[i][0]
            lazy[i<<1][1]+=lazy[i][1]
            tree[i<<1].lv+=lazy[i][0]
            if tree[i<<1].ls!=None:
                tree[i<<1].ls+=lazy[i][1]
            tree[i<<1].rv+=lazy[i][0]+lazy[i][1]*(m-1)
            if tree[i<<1].rs!=None:
                tree[i<<1].rs-=lazy[i][1]
            lazy[i<<1|1][0]+=lazy[i][0]+lazy[i][1]*m
            lazy[i<<1|1][1]+=lazy[i][1]
            tree[i<<1|1].lv+=lazy[i][0]+lazy[i][1]*m
            if tree[i<<1|1].ls!=None:
                tree[i<<1|1].ls+=lazy[i][1]
            tree[i<<1|1].rv+=lazy[i][0]+lazy[i][1]*(e-s-1)
            if tree[i<<1|1].rs!=None:
                tree[i<<1|1].rs-=lazy[i][1]
        lazy[i]=[0,0]

def update_lazy(s,e,l,r,x,y,i=1):
    if e<=l or r<=s:
        propagate(s,e,i)
        return tree[i]
    if l<=s and e<=r:
        lazy[i][0]+=x
        lazy[i][1]+=y
        tree[i].lv+=x
        if tree[i].ls!=None:
            tree[i].ls+=y
        tree[i].rv+=x+y*(e-s-1)
        if tree[i].rs!=None:
            tree[i].rs-=y
        return tree[i]
    propagate(s,e,i)
    m=s+e>>1
    tree[i]=merge(update_lazy(s,m,l,r,x,y,i<<1),update_lazy(m,e,l,r,x+y*(m-s),y,i<<1|1))
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

for _ in[0]*int(input()):
    q,i,j,*l=map(int,input().split())
    if q<2:
        x,y=l
        update_lazy(0,N,i-1,j,x-y*(i-1),y)
    else:
        print(get_val(0,N,i-1,j).max)