N,K,*s=map(int,open(0).read().split())

from functools import*

@cache
def recur(l,r):
    if l+1==r:
        return 0
    ret=float('inf')
    for m in range(l+1,r):
        ret=min(ret,recur(l,m)+recur(m,r)+(s[l]!=s[m]))
    return ret

print(recur(0,N))