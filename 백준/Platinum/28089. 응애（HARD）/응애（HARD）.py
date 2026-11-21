n,m,k,*A=map(int,open(0).read().split())
X=[0]*n
for a in A:X[a]=i=1
while k:i*=2;X=k%2*[X[j]^X[(j+i)%n]for j in range(n)]or X;k//=2
print(sum(X))