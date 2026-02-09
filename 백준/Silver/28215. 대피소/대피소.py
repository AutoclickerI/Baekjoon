[N,K],*l=[[*map(int,i.split())]for i in open(0)]

def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

from itertools import*

r=1e9

for p in combinations(l,K):
    m=0
    for i in l:
        m=max(m,min(dist(j,i)for j in p))
    r=min(r,m)
print(r)