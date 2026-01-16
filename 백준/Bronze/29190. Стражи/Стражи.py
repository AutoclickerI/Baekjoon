n,m,x,y,k=map(int,open(0).read().split())
print(sum(k>=abs(i//m+1-x)+abs(i%m+1-y)for i in range(n*m))-1)