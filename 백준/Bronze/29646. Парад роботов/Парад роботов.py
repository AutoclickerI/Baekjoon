(n,k),*l=[map(int,i.split())for i in open(0)]
x,y=zip(*l)
X,Y=sum(x),sum(y)
for i in range(k-1):
    X+=X/n-x[i]
    Y+=Y/n-y[i]
print(X/n,Y/n)