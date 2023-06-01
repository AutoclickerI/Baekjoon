n,*l=map(int,open(0).read().split())
print(sum(~i%2-3+min(j,7)for i,j in zip(range(n),l)))