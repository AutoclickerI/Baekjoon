import math
[N,T],A,*l=[[*map(int,i.split())]for i in open(0)]
blk=math.isqrt(N)

r=0
v=[0]*1000001
ps=pe=0
d={}

for s,e in sorted(l,key=lambda i:(i[0]//blk,i[1])):
    s-=1
    while pe<e:
        r+=A[pe]*(2*v[A[pe]]+1)
        v[A[pe]]+=1
        pe+=1
    while e<pe:
        pe-=1
        v[A[pe]]-=1
        r-=A[pe]*(2*v[A[pe]]+1)
    while ps<s:
        v[A[ps]]-=1
        r-=A[ps]*(2*v[A[ps]]+1)
        ps+=1
    while s<ps:
        ps-=1
        r+=A[ps]*(2*v[A[ps]]+1)
        v[A[ps]]+=1
    d[s+1,e]=r

for s,e in l:print(d[s,e])