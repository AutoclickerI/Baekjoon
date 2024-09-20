n,*l=map(int,open(0))
print(sum(i==j for i,j in zip(l,l[n//2:]+l)))