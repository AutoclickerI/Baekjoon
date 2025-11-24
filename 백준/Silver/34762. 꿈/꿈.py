N,K,_,*l=map(int,open(0).read().split())
print('YNEOS'[any(1<j-i<K+2for i,j in zip(l,l[1:]+[N+1]))::2])