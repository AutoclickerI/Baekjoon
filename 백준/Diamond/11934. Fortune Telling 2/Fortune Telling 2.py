[N,M],*l=[[*map(int,i.split())]for i in open(0)]

f=[0]*N

for i in range(N):
    s,e=l[i]
    if e<s:
        f[i]=1
        l[i]=[e,s]

sA=sorted({*sum(l,[])})

dA={}
for i,v in enumerate(sA):
    dA[v]=i

tmiN=len(sA)
tree=[-1]*2*tmiN

def update(i,v):
    tree[i]=v
    while i:=i>>1:
        tree[i]=max(tree[i<<1],tree[i<<1|1])

def getval(l,r):
    l+=tmiN
    r+=tmiN
    ret=-1
    while l<r:
        if l&1:
            ret=max(ret,tree[l])
            l+=1
        if r&1:
            r-=1
            ret=max(ret,tree[r])
        l>>=1
        r>>=1
    return ret

for i,[v]in enumerate(l[N:]):
    update(dA[v]+tmiN,i)

def merge(A,B):
    ret=[]
    A=A[::-1]
    B=B[::-1]
    while A and B:
        if A[-1]<B[-1]:
            ret+=A.pop(),
        else:
            ret+=B.pop(),
    return ret+A[::-1]+B[::-1]

mstree=[0]*M+l[N:]
for i in range(M-1,0,-1):
    mstree[i]=merge(mstree[i<<1],mstree[i<<1|1])

from bisect import*

def gtK(arr,K):
    i=bisect_left(arr,K)
    return len(arr)-i
    
def getgtK(l,r,K):
    l+=M
    r+=M
    ret=0
    while l<r:
        if l&1:
            ret+=gtK(mstree[l],K)
            l+=1
        if r&1:
            r-=1
            ret+=gtK(mstree[r],K)
        l>>=1
        r>>=1
    return ret

for i,(s,e) in enumerate(l[:N]):
    ix=getval(dA[s],dA[e])
    if-1<ix:
        f[i]=1
    f[i]^=getgtK(ix+1,M,e)&1
print(sum(i[j]for i,j in zip(l,f)))