[N,_],L,*K=[[*map(int,i.split())]for i in open(0)]
print('YNEOS'[sum(2e3<sum(abs(i-j)for i,j in zip(L,k))for k in K)*2<N-1::2])