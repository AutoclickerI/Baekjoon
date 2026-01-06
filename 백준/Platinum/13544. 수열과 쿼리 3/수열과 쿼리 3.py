[N],v,_,*Q=[[*map(int,i.split())]for i in open(0)]

tree=[[]for _ in[0]*2*N]
for i in range(N):
    tree[i+N]=[v[i]]
for i in range(N-1,0,-1):
    tree[i]=sorted(tree[i*2]+tree[i*2+1])

from bisect import*
def getval(l,r,k):
    l+=N
    r+=N
    v=0
    while l<r:
        if l%2:
            v+=len(tree[l])-bisect_left(tree[l],k+1)
            l+=1
        if r%2:
            r-=1
            v+=len(tree[r])-bisect_left(tree[r],k+1)
        l//=2
        r//=2
    return v

la=0
for a,b,c in Q:
    i,j,k=a^la,b^la,c^la
    print(la:=getval(i-1,j,k))