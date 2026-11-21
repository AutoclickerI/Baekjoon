N,K,*l=map(int,open(0).read().split())
m=10**9+7
print(sum(l[~i]-K and pow((K:=6-K-l[~i])*0+2,N+~i,m)for i in range(N))%m)