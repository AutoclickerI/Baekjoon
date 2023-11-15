n,p,*l=map(int,open(0).read().split())
print(n+min(p-1,n-p)+sum(l)-1)