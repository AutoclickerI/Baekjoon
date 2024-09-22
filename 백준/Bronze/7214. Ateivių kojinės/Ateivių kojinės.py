n,m,*a=map(int,open(0).read().split())
print(sum(min(c,n-1)for c in a)+1)