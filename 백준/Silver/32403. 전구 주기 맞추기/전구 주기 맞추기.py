N,T,*A=map(int,open(0).read().split())
l=[i for i in range(1,T+1)if T%i<1]
print(sum(min(abs(i-j)for j in l)for i in A))