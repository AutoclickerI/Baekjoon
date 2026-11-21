N,H,W,*X=map(int,open(0).read().split())
print(H*sum(W-abs(i+j-W)for i,j in zip(*[iter(X)]*2)))