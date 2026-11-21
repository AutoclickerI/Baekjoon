n,*l=map(int,open(0).read().split())
print(*all(i<j for i,j in zip(l,l[1:]))*'0'or[n,*range(1,n+1)])