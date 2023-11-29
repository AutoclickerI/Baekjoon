n,a,b,c,d=map(int,open(0))
p,q=n-b,n-a
print(max(0,min(d,q)-max(c,p)+1))