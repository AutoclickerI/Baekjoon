N,M,K,*l=map(int,open(0).read().split())
K-=.7
v=[1]*(N+2)
for b in l[N:]:d=1<<30;p=min([i for i in range(N)if v[i]*l[i]==b]or[i for i in range(N)if v[i]*l[i]>b]or[-2],key=lambda i:abs(K-i));print(p+1);v[p]=0