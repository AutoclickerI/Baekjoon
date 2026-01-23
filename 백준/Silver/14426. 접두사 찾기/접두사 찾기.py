L,*X=open(0)
N=int(L:=L.split()[0])
S=L+L.join(X[:N])
print(sum(L+i[:-1]in S for i in X)-N)