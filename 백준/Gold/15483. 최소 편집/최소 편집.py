import sys
sys.setrecursionlimit(2*10**5)

from functools import*

@cache
def lev(a,b):
    if a=='':
        return len(b)
    if b=='':
        return len(a)
    if a[0]==b[0]:
        return lev(a[1:],b[1:])
    return 1+min(lev(a[1:],b[1:]),lev(a,b[1:]),lev(a[1:],b))

print(lev(input(),input()))