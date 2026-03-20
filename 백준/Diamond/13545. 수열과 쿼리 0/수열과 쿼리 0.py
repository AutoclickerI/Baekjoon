import sys
input=sys.stdin.readline

import math
from collections import deque
from heapq import*

tN=100001
tree=[0]*2*tN

def update(i,v):
    i+=tN
    tree[i]+=v
    while i:=i>>1:
        tree[i]=tree[i<<1]+tree[i<<1|1]

def getval(l,r):
    l+=tN
    r+=tN
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

[N],A,_,*l=[[*map(int,i.split())]for i in open(0)]

blk=500

sA=[0]
for i in A:
    sA+=sA[-1]+i,

hq=[]
dql=[deque()for _ in[0]*200002]
d={}
ps=pe=0
for s,e in sorted(l,key=lambda i:(i[0]//blk,i[1])):
    s-=1
    e+=1
    while pe<e:
        if dql[sA[pe]]:
            update(dql[sA[pe]][-1]-dql[sA[pe]][0],-1)
        dql[sA[pe]]+=pe,
        update(dql[sA[pe]][-1]-dql[sA[pe]][0],1)
        pe+=1
    while e<pe:
        pe-=1
        update(dql[sA[pe]][-1]-dql[sA[pe]][0],-1)
        dql[sA[pe]].pop()
        if dql[sA[pe]]:
            update(dql[sA[pe]][-1]-dql[sA[pe]][0],1)
    while s<ps:
        ps-=1
        if dql[sA[ps]]:
            update(dql[sA[ps]][-1]-dql[sA[ps]][0],-1)
        dql[sA[ps]].appendleft(ps)
        update(dql[sA[ps]][-1]-dql[sA[ps]][0],1)
    while ps<s:
        update(dql[sA[ps]][-1]-dql[sA[ps]][0],-1)
        dql[sA[ps]].popleft()
        if dql[sA[ps]]:
            update(dql[sA[ps]][-1]-dql[sA[ps]][0],1)
        ps+=1
    ts=0
    te=tN+1
    while 1<te-ts:
        m=ts+te>>1
        if getval(m,tN):
            ts=m
        else:
            te=m
    d[s+1,e-1]=ts

for s,e in l:print(d[s,e])