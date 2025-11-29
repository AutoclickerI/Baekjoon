N,K,*A=map(int,open(r:=0).read().split())
from itertools import*
for i in permutations(range(N)):c=0;r+=max(c:=c+K-A[v]for v in i)<1
print(r)