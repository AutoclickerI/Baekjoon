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

[N],A,_,*l=[[*map(int,i.split())]for i in open(0)]
blk=math.isqrt(N)

v=[0]*tN

m=0

ps=pe=0

d={}

for s,e in sorted(l,key=lambda i:(i[0]//blk,i[1])):
    s-=1
    while pe<e:
        v[A[pe]]+=1
        update(A[pe],1)
        pe+=1
    while e<pe:
        pe-=1
        v[A[pe]]-=1
        update(A[pe],-1)
    while ps<s:
        v[A[ps]]-=1
        update(A[ps],-1)
        ps+=1
    while s<ps:
        ps-=1
        v[A[ps]]+=1
        update(A[ps],1)
    d[s+1,e]=getval(0,tN)

for s,e in l:print(d[s,e])