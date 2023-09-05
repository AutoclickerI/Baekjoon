W,N,_,*l=map(int,open(0).read().split())
print(sum(W<=i<=N for i in l))