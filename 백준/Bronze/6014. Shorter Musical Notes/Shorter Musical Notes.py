N,Q,*A=map(int,open(i:=0).read().split())
X=[]
for a in A[:N]:i+=1;X+=[i]*a
for a in A[N:]:print(X[a])