n,*l=map(int,open(0).read().split())
f=l.count
p=f(0)
print(p*n+p*~p//2+p*f(1))