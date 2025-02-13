_,n,X=[[*map(int,i.split())]for i in open(0)]
a=0
while X and n:X[0]-=n.pop(0);a-=X[0]<1and X.pop(0)
print(X and-1or a+sum(n))