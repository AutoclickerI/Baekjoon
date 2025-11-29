K,A=open(r:=0)
from itertools import*
for i in permutations(A.split()):c=0;r+=max(c:=c+int(K[2:])-int(v)for v in i)<1
print(r)