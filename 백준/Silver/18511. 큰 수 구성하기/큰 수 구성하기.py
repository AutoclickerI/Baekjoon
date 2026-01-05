N,K=input().split()
l=input().split()
from itertools import*
m=0
for i in product(l,repeat=len(N)):
    n=int(''.join(i))
    if n<=int(N):
        m=max(m,n)
for i in product(l,repeat=len(N)-1):
    n=int(''.join(i))
    if n<=int(N):
        m=max(m,n)
print(m)