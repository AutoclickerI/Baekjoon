a,b=open(0)
from itertools import*
print(sorted(''.join(i)for i in permutations(a.split(),3)).index(b.strip())+1)