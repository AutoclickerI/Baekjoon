N,M,K,*l=map(int,open(0).read().split())
X=[0]*N
for i in l:X[i]=1
while K:X=[X[j]^X[j-2]for j in range(N)];K-=1
print(sum(X))