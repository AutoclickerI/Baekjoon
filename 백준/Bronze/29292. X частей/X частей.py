_,n,X=[[*map(int,i.split()[::-1])]for i in open(0)]
a=0
while X and n:X[-1]-=n.pop();a-=X[-1]<1and X.pop()
print(X and-1or a+sum(n))