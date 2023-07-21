n,m=map(int,open(0))
v=sum(i%m+i//m==8for i in range(n*m))
print('There','airse'[v==1::2],v,'way'+'s'*(v!=1),'to get the sum 10.')