n,p,m,*l=map(int,open(0).read().split())
for i,j in zip(*[iter(l)]*2):
    if p in(i,j):
        p^=i^j
print(p)