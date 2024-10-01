n,*l=map(int,open(0).read().split())
print(*[[n,*range(1,n+1)],[0]][all(i<j for i,j in zip(l,l[1:]))])