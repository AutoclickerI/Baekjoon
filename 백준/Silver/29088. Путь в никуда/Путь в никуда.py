n,m,x,y=map(int,open(0).read().split())
m+=1-y
m*=2
print(min((n-x<<1|1)**2,4*x*x,m*-~m,4*y*y-2*y))