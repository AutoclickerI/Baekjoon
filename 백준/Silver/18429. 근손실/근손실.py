N,K,*A=map(int,open(r:=0).read().split())
from itertools import*
for i in permutations(A):c=0;r+=max(c:=c+K-v for v in i)<1
print(r)