N,Q,*A=map(int,open(i:=0).read().split())
X=[]
exec('i+=1;X+=[i]*A.pop(0);'*N)
for a in A:print(X[a])