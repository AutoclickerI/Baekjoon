n,m,x,y=map(int,open(0).read().split())
m+=1-y
print(min((n-x<<1|1)**2,4*x*x,4*m*m+2*m,4*y*y-2*y))