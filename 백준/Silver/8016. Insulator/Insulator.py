n,*l=map(int,open(0))
l.sort()
print(2*sum(l[n//2:])-n%2*l[n//2])