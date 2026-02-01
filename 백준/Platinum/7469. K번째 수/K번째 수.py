[N,M],v,*Q=[[*map(int,i.split())]for i in open(0)]
tree=[0]*2*N

for i in range(N):
    tree[i+N]=[v[i]]

for i in range(1,N)[::-1]:
    tree[i]=sorted(tree[i*2]+tree[i*2|1])

from bisect import bisect

def getval(s,e,v):
    s+=N
    e+=N
    r=0
    while s<e:
        if s&1:
            r+=bisect(tree[s],v)
            s+=1
        if e&1:
            e-=1
            r+=bisect(tree[e],v)
        s>>=1
        e>>=1
    return r

for i,j,k in Q:
    s=-10**10
    e=10**10
    while 1<e-s:
        m=s+e>>1
        if getval(i-1,j,m)<k:
            s=m
        else:
            e=m
    print(e)