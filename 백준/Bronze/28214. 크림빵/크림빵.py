N,K,P,*l=map(int,open(0).read().split())
print(sum(sum(l[K*i:K*-~i])>K-P for i in range(N)))