tN=1<<16
blk=256
mod=10**9+7
class node:
    def __init__(self,e,o,cnt):
        self.e=e
        self.o=o
        self.cnt=cnt

def merge(L,R):
    if L==None:
        return R
    if R==None:
        return L
    return node((L.e+[R.e,R.o][L.cnt%2])%mod,(L.o+[R.o,R.e][L.cnt%2])%mod,L.cnt+R.cnt)

def update(i,v,c):
    i+=tN
    tree[i]=node(v,0,c)
    while i:=i>>1:
        tree[i]=merge(tree[i<<1],tree[i<<1|1])

[N,Q],A,*l=[[*map(int,i.split())]for i in open(0)]

sd={v:i for i,v in enumerate(sorted(A))}

tree=[node(0,0,0)]*2*tN
d={}
ps=pe=0

for s,e in sorted(l,key=lambda i:(i[0]//blk,i[1])):
    e+=1
    while pe<e:
        update(sd[A[pe]],A[pe],1)
        pe+=1
    while s<ps:
        ps-=1
        update(sd[A[ps]],A[ps],1)
    while e<pe:
        pe-=1
        update(sd[A[pe]],0,0)
    while ps<s:
        update(sd[A[ps]],0,0)
        ps+=1
    d[s,e-1]=tree[1].e

for s,e in l:print(d[s,e])