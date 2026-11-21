n,m,*l=map(int,open(0).read().split())
print('NDEA'[m<=n<=sum(i//4-1e9*(i<4)for i in l)::2])