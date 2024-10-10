import sys
import math

sys.setrecursionlimit(10**5)
def get_len(n):
    s=0
    while n:
        s+=1
        n//=10
    return s

def multifact(n,s):
    if n<2:
        return 1
    else:
        return n*multifact(n-s,s)
d=[get_len(multifact(9000,i))for i in range(9000,0,-1)]

from bisect import*
for T in range(int(input())):
    i=bisect_left(d,int(input()))
    if i<1:
        print(f'Case #{T+1}: ...')
    else:
        print(f"Case #{T+1}: IT'S OVER 9000"+'!'*(9001-i))