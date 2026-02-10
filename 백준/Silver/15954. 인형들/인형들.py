N,K,*l=map(int,open(0).read().split())

m=1e9
for K in range(K,N+1):
    s=sum(l[:K])
    q=sum(i*i for i in l[:K])
    v=(q*K-s*s)/K/K
    for i,j in zip(l,l[K:]):
        s+=j-i
        q+=j*j-i*i
        v=min(v,(q*K-s*s)/K/K)
    m=min(m,v**.5)
print(m)