x,y,d=map(int,open(0).read().split())
n=100*x+y+2*d>>2
print(n//100,n%100,*divmod(n-d,100))