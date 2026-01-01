N,K,B,*l=map(int,open(0).read().split())
v=[0]*N
for i in l:v[-i]=1
m=s=sum(v[:K])
for i in range(N-K):s+=v[i+K]-v[i];m=min(m,s)
print(m)