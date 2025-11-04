n,k,*l=map(str.strip,open(0))
from itertools import*
print(len({*map(''.join,permutations(l,int(k)))}))