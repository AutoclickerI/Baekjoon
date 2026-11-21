N,K,*l=map(int,open(0).read().split())
print(sum(l[~i]-K and(K:=6-K-l[~i])and pow(2,N+~i,10**9+7)for i in range(N))%(10**9+7))