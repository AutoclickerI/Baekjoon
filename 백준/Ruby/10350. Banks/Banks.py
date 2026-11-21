n,*l=map(int,open(0).read().split())
s=sum(l)
print(-sum((v:=(i%n and v)+l[i//n+i%n-n])//s*(v<0)for i in range(n*n)))