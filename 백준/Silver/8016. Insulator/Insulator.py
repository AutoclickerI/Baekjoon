n,*l=map(int,open(0))
l.sort()
print(n%2*l[n//2]+2*sum(l[-~n//2:]))