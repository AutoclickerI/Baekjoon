n,m,*l=map(int,open(0).read().split())
f=l.index
x=f(1)
y=f(1,x+1)
print(y//m-x//m+abs(x%m-y%m))