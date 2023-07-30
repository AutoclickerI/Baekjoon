n,k,x,y,*l=map(int,open(0).read().split())
print(sum((l[2*i]-x)**2+(l[2*i+1]-y)**2>k**2for i in range(n)))