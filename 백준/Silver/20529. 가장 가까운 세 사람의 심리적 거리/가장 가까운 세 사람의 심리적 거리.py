from itertools import*
d=lambda*l:sum(map(str.__ne__,*l))
for i in[*open(0)][2::2]:print(+(len(i)<161)and min(d(a,b)+d(b,c)+d(c,a)for a,b,c in combinations(i.split(),3)))