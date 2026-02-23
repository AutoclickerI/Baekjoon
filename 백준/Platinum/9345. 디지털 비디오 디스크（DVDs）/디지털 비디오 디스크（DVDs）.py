import sys
input=sys.stdin.readline

class node:
    def __init__(self,max,min):
        self.max=max
        self.min=min

def merge(L,R):
    if L==None:
        return R
    if R==None:
        return L
    return node(max(L.max,R.max),min(L.min,R.min))

def update(i):
    i+=N
    while i:=i>>1:
        tree[i]=merge(tree[i<<1],tree[i<<1|1])

def getval(l,r):
    l+=N
    r+=N
    ret=node(-float('inf'),float('inf'))
    while l<r:
        if l%2:
            ret=merge(ret,tree[l])
            l+=1
        if r%2:
            r-=1
            ret=merge(tree[r],ret)
        l>>=1
        r>>=1
    return ret

for _ in[0]*int(input()):
    N,K=map(int,input().split())
    tree=[0]*N+[node(i,i)for i in range(N)]
    for i in range(N-1,0,-1):
        tree[i]=merge(tree[i<<1],tree[i<<1|1])
    for _ in[0]*K:
        q,i,j=map(int,input().split())
        if q:
            v=getval(i,j+1)
            print('YNEOS'[(v.min,v.max)!=(i,j)::2])
        else:
            tree[i+N],tree[j+N]=tree[j+N],tree[i+N]
            update(i)
            update(j)