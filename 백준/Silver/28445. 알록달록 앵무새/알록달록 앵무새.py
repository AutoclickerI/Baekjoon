from itertools import*
s={*open(0).read().split()}
for i in sorted(product(s,repeat=2)):print(*i)