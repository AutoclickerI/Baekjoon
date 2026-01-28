import sys
sys.setrecursionlimit(2*10**5)

from functools import cache

@cache
def f(n,b):
    if b==1:
        return 1
    if n<b:
        return f(n,b//2)
    return(f(n-b,b)+f(n,b//2))%10**9

n=int(input())
print(f(n,1<<n.bit_length()))