tN=100001
tree=[0]*2*tN

def update(i,v):
    i+=tN
    tree[i]+=v
    while i:=i>>1:
        tree[i]=max(tree[i<<1],tree[i<<1|1])

def getval(l,r):
    l+=tN
    r+=tN
    ret=0
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

import math

[N,Q],X,*l=[[*map(int,i.split())]for i in open(0)]

sl={}
vm={}
for i,v in enumerate(sorted(X)):
    sl[v]=i
    vm[i]=v
A=[sl[i]for i in X]

blk=math.isqrt(N)

sl=sorted(l,key=lambda i:(i[0]//blk,i[1]))

d={}

sp=ep=0
for s,e in sl:
    s-=1
    while ep<e:
        update(A[ep],vm[A[ep]])
        ep+=1
    while e<ep:
        ep-=1
        update(A[ep],-vm[A[ep]])
    while sp<s:
        update(A[sp],-vm[A[sp]])
        sp+=1
    while s<sp:
        sp-=1
        update(A[sp],vm[A[sp]])
    d[s+1,e]=getval(0,tN)
for s,e in l:print(d[s,e])