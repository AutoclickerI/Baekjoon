import math

tN=1<<17
ta=[0]*2*tN
tb=[0]*2*tN

def update(tree,i,v):
    i+=tN
    tree[i]+=v
    tree[i>>4]+=v
    tree[i>>8]+=v
    tree[i>>12]+=v
    tree[i>>16]+=v

def getval(k):
    m=math.isqrt(k)
    ca=cb=ret=0
    r=k+1+tN
    for t in range(1,m+1):
        ca+=ta[tN+t]
        cb+=tb[tN+t]
        l=h=max(k//(t+1),m)+1+tN
        while l<r:
            while l<r and l&15:
                ret+=cb*ta[l]+ca*tb[l]
                l+=1
            while l<r and r&15:
                r-=1
                ret+=cb*ta[r]+ca*tb[r]
            l>>=4
            r>>=4
        r=h
    return ret+ca*cb

[N],A,B,_,*l=[[*map(int,i.split())]for i in open(0)]
blk=math.isqrt(N)

ps=pe=0

d={}

for s,e,k in sorted(l,key=lambda i:(i[0]//blk,i[1])):
    s-=1
    while pe<e:
        update(ta,A[pe],1)
        update(tb,B[pe],1)
        pe+=1
    while e<pe:
        pe-=1
        update(ta,A[pe],-1)
        update(tb,B[pe],-1)
    while ps<s:
        update(ta,A[ps],-1)
        update(tb,B[ps],-1)
        ps+=1
    while s<ps:
        ps-=1
        update(ta,A[ps],1)
        update(tb,B[ps],1)
    d[s+1,e,k]=getval(k)

for s,e,k in l:print(d[s,e,k])