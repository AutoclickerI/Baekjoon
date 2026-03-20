import sys
input=sys.stdin.readline

import math
from collections import deque
from heapq import*

P=int(input())
s=input().strip()
N=len(s)

blk=math.isqrt(N)

l=[[*map(int,input().split())]for _ in[0]*int(input())]
sl=sorted(l,key=lambda i:(i[0]//blk,i[1]))

if P in[2,5]:
    s=[int(i)%P<1 for i in s]
    ps=[0]
    for i in s:ps+=ps[-1]+i,
    pm=[0]
    for i,v in enumerate(s,1):pm+=pm[-1]+v*i,
    
    for s,e in l:
        print(pm[e]-pm[s-1]-(ps[e]-ps[s-1])*(s-1))
else:
    A=[0]
    mv=pow(10,-1,P)
    for i in s:
        A+=(A[-1]*10+int(i))%P,
    r=10
    sA=[i*(r:=r*mv%P)%P for i in A]

    sl={v:i for i,v in enumerate(sorted({*sA}))}
    sA=[sl[i]for i in sA]
    
    N=len(sl)
    
    d={}
    ql=[0]*N
    ps=pe=0
    r=0
    for s,e in sorted(l,key=lambda i:(i[0]//blk,i[1])):
        s-=1;e+=1
        while pe<e:
            r+=ql[sA[pe]]
            ql[sA[pe]]+=1
            pe+=1
        while e<pe:
            pe-=1
            ql[sA[pe]]-=1
            r-=ql[sA[pe]]
        while s<ps:
            ps-=1
            r+=ql[sA[ps]]
            ql[sA[ps]]+=1
        while ps<s:
            ql[sA[ps]]-=1
            r-=ql[sA[ps]]
            ps+=1
        d[s+1,e-1]=r
    
    for s,e in l:print(d[s,e])