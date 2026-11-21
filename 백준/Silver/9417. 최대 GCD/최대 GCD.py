import math,itertools as I
for i in[*open(0)][1:]:print(max(math.gcd(*c)for c in I.combinations(map(int,i.split()),2)))