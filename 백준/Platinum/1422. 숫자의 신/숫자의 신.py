K,N=map(int,input().split())
l=[input()for _ in[0]*K]
m=max(l,key=lambda i:(len(i),i))
l+=[m]*(N-K)

from functools import*

def cmp(a,b):
    if a+b<b+a:
        return 1
    else:
        return -1

l.sort(key=cmp_to_key(cmp))
print(*l,sep='')