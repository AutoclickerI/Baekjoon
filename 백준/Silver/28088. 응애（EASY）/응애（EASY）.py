N,M,K,*l=map(int,open(0).read().split())
X=[k:=0]*N
for i in l:X[i]=1
while K:k+=1;X=K%2*[X[j]^X[j-2**k%N]for j in range(N)]or X;K//=2
print(sum(X))