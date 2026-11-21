import sys
from bisect import*
input=sys.stdin.readline
p,q=map(int,input().split())
*l,=map(int,input().split())
for i in range(q-1):
    l[i+1]+=l[i]
for _ in[0]*p:
    n=bisect_left(l,int(input()))
    print(n+1 if n!=q else'Go away!')