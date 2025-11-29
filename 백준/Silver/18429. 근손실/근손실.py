N,K,*A=map(int,open(0).read().split())
from itertools import*
def sim():
    c=0
    for v in i:
        c+=A[v]-K
        if c<0:return 0
    return 1
r=0
for i in permutations(range(N)):r+=sim()
print(r)