import sys
input=sys.stdin.readline

N=int(input())

import math
from bisect import*

blk=math.isqrt(N)

blocks=[[]for _ in(N+blk-1)//blk*[0]]

*l,=map(int,input().split())

for i,v in enumerate(l):
    blocks[i//blk]+=v,

for i in blocks:i.sort()

def update(i,v):
    arr=blocks[i//blk]
    arr.pop(bisect_left(arr,l[i]))
    l[i]=v
    insort(arr,v)

def getval(le,ri,k):
    ls=(le+blk-1)//blk
    rs=ri//blk
    if ri-le<=blk:
        return sum(k<l[i]for i in range(le,ri))
    ret=sum(k<l[i]for rg in(range(le,min(ls*blk,N)),range(rs*blk,ri))for i in rg)
    for i in range(ls,rs):
        ret+=len(blocks[i])-bisect_left(blocks[i],k+1)
    return ret

for _ in[0]*int(input()):
    q,*z=map(int,input().split())
    z[0]-=1
    if q==2:
        update(*z)
    else:
        print(getval(*z))