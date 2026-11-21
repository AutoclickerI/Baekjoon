[N,M],*l=[[*map(int,i.split())]for i in open(0)]
A=[0]+[a for a,in l[:N]]+[0]
Q=l[N:]
V=sorted({*A,*(q[-1]for q in Q)})
idx={v:i for i,v in enumerate(V)}
K=len(V)
tree=[0]*2*K

def update(i,v):
    i+=K
    tree[i]+=v
    while i:=i>>1:
        tree[i]=tree[i<<1]+tree[i<<1|1]

def getval(l,r):
    l+=K
    r+=K
    ret=0
    while l<r:
        if l&1:
            ret+=tree[l]
            l+=1
        if r&1:
            r-=1
            ret+=tree[r]
        l>>=1
        r>>=1
    return ret

for i in range(1,N+1):
    tree[K+idx[A[i]]]+=1
for i in range(N+1):
    tree[K+idx[min(A[i],A[i+1])]]-=1
for i in range(K-1,0,-1):
    tree[i]=tree[i<<1]+tree[i<<1|1]

r=[]
for q,c,*d in Q:
    if q<2:
        r+=getval(idx[c],K),
    else:
        for i in c-1,c:
            update(idx[min(A[i],A[i+1])],1)
        update(idx[A[c]],-1)
        A[c]=d[0]
        update(idx[d[0]],1)
        for i in c-1,c:
            update(idx[min(A[i],A[i+1])],-1)
print(*r)