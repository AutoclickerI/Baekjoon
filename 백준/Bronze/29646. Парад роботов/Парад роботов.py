(n,k),*l=[map(int,i.split())for i in open(0)]
x,y=zip(*l)
X,Y=sum(x),sum(y)
for i,j in zip(x,y[:k-1]):X+=X/n-i;Y+=Y/n-j
print(X/n,Y/n)