N,K,_,*l=map(int,open(0).read().split())
print('YNEOS'[min([j+~i for i,j in zip(l,l[1:]+[N+1])if j!=i+1]+[1e9])<=K::2])