[N],*l=[map(int,i.split())for i in open(0)]

A=[0]*N
B=A[:]
C=B[:]

for i,(a,b,c)in enumerate(zip(*l)):
    A[a-1]=i
    B[b-1]=i
    C[c-1]=i

tree=[float('inf')]*2*N

def update(i,v):
    i+=N
    tree[i]=v
    while i:=i>>1:
        tree[i]=min(tree[i<<1],tree[i<<1|1])

def get_val(l,r):
    l+=N
    r+=N
    ret=float('inf')
    while l<r:
        if l&1:
            ret=min(ret,tree[l])
            l+=1
        if r&1:
            r-=1
            ret=min(ret,tree[r])
        l>>=1
        r>>=1
    return ret

ret=0

for a,b,c in sorted(zip(A,B,C)):
    ret+=c<get_val(0,b)
    update(b,c)

print(ret)