N,K,B,*l=map(int,open(0).read().split())
v=[0]*N
for i in l:v[-i]=1
s=sum(v[:K])
print(min([s]+[s:=s+v[i+K]-v[i]for i in range(N-K)]))