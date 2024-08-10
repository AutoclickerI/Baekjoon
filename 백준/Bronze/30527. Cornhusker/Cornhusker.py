*l,N,K=map(int,open(0).read().split())
print(sum(i*j for i,j in zip(l[::2],l[1::2]))//5*N//K)