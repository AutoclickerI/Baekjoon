n=int(input())
l=[]
from itertools import*

for i in permutations(str(n)):
    v=int(''.join(i))
    if n<v:l+=v,
print(min(l or[0]))