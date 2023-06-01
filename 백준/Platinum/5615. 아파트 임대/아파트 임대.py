import sys
import math
from random import*
sys.setrecursionlimit(10**9)

def miller_rabin(n,a):
    r=0;d=n-1
    while d%2-1:r+=1;d//=2
    x=pow(a,d,n)
    if not 1!=x!=n-1:return 1
    for i in range(r-1):
        if(x:=pow(x,2,n))==n-1:return 1
 
def is_prime(n):
    n=2*int(n)+1
    if n<2:return 0
    if n<4:return 1
    if n%2-1:return 0
    for i in[2,7,61]:
        if n==i:return 1
        if not miller_rabin(n,i):return 0
    return 1

print(sum(map(is_prime,[*open(0)][1:])))