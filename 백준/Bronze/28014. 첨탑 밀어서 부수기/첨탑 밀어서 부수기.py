n,*l=map(int,open(0).read().split())
print(1+sum(i<=j for i,j in zip(l,l[1:])))